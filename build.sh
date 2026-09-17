#!/bin/bash

set -xe

# Run this on an arch aarch64 machine
#
# You need to also have the asahi-alarm repo checked out next to this one
# for the release option to work
#
# It will build all packages or the packages given on the command line
# if you pass -r option, it will also create a new release on github
#
# This also requires the github-cli tool to be installed and logged in

# default packages, can be overridden on command line
PKGS="asahi-fix27 asahi-scripts m1n1 uboot-asahi linux-asahi alsa-ucm-conf-asahi bankstown speakersafetyd asahi-audio calamares \
 asahi-calamares-configs asahi-configs lzfse asahi-fwextract asahi-alarm-keyring \
 virglrenderer tiny-dfr widevine \
 libkrunfw libkrun muvm FEX-Emu asahi-bless fex-emu-rootfs-arch steam \
 asahi-desktop-meta asahi-meta"

if [ $# -ge 1 ]; then
  PKGS="$*"
fi

if [ ! -d packages ]; then
  mkdir packages
fi

# Build packages
for srcpkg in $PKGS; do
  # mesa only builds the x86 FEX-Emu overlays (+ mesa-dummy) these days; those need
  # an x86_64 host and are built by the separate 'mesa' job in .github/workflows.
  # The native aarch64 mesa package now comes from the ALARM [extra] repo.
  if [ "$srcpkg" == "mesa" ]; then
    echo "Skipping mesa: the x86 FEX-Emu overlays are built on an x86_64 host"
    continue
  fi
  pushd "$srcpkg"
  echo "Building $srcpkg"
  # remove src andn pkg folders
  rm -rf src pkg
  # Remove any previously created packages
  rm -f -- *.pkg.tar.xz
  makepkg -CsA --noconfirm
  pkg=$(ls -- *.pkg.tar.xz)
  sudo pacman -U --noconfirm $pkg
  mv $pkg ../packages/
  popd
done
