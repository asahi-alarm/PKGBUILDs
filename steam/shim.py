#!/usr/bin/python3
#
# Copyright 2024 Alyssa Rosenzweig
# SPDX-License-Identifier: MIT
from xdg import BaseDirectory
import sys
import os
import pexpect
import subprocess
import time

LAUNCHER_NAME = 'fex-steam'
URL = "https://repo.steampowered.com/steam/archive/stable/steam_1.0.0.81.tar.gz"

MANIFEST = [
    'steam-launcher/steam_subscriber_agreement.txt',
    'steam-launcher/bin_steam.sh',
    'steam-launcher/bootstraplinux_ubuntu12_32.tar.xz',
]

# prevent user from running as root
if os.geteuid() == 0:
    sys.exit(f"Do not run `{sys.argv[0]}` as root")

# Performance fix for Big Picture mode
STEAM_ARGS = ["-cef-force-occlusion"]

# Append user provided args
provided_args = sys.argv[1:]
STEAM_ARGS += provided_args

# We display a splash so the user gets rapid feedback. This happens before we
# start downloading Steam - we want the splash to come up instantly even if the
# Internet connection is slow.
#
# TODO: Suppress this if Steam is already up i.e. when handling steam:// URLs.
# This is tricky to detect.
show_splash = True

def is_latest_installed(data_dir):
    try:
        with open(f'{data_dir}/version', 'r') as f:
            return f.read() == URL
    except FileNotFoundError:
        # No version file means we weren't installed yet.
        return False

def drop_old_install(data_dir):
    from pathlib import Path

    install = f'{data_dir}/steam-launcher'
    if os.path.isdir(install):
        for item in MANIFEST:
            Path(f'{data_dir}/{item}').unlink(missing_ok=True)

def download(url, data_dir):
    import requests
    import tarfile

    # Reset our install directory to a known state
    os.makedirs(data_dir, exist_ok=True)
    drop_old_install(data_dir)

    # Grab the files we need
    resp = requests.get(url, stream=True)
    tar = tarfile.open(fileobj=resp.raw, mode='r|gz')

    def member_generator(members):
        for tarinfo in members:
            if tarinfo.name in MANIFEST:
                yield tarinfo

    tar.extractall(path=data_dir, members=member_generator(tar), filter='data')
    tar.close()

    # Install our launch script. Not strictly necessary to do it this way but very convenient.
    LAUNCH = f"{data_dir}/steam-launcher/bin_steam.sh {STEAM_ARGS}"
    open(f'{data_dir}/launch.sh', 'w').write(LAUNCH)

    # Mark the version so we know for later updates.
    # This needs to be last in case we got interrupted.
    open(f'{data_dir}/version', 'w').write(URL)

def muvm(cmd):
    return pexpect.spawn("muvm", ["--"] + cmd)

# Kludge to check if the window is open. Without muvm-interactive, this muvm
# call is one-shot so we poll a file to grab the output. Fortunately, it
# doesn't really matter if we're late, as long as we eventually notice that
# Steam is open.
def is_steam_open(path):
    tmp = f'{path}/status.txt'
    with open(tmp, 'w') as f:
        f.write("not ready")

    return subprocess.run('xwininfo -tree -root|grep -E \'Steam Big|"Steam":.*steamwebhelper\'', shell=True).returncode == 0

aborting = False

steam_is_ready = False
def watch_steam(path):
    global steam_is_ready
    global aborting
    while not steam_is_ready and not aborting:
        steam_is_ready = is_steam_open(path)
        time.sleep(0.1)

steam = None

def launch_steam(path):
    global steam
    global aborting

    # Update the steam launcher
    if not is_latest_installed(path):
        download(URL, path)

    # Launch steam
    steam_arg_string = ' '.join(STEAM_ARGS)
    steam = muvm(["FEXBash", "-c", f'{path}/steam-launcher/bin_steam.sh {steam_arg_string}'])
    while True:
        if not steam.isalive():
            aborting = True

            # Be silent for steam:// handling
            if show_splash:
                print("Steam quit")

            break

        if aborting:
            print("Aborting - killing Steam")
            steam.terminate(True)
            break

        try:
            sys.stdout.write(steam.readline().decode())
        except pexpect.exceptions.TIMEOUT:
            pass

# Here is where we learn Alyssa doesn't know how to write GUIs
def splash(path):
    from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow
    from PyQt6.QtCore import Qt, QTimer
    import threading

    steam_thread = threading.Thread(target=launch_steam, args=(path,))
    steam_thread.start()

    watcher_thread = None

    app = QApplication([])
    window = QMainWindow()
    window.resize(app.primaryScreen().availableGeometry().size() * 0.5)
    #window.setWindowState(Qt.WindowState.WindowFullScreen)
    window.setWindowTitle("Steam Launcher")
    window.setStyleSheet("""
    background-color: #1b2838;
    color: #c7d5e0;
    """)

    DOWNLOADING = 'Bootstrapping'
    LAUNCHING = 'Launching'
    initial_state = LAUNCHING if is_latest_installed(path) else DOWNLOADING

    state = initial_state
    def label_for_ticks(state, ticks):
        dots = '.' * ((ticks % 3))
        return f'{state} Steam.{dots}'

    ticks = 0
    msg = QLabel(label_for_ticks(state, ticks), parent=window)
    font = msg.font()
    font.setPointSize(60)
    msg.setFont(font)
    msg.setStyleSheet("font-family: Lato")
    msg.setAlignment(Qt.AlignmentFlag.AlignCenter)
    window.setCentralWidget(msg)
    window.show()

    # Poll steam's status while launching.
    timer = QTimer()
    exiting = False
    steam = None
    ticks = 0
    def update():
        nonlocal ticks
        nonlocal exiting
        nonlocal state
        nonlocal watcher_thread
        global steam
        global steam_is_ready

        ticks += 1

        # FSM transition.
        if state == DOWNLOADING and steam is not None:
            state = LAUNCHING
            ticks = 0

        # Animate the label to display progress
        msg.setText(label_for_ticks(state, ticks))

        # If Steam failed to start, kill the splash.
        if aborting:
            print("Aborting")
            window.close()
            timer.timeout.disconnect()
            return

        # Only start watching Steam after launching Steam
        if steam is not None and watcher_thread is None and ticks > 10:
            watcher_thread = threading.Thread(target=watch_steam, args=(path,))
            watcher_thread.start()

        # Once the steam window is open, we don't need the splash.
        # But, delay exit by a tick so we have a seamless handoff.
        # ..since is_steam_open will return true a few hundred ms before Steam draws.
        # Might be possible to make less racey? shrug.
        #
        # TODO: maybe disassociate process to free up some RAM
        if exiting:
            print("Steam is up - hiding the launcher")
            window.hide()
            timer.timeout.disconnect()
            app.quit()

        exiting = steam_is_ready

    def abort():
        nonlocal exiting
        global aborting
        if exiting:
            return
        # If Steam is not ready, this is an early-exit.
        # If Steam is ready, this is just Qt tidying up after we closed the window.
        # We can sys.exit, Steam is in a helper thread.
        aborting = not steam_is_ready
        print(f"Qt says we're gone, aborting={aborting}")

    app.aboutToQuit.connect(abort)
    timer.timeout.connect(update)
    timer.start(1000)
    app.exec()

# Ok. Time to kick everything off.
# Grab our data directory, xdg compliant
path = BaseDirectory.save_data_path(LAUNCHER_NAME)

if show_splash:
    splash(path)
else:
    launch_steam(path)
