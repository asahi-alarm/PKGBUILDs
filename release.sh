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

KEY=12CE6799A94A3F1B5DDFFE88F576553597FB8FEB
REPO=asahi-alarm
TAG=aarch64
RELEASE=false

# Parse options
while getopts ":R:crp:t:h" opt; do
  case $opt in
    R)
      REPO=$OPTARG
      if [ ! -d "$REPO" ]; then
        mkdir -p "../$REPO"
      fi
      ;;
    c)
      echo "cleaning files"
      rm -f ../$REPO/*.xz ../$REPO/*.sig ../$REPO/$REPO.db* ../$REPO/$REPO.files* || true
      ;;
    r)
      RELEASE=true
      ;;
    t)
      TAG=$OPTARG
      ;;
    h)
      echo "Usage: $0 [-R <dir>] [-r] [-c] -p <gpg passphrase> -t <tag> [PKGS]"
      echo -e "    -R <dir>: place packages in <dir>. Provide this first to override the default 'asahi-alarm'"
      echo -e "    -p <passphrase>: pass in the passphrase as argument instead of asking for it"
      echo -e "    -r: create a release on github. Default: false"
      echo -e "    -t <tag>: use <tag> as tag on the release git repo. This will also be the release name. This only \
        has effect if -r is passed. Default: aarch64"
      echo -e "    -c: clean the packages in ../$REPO before building. Default: false"
      exit 1
      ;;
    p)
      GPG_PASSPHRASE=$OPTARG
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
# NOTE fex-emu-rootfs-arch needs the rootfs to be placed in the same folder as the PKGBUILD as
# default.erofs.xz to work.
PKGS="linux-asahi alsa-ucm-conf-asahi bankstown speakersafetyd asahi-audio calamares \
  asahi-calamares-configs asahi-configs asahi-fwextract asahi-alarm-keyring asahi-scripts lzfse \
  m1n1 mesa tiny-dfr uboot-asahi widevine asahi-desktop-meta asahi-meta\
  virglrenderer libkrun libkrunfw muvm FEX-Emu fex-emu-rootfs-arch vulkan-tools asahi-bless steam"

if [ $# -ge 1 ]; then
  PKGS=("$@")
fi

if [ -z "$GPG_PASSPHRASE" ]; then
  echo "Enter GPG passphrase:"
  read -s GPG_PASSPHRASE
fi

echo "RELEASE=$RELEASE"
echo "REPO=$REPO"
echo "TAG=$TAG"
echo "RELEASE=$RELEASE"

# Build packages
for srcpkg in $PKGS; do
  pushd $srcpkg
  echo "Building $srcpkg"
  # Remove any previous created packages
  rm -f *.pkg.tar.xz *.pkg.tar.xz.sig
  makepkg -Cs --noconfirm
  # NOTE mesa also builds the fex overlays, but these need to be built on x86, so these
  # packages should be ignored for release
  pkg=$(ls -- *.pkg.tar.xz | grep -v fex-emu-overlay)
  # there could be multiple packages built from same PKGBUILD
  for bin in $pkg; do
    echo "$GPG_PASSPHRASE" | gpg --local-user $KEY --pinentry-mode loopback --passphrase-fd 0 --detach-sign "${bin}"
    mv "$bin"* ../../$REPO/
    repo-add --key $KEY --sign ../../$REPO/$REPO.db.tar.gz "../../$REPO/$bin"
  done
  popd
done

# Release packages on github if requested
if [ "$RELEASE" = true ]; then
  cd ../$REPO
  git tag -d $TAG && git tag $TAG && git push -f --tags

  gh release delete -y $TAG
  gh release create $TAG --notes ""
  gh release upload $TAG -- *.xz *.xz.sig $REPO.db* $REPO.files*
fi
