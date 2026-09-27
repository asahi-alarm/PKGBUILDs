# Experimental Asahi USB-C display kernel

This package builds Asahi's existing `fairydust` branch at commit
`ce9f2eba72c061a50b2d790450e90af3439d8c24` (Linux 7.1.13). It is intended for
hardware testing, not promotion of experimental support to a stable default.
The driver implementation is entirely upstream Asahi work.

It installs alongside `linux-asahi`, with distinct kernel, initramfs and module
names. The kernel configuration is copied from this repository's stock package,
except for the local version suffix. The empty `CONFIG_LOCALVERSION`, combined
with `localversion.10-pkgrel`, gives release `7.1.13-3-1-fairydust`.

## Build

Install the PKGBUILD's build dependencies. With rustup, select a compiler and
install its source and formatter components before running makepkg. The initial
build uses Rust 1.93.1, matching the stock package configuration:

```sh
rustup toolchain install 1.93.1 --profile minimal --component rust-src,rustfmt
RUSTUP_TOOLCHAIN=1.93.1 MAKEFLAGS=-j6 makepkg
```

The source archive is pinned to a full commit and verified with SHA-256.
`makepkg` builds packages only. It does not install them or reboot.

## Boot activation is separate

**Installing this package alone does not enable the display.** The experimental
device trees must also reach m1n1. The kernel release deliberately does not end
in `-ARCH`, excluding it from the current Asahi ALARM `update-m1n1` script's
automatic device-tree selection. Inspect that script on your system: this
behavior is distribution-specific and could change.

Before activation, preserve the stock kernel package, a stock GRUB entry, the
current m1n1 boot image, and the bootloader configuration. Device trees embedded
in m1n1 are shared between GRUB entries; selecting the stock kernel does not
itself restore the old device trees. Have a way to restore the original m1n1
image if boot fails before GRUB. Do not assume an ordinary filesystem snapshot
includes the EFI system partition.

After reviewing the system's boot layout, activation requires an explicit
`DTBS` selection when invoking `update-m1n1`, plus a boot entry and initramfs for
the new kernel. Keep the stock entry as the normal default and test the new
entry manually first. Stock package updates may restore stock device trees;
recheck the boot image when repeating a test.

## J293 test setup

For the MacBook Pro 13-inch M1 (2020), the pinned branch connects the external
display engine to `typec1`, labeled `USB-C Left-front` in the device tree. Use
the port nearer the trackpad. Begin with the monitor connected before boot,
then test hotplug and suspend separately. USB hub operation alone does not
establish that display output works.

Record the exact monitor, adapter, resolution, kernel release, connector state,
hotplug and suspend behavior, reporting each test separately.

Both packages built successfully on a J293, and HDMI video was confirmed through
an ADAM hub to an LG 32GS75Q-B. After a local monitor configuration adjustment,
Hyprland reported 2560x1440@59.951 at scale 1. On the first boot, the display
appeared after reconnecting the hub; repeatability has not been established.
Suspend/resume, HDMI audio and repeated hotplug cycles remain untested.

## References

- https://asahilinux.org/2026/02/progress-report-6-19/
- https://github.com/AsahiLinux/linux/tree/fairydust
- https://asahilinux.org/docs/platform/feature-support/m1/

Packaging changes and this documentation were prepared with AI assistance.
The package uses the upstream kernel source without additional driver changes.
