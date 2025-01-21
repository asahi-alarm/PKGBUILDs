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
# TODO: remove lsp-plugins once a new version is released
# NOTE fex-emu-rootfs-arch needs the rootfs to be placed in the same folder as the PKGBUILD as
# default.erofs.xz to work.

PKGS="m1n1 uboot-asahi linux-asahi lsp-plugins alsa-ucm-conf-asahi bankstown speakersafetyd asahi-audio calamares \
 asahi-calamares-configs asahi-configs asahi-scripts lzfse asahi-fwextract asahi-alarm-keyring \
 virglrenderer-asahi mesa-asahi tiny-dfr xkeyboard-config-asahi widevine \
 libkrunfw libkrun muvm FEX-Emu vulkan-tools asahi-bless steam \
 asahi-desktop-meta asahi-meta"

if [ $# -ge 1 ]; then
  PKGS=("$@")
fi

# Build packages
for srcpkg in $PKGS; do
  pushd "$srcpkg"
  echo "Building $srcpkg"
  # remove src andn pkg folders
  rm -rf src pkg
  # Remove any previous created packages
  rm -f -- *.pkg.tar.xz
  makepkg -Cs --noconfirm
  if [ "$srcpkg" == "mesa-asahi" ]; then
    # HACK: remove the unwanted mesa packages to avoid failing the build due to conflict
    rm -f mesa-asahi-fex-emu-overlay-x86_64* mesa-asahi-fex-emu-overlay-i386* mesa-asahi-dummy*
    # we need to remove mesa to avoid conflicts, not sure why -U --noconfirm isn't enough
    sudo pacman -Rdd --noconfirm mesa
  fi

  pkg=$(ls -- *.pkg.tar.xz)
  sudo pacman -U --noconfirm $pkg
  mv $pkg ../packages/
  popd
done
