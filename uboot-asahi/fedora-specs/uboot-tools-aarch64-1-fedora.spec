
Name:     uboot-tools
Version:  2025.07
Release:  104
Epoch:    1
Summary:  U-Boot utilities

License:  GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LGPL-2.1-or-later AND LGPL-2.0-or-later
URL:      http://www.denx.de/wiki/U-Boot
ExcludeArch: s390x
Source0:  https://ftp.denx.de/pub/u-boot/u-boot-2025.07.tar.bz2
Source1:  aarch64-boards
Source2:  riscv64-boards

Patch1:   disable-VBE-by-default.patch
Patch2:   enable-bootmenu-by-default.patch

Patch3:   uefi-distro-load-FDT-from-any-partition-on-boot-device.patch

Patch4:   uefi-Add-all-options-for-EFI-System-Partitions.patch

Patch6:   uefi-initial-find_fdt_location-for-finding-the-DT-on-disk.patch

Patch7:   uefi-enable-SetVariableRT-with-volotile-storage.patch

Patch8:   uefi-enable-https-boot-by-default.patch

Patch9:   tools-termios_linux.h-Fix-build-error-on-ppc64.patch

Patch10:  USB-PD-TCPM-improvements.patch

Patch11:  rockchip-Enable-preboot-start-for-pci-usb.patch

Patch12:  Rebase-to-upstream-6.15.5-rockchip-DTs.patch
Patch13:  Initial-MNT-Reform2-support.patch

Patch14:  p3450-fix-board.patch

Patch20:  disk-efi-Move-logic-to-get-a-GPT-entry-into-a-helper.patch
Patch21:  disk-efi-expose-the-part_get_gpt_pte-helper-function.patch
Patch22:  efi_loader-disk-add-EFI_PARTITION_INFO_PROTOCOL-supp.patch
Patch23:  efi_selftest-Add-basic-partition-info-check-to-block.patch

Patch90:  openssl-no-engine.patch

Patch100: https://github.com/AsahiLinux/u-boot/commit/a0f2eb2c0e05cbfa655009ca232fb454b9904bba.patch#/asahi-a0f2eb2c0e05cbfa655009ca232fb454b9904bba.patch

Patch101: https://github.com/AsahiLinux/u-boot/commit/4d5839ad4b935f5555613123f4d0e0b788b95e7b.patch#/asahi-4d5839ad4b935f5555613123f4d0e0b788b95e7b.patch

Patch102: https://github.com/AsahiLinux/u-boot/commit/d2bdb6fec9130813662e623b29a0d1487b70cf77.patch#/asahi-d2bdb6fec9130813662e623b29a0d1487b70cf77.patch

Patch103: https://github.com/AsahiLinux/u-boot/commit/d00dd16498d0c0b15172561cac4c5b4901150298.patch#/asahi-d00dd16498d0c0b15172561cac4c5b4901150298.patch

Patch104: https://github.com/AsahiLinux/u-boot/commit/04d2676ac2d74aae3bc797f30db2a161f98a3ac8.patch#/asahi-04d2676ac2d74aae3bc797f30db2a161f98a3ac8.patch

Patch105: https://github.com/AsahiLinux/u-boot/commit/08980606eb0dc35252df8b67dd73775e1604838b.patch#/asahi-08980606eb0dc35252df8b67dd73775e1604838b.patch

Patch106: https://github.com/AsahiLinux/u-boot/commit/52d2343f9dd4cf754e55168a83673a3f1a957697.patch#/asahi-52d2343f9dd4cf754e55168a83673a3f1a957697.patch

Patch107: https://github.com/AsahiLinux/u-boot/commit/1d4edd84a380da7e14272fa56c4ff33ca4ce9dba.patch#/asahi-1d4edd84a380da7e14272fa56c4ff33ca4ce9dba.patch

Patch108: https://github.com/AsahiLinux/u-boot/commit/afdf8e769379ad9f4ff3ed7ef4145a7c3f5d36a7.patch#/asahi-afdf8e769379ad9f4ff3ed7ef4145a7c3f5d36a7.patch

Patch109: https://github.com/AsahiLinux/u-boot/commit/4f89bdfe053b367dae6b76e182087c2165654010.patch#/asahi-4f89bdfe053b367dae6b76e182087c2165654010.patch

Patch110: https://github.com/AsahiLinux/u-boot/commit/783edefb9c2fbfdf170697aec2d6b6245b48b0cb.patch#/asahi-783edefb9c2fbfdf170697aec2d6b6245b48b0cb.patch

Patch111: https://github.com/AsahiLinux/u-boot/commit/e372aa8287ad30ffe55b62ffdd7c06995be3fb17.patch#/asahi-e372aa8287ad30ffe55b62ffdd7c06995be3fb17.patch

Patch112: https://github.com/AsahiLinux/u-boot/commit/1115e7909d48f2b7e98021e1ee26f4fc509cdab2.patch#/asahi-1115e7909d48f2b7e98021e1ee26f4fc509cdab2.patch

Patch113: https://github.com/AsahiLinux/u-boot/commit/b7abd70a31aba7eb6773c9114199772bcafb19e4.patch#/asahi-b7abd70a31aba7eb6773c9114199772bcafb19e4.patch

Patch114: https://github.com/AsahiLinux/u-boot/commit/b3b0654ffba05c3f270a05996f05f5609303f9a3.patch#/asahi-b3b0654ffba05c3f270a05996f05f5609303f9a3.patch

Patch115: https://github.com/AsahiLinux/u-boot/commit/5e18100fc5ade9ec6ed761ba626053a39535b7c2.patch#/asahi-5e18100fc5ade9ec6ed761ba626053a39535b7c2.patch

Patch116: https://github.com/AsahiLinux/u-boot/commit/e6cb17b8b659fa82faf2bd39b35d4c03311dbbab.patch#/asahi-e6cb17b8b659fa82faf2bd39b35d4c03311dbbab.patch

Patch117: https://github.com/AsahiLinux/u-boot/commit/3ae98d5faade779175de1c1272ea69fb9c871483.patch#/asahi-3ae98d5faade779175de1c1272ea69fb9c871483.patch

Patch118: https://github.com/AsahiLinux/u-boot/commit/b5b73496107e495e483f20f7bd095233f0e6fb2c.patch#/asahi-b5b73496107e495e483f20f7bd095233f0e6fb2c.patch

Patch119: https://github.com/AsahiLinux/u-boot/commit/707ca674f5fc0f5881a1a199da41063a9bde0eeb.patch#/asahi-707ca674f5fc0f5881a1a199da41063a9bde0eeb.patch

Patch120: https://github.com/AsahiLinux/u-boot/commit/9a5d52dac06385940ae90a9d029bc3ade9f441e4.patch#/asahi-9a5d52dac06385940ae90a9d029bc3ade9f441e4.patch

Patch121: https://github.com/AsahiLinux/u-boot/commit/21b8175af602199c1b4152066ca1de109b907d9b.patch#/asahi-21b8175af602199c1b4152066ca1de109b907d9b.patch

Patch122: https://github.com/AsahiLinux/u-boot/commit/184a4b36592c9fa36bae92e178c8c7f49feb23dc.patch#/asahi-184a4b36592c9fa36bae92e178c8c7f49feb23dc.patch

Patch123: https://github.com/AsahiLinux/u-boot/commit/e5b8e888556e1532ea5072c87c317565ff59bc81.patch#/asahi-e5b8e888556e1532ea5072c87c317565ff59bc81.patch

Patch124: https://github.com/AsahiLinux/u-boot/commit/099dc2ff29a97d8f37a8c8ef6984d22fb15abde5.patch#/asahi-099dc2ff29a97d8f37a8c8ef6984d22fb15abde5.patch

Patch125: https://github.com/AsahiLinux/u-boot/commit/50c5c3660f8f9f5c486638ae86c26b82c4d2f0e5.patch#/asahi-50c5c3660f8f9f5c486638ae86c26b82c4d2f0e5.patch

Patch126: https://github.com/AsahiLinux/u-boot/commit/60a30528d34718f56f31cf48b2e397cbf2a7fa41.patch#/asahi-60a30528d34718f56f31cf48b2e397cbf2a7fa41.patch

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

BuildRequires:  arm-trusted-firmware-armv8
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
rm -rf 'u-boot-2025.07'
rpmuncompress -x 'u-boot-2025.07.tar.bz2'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'u-boot-2025.07'
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

rpmuncompress tools-termios_linux.h-Fix-build-error-on-ppc64.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress USB-PD-TCPM-improvements.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress rockchip-Enable-preboot-start-for-pci-usb.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress Rebase-to-upstream-6.15.5-rockchip-DTs.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress Initial-MNT-Reform2-support.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress p3450-fix-board.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress disk-efi-Move-logic-to-get-a-GPT-entry-into-a-helper.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress disk-efi-expose-the-part_get_gpt_pte-helper-function.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress efi_loader-disk-add-EFI_PARTITION_INFO_PROTOCOL-supp.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress efi_selftest-Add-basic-partition-info-check-to-block.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress openssl-no-engine.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

echo 'Cannot read asahi-a0f2eb2c0e05cbfa655009ca232fb454b9904bba.patch'; exit 1;

echo 'Cannot read asahi-4d5839ad4b935f5555613123f4d0e0b788b95e7b.patch'; exit 1;

echo 'Cannot read asahi-d2bdb6fec9130813662e623b29a0d1487b70cf77.patch'; exit 1;

echo 'Cannot read asahi-d00dd16498d0c0b15172561cac4c5b4901150298.patch'; exit 1;

echo 'Cannot read asahi-04d2676ac2d74aae3bc797f30db2a161f98a3ac8.patch'; exit 1;

echo 'Cannot read asahi-08980606eb0dc35252df8b67dd73775e1604838b.patch'; exit 1;

echo 'Cannot read asahi-52d2343f9dd4cf754e55168a83673a3f1a957697.patch'; exit 1;

echo 'Cannot read asahi-1d4edd84a380da7e14272fa56c4ff33ca4ce9dba.patch'; exit 1;

echo 'Cannot read asahi-afdf8e769379ad9f4ff3ed7ef4145a7c3f5d36a7.patch'; exit 1;

echo 'Cannot read asahi-4f89bdfe053b367dae6b76e182087c2165654010.patch'; exit 1;

echo 'Cannot read asahi-783edefb9c2fbfdf170697aec2d6b6245b48b0cb.patch'; exit 1;

echo 'Cannot read asahi-e372aa8287ad30ffe55b62ffdd7c06995be3fb17.patch'; exit 1;

echo 'Cannot read asahi-1115e7909d48f2b7e98021e1ee26f4fc509cdab2.patch'; exit 1;

echo 'Cannot read asahi-b7abd70a31aba7eb6773c9114199772bcafb19e4.patch'; exit 1;

echo 'Cannot read asahi-b3b0654ffba05c3f270a05996f05f5609303f9a3.patch'; exit 1;

echo 'Cannot read asahi-5e18100fc5ade9ec6ed761ba626053a39535b7c2.patch'; exit 1;

echo 'Cannot read asahi-e6cb17b8b659fa82faf2bd39b35d4c03311dbbab.patch'; exit 1;

echo 'Cannot read asahi-3ae98d5faade779175de1c1272ea69fb9c871483.patch'; exit 1;

echo 'Cannot read asahi-b5b73496107e495e483f20f7bd095233f0e6fb2c.patch'; exit 1;

echo 'Cannot read asahi-707ca674f5fc0f5881a1a199da41063a9bde0eeb.patch'; exit 1;

echo 'Cannot read asahi-9a5d52dac06385940ae90a9d029bc3ade9f441e4.patch'; exit 1;

echo 'Cannot read asahi-21b8175af602199c1b4152066ca1de109b907d9b.patch'; exit 1;

echo 'Cannot read asahi-184a4b36592c9fa36bae92e178c8c7f49feb23dc.patch'; exit 1;

echo 'Cannot read asahi-e5b8e888556e1532ea5072c87c317565ff59bc81.patch'; exit 1;

echo 'Cannot read asahi-099dc2ff29a97d8f37a8c8ef6984d22fb15abde5.patch'; exit 1;

echo 'Cannot read asahi-50c5c3660f8f9f5c486638ae86c26b82c4d2f0e5.patch'; exit 1;

echo 'Cannot read asahi-60a30528d34718f56f31cf48b2e397cbf2a7fa41.patch'; exit 1;

echo 'Cannot read asahi-426359502f4d0b0c72cf32c28f3c4cabb89ff462.patch'; exit 1;

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

