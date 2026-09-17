#!/bin/bash
# Verify that the mesa release we build the FEX-Emu overlays from is the same one
# ALARM currently ships as the aarch64 mesa package.
#
# The overlays provide the x86 mesa used inside the FEX rootfs, while the host runs
# the aarch64 mesa from ALARM's [extra]. Both have to come from the same mesa release
# or the guest and host drivers disagree and FEX breaks. We used to get that for free
# because this PKGBUILD built both; now that the aarch64 package comes from ALARM it
# has to be checked.
#
# Env:
#   ALARM_MIRROR            override the mirror to query
#   SKIP_HOST_MESA_CHECK=1  build anyway (e.g. deliberately staging ahead of ALARM)

set -euo pipefail

if [ "${SKIP_HOST_MESA_CHECK:-0}" = "1" ]; then
  echo "SKIP_HOST_MESA_CHECK=1 set, not comparing against ALARM's mesa"
  exit 0
fi

cd "$(dirname "$0")"

# shellcheck source=/dev/null
our_pkgver=$(. ./PKGBUILD >/dev/null && echo "$pkgver")

MIRROR=${ALARM_MIRROR:-http://mirror.archlinuxarm.org}
DB=$(mktemp)
trap 'rm -f "$DB"' EXIT

echo "Fetching ALARM aarch64 [extra] database from $MIRROR"
curl -sfL --retry 3 --max-time 180 -o "$DB" "$MIRROR/aarch64/extra/extra.db.tar.gz"

# db entries look like "mesa-1:26.2.2-1/" -- keep epoch+pkgrel for the message,
# strip them for the comparison. "[0-9]" after the dash keeps out mesa-demos etc.
alarm_full=$(tar tzf "$DB" | sed 's!/$!!' | sed -n 's!^mesa-\([0-9][^/]*\)$!\1!p' | sort -u | head -1)
if [ -z "$alarm_full" ]; then
  echo "ERROR: no mesa package found in ALARM's [extra] database" >&2
  exit 1
fi
alarm_pkgver=${alarm_full#*:}   # drop epoch
alarm_pkgver=${alarm_pkgver%-*} # drop pkgrel

echo "overlay pkgver:    $our_pkgver"
echo "ALARM aarch64 mesa: $alarm_full (pkgver $alarm_pkgver)"

if [ "$our_pkgver" != "$alarm_pkgver" ]; then
  cat >&2 <<MSG

ERROR: mesa version mismatch.

  this PKGBUILD builds the FEX overlays from mesa  $our_pkgver
  ALARM ships aarch64 mesa                         $alarm_pkgver

The x86 overlays and the aarch64 host mesa must be the same mesa release or FEX
will break. Bump this PKGBUILD to $alarm_pkgver (or wait for ALARM to catch up)
and rebuild. Set SKIP_HOST_MESA_CHECK=1 to build anyway.
MSG
  exit 1
fi

echo "OK: overlays match ALARM's aarch64 mesa"
