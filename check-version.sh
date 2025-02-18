#!/bin/bash

declare -A mappings

mappings["bankstown"]="lv2-bankstown"
mappings["widevine"]="widevine-installer"
mappings["lzfse"]="lzfse-libs"
mappings["FEX-Emu"]="fex-emu"
mappings["fex-emu-rootfs-arch"]="fex-emu-rootfs-fedora"
mappings["linux-asahi"]="kernel-16k"
mappings["linux-asahi-headers"]="kernel-headers"
mappings["mesa"]="mesa-vulkan-drivers"
mappings["alsa-ucm-conf-asahi"]="alsa-ucm-asahi"
mappings["tiny-dfr"]="rust-tiny-dfr"
mappings["binfmt-dispatcher"]="rust-binfmt-dispatcher"
mappings["muvm"]="rust-muvm"
mappings["asahi-bless"]="rust-asahi-bless"
mappings["triforce-lv2"]="rust-triforce-lv2"
mappings["speakersafetyd"]="rust-speakersafetyd"

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
  if [[ -n "${mappings[$B]}" ]]; then
    B=${mappings[$B]}
  fi
  F=$(curl -s "https://bodhi.fedoraproject.org/updates/?search=$B&status=stable&releases=F41" | jq -r '[ first(.updates.[] | select(.status | contains("stable"))) | { nvr: .builds.[].nvr } ]' | jq -r '.[] | select(.nvr | contains ("'$B'"))' | jq -r '.nvr')
  if [[ -n $F ]]; then
    F=$(echo $F | sed "s/$B-\([0-9].*\)/\1/")
  else
    F="/"
  fi
  printf "%-30s %-30s %-30s\n" "$O" "$F" "$V"
done
