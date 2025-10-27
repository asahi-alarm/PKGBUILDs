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
PKGS="asahi-scripts m1n1 uboot-asahi linux-asahi alsa-ucm-conf-asahi bankstown speakersafetyd asahi-audio calamares \
 asahi-calamares-configs asahi-configs lzfse asahi-fwextract asahi-alarm-keyring \
 tiny-dfr widevine \
 muvm FEX-Emu asahi-bless fex-emu-rootfs-arch steam \
 asahi-desktop-meta asahi-meta"

if [ $# -ge 1 ]; then
  PKGS="$*"
fi

if [ ! -d packages ]; then
  mkdir packages
fi

# Build packages
for srcpkg in $PKGS; do
  pushd "$srcpkg"
  echo "Building $srcpkg"
  # remove src andn pkg folders
  rm -rf src pkg
  # Remove any previously created packages
  rm -f -- *.pkg.tar.xz
  makepkg -Cs --noconfirm
  # if [ "$srcpkg" == "mesa" ]; then
  #   # HACK: move the unwanted mesa-dummy package out of the way so it doesn't get picked up by 'ls'
  #   # we DO want it in packages though, but not install it since it conflicts with mesa
  #   mv mesa-dummy* ../packages/
  #   # we need to remove mesa to avoid conflicts, not sure why -U --noconfirm isn't enough
  #   sudo pacman -Rdd --noconfirm mesa
  # fi

  pkg=$(ls -- *.pkg.tar.xz)
  sudo pacman -U --noconfirm $pkg
  mv $pkg ../packages/
  popd
done
