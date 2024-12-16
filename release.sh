#!/bin/bash

set -x
set -e

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
    cp "$bin"* ../../$PROJECT/
    repo-add --sign ../../$PROJECT/$PROJECT.db.tar.gz "../../$PROJECT/$bin"
  done
  popd
done

# Release packages
cd ../$REPO
git tag -d aarch64 && git tag aarch64 && git push -f --tags

yes | gh release delete aarch64
gh release create aarch64 --notes ""
gh release upload aarch64 -- *
