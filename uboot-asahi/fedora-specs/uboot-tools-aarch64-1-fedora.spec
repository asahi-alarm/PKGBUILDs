
Name:     uboot-tools
Version:  2026.07
Release:  101
Epoch:    1
Summary:  U-Boot utilities

License:  GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LGPL-2.1-or-later AND LGPL-2.0-or-later
URL:      https://u-boot-project.org/
ExcludeArch: s390x
Source0:  https://ftp.denx.de/pub/u-boot/u-boot-2026.07.tar.bz2
Source1:  aarch64-boards
Source2:  riscv64-boards
Source3:  x86_64-boards

Patch1:   disable-VBE-by-default.patch
Patch2:   enable-bootmenu-by-default.patch

Patch3:   uefi-distro-load-FDT-from-any-partition-on-boot-device.patch

Patch4:   uefi-Add-all-options-for-EFI-System-Partitions.patch

Patch5:   uefi-initial-find_fdt_location-for-finding-the-DT-on-disk.patch

Patch6:   uefi-enable-SetVariableRT-with-volotile-storage.patch

Patch7:   uefi-enable-https-boot-by-default.patch

Patch8:   pylibfdt-Replace-removed-SWIG-Python-2-compatibility-macros.patch

Patch10:  USB-PD-TCPM-improvements.patch

Patch11:  rockchip-Enable-preboot-start-for-pci-usb.patch
Patch12:  rockchip-rk3568-nanopi-r5-Drop-duplicated-extra-sdhc.patch
Patch13:  rockchip-rk356x-Stop-overriding-sdhci-mmc-aliases.patch

Patch14:  p3450-fix-board.patch
Patch15:  JetsonTX2-Fix-upstream-device-tree-naming.patch

Patch16:  Allwinner-fix-booting-on-a-number-of-devices.patch

Patch20:  Fix-NVMe-not-only-on-Raspberry-Pi-5.patch
Patch21:  raspberrypi-Add-quirk-for-RPi5-2Gb-rev-1.0.patch

Patch90:  openssl-no-engine.patch

Patch100: https://github.com/AsahiLinux/u-boot/commit/6835515ba36f290390bc92644e4c47df857a14b3.patch#/asahi-6835515ba36f290390bc92644e4c47df857a14b3.patch

Patch101: https://github.com/AsahiLinux/u-boot/commit/812c17b106e7522c8eb8d416923fd447c9a746c4.patch#/asahi-812c17b106e7522c8eb8d416923fd447c9a746c4.patch

Patch102: https://github.com/AsahiLinux/u-boot/commit/10fb7ce4f5eec2d12a6d480e809f71dba35d398b.patch#/asahi-10fb7ce4f5eec2d12a6d480e809f71dba35d398b.patch

Patch103: https://github.com/AsahiLinux/u-boot/commit/247988ff7034b3277a985fe35665992eb652ec5d.patch#/asahi-247988ff7034b3277a985fe35665992eb652ec5d.patch

Patch104: https://github.com/AsahiLinux/u-boot/commit/1527497f6729de9d70cf40070e03984bd69dcdad.patch#/asahi-1527497f6729de9d70cf40070e03984bd69dcdad.patch

Patch105: https://github.com/AsahiLinux/u-boot/commit/96ddc124c2fc12ebd40a304c570cd9aa7cf84048.patch#/asahi-96ddc124c2fc12ebd40a304c570cd9aa7cf84048.patch

Patch106: https://github.com/AsahiLinux/u-boot/commit/4cb43c165ad964258c32d504fe939a10ef5e1ce3.patch#/asahi-4cb43c165ad964258c32d504fe939a10ef5e1ce3.patch

Patch107: https://github.com/AsahiLinux/u-boot/commit/e141ab229f5176952955ede699e5ae16795f0b42.patch#/asahi-e141ab229f5176952955ede699e5ae16795f0b42.patch

Patch108: https://github.com/AsahiLinux/u-boot/commit/63091fcaa4736a9a9086c943c53d2238080fb5cb.patch#/asahi-63091fcaa4736a9a9086c943c53d2238080fb5cb.patch

Patch109: https://github.com/AsahiLinux/u-boot/commit/6c8f104a1463560eb887db688eb34d3ba521e3ed.patch#/asahi-6c8f104a1463560eb887db688eb34d3ba521e3ed.patch

Patch110: https://github.com/AsahiLinux/u-boot/commit/e03fdb9b4f20b869996393e3e7e0c29595f36df8.patch#/asahi-e03fdb9b4f20b869996393e3e7e0c29595f36df8.patch

Patch111: https://github.com/AsahiLinux/u-boot/commit/eacc5c5f848f7ba490e7f2127145543d62cd9f48.patch#/asahi-eacc5c5f848f7ba490e7f2127145543d62cd9f48.patch

Patch112: https://github.com/AsahiLinux/u-boot/commit/3c9a9164b1da60e6f6bc9c8452ba49a75bcf6504.patch#/asahi-3c9a9164b1da60e6f6bc9c8452ba49a75bcf6504.patch

Patch113: https://github.com/AsahiLinux/u-boot/commit/50669696be033e8c76f78e182a14e9cadd08387f.patch#/asahi-50669696be033e8c76f78e182a14e9cadd08387f.patch

Patch114: https://github.com/AsahiLinux/u-boot/commit/a0af6e889957dc72df6f8d7d07f000518fb45668.patch#/asahi-a0af6e889957dc72df6f8d7d07f000518fb45668.patch

Patch115: https://github.com/AsahiLinux/u-boot/commit/88b9ffc80e1777a0b44154f9dafc6580fee8cdc4.patch#/asahi-88b9ffc80e1777a0b44154f9dafc6580fee8cdc4.patch

Patch116: https://github.com/AsahiLinux/u-boot/commit/19b32bfe962dbd5115afe4c334e4669063273843.patch#/asahi-19b32bfe962dbd5115afe4c334e4669063273843.patch

Patch117: https://github.com/AsahiLinux/u-boot/commit/8db950bebbb91cbb5ee2c5360df38afb83b4f0ec.patch#/asahi-8db950bebbb91cbb5ee2c5360df38afb83b4f0ec.patch

Patch118: https://github.com/AsahiLinux/u-boot/commit/13a7dd0cbd66be4f3e5621b5cb97a3176db15783.patch#/asahi-13a7dd0cbd66be4f3e5621b5cb97a3176db15783.patch

Patch119: https://github.com/AsahiLinux/u-boot/commit/af5a1e21ea6aa22b5e8e6d9dcee866002c5f3524.patch#/asahi-af5a1e21ea6aa22b5e8e6d9dcee866002c5f3524.patch

Patch120: https://github.com/AsahiLinux/u-boot/commit/b880dc016cfde814ad6257f6b8fe90fbe3ca167c.patch#/asahi-b880dc016cfde814ad6257f6b8fe90fbe3ca167c.patch

Patch121: https://github.com/AsahiLinux/u-boot/commit/73b78347959e579ed2a1f008faa8a159d9bd9d1c.patch#/asahi-73b78347959e579ed2a1f008faa8a159d9bd9d1c.patch

Patch122: https://github.com/AsahiLinux/u-boot/commit/7f01e6365be00301b1edec7b79c9d72bf07d9eaa.patch#/asahi-7f01e6365be00301b1edec7b79c9d72bf07d9eaa.patch

Patch123: https://github.com/AsahiLinux/u-boot/commit/e23275e7b46f1f582fde4dd7c824e2263477e999.patch#/asahi-e23275e7b46f1f582fde4dd7c824e2263477e999.patch

Patch124: https://github.com/AsahiLinux/u-boot/commit/5654e6e9f2b4dc7af138600bf9beb983c92097ef.patch#/asahi-5654e6e9f2b4dc7af138600bf9beb983c92097ef.patch

Patch125: https://github.com/AsahiLinux/u-boot/commit/51b63835a99d660933546251e45ce499500ff355.patch#/asahi-51b63835a99d660933546251e45ce499500ff355.patch

Patch126: https://github.com/AsahiLinux/u-boot/commit/dbd2154cb0d3a5552505cfcc00a8b5f8da737030.patch#/asahi-dbd2154cb0d3a5552505cfcc00a8b5f8da737030.patch

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

BuildRequires:  arm-trusted-firmware-armv8
BuildRequires:  optee-os-firmware-armv8
BuildRequires:  crust-firmware
BuildRequires:  python3-pyelftools
BuildRequires:  xxd

Requires:       dtc

%description
This package contains a few U-Boot utilities - mkimage for creating boot images
and fw_printenv/fw_setenv for manipulating the boot environment variables.

%package     -n uboot-images-armv8
Summary:     U-Boot firmware images for aarch64 boards
BuildArch:   noarch

%description -n uboot-images-armv8
U-Boot firmware binaries for aarch64 boards

%prep

cd './'
rm -rf 'u-boot-2026.07'
rpmuncompress -x 'u-boot-2026.07.tar.bz2'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'u-boot-2026.07'
chmod -Rf a+rX,u+w,g-w,o-w .

rpmuncompress disable-VBE-by-default.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress enable-bootmenu-by-default.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress uefi-distro-load-FDT-from-any-partition-on-boot-device.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress uefi-Add-all-options-for-EFI-System-Partitions.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress uefi-initial-find_fdt_location-for-finding-the-DT-on-disk.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress uefi-enable-SetVariableRT-with-volotile-storage.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress uefi-enable-https-boot-by-default.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress pylibfdt-Replace-removed-SWIG-Python-2-compatibility-macros.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress USB-PD-TCPM-improvements.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress rockchip-Enable-preboot-start-for-pci-usb.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress rockchip-rk3568-nanopi-r5-Drop-duplicated-extra-sdhc.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress rockchip-rk356x-Stop-overriding-sdhci-mmc-aliases.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress p3450-fix-board.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress JetsonTX2-Fix-upstream-device-tree-naming.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress Allwinner-fix-booting-on-a-number-of-devices.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress Fix-NVMe-not-only-on-Raspberry-Pi-5.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress raspberrypi-Add-quirk-for-RPi5-2Gb-rev-1.0.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress openssl-no-engine.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

echo 'Cannot read asahi-6835515ba36f290390bc92644e4c47df857a14b3.patch'; exit 1;

echo 'Cannot read asahi-812c17b106e7522c8eb8d416923fd447c9a746c4.patch'; exit 1;

echo 'Cannot read asahi-10fb7ce4f5eec2d12a6d480e809f71dba35d398b.patch'; exit 1;

echo 'Cannot read asahi-247988ff7034b3277a985fe35665992eb652ec5d.patch'; exit 1;

echo 'Cannot read asahi-1527497f6729de9d70cf40070e03984bd69dcdad.patch'; exit 1;

echo 'Cannot read asahi-96ddc124c2fc12ebd40a304c570cd9aa7cf84048.patch'; exit 1;

echo 'Cannot read asahi-4cb43c165ad964258c32d504fe939a10ef5e1ce3.patch'; exit 1;

echo 'Cannot read asahi-e141ab229f5176952955ede699e5ae16795f0b42.patch'; exit 1;

echo 'Cannot read asahi-63091fcaa4736a9a9086c943c53d2238080fb5cb.patch'; exit 1;

echo 'Cannot read asahi-6c8f104a1463560eb887db688eb34d3ba521e3ed.patch'; exit 1;

echo 'Cannot read asahi-e03fdb9b4f20b869996393e3e7e0c29595f36df8.patch'; exit 1;

echo 'Cannot read asahi-eacc5c5f848f7ba490e7f2127145543d62cd9f48.patch'; exit 1;

echo 'Cannot read asahi-3c9a9164b1da60e6f6bc9c8452ba49a75bcf6504.patch'; exit 1;

echo 'Cannot read asahi-50669696be033e8c76f78e182a14e9cadd08387f.patch'; exit 1;

echo 'Cannot read asahi-a0af6e889957dc72df6f8d7d07f000518fb45668.patch'; exit 1;

echo 'Cannot read asahi-88b9ffc80e1777a0b44154f9dafc6580fee8cdc4.patch'; exit 1;

echo 'Cannot read asahi-19b32bfe962dbd5115afe4c334e4669063273843.patch'; exit 1;

echo 'Cannot read asahi-8db950bebbb91cbb5ee2c5360df38afb83b4f0ec.patch'; exit 1;

echo 'Cannot read asahi-13a7dd0cbd66be4f3e5621b5cb97a3176db15783.patch'; exit 1;

echo 'Cannot read asahi-af5a1e21ea6aa22b5e8e6d9dcee866002c5f3524.patch'; exit 1;

echo 'Cannot read asahi-b880dc016cfde814ad6257f6b8fe90fbe3ca167c.patch'; exit 1;

echo 'Cannot read asahi-73b78347959e579ed2a1f008faa8a159d9bd9d1c.patch'; exit 1;

echo 'Cannot read asahi-7f01e6365be00301b1edec7b79c9d72bf07d9eaa.patch'; exit 1;

echo 'Cannot read asahi-e23275e7b46f1f582fde4dd7c824e2263477e999.patch'; exit 1;

echo 'Cannot read asahi-5654e6e9f2b4dc7af138600bf9beb983c92097ef.patch'; exit 1;

echo 'Cannot read asahi-51b63835a99d660933546251e45ce499500ff355.patch'; exit 1;

echo 'Cannot read asahi-dbd2154cb0d3a5552505cfcc00a8b5f8da737030.patch'; exit 1;

%build
mkdir builds

/usr/bin/make -O -j${RPM_BUILD_NCPUS} V=1 VERBOSE=1 HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="" tools-only_defconfig O=builds/
/usr/bin/make -O -j${RPM_BUILD_NCPUS} V=1 VERBOSE=1 HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="" tools-all O=builds/

# OpenSBI firmware is distributed in U-Boot SPL images

for board in $(cat aarch64-boards)
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
  rk3328=(evb-rk3328 generic-rk3328 nanopi-r2c-plus-rk3328 nanopi-r2c-rk3328 nanopi-r2s-rk3328 nanopi-r2s-plus-rk3328 orangepi-r1-plus-lts-rk3328 orangepi-r1-plus-rk3328 roc-cc-rk3328 rock64-rk3328 rock-pi-e-rk3328 rock-pi-e-v3-rk3328)
  if [[ " ${rk3328[*]} " == *" $board "* ]]; then
    echo "Board: $board using rk3328"
    cp /usr/share/arm-trusted-firmware/rk3328/bl31.elf builds/$(echo $board)/atf-bl31
  fi
  rk3368=(evb-px5 geekbox)
  if [[ " ${rk3368[*]} " == *" $board "* ]]; then
    echo "Board: $board using rk3368"
    cp /usr/share/arm-trusted-firmware/rk3368/bl31.elf builds/$(echo $board)/atf-bl31
  fi
  rk3399=(eaidk-610-rk3399 evb-rk3399 ficus-rk3399 firefly-rk3399 generic-rk3399 khadas-edge-captain-rk3399 khadas-edge-rk3399 khadas-edge-v-rk3399 leez-rk3399 nanopc-t4-rk3399 nanopi-m4-2gb-rk3399 nanopi-m4b-rk3399 nanopi-m4-rk3399 nanopi-neo4-rk3399 nanopi-r4s-rk3399 orangepi-rk3399 pinebook-pro-rk3399 pinephone-pro-rk3399 puma-rk3399 rock-4c-plus-rk3399 rock-4se-rk3399 rock960-rk3399 rock-pi-4c-rk3399 rock-pi-4-rk3399 rock-pi-n10-rk3399pro rockpro64-rk3399 roc-pc-mezzanine-rk3399 roc-pc-rk3399)
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

  # skip tegra p3450-0000 on f41 and epel 10 due to build failures

  make $(echo $board)_defconfig O=builds/$(echo $board)/
  BL31=builds/$(echo $board)/atf-bl31 /usr/bin/make -O -j${RPM_BUILD_NCPUS} V=1 VERBOSE=1 HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="" O=builds/$(echo $board)/

done

%install
mkdir -p fakeinstall/usr/bin
mkdir -p fakeinstall/usr/share/man/man1
mkdir -p fakeinstall/usr/share/uboot/

for board in $(ls builds)
do
 for file in u-boot.bin u-boot.img u-boot-dtb.img u-boot-sunxi-with-spl.bin u-boot-rockchip-spi.bin u-boot-rockchip.bin
 do
  if [ -f builds/$(echo $board)/$(echo $file) ]; then
    install -pD -m 0644 builds/$(echo $board)/$(echo $file) fakeinstall/usr/share/uboot/$(echo $board)/$(echo $file)
  fi
 done
done

# Just for xilinx_zynqmp
for board in "xilinx_zynqmp_kria xilinx_zynqmp_virt"
do
 for file in u-boot.itb spl/boot.bin
 do
  if [ -f builds/$(echo $board)/$(echo $file) ]; then
    install -pD -m 0644 builds/$(echo $board)/$(echo $file) fakeinstall/usr/share/uboot/$(echo $board)/$(echo $file)
  fi
 done
done

# For Apple M-series we also need the nodtb variant
install -pD -m 0644 builds/apple_m1/u-boot-nodtb.bin fakeinstall/usr/share/uboot/apple_m1/u-boot-nodtb.bin

# Bit of a hack to remove binaries we don't use as they're large
for board in $(ls builds)
do
  rm -f fakeinstall/usr/share/uboot/$(echo $board)/u-boot.dtb
  if [ -f fakeinstall/usr/share/uboot/$(echo $board)/u-boot-sunxi-with-spl.bin ]; then
    rm -f fakeinstall/usr/share/uboot/$(echo $board)/u-boot{,-dtb}.*
  fi
  if [ -f fakeinstall/usr/share/uboot/$(echo $board)/u-boot-rockchip.bin ]; then
    rm -f fakeinstall/usr/share/uboot/$(echo $board)/u-boot{,-dtb}.*
  fi
done

for tool in dumpimage env/fw_printenv fdt_add_pubkey fit_check_sign fit_info gdb/gdbcont gdb/gdbsend gen_eth_addr gen_ethaddr_crc ifwitool img2srec kwboot mkeficapsule mkenvimage mkimage mksunxiboot ncb proftool sunxi-spl-image-builder
do
install -p -m 0755 builds/tools/$tool fakeinstall/usr/bin
done
for tool in dumpimage kwboot mkeficapsule mkimage
do
install -p -m 0644 doc/$tool.1 fakeinstall/usr/share/man/man1
done

install -p -m 0755 builds/tools/env/fw_printenv fakeinstall/usr/bin
( cd fakeinstall/usr/bin; ln -sf fw_printenv fw_setenv )

%files
%license Licenses/*
%doc README doc/develop/distro.rst doc/README.gpt
%doc doc/develop/uefi doc/usage doc/arch/arm64.rst
/usr/bin/*
/usr/share/man/man1/dumpimage.1*
/usr/share/man/man1/kwboot.1*
/usr/share/man/man1/mkeficapsule.1*
/usr/share/man/man1/mkimage.1*

%files -n uboot-images-armv8
%license Licenses/*
%dir /usr/share/uboot/
/usr/share/uboot/*

