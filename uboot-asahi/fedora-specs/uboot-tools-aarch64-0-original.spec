#global candidate rc0
%if 0%{?rhel}
%bcond_with toolsonly
%else
%bcond_without toolsonly
%endif

Name:     uboot-tools
Version:  2023.07
Release:  5%{?candidate:.%{candidate}}%{?dist}
Summary:  U-Boot utilities
License:  GPLv2+ BSD LGPL-2.1+ LGPL-2.0+
URL:      http://www.denx.de/wiki/U-Boot

ExcludeArch: s390x
Source0:  https://ftp.denx.de/pub/u-boot/u-boot-%{version}%{?candidate:-%{candidate}}.tar.bz2
Source1:  aarch64-boards

# Fedoraisms patches
# Needed to find DT on boot partition that's not the first partition
# Breaks Asahi, gated out for the time being
# Patch1:   uefi-distro-load-FDT-from-any-partition-on-boot-device.patch
Patch2:   smbios-Simplify-reporting-of-unknown-values.patch
Patch3:   0001-disable-NFS-support-by-default.patch
Patch4:   fix-release-rev.patch

# Board fixes and enablement
# RPi - uses RPI firmware device tree for HAT support
Patch5:   rpi-Enable-using-the-DT-provided-by-the-Raspberry-Pi.patch
# Rockchips improvements
Patch6:   rockchip-Add-initial-support-for-the-PinePhone-Pro.patch
Patch7:   0001-Revert-rockchip-rockpro64-Build-u-boot-rockchip-spi..patch

# Asahi patches from gen-asahi-patches.sh
# input: apple: Split off report handling into a separate file
Patch100: https://github.com/AsahiLinux/u-boot/commit/f28906758d6ae5edfd265df75e94697e50ba973e.patch#/asahi-f28906758d6ae5edfd265df75e94697e50ba973e.patch
# arm: apple: rtkit: Add support for AP power & syslogs
Patch101: https://github.com/AsahiLinux/u-boot/commit/d2afe04bc7fe1db4ff4323822f07ab36400ba902.patch#/asahi-d2afe04bc7fe1db4ff4323822f07ab36400ba902.patch
# arm: apple: rtkit: Add default buffer handlers
Patch102: https://github.com/AsahiLinux/u-boot/commit/403e6561b81e465863e980844f71a2c64a672492.patch#/asahi-403e6561b81e465863e980844f71a2c64a672492.patch
# arm: apple: rtkit: Add a generic RTKit helper driver
Patch103: https://github.com/AsahiLinux/u-boot/commit/ae41d19a39a7f1eff327d6e0eaef3a31cf44b055.patch#/asahi-ae41d19a39a7f1eff327d6e0eaef3a31cf44b055.patch
# input: apple: Add support for Apple MTP keyboard
Patch104: https://github.com/AsahiLinux/u-boot/commit/8ee5429c68beae7a8bfa6fd019fec017093d4483.patch#/asahi-8ee5429c68beae7a8bfa6fd019fec017093d4483.patch
# arm: apple: Add MTP keyboard options to defconfig
Patch105: https://github.com/AsahiLinux/u-boot/commit/89f1801b1a53b2cfd668f9dd92305a7b2410c9e2.patch#/asahi-89f1801b1a53b2cfd668f9dd92305a7b2410c9e2.patch
# phy: Add support for the Apple Type-C PHY
Patch106: https://github.com/AsahiLinux/u-boot/commit/ee317f3f2f00f9a6e29b09b6c8fc981dbeba51c6.patch#/asahi-ee317f3f2f00f9a6e29b09b6c8fc981dbeba51c6.patch
# apple: Set up file system firmware loader
Patch107: https://github.com/AsahiLinux/u-boot/commit/07e39c5e717c917187091687c17f6b8e2f6b18c5.patch#/asahi-07e39c5e717c917187091687c17f6b8e2f6b18c5.patch
# iopoll: Add readb_poll_sleep_timeout
Patch108: https://github.com/AsahiLinux/u-boot/commit/dae9ae738e9489bfbd19e57a5d71d5365eb893b8.patch#/asahi-dae9ae738e9489bfbd19e57a5d71d5365eb893b8.patch
# usb: xhci-pci: Load ASMedia XHCI controller firmware
Patch109: https://github.com/AsahiLinux/u-boot/commit/eb7a3b52c7ddcbb7641b85f63783240964c30d06.patch#/asahi-eb7a3b52c7ddcbb7641b85f63783240964c30d06.patch
# env: apple: Enable ENV_IS_IN_FAT
Patch110: https://github.com/AsahiLinux/u-boot/commit/be836c7e251ef6617b773740bdfe1e682144320c.patch#/asahi-be836c7e251ef6617b773740bdfe1e682144320c.patch
# apple: Nail down the EFI system partition
Patch111: https://github.com/AsahiLinux/u-boot/commit/3eaded9904190e322975ed936f5396726107ec20.patch#/asahi-3eaded9904190e322975ed936f5396726107ec20.patch
# apple: Generate EFI boot option for the EFI system partition
Patch112: https://github.com/AsahiLinux/u-boot/commit/c782e304a068b65e8c9926a974f2e3ae248a5d81.patch#/asahi-c782e304a068b65e8c9926a974f2e3ae248a5d81.patch
# scripts/dtc: Add support for floating-point literals
Patch113: https://github.com/AsahiLinux/u-boot/commit/de4de7a2d9132da92ad5cfc7cd71cdfb514b4b6f.patch#/asahi-de4de7a2d9132da92ad5cfc7cd71cdfb514b4b6f.patch
# arm: dts: apple: Update Apple M1 device trees
Patch114: https://github.com/AsahiLinux/u-boot/commit/38eae1d40a21019238b6b39be1ac648a737624e4.patch#/asahi-38eae1d40a21019238b6b39be1ac648a737624e4.patch
# arm: dts: apple: Add Apple M1 Pro/Max/Ultra device trees
Patch115: https://github.com/AsahiLinux/u-boot/commit/71345875f8f49f1ed1b5d4a183adeee77ab62e62.patch#/asahi-71345875f8f49f1ed1b5d4a183adeee77ab62e62.patch
# arm: dts: apple: Add Apple M2 device trees
Patch116: https://github.com/AsahiLinux/u-boot/commit/3d4ff95b859111da800f937f27be8775907d88c2.patch#/asahi-3d4ff95b859111da800f937f27be8775907d88c2.patch
# arm: dts: apple: Add Apple M2 Pro/Max device trees
Patch117: https://github.com/AsahiLinux/u-boot/commit/b9926890b37ecd2269858f7771b11932ae8b2ea2.patch#/asahi-b9926890b37ecd2269858f7771b11932ae8b2ea2.patch
# pci: apple: Enable CONFIG_SYS_PCI_64BIT
Patch118: https://github.com/AsahiLinux/u-boot/commit/3a6996e261a698d33627460efd1604deb44dde90.patch#/asahi-3a6996e261a698d33627460efd1604deb44dde90.patch
# arm: apple: Add initial Apple M2 Ultra support
Patch119: https://github.com/AsahiLinux/u-boot/commit/46d6873a2428a9e037660312d756c0ca412b1bdf.patch#/asahi-46d6873a2428a9e037660312d756c0ca412b1bdf.patch
# apple_m1_defconfig: Disable EFI variable store
Patch120: https://github.com/AsahiLinux/u-boot/commit/a79ee83e71a28825425cbe8ec9af8d2609367683.patch#/asahi-a79ee83e71a28825425cbe8ec9af8d2609367683.patch
# usb: xhci: Guard all calls to xhci_wait_for_event
Patch121: https://github.com/AsahiLinux/u-boot/commit/20df54a0355bbbc30b682f00d0648183734bf0bd.patch#/asahi-20df54a0355bbbc30b682f00d0648183734bf0bd.patch
# usb: xhci: Fix DMA address calculation in queue_trb
Patch122: https://github.com/AsahiLinux/u-boot/commit/ce490b6f0502cdba56004838f0b52bb5c942da1f.patch#/asahi-ce490b6f0502cdba56004838f0b52bb5c942da1f.patch
# usb: xhci: Better error handling in abort_td()
Patch123: https://github.com/AsahiLinux/u-boot/commit/8079fe5d87267868381dd1928c70e3d95042f7da.patch#/asahi-8079fe5d87267868381dd1928c70e3d95042f7da.patch
# usb: xhci: Add more debugging
Patch124: https://github.com/AsahiLinux/u-boot/commit/405aa60ef20a9cbaf770b1edc7ed1fc5feb1056e.patch#/asahi-405aa60ef20a9cbaf770b1edc7ed1fc5feb1056e.patch
# usb: storage: Clear endpoint stalls properly
Patch125: https://github.com/AsahiLinux/u-boot/commit/fca97b0c02d6d6e6a2a03631772369d5044756f8.patch#/asahi-fca97b0c02d6d6e6a2a03631772369d5044756f8.patch
# usb: xhci: Allow context state errors when halting an endpoint
Patch126: https://github.com/AsahiLinux/u-boot/commit/8b8a56cb1e8465a1a9ce40d329b70e83af485026.patch#/asahi-8b8a56cb1e8465a1a9ce40d329b70e83af485026.patch
# usb: xhci: Recover from halted non-control endpoints
Patch127: https://github.com/AsahiLinux/u-boot/commit/ad398d3dbf53703fea52dd3f144c64d1fb51fe09.patch#/asahi-ad398d3dbf53703fea52dd3f144c64d1fb51fe09.patch
# usb: xhci: Fail on attempt to queue TRBs to a halted endpoint
Patch128: https://github.com/AsahiLinux/u-boot/commit/d797bf2643013840f5247ae8a0511d38e7eacb00.patch#/asahi-d797bf2643013840f5247ae8a0511d38e7eacb00.patch
# usb: Pass through timeout to drivers
Patch129: https://github.com/AsahiLinux/u-boot/commit/ae6fe5bd9ad88dfe4bb40e35f79508e2de5d2a8d.patch#/asahi-ae6fe5bd9ad88dfe4bb40e35f79508e2de5d2a8d.patch
# usb: xhci: Hook up timeouts
Patch130: https://github.com/AsahiLinux/u-boot/commit/d063fc77c802a2ec4f1679cd1f8d95871e96e75c.patch#/asahi-d063fc77c802a2ec4f1679cd1f8d95871e96e75c.patch
# scsi: Fix a bunch of SCSI definitions.
Patch131: https://github.com/AsahiLinux/u-boot/commit/40d8c4d337e5c1a1bf55ded9eba3e2ce3a38dd6e.patch#/asahi-40d8c4d337e5c1a1bf55ded9eba3e2ce3a38dd6e.patch
# usb: storage: Increase read/write timeout
Patch132: https://github.com/AsahiLinux/u-boot/commit/311d4fe3b468dccb62cca8b49b648b30afeeacf0.patch#/asahi-311d4fe3b468dccb62cca8b49b648b30afeeacf0.patch
# usb: storage: Use the correct CBW lengths
Patch133: https://github.com/AsahiLinux/u-boot/commit/efc46536d89374c0bf07c95c95c597fecf366b38.patch#/asahi-efc46536d89374c0bf07c95c95c597fecf366b38.patch
# usb: storage: Implement 64-bit LBA support
Patch134: https://github.com/AsahiLinux/u-boot/commit/d4ef6c148d5152500ba11ad0d9c451fe46d8f693.patch#/asahi-d4ef6c148d5152500ba11ad0d9c451fe46d8f693.patch
# usb: Ignore endpoints in non-zero altsettings
Patch135: https://github.com/AsahiLinux/u-boot/commit/039791d6bc96194defda3c4d6daffad11d64e2a1.patch#/asahi-039791d6bc96194defda3c4d6daffad11d64e2a1.patch
# usb: hub: Add missing reset recovery delay
Patch136: https://github.com/AsahiLinux/u-boot/commit/d63c269a019b15a4143957d20e162a8e460056b3.patch#/asahi-d63c269a019b15a4143957d20e162a8e460056b3.patch
# apple_m1_defconfig: Turn on CONFIG_SYS_64BIT_LBA
Patch137: https://github.com/AsahiLinux/u-boot/commit/97bb2192361741021a4291d19f88a2bb69ad2f32.patch#/asahi-97bb2192361741021a4291d19f88a2bb69ad2f32.patch
# usb: kbd: Ignore Yubikeys
Patch138: https://github.com/AsahiLinux/u-boot/commit/b7cc8dac8646c91690adcccb4d065135ff540684.patch#/asahi-b7cc8dac8646c91690adcccb4d065135ff540684.patch
# usb: xhci: Do not panic on event timeouts
Patch139: https://github.com/AsahiLinux/u-boot/commit/b4cc61d057065794933120215d8b60f8a83380a2.patch#/asahi-b4cc61d057065794933120215d8b60f8a83380a2.patch
# arm: apple: rtkit: Add OSLog buffer support
Patch140: https://github.com/AsahiLinux/u-boot/commit/0190c00f5687ef54817f75b86cec8595b736c3f8.patch#/asahi-0190c00f5687ef54817f75b86cec8595b736c3f8.patch
# arm: apple: rtkit: Add endpoint field to buffers
Patch141: https://github.com/AsahiLinux/u-boot/commit/35693e4799c9cd61f3c970aaad920b9b143959dd.patch#/asahi-35693e4799c9cd61f3c970aaad920b9b143959dd.patch
# arm: apple: rtkit: Support allocating OSLog out of SRAM in helper
Patch142: https://github.com/AsahiLinux/u-boot/commit/0203fd3d70b229ea2e50abe40b85ae8adc5c49f3.patch#/asahi-0203fd3d70b229ea2e50abe40b85ae8adc5c49f3.patch

BuildRequires:  bc
BuildRequires:  bison
BuildRequires:  dtc
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gnutls-devel
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  perl-interpreter
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-libfdt
BuildRequires:  SDL2-devel
BuildRequires:  swig
%if %{with toolsonly}
%ifarch aarch64
BuildRequires:  arm-trusted-firmware-armv8
BuildRequires:  python3-pyelftools
%endif
%endif
Requires:       dtc

%description
This package contains a few U-Boot utilities - mkimage for creating boot images
and fw_printenv/fw_setenv for manipulating the boot environment variables.

%if %{with toolsonly}
%ifarch aarch64
%package     -n uboot-images-armv8
Summary:     U-Boot firmware images for aarch64 boards
BuildArch:   noarch

%description -n uboot-images-armv8
U-Boot firmware binaries for aarch64 boards
%endif
%endif

%prep
%autosetup -p1 -n u-boot-%{version}%{?candidate:-%{candidate}}

cp %SOURCE1 .

%build
mkdir builds

%make_build HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="" tools-only_defconfig O=builds/
%make_build HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="" tools-all O=builds/

%if %{with toolsonly}
%ifarch aarch64
for board in $(cat %{_arch}-boards)
do
  echo "Building board: $board"
  mkdir builds/$(echo $board)/

  # ATF selection, needs improving, suggestions of ATF SoC to Board matrix welcome
  sun50i=(a64-olinuxino amarula_a64_relic bananapi_m2_plus_h5 bananapi_m64 libretech_all_h3_cc_h5 nanopi_a64 nanopi_neo2 nanopi_neo_plus2 orangepi_pc2 orangepi_prime orangepi_win orangepi_zero_plus orangepi_zero_plus2 pine64-lts pine64_plus pinebook pinephone pinetab sopine_baseboard teres_i)
  if [[ " ${sun50i[*]} " == *" $board "* ]]; then
    echo "Board: $board using sun50i_a64"
    cp /usr/share/arm-trusted-firmware/sun50i_a64/* builds/$(echo $board)/
  fi
  sun50h6=(beelink_gs1 orangepi_3 orangepi_lite2 orangepi_one_plus orangepi_zero2 pine_h64 tanix_tx6)
  if [[ " ${sun50h6[*]} " == *" $board "* ]]; then
    echo "Board: $board using sun50i_h6"
    cp /usr/share/arm-trusted-firmware/sun50i_h6/* builds/$(echo $board)/
  fi
  rk3328=(evb-rk3328 nanopi-r2s-rk3328 rock64-rk3328 rock-pi-e-rk3328 roc-cc-rk3328)
  if [[ " ${rk3328[*]} " == *" $board "* ]]; then
    echo "Board: $board using rk3328"
    cp /usr/share/arm-trusted-firmware/rk3328/bl31.elf builds/$(echo $board)/atf-bl31
  fi
  rk3399=(evb-rk3399 ficus-rk3399 firefly-rk3399 khadas-edge-captain-rk3399 khadas-edge-rk3399 khadas-edge-v-rk3399 leez-rk3399 nanopc-t4-rk3399 nanopi-m4-2gb-rk3399 nanopi-m4b-rk3399 nanopi-m4-rk3399 nanopi-neo4-rk3399 nanopi-r4s-rk3399 orangepi-rk3399 pinebook-pro-rk3399 pinephone-pro-rk3399 puma-rk3399 rock960-rk3399 rock-pi-4c-rk3399 rock-pi-4-rk3399 rock-pi-n10-rk3399pro rockpro64-rk3399 roc-pc-mezzanine-rk3399 roc-pc-rk3399 eaidk-610-rk3399)
  if [[ " ${rk3399[*]} " == *" $board "* ]]; then
    echo "Board: $board using rk3399"
    cp /usr/share/arm-trusted-firmware/rk3399/* builds/$(echo $board)/
    cp builds/$(echo $board)/bl31.elf builds/$(echo $board)/atf-bl31
  fi
  # End ATF

  BINMAN_ALLOW_MISSING=1 make $(echo $board)_defconfig O=builds/$(echo $board)/
  BINMAN_ALLOW_MISSING=1 %make_build HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="" O=builds/$(echo $board)/

  # build spi images for rockchip boards with SPI flash
  rkspi=(rock64-rk3328)
  if [[ " ${rkspi[*]} " == *" $board "* ]]; then
    echo "Board: $board with SPI flash"
    builds/$(echo $board)/tools/mkimage -n rk3328 -T rkspi -d builds/$(echo $board)/tpl/u-boot-tpl.bin:builds/$(echo $board)/spl/u-boot-spl.bin builds/$(echo $board)/idbloader.spi
  fi
  rkspi=(evb-rk3399 khadas-edge-captain-rk3399 khadas-edge-rk3399 khadas-edge-v-rk3399 nanopc-t4-rk3399 pinebook-pro-rk3399 pinephone-pro-rk3399 rockpro64-rk3399 roc-pc-mezzanine-rk3399 roc-pc-rk3399)
  if [[ " ${rkspi[*]} " == *" $board "* ]]; then
    echo "Board: $board with SPI flash"
    builds/$(echo $board)/tools/mkimage -n rk3399 -T rkspi -d builds/$(echo $board)/tpl/u-boot-tpl.bin:builds/$(echo $board)/spl/u-boot-spl.bin builds/$(echo $board)/idbloader.spi
  fi
done

%endif
%endif

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/uboot/

%if %{with toolsonly}
%ifarch aarch64
for board in $(ls builds)
do
 mkdir -p %{buildroot}%{_datadir}/uboot/$(echo $board)/
 for file in u-boot.bin u-boot.dtb u-boot.img u-boot-dtb.img u-boot.itb u-boot-sunxi-with-spl.bin u-boot-rockchip.bin idbloader.img idbloader.spi spl/boot.bin spl/sunxi-spl.bin
 do
  if [ -f builds/$(echo $board)/$(echo $file) ]; then
    install -p -m 0644 builds/$(echo $board)/$(echo $file) %{buildroot}%{_datadir}/uboot/$(echo $board)/
  fi
 done
done

# For Apple M1 we also need the nodtb variant
install -p -m 0644 builds/apple_m1/u-boot-nodtb.bin %{buildroot}%{_datadir}/uboot/apple_m1/u-boot-nodtb.bin
%endif

# Bit of a hack to remove binaries we don't use as they're large
%ifarch aarch64
for board in $(ls builds)
do
  rm -f %{buildroot}%{_datadir}/uboot/$(echo $board)/u-boot.dtb
  if [ -f %{buildroot}%{_datadir}/uboot/$(echo $board)/u-boot-sunxi-with-spl.bin ]; then
    rm -f %{buildroot}%{_datadir}/uboot/$(echo $board)/u-boot{,-dtb}.*
  fi
  if [ -f %{buildroot}%{_datadir}/uboot/$(echo $board)/MLO ]; then
    rm -f %{buildroot}%{_datadir}/uboot/$(echo $board)/u-boot.bin
  fi
  if [ -f %{buildroot}%{_datadir}/uboot/$(echo $board)/SPL ]; then
    rm -f %{buildroot}%{_datadir}/uboot/$(echo $board)/u-boot.bin
  fi
  if [ -f %{buildroot}%{_datadir}/uboot/$(echo $board)/u-boot.imx ]; then
    rm -f %{buildroot}%{_datadir}/uboot/$(echo $board)/u-boot.bin
  fi
  if [ -f %{buildroot}%{_datadir}/uboot/$(echo $board)/u-boot-spl.kwb ]; then
    rm -f %{buildroot}%{_datadir}/uboot/$(echo $board)/u-boot.*
    rm -f %{buildroot}%{_datadir}/uboot/$(echo $board)/u-boot-spl.bin
  fi
  if [ -f %{buildroot}%{_datadir}/uboot/$(echo $board)/idbloader.img ]; then
    rm -f %{buildroot}%{_datadir}/uboot/$(echo $board)/u-boot.bin
    rm -f %{buildroot}%{_datadir}/uboot/$(echo $board)/u-boot{,-dtb}.img
  fi
done
%endif
%endif

for tool in dumpimage env/fw_printenv fit_check_sign fit_info gdb/gdbcont gdb/gdbsend gen_eth_addr gen_ethaddr_crc ifwitool img2srec kwboot mkeficapsule mkenvimage mkimage mksunxiboot ncb proftool sunxi-spl-image-builder
do
install -p -m 0755 builds/tools/$tool %{buildroot}%{_bindir}
done
install -p -m 0644 doc/mkimage.1 %{buildroot}%{_mandir}/man1

install -p -m 0755 builds/tools/env/fw_printenv %{buildroot}%{_bindir}
( cd %{buildroot}%{_bindir}; ln -sf fw_printenv fw_setenv )

# Copy some useful docs over
mkdir -p builds/docs
cp -p board/hisilicon/hikey/README builds/docs/README.hikey
cp -p board/rockchip/evb_rk3399/README builds/docs/README.evb_rk3399
cp -p board/sunxi/README.sunxi64 builds/docs/README.sunxi64
cp -p board/sunxi/README.nand builds/docs/README.sunxi-nand

%files
%doc README doc/develop/distro.rst doc/README.gpt
%doc doc/README.rockchip doc/develop/uefi doc/usage doc/arch/arm64.rst
%doc builds/docs/* doc/board/amlogic/ doc/board/rockchip/
%{_bindir}/*
%{_mandir}/man1/mkimage.1*
%dir %{_datadir}/uboot/

%if %{with toolsonly}
%ifarch aarch64
%files -n uboot-images-armv8
%{_datadir}/uboot/*
%endif
%endif

%changelog
* Thu Oct 12 2023 Davide Cavalca <dcavalca@fedoraproject.org> - 2023.07-5
- Resync to asahi-v2023.07.02-3

* Wed Aug 02 2023 Davide Cavalca <dcavalca@fedoraproject.org> - 2023.07-4
- Resync to asahi-v2023.07.02-2

* Wed Aug 02 2023 Davide Cavalca <dcavalca@fedoraproject.org> - 2023.07-3
- Backport Asahi Linux patches for Apple Silicon support

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2023.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.07-1
- Update to 2023.07 GA

* Fri Jun 16 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.07-0.4.rc4
- Disable NFS by default

* Mon Jun 12 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.07-0.3.rc4
- Update to 2023.07 RC4

* Sun Jun 11 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.07-0.2.rc3
- Update to 2023.07 RC3
- Fixes for the Pinephone Pro, RockPro64

* Wed May 17 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.07-0.1.rc2
- Update to 2023.07 RC2

* Tue Apr 04 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.04-1
- Update to 2023.04 GA

* Tue Mar 28 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.04-0.4.rc5
- Update to 2023.04 RC5
- Drop upstreamed patches
- Rockchip boot fixes

* Tue Mar 14 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.04-0.3.rc4
- Update to 2023.04 RC4

* Fri Feb 17 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.04-0.2.rc2
- Update to 2023.04 RC2

* Tue Jan 31 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.04-0.1.rc1
- Update to 2023.04 RC1
- Drop bmp_logo tool

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2023.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.01-1
- Update to 2023.01 GA

* Sat Dec 31 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.01-0.4.rc4
- Update PinePhone Pro to latest rev

* Tue Dec 20 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.01-0.3.rc4
- Update to 2023.01 RC4

* Mon Dec 05 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.01-0.2.rc3
- Update to 2023.01 RC3

* Thu Nov 24 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2023.01-0.1.rc2
- Update to U-Boot 2023.01 RC2
- Update Pinephone Pro patches

* Mon Oct 10 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.10-1
- Update to 2022.10 GA

* Tue Sep 06 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.10-0.6.rc4
- Update SMBIOS patch

* Tue Sep 06 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.10-0.5.rc4
- Update to 2022.10 RC4
- Fix for booting Rockchip devices from NVME

* Tue Aug 23 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.10-0.4.rc3
- Update to 2022.10 RC3

* Mon Aug 22 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 2022.10-0.3.rc1
- Install nodtb variant for Apple M1 (rhbz#2068958)

* Tue Aug 16 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.10-0.2.rc1
- Fix for DT property propogation via firmware

* Thu Jul 28 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.10-0.1.rc1
- Update to 2022.10 RC1
- Enable LTO for firmware builds

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 17 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.07-1
- Update to 2022.07 GA

* Mon Jul 04 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.07-0.6.rc6
- Update to 2022.07 RC6

* Mon Jun 20 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.07-0.5.rc5
- Update to 2022.07 RC5

* Sun Jun 12 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.07-0.4.rc4
- Update to 2022.07 RC4
- Some minor Rockchips device fixes

* Wed May 25 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.07-0.3.rc3
- Update to 2022.07 RC3

* Sat May 14 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.07-0.2.rc2
- Update to 2022.07 RC2

* Tue Apr 26 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.07-0.1.rc1
- Update to 2022.07 RC1

* Mon Apr 04 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.04-1
- Update to 2022.04 GA

* Mon Mar 28 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.04-0.4.rc5
- Update to 2022.04 RC5

* Tue Mar 08 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.04-0.3.rc3
- Update to 2022.04 RC3
- Enable new Rockchip devices

* Tue Feb 15 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.04-0.2.rc2
- Update to 2022.04 RC2

* Wed Feb 02 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.04-0.1.rc1
- Update to 2022.04 RC1

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.01-1
- Update to 2022.01

* Wed Jan 05 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.01-0.3.rc4
- Upstream fixes for PHY and UEFI

* Mon Dec 20 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.01-0.2.rc4
- Update to 2022.01 RC4

* Mon Nov 15 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2022.01-0.1.rc2
- Update to 2022.01 RC2

* Mon Nov 15 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.10-3
- Fixes for rk3399 devices

* Thu Oct 14 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.10-2
- Fix booting from MMC for Rockchip 3399 (rhbz #2014182)
- Enable new rk3399 devices (Leez, NanoPi-M4B, NanoPi-4S, NanoPi-T4) (rhbz #2009126)

* Mon Oct 04 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.10-1
- Update to 2021.10

* Mon Sep 27 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.10-0.7.rc5
- Update to 2021.10 RC5

* Wed Sep 15 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.10-0.6.rc4
- Update to 2021.10 RC4
- Proposed fix for RPi MMC clock issue

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2021.10-0.6.rc3
- Rebuilt with OpenSSL 3.0.0

* Mon Aug 30 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.10-0.5.rc3
- Update to 2021.10 RC3

* Tue Aug 24 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.10-0.4.rc2
- Fix for Raspberry Pi firmware properties

* Mon Aug 23 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.10-0.3.rc2
- Fix for rockchip SPI

* Mon Aug 16 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.10-0.2.rc2
- Update to 2021.10 RC2

* Sun Aug 08 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.10-0.1.rc1
- Update to 2021.10 RC1

* Thu Jul 22 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.07-2
- Fix regression for Rockchip devices running firmware from SPI flash

* Mon Jul 05 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.07-1
- Update to 2021.07 GA

* Mon Jun 28 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.07-0.6.rc5
- Update to 2021.07 RC5
- Build SPI fash images for ROC-PC-RK3399

* Mon Jun 07 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.07-0.5.rc4
- Update to 2021.07 RC4

* Sat Jun 05 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.07-0.4.rc3
- Fix AllWinner devices booting from mSD/MMC

* Tue May 25 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.07-0.3.rc3
- Update to 2021.07 RC3
- Build against ATF 2.5 GA

* Thu May 13 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.07-0.2.rc2
- Build against new ATF 2.5-rc1

* Mon May 10 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.07-0.1.rc2
- Update to 2021.07 RC2

* Wed Apr 28 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.04-3
- Upstream fix for console regression (rhbz 1946278)
- Fix for fallback.efi crash (rhbz 1733817)

* Wed Apr 21 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.04-2
- Revert keyboard console regression change (rhbz 1946278)

* Sun Apr 18 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.04-1
- Update to 2021.04 GA
- Fix DTB load check (rhbz 1946278)
- Build Rockchip SPI support as idbloader.spi
- Fixes for Rockchip devices
- Build Turris Omnia for MMC/SPI/UART

* Wed Mar 17 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.04-0.6.rc4
- Update to 2021.04 RC4
- Move to upstream fix for SMP on RPi3B and RPi3B+

* Sat Mar 13 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.04-0.5.rc3
- Fix for SMP on RPi3B and RPi3B+
- Initial support for Pinephone 3Gb edition

* Mon Mar 08 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.04-0.4.rc3
- Update to 2021.04 RC3

* Tue Feb 16 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.04-0.3.rc2
- Update to 2021.04 RC2

* Mon Feb 15 2021 Dennis Gilmore <dennis@ausil.us>
- build spi and uart images in addition to mmc for helios4 and clearfog

* Wed Feb 10 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.04-0.2.rc1
- Fixes for network issues on some Allwinner devices

* Mon Feb 01 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.04-0.1.rc1
- Update to 2021.04 RC1
- Add new upstream devices

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.01-1
- Update to 2021.01 GA
- Updates for Raspberry Pi 4 Series of devices

* Tue Jan  5 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.01-0.5.rc5
- Update to 2021.01 RC5

* Sun Dec 27 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.01-0.4.rc4
- Update to 2021.01 RC4
- Latest RPi-400/CM4 support patch

* Tue Dec 15 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.01-0.3.rc3
- Update to 2021.01 RC3
- Latest RPi-400/CM4 support patch
- Re-enable previously disabled device support

* Mon Dec 14 2020 Javier Martinez Canillas <javierm@redhat.com> - 2021.01-0.2.rc2
- Fix a "scan_dev_for_efi" not defined error

* Sun Nov 22 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2021.01-0.1.rc2
- Update to 2021.01 RC2
- Latest Pinebook Pro display patches
- Initial RPi-400 support patch
- Update Fedora specific patches

* Sun Nov  8 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.10-3
- Fix SPI on Rockchip devices
- Latest Pinebook Pro display patches
- Fix Keyboard and USB-A ports on Pinebook Pro

* Wed Oct 28 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.10-2
- Fix kernel installs for non EBBR systems
- Fix for wired networks on some Allwinner devices

* Tue Oct 06 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.10-1
- Update to 2020.10

* Sun Sep 27 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.10-0.6.rc5
- Initial support for display output on Pinebook Pro

* Tue Sep 22 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.10-0.5.rc5
- Update to 2020.10 RC5

* Wed Sep 09 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.10-0.4.rc4
- Update to 2020.10 RC4

* Wed Aug 19 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.10-0.3.rc2
- Enable a number of new Rockchip devices

* Mon Aug 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.10-0.2.rc2
- Update to 2020.10 RC2

* Tue Jul 28 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.10-0.1.rc1
- 2020.10 RC1

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 2020.07-2
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Mon Jul 06 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.07-1
- 2020.07 GA

* Tue Jun 23 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.07-0.5.rc5
- 2020.07 RC5

* Thu Jun 18 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.07-0.4.rc4
- Update various patches to latest upstream

* Wed Jun 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.07-0.3.rc4
- 2020.07 RC4
- Minor updates and other fixes

* Tue May 12 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.07-0.2.rc2
- 2020.07 RC2
- Minor device updates

* Wed Apr 29 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.07-0.1.rc1
- 2020.07 RC1

* Tue Apr 21 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.04-4
- Initial support for USB on Rasperry Pi 4

* Tue Apr 21 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.04-3
- Ship u-boot-rockchip.bin for SPI flash

* Mon Apr 20 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.04-2
- Fix ATF for new aarch64 devices
- Fix Wandboard board detection (rhbz 1825247)
- Fix mSD card on RockPro64
- Enable (inital) Pinebook Pro

* Tue Apr 14 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.04-1
- 2020.04

* Tue Apr  7 2020 Peter Robinson <pbrobinson@fedoraproject.org> 2020.04-0.7-rc5
- 2020.04 RC5

* Tue Mar 31 2020 Peter Robinson <pbrobinson@fedoraproject.org> 2020.04-0.6-rc4
- 2020.04 RC4
- Updates for NVIDIA Jetson platforms
- Support RNG for random seed for KASLR on some Rockchip devices

* Thu Mar 26 2020 Peter Robinson <pbrobinson@fedoraproject.org> 2020.04-0.5-rc3
- Fix ext4 alignment issue seen on some NXP i.MX devices

* Wed Feb 26 2020 Peter Robinson <pbrobinson@fedoraproject.org> 2020.04-0.4-rc3
- 2020.04 RC3

* Thu Feb 13 2020 Peter Robinson <pbrobinson@fedoraproject.org> 2020.04-0.3-rc2
- 2020.04 RC2

* Sun Feb  2 2020 Peter Robinson <pbrobinson@fedoraproject.org> 2020.04-0.2-rc1
- Update genet NIC driver

* Wed Jan 29 2020 Peter Robinson <pbrobinson@fedoraproject.org> 2020.04-0.1-rc1
- 2020.04 RC1

* Tue Jan  7 2020 Peter Robinson <pbrobinson@fedoraproject.org> 2020.01-1
- 2020.01
