#!/bin/bash

declare -A mappings
declare -A mappings_fedora_repo

mappings_fedora_repo["bankstown"]="EPEL-10.0"
mappings_fedora_repo["alsa-ucm-conf-asahi"]="EPEL-10.0"

mappings["bankstown"]="rust-bankstown-lv2"
mappings["widevine"]="widevine-installer"
mappings["lzfse"]="lzfse-libs"
mappings["FEX-Emu"]="fex-emu"
mappings["fex-emu-rootfs-arch"]="fex-emu-rootfs-fedora"
mappings["linux-asahi"]="kernel-16k"
mappings["linux-asahi-headers"]="kernel-headers"
mappings["mesa"]="mesa-vulkan-drivers"
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

DB=asahi-alarm.db.tar.gz

wget -O $DB -q https://github.com/asahi-alarm/asahi-alarm/releases/download/aarch64/$DB
PKGS=$(tar tvf $DB | grep -v .sig | grep -v desc | awk '{ print $6}' | sed 's!/$!!g')
rm $DB

echo

printf "%-30s %-30s %-30s\n" "Package" "Fedora Version" "ALARM Version"
for P in $PKGS; do
  B=$(echo $P | sed 's/\([A-Za-z-]*\)-[0-9].*/\1/')
  V=$(echo $P | sed "s/$B-\([0-9].*\)/\1/")
  if [[ "$B" == *overlay* ]]; then
    continue
  fi
  O=$B

  if [[ -n "${mappings_fedora_repo[$B]}" ]]; then
    REPO=${mappings_fedora_repo[$B]}
  else
    REPO="F41"
  fi

  if [[ -n "${mappings[$B]}" ]]; then
    B=${mappings[$B]}
  fi

  F=$(curl -s "https://bodhi.fedoraproject.org/updates/?search=$B&status=stable&releases=$REPO" | jq -r '[ first(.updates[] | { nvr: .builds.[].nvr } | select(.nvr | contains("'$B'"))) ]' | jq -r '.[].nvr' | sed "s/$B-\([0-9].*\)/\1/" | sed 's/.[^.]*$//')
  if [[ -z $F ]]; then
    F="/"
  fi
  printf "%-30s %-30s %-30s\n" "$O" "$F" "$V"
done
