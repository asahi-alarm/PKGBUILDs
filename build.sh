#!/bin/bash

set -e

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
PKGS="linux-asahi lsp-plugins alsa-ucm-conf-asahi bankstown speakersafetyd asahi-audio calamares \
  asahi-calamares-configs asahi-configs asahi-fwextract asahi-alarm-keyring asahi-scripts lzfse \
  m1n1 mesa-asahi tiny-dfr uboot-asahi xkeyboard-config-asahi widevine asahi-desktop-meta asahi-meta\
  virglrenderer-asahi libkrun libkrunfw muvm FEX-Emu vulkan-tools asahi-bless steam"

if [ $# -ge 1 ]; then
  PKGS=("$@")
fi

# Build packages
for srcpkg in $PKGS; do
  pushd $srcpkg
  echo "Building $srcpkg"
  # Remove any previous created packages
  rm -f *.pkg.tar.xz *.pkg.tar.xz.sig
  makepkg -Cs --noconfirm
  # NOTE mesa-asahi also builds the fex overlays, but these need to be built on x86, so these
  # packages should be ignored for release
  pkg=$(ls -- *.pkg.tar.xz | grep -v fex-emu-overlay)
  # there could be multiple packages built from same PKGBUILD
  for bin in $pkg; do
    mv "$bin" ../packages/
  done
  popd
done
