#!/bin/bash

declare -A mappings
declare -A mappings_fedora_repo
declare -A copr

mappings_fedora_repo["bankstown"]="EPEL-10.0"

mappings["bankstown"]="rust-bankstown-lv2"
mappings["widevine"]="widevine-installer"
mappings["lzfse"]="lzfse-libs"
mappings["FEX-Emu"]="fex-emu"
mappings["fex-emu-rootfs-arch"]="fex-emu-rootfs-fedora"
mappings["linux-asahi"]="kernel"
mappings["linux-asahi-headers"]="kernel"
mappings["uboot-asahi"]="u-boot"
mappings["alsa-ucm-conf-asahi"]="alsa-ucm-asahi"
mappings["asahi-bless"]="rust-asahi-bless"
mappings["asahi-scripts"]="asahi-scripts"
mappings["binfmt-dispatcher"]="rust-binfmt-dispatcher"
mappings["calamares"]="calamares"
mappings["libkrun"]="libkrun"
mappings["libkrunfw"]="libkrunfw"
mappings["tiny-dfr"]="rust-tiny-dfr"
mappings["triforce-lv2"]="rust-triforce-lv2"
mappings["virglrenderer"]="virglrenderer"
mappings["muvm"]="rust-muvm"
mappings["speakersafetyd"]="rust-speakersafetyd"
mappings["alsa-ucm-conf-asahi"]="alsa-ucm-asahi"
mappings["asahi-calamares-configs"]="fedora-remix-scripts"

copr["kernel"]="kernel"
copr["mesa"]="mesa"
copr["virglrenderer"]="mesa"
copr["steam"]="steam"
copr["u-boot"]="uboot-tools"
copr["fedora-remix-scripts"]="calamares-firstboot-config"

DB=asahi-alarm.db.tar.gz

FEDORA_REPO="F41"

if [ $# == 1 ]; then
  FEDORA_REPO=$1
fi

wget -O $DB -q https://github.com/asahi-alarm/asahi-alarm/releases/download/aarch64/$DB
PKGS=$(tar tvf $DB | grep -v .sig | grep -v desc | awk '{ print $6}' | sed 's!/$!!g')
rm $DB

echo

printf "%-30s %-30s %-30s\n" "Package" "Fedora Version" "ALARM Version"
for P in $PKGS; do
  B=$(echo $P | sed 's/\([A-Za-z-]*\)-[0-9].*/\1/')
  V=$(echo $P | sed "s/$B-\([0-9].*\)/\1/")
  if [[ "$B" == *overlay* || "$B" == *dummy* ]]; then
    continue
  fi
  O=$B

  if [[ -n "${mappings_fedora_repo[$B]}" ]]; then
    REPO=${mappings_fedora_repo[$B]}
  else
    REPO=$FEDORA_REPO
  fi

  if [[ -n "${mappings[$B]}" ]]; then
    B=${mappings[$B]}
  fi
  if [[ -n "${copr[$B]}" ]]; then
    # search in copr
    PACKAGE=${copr[$B]}
    if [ "$B" == "virglrenderer" ]; then
      F=$(curl -s -X 'GET' "https://copr.fedorainfracloud.org/api_3/package/?ownername=%40asahi&projectname=mesa&packagename=$B&with_latest_build=false&with_latest_succeeded_build=false" -H 'accept: application/json' | jq -r '.builds.latest.source_package.version')
    else
      F=$(curl -s -X 'GET' "https://copr.fedorainfracloud.org/api_3/package/?ownername=%40asahi&projectname=$B&packagename=$PACKAGE&with_latest_build=false&with_latest_succeeded_build=false" -H 'accept: application/json' | jq -r '.builds.latest.source_package.version')
    fi
  else
    F=$(curl -s "https://bodhi.fedoraproject.org/updates/?search=$B&status=stable&releases=$REPO" | jq -r '[ first(.updates[] | { nvr: .builds.[].nvr } | select(.nvr | contains("'$B'"))) ]' | jq -r '.[].nvr' | sed "s/$B-\([0-9].*\)/\1/" | sed 's/.[^.]*$//')
  fi
  if [[ -z $F ]]; then
    F="/"
  else
    F=${F#rust-}
  fi
  printf "%-30s %-30s %-30s\n" "$O" "$F" "$V"
done
