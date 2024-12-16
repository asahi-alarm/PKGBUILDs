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

RELEASE=false

# Parse options
while getopts ":rh" opt; do
  case $opt in
    r)
      RELEASE=true
      ;;
    h)
      echo "Usage: $0 [-r] [PKGS]"
      exit 1
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

# Remove parsed options from arguments
shift $((OPTIND - 1))

# default packages, can be overridden on command line
# re-add calamares stuff when we get to the installer
PKGS="linux-asahi alsa-ucm-conf-asahi bankstown speakersafetyd asahi-audio asahi-configs asahi-fwextract asahi-alarm-keyring asahi-scripts lzfse m1n1 mesa-asahi tiny-dfr uboot-asahi xkeyboard-config-asahi asahi-desktop-meta asahi-meta"

if [ $# -ge 1 ]; then
  PKGS=("$@")
fi

echo "building packages: ${PKGS[*]}"
REPO=asahi-alarm

echo "Enter GPG passphrase:"
read -s GPG_PASSPHRASE

# Build packages
for srcpkg in $PKGS; do
  pushd $srcpkg
  echo "Building $srcpkg"
  makepkg -Cfs --noconfirm
  pkg=$(ls -- *.pkg.tar.xz)
  # there could be multiple packages
  for bin in $pkg; do
    echo "$GPG_PASSPHRASE" | gpg --pinentry-mode loopback --passphrase-fd 0 --detach-sign "${bin}"
    cp "$bin"* ../../$REPO/
    repo-add --sign ../../$REPO/$REPO.db.tar.gz "../../$REPO/$bin"
  done
  popd
done

# Release packages on github if requested
if [ "$RELEASE" = true ]; then
  cd ../$REPO
  git tag -d aarch64 && git tag aarch64 && git push -f --tags

  yes | gh release delete aarch64
  gh release create aarch64 --notes ""
  gh release upload aarch64 -- *.xz *.sig asahi-alarm.db* asahi-alarm.files*
fi