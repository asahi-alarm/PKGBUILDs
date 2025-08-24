#global candidate rc0
%bcond_without toolsonly

# Set it to "opensbi" (stable) or "opensbi-unstable" (unstable, git)
%global opensbi opensbi

Name:     uboot-tools
Version:  2025.07
Release:  103%{?candidate:.%{candidate}}%{?dist}
Epoch:    1
Summary:  U-Boot utilities
# Automatically converted from old format: GPLv2+ BSD LGPL-2.1+ LGPL-2.0+ - review is highly recommended.
License:  GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LGPL-2.1-or-later AND LGPL-2.0-or-later
URL:      http://www.denx.de/wiki/U-Boot
ExcludeArch: s390x
Source0:  https://ftp.denx.de/pub/u-boot/u-boot-%{version}%{?candidate:-%{candidate}}.tar.bz2
Source1:  aarch64-boards
Source2:  riscv64-boards

# Fedora patches to enable/disable features
Patch1:   disable-VBE-by-default.patch
Patch2:   enable-bootmenu-by-default.patch
# This is now legacy, most devices use bootflow, we keep this for the laggards
Patch3:   uefi-distro-load-FDT-from-any-partition-on-boot-device.patch
# Identify VFAT partitions as ESP, allows EFI setvar on our images
Patch4:   uefi-Add-all-options-for-EFI-System-Partitions.patch
# New function to find fdt for loading from disk
Patch6:   uefi-initial-find_fdt_location-for-finding-the-DT-on-disk.patch
# Enable UEFI SetVariable for devices without backed storage
Patch7:   uefi-enable-SetVariableRT-with-volotile-storage.patch
# Enable UEFI HTTPS boot for all Fedora firmware
Patch8:   uefi-enable-https-boot-by-default.patch
# Fix PPC tools build
Patch9:   tools-termios_linux.h-Fix-build-error-on-ppc64.patch

# Device improvments
# USB-PD improvements
Patch10:  USB-PD-TCPM-improvements.patch
# Rockchips improvements
Patch11:  rockchip-Enable-preboot-start-for-pci-usb.patch
# Rockchip DT rebase for fixes
Patch12:  Rebase-to-upstream-6.15.5-rockchip-DTs.patch
Patch13:  Initial-MNT-Reform2-support.patch
# Fix Jetson Nano
Patch14:  p3450-fix-board.patch

# Add EFI_PARTITION_INFO_PROTOCOL support
Patch20:  disk-efi-Move-logic-to-get-a-GPT-entry-into-a-helper.patch
Patch21:  disk-efi-expose-the-part_get_gpt_pte-helper-function.patch
Patch22:  efi_loader-disk-add-EFI_PARTITION_INFO_PROTOCOL-supp.patch
Patch23:  efi_selftest-Add-basic-partition-info-check-to-block.patch

# Build with OPENSSL_NO_ENGINE
Patch90:  openssl-no-engine.patch

# input: apple: Split off report handling into a separate file
Patch100: https://github.com/AsahiLinux/u-boot/commit/a0f2eb2c0e05cbfa655009ca232fb454b9904bba.patch#/asahi-a0f2eb2c0e05cbfa655009ca232fb454b9904bba.patch
# input: apple: Add support for Apple MTP keyboard
Patch101: https://github.com/AsahiLinux/u-boot/commit/4d5839ad4b935f5555613123f4d0e0b788b95e7b.patch#/asahi-4d5839ad4b935f5555613123f4d0e0b788b95e7b.patch
# arm: apple: Add MTP keyboard options to defconfig
Patch102: https://github.com/AsahiLinux/u-boot/commit/d2bdb6fec9130813662e623b29a0d1487b70cf77.patch#/asahi-d2bdb6fec9130813662e623b29a0d1487b70cf77.patch
# apple: Set up file system firmware loader
Patch103: https://github.com/AsahiLinux/u-boot/commit/d00dd16498d0c0b15172561cac4c5b4901150298.patch#/asahi-d00dd16498d0c0b15172561cac4c5b4901150298.patch
# iopoll: Add readb_poll_sleep_timeout
Patch104: https://github.com/AsahiLinux/u-boot/commit/04d2676ac2d74aae3bc797f30db2a161f98a3ac8.patch#/asahi-04d2676ac2d74aae3bc797f30db2a161f98a3ac8.patch
# usb: xhci-pci: Load ASMedia XHCI controller firmware
Patch105: https://github.com/AsahiLinux/u-boot/commit/08980606eb0dc35252df8b67dd73775e1604838b.patch#/asahi-08980606eb0dc35252df8b67dd73775e1604838b.patch
# env: apple: Enable ENV_IS_IN_FAT
Patch106: https://github.com/AsahiLinux/u-boot/commit/52d2343f9dd4cf754e55168a83673a3f1a957697.patch#/asahi-52d2343f9dd4cf754e55168a83673a3f1a957697.patch
# apple: Nail down the EFI system partition
Patch107: https://github.com/AsahiLinux/u-boot/commit/1d4edd84a380da7e14272fa56c4ff33ca4ce9dba.patch#/asahi-1d4edd84a380da7e14272fa56c4ff33ca4ce9dba.patch
# scripts/dtc: Add support for floating-point literals
Patch108: https://github.com/AsahiLinux/u-boot/commit/afdf8e769379ad9f4ff3ed7ef4145a7c3f5d36a7.patch#/asahi-afdf8e769379ad9f4ff3ed7ef4145a7c3f5d36a7.patch
# arm: dts: apple: Update Apple M1 device trees
Patch109: https://github.com/AsahiLinux/u-boot/commit/4f89bdfe053b367dae6b76e182087c2165654010.patch#/asahi-4f89bdfe053b367dae6b76e182087c2165654010.patch
# arm: dts: apple: Add Apple M1 Pro/Max/Ultra device trees
Patch110: https://github.com/AsahiLinux/u-boot/commit/783edefb9c2fbfdf170697aec2d6b6245b48b0cb.patch#/asahi-783edefb9c2fbfdf170697aec2d6b6245b48b0cb.patch
# arm: dts: apple: Add Apple M2 device trees
Patch111: https://github.com/AsahiLinux/u-boot/commit/e372aa8287ad30ffe55b62ffdd7c06995be3fb17.patch#/asahi-e372aa8287ad30ffe55b62ffdd7c06995be3fb17.patch
# arm: dts: apple: Add Apple M2 Pro/Max device trees
Patch112: https://github.com/AsahiLinux/u-boot/commit/1115e7909d48f2b7e98021e1ee26f4fc509cdab2.patch#/asahi-1115e7909d48f2b7e98021e1ee26f4fc509cdab2.patch
# efi_loader: prefer EFI system partition
Patch113: https://github.com/AsahiLinux/u-boot/commit/b7abd70a31aba7eb6773c9114199772bcafb19e4.patch#/asahi-b7abd70a31aba7eb6773c9114199772bcafb19e4.patch
# usb: xhci: Add more debugging
Patch114: https://github.com/AsahiLinux/u-boot/commit/b3b0654ffba05c3f270a05996f05f5609303f9a3.patch#/asahi-b3b0654ffba05c3f270a05996f05f5609303f9a3.patch
# usb: storage: Clear endpoint stalls properly
Patch115: https://github.com/AsahiLinux/u-boot/commit/5e18100fc5ade9ec6ed761ba626053a39535b7c2.patch#/asahi-5e18100fc5ade9ec6ed761ba626053a39535b7c2.patch
# usb: Pass through timeout to drivers
Patch116: https://github.com/AsahiLinux/u-boot/commit/e6cb17b8b659fa82faf2bd39b35d4c03311dbbab.patch#/asahi-e6cb17b8b659fa82faf2bd39b35d4c03311dbbab.patch
# usb: xhci: Hook up timeouts
Patch117: https://github.com/AsahiLinux/u-boot/commit/3ae98d5faade779175de1c1272ea69fb9c871483.patch#/asahi-3ae98d5faade779175de1c1272ea69fb9c871483.patch
# scsi: Fix a bunch of SCSI definitions.
Patch118: https://github.com/AsahiLinux/u-boot/commit/b5b73496107e495e483f20f7bd095233f0e6fb2c.patch#/asahi-b5b73496107e495e483f20f7bd095233f0e6fb2c.patch
# usb: storage: Increase read/write timeout
Patch119: https://github.com/AsahiLinux/u-boot/commit/707ca674f5fc0f5881a1a199da41063a9bde0eeb.patch#/asahi-707ca674f5fc0f5881a1a199da41063a9bde0eeb.patch
# usb: storage: Implement 64-bit LBA support
Patch120: https://github.com/AsahiLinux/u-boot/commit/9a5d52dac06385940ae90a9d029bc3ade9f441e4.patch#/asahi-9a5d52dac06385940ae90a9d029bc3ade9f441e4.patch
# usb: Ignore endpoints in non-zero altsettings
Patch121: https://github.com/AsahiLinux/u-boot/commit/21b8175af602199c1b4152066ca1de109b907d9b.patch#/asahi-21b8175af602199c1b4152066ca1de109b907d9b.patch
# video: console: Select default font based on video_priv.font_size
Patch122: https://github.com/AsahiLinux/u-boot/commit/184a4b36592c9fa36bae92e178c8c7f49feb23dc.patch#/asahi-184a4b36592c9fa36bae92e178c8c7f49feb23dc.patch
# video: simplefb: HACK: Set video font size
Patch123: https://github.com/AsahiLinux/u-boot/commit/e5b8e888556e1532ea5072c87c317565ff59bc81.patch#/asahi-e5b8e888556e1532ea5072c87c317565ff59bc81.patch
# configs: apple: Do not show the boot menu automatically
Patch124: https://github.com/AsahiLinux/u-boot/commit/099dc2ff29a97d8f37a8c8ef6984d22fb15abde5.patch#/asahi-099dc2ff29a97d8f37a8c8ef6984d22fb15abde5.patch
# FEDORA: configs: apple: Disable AUTOBOOT_KEYED
Patch125: https://github.com/AsahiLinux/u-boot/commit/50c5c3660f8f9f5c486638ae86c26b82c4d2f0e5.patch#/asahi-50c5c3660f8f9f5c486638ae86c26b82c4d2f0e5.patch
# usb: dwc3: Add "apple,t8103-dwc3" compatible
Patch126: https://github.com/AsahiLinux/u-boot/commit/60a30528d34718f56f31cf48b2e397cbf2a7fa41.patch#/asahi-60a30528d34718f56f31cf48b2e397cbf2a7fa41.patch
# configs: apple: decrease boot delay to 1 second
Patch127: https://github.com/AsahiLinux/u-boot/commit/426359502f4d0b0c72cf32c28f3c4cabb89ff462.patch#/asahi-426359502f4d0b0c72cf32c28f3c4cabb89ff462.patch

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
BuildRequires:  crust-firmware
BuildRequires:  python3-pyelftools
BuildRequires:  xxd
%endif
%ifarch riscv64
BuildRequires:  %{opensbi}
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

%ifarch riscv64
%package     -n uboot-images-riscv64
Summary:     U-Boot firmware images for riscv64 boards
BuildArch:   noarch

%description -n uboot-images-riscv64
U-Boot firmware binaries for riscv64 boards
%endif
%endif

%prep
%autosetup -p1 -n u-boot-%{version}%{?candidate:-%{candidate}}

cp %SOURCE1 %SOURCE2 .

%build
mkdir builds

%make_build HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="" tools-only_defconfig O=builds/
%make_build HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="" tools-all O=builds/

%if %{with toolsonly}
# OpenSBI firmware is distributed in U-Boot SPL images
%ifarch riscv64
export OPENSBI=%{_datadir}/%{opensbi}/generic/firmware/fw_dynamic.bin
%endif

%ifarch aarch64 riscv64
for board in $(cat %{_arch}-boards)
do
  echo "Building board: $board"
  mkdir builds/$(echo $board)/

  # ATF selection, needs improving, suggestions of ATF SoC to Board matrix welcome
  sun50i=(a64-olinuxino a64-olinuxino-emmc amarula_a64_relic bananapi_m64 nanopi_a64 oceanic_5205_5inmfd orangepi_win pine64-lts pine64_plus pine64_plus pinebook pinephone pinephone pinetab sopine_baseboard teres_i)
  if [[ " ${sun50i[*]} " == *" $board "* ]]; then
    echo "Board: $board using sun50i_a64"
    cp /usr/share/arm-trusted-firmware/sun50i_a64/bl31.bin builds/$(echo $board)/atf-bl31
    cp /usr/share/crust-firmware/a64/scp.bin builds/$(echo $board)/
  fi
  sun50h5=(bananapi_m2_plus_h5 emlid_neutis_n5_devboard libretech_all_h3_cc_h5 libretech_all_h3_it_h5 libretech_all_h5_cc_h5 nanopi_neo2 nanopi_neo_plus2 nanopi_r1s_h5 orangepi_pc2 orangepi_prime orangepi_zero_plus2 orangepi_zero_plus)
  if [[ " ${sun50h5[*]} " == *" $board "* ]]; then
    echo "Board: $board using sun50i_h6"
    cp /usr/share/arm-trusted-firmware/sun50i_a64/bl31.bin builds/$(echo $board)/atf-bl31
    cp /usr/share/crust-firmware/h5/scp.bin builds/$(echo $board)/
  fi
  sun50h6=(beelink_gs1 emlid_neutis_n5_devboard orangepi_3 orangepi_lite2 orangepi_one_plus pine_h64 tanix_tx6)
  if [[ " ${sun50h6[*]} " == *" $board "* ]]; then
    echo "Board: $board using sun50i_h6"
    cp /usr/share/arm-trusted-firmware/sun50i_h6/bl31.bin builds/$(echo $board)/atf-bl31
    cp /usr/share/crust-firmware/h6/scp.bin builds/$(echo $board)/
  fi
  sun50i_h616=(anbernic_rg35xx_h700 orangepi_zero2 orangepi_zero2w orangepi_zero3 transpeed-8k618-t x96_mate)
  if [[ " ${sun50i_h616[*]} " == *" $board "* ]]; then
    echo "Board: $board using sun50i_h616"
    cp /usr/share/arm-trusted-firmware/sun50i_h616/bl31.bin builds/$(echo $board)/atf-bl31
  fi
  rk3328=(evb-rk3328 nanopi-r2c-plus-rk3328 nanopi-r2c-rk3328 nanopi-r2s-rk3328 nanopi-r2s-plus-rk3328 orangepi-r1-plus-lts-rk3328 orangepi-r1-plus-rk3328 roc-cc-rk3328 rock64-rk3328 rock-pi-e-rk3328 rock-pi-e-v3-rk3328)
  if [[ " ${rk3328[*]} " == *" $board "* ]]; then
    echo "Board: $board using rk3328"
    cp /usr/share/arm-trusted-firmware/rk3328/bl31.elf builds/$(echo $board)/atf-bl31
  fi
  rk3368=(evb-px5 geekbox)
  if [[ " ${rk3368[*]} " == *" $board "* ]]; then
    echo "Board: $board using rk3368"
    cp /usr/share/arm-trusted-firmware/rk3368/bl31.elf builds/$(echo $board)/atf-bl31
  fi
  rk3399=(eaidk-610-rk3399 evb-rk3399 ficus-rk3399 firefly-rk3399 khadas-edge-captain-rk3399 khadas-edge-rk3399 khadas-edge-v-rk3399 leez-rk3399 nanopc-t4-rk3399 nanopi-m4-2gb-rk3399 nanopi-m4b-rk3399 nanopi-m4-rk3399 nanopi-neo4-rk3399 nanopi-r4s-rk3399 orangepi-rk3399 pinebook-pro-rk3399 pinephone-pro-rk3399 puma-rk3399 rock-4c-plus-rk3399 rock-4se-rk3399 rock960-rk3399 rock-pi-4c-rk3399 rock-pi-4-rk3399 rock-pi-n10-rk3399pro rockpro64-rk3399 roc-pc-mezzanine-rk3399 roc-pc-rk3399)
  if [[ " ${rk3399[*]} " == *" $board "* ]]; then
    echo "Board: $board using rk3399"
    cp /usr/share/arm-trusted-firmware/rk3399/* builds/$(echo $board)/
    cp builds/$(echo $board)/bl31.elf builds/$(echo $board)/atf-bl31
  fi
  zynqmp=(xilinx_zynqmp_kria xilinx_zynqmp_virt)
  if [[ " ${zynqmp[*]} " == *" $board "* ]]; then
    echo "Board: $board using zynqmp"
    cp /usr/share/arm-trusted-firmware/zynqmp/bl31.bin builds/$(echo $board)/atf-bl31
  fi
  # End ATF

  make $(echo $board)_defconfig O=builds/$(echo $board)/
  BL31=builds/$(echo $board)/atf-bl31 %make_build HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="" O=builds/$(echo $board)/

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
 for file in u-boot.bin u-boot.img u-boot-dtb.img u-boot-sunxi-with-spl.bin u-boot-rockchip-spi.bin u-boot-rockchip.bin
 do
  if [ -f builds/$(echo $board)/$(echo $file) ]; then
    install -pD -m 0644 builds/$(echo $board)/$(echo $file) %{buildroot}%{_datadir}/uboot/$(echo $board)/$(echo $file)
  fi
 done
done

# Just for xilinx_zynqmp
for board in "xilinx_zynqmp_kria xilinx_zynqmp_virt"
do
 for file in u-boot.itb spl/boot.bin
 do
  if [ -f builds/$(echo $board)/$(echo $file) ]; then
    install -pD -m 0644 builds/$(echo $board)/$(echo $file) %{buildroot}%{_datadir}/uboot/$(echo $board)/$(echo $file)
  fi
 done
done

# For Apple M-series we also need the nodtb variant
install -pD -m 0644 builds/apple_m1/u-boot-nodtb.bin %{buildroot}%{_datadir}/uboot/apple_m1/u-boot-nodtb.bin
%endif

%ifarch riscv64
for board in $(ls builds)
do
 for file in u-boot.itb spl/u-boot-spl.bin spl/u-boot-spl.bin.normal.out
 do
  if [ -f builds/$(echo $board)/$(echo $file) ]; then
    install -pD -m 0644 builds/$(echo $board)/$(echo $file) %{buildroot}%{_datadir}/uboot/$(echo $board)/$(echo $file)
  fi
 done
done
%endif

# Bit of a hack to remove binaries we don't use as they're large
for board in $(ls builds)
do
  rm -f %{buildroot}%{_datadir}/uboot/$(echo $board)/u-boot.dtb
  if [ -f %{buildroot}%{_datadir}/uboot/$(echo $board)/u-boot-sunxi-with-spl.bin ]; then
    rm -f %{buildroot}%{_datadir}/uboot/$(echo $board)/u-boot{,-dtb}.*
  fi
done
%endif

for tool in dumpimage env/fw_printenv fdt_add_pubkey fit_check_sign fit_info gdb/gdbcont gdb/gdbsend gen_eth_addr gen_ethaddr_crc ifwitool img2srec kwboot mkeficapsule mkenvimage mkimage mksunxiboot ncb proftool sunxi-spl-image-builder
do
install -p -m 0755 builds/tools/$tool %{buildroot}%{_bindir}
done
for tool in dumpimage kwboot mkeficapsule mkimage
do
install -p -m 0644 doc/$tool.1 %{buildroot}%{_mandir}/man1
done

install -p -m 0755 builds/tools/env/fw_printenv %{buildroot}%{_bindir}
( cd %{buildroot}%{_bindir}; ln -sf fw_printenv fw_setenv )

%files
%license Licenses/*
%doc README doc/develop/distro.rst doc/README.gpt
%doc doc/develop/uefi doc/usage doc/arch/arm64.rst
%{_bindir}/*
%{_mandir}/man1/dumpimage.1*
%{_mandir}/man1/kwboot.1*
%{_mandir}/man1/mkeficapsule.1*
%{_mandir}/man1/mkimage.1*

%if %{with toolsonly}
%ifarch aarch64
%files -n uboot-images-armv8
%license Licenses/*
%dir %{_datadir}/uboot/
%{_datadir}/uboot/*
%endif

%ifarch riscv64
%files -n uboot-images-riscv64
%license Licenses/*
%dir %{_datadir}/uboot/
%{_datadir}/uboot/*
%endif
%endif

%changelog
* Sun Aug 24 2025 Davide Cavalca <dcavalca@fedoraproject.org> - 1:2025.07-103
- Restore patch to build without openssl engine

* Sun Aug 24 2025 Davide Cavalca <dcavalca@fedoraproject.org> - 1:2025.07-102
- Unconditionally build images

* Sun Aug 24 2025 Janne Grunau <j@jannau.net> - 1:2025.07-101
- Bump Release to Asahi specific "101"
- Import Asahi patches for v2025.07

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:2025.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jul 10 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2025.07-2
- Update patch for rebase issue

* Wed Jul 09 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2025.07-1
- Update to 2025.07 GA

* Fri Jun 27 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2025.07-0.5.rc5
- Update to 2025.07 RC5
- Enable LWIP stack by default
- Enable HTTP(s) boot support

* Thu Jun 26 2025 Javier Martinez Canillas <javierm@redhat.com> - 1:2025.07-0.4.rc4
- Add EFI_PARTITION_INFO_PROTOCOL support

* Sun Jun 15 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2025.07-0.3.rc4
- Update to 2025.07 RC4

* Tue May 13 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2025.07-0.2.rc2
- Update to 2025.07 RC2

* Thu May 01 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2025.07-0.1.rc1
- Update to 2025.07 RC1

* Sun Apr 20 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2025.04-2
- Fix for RPi5 serial console

* Tue Apr 08 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2025.04-1
- Update to 2025.04 GA

* Tue Mar 25 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2025.04-0.7.rc5
- Update to 2025.04 RC5

* Wed Mar 12 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2025.04-0.6.rc4
- Update to 2025.04 RC4

* Wed Feb 26 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2025.04-0.5.rc3
- Update to 2025.04 RC3

* Tue Feb 18 2025 David Abdurachmanov <davidlt@rivosinc.com> - 1:2025.04-0.4.rc2
- Add support for riscv64

* Tue Feb 11 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2025.04-0.3.rc2
- Update to 2025.05 RC2

* Tue Feb 11 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2025.04-0.2.rc1
- Update to 2025.05 RC1

* Tue Jan 28 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2025.01-3
- Add new fdt_add_pubkey tool

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:2025.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2025.01-1
- Update to 2025.01 GA

* Mon Jan 06 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2025.01-0.2.rc6
- Rebuild for TF-A 2.12

* Tue Dec 31 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2025.01-0.1.rc6
- Update to 2025.01 RC6

* Fri Oct 11 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.10-1
- Update to 2024.10 GA
- Fix passing RPi firmware CMA setting to kernel DT
- Update Geekbox

* Thu Oct 03 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.10-0.8.rc6
- Pass CMA FW setting through to kernel DT for Raspberry Pi

* Tue Oct 01 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.10-0.7.rc6
- Update to 2024.10 RC6

* Mon Sep 16 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.10-0.6.rc5
- Update to 2024.10 RC5

* Fri Sep  6 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.10-0.5.rc4
- Add missing licenses directory

* Tue Sep 03 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.10-0.4.rc4
- Update to 2024.10 RC4

* Mon Sep 02 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.10-0.3.rc3
- Fix Allwinner firmware chainloading (rhbz#2309138)
- Fix ATF firmware selection on a number of devices
- Support Allwinner SCP firmware (fixes suspend/resume)

* Tue Aug 27 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.10-0.2.rc3
- Update to 2024.10 RC3
- Enable initial QCM6490 SoC support

* Thu Aug 15 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.10-0.1.rc2
- Update to 2024.10 RC2

* Tue Jul 23 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.07-1
- Update to 2024.07

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2024.07-0.3.rc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.07-0.2.rc4
- Update to 2024.07 RC4

* Sat May 25 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.07-0.1.rc3
- Update to 2024.07 RC3

* Wed Apr 03 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.04-1
- Update to 2024.04 GA
- Rockchip rk3328 USB fixes

* Wed Mar 27 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.04-0.8.rc5
- Update to 2024.04 RC5

* Thu Mar 21 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.04-0.7.rc4
- Updated patch for DTB loading

* Fri Mar 15 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.04-0.6.rc4
- Updated fix for FDT load

* Wed Mar 13 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.04-0.5.rc4
- Fixes for Rockchip rk3399 autoboot

* Tue Mar 12 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.04-0.4.rc4
- Update to 2024.04 RC4
- Initial fix for loading DT off /boot (rhbz 2247873)

* Thu Feb 29 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.04-0.3.rc3
- Update to 2024.04 RC3
- Enable a number of new upstream devices
- Upstream now builds Rockchip SPI artifacts
- Various cleanups
- Fix ESP partition detection to enable EFI vars

* Wed Feb 14 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.04-0.2.rc2
- Update to 2024.04 RC2

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2024.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 08 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1:2024.01-1
- Update to 2024.01
