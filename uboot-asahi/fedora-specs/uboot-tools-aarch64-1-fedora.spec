
Name:     uboot-tools
Version:  2026.04
Release:  101
Epoch:    1
Summary:  U-Boot utilities

License:  GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LGPL-2.1-or-later AND LGPL-2.0-or-later
URL:      http://www.denx.de/wiki/U-Boot
ExcludeArch: s390x
Source0:  https://ftp.denx.de/pub/u-boot/u-boot-2026.04.tar.bz2
Source1:  aarch64-boards
Source2:  riscv64-boards
Source3:  x86_64-boards

Patch1:   disable-VBE-by-default.patch
Patch2:   enable-bootmenu-by-default.patch

Patch3:   uefi-distro-load-FDT-from-any-partition-on-boot-device.patch

Patch4:   uefi-Add-all-options-for-EFI-System-Partitions.patch

Patch5:   0001-Revert-efi_loader-install-device-tree-on-configurati.patch

Patch6:   uefi-initial-find_fdt_location-for-finding-the-DT-on-disk.patch

Patch7:   uefi-enable-SetVariableRT-with-volotile-storage.patch

Patch8:   uefi-enable-https-boot-by-default.patch
Patch9:   efi_loader-disk-Add-EFI_PARTITION_INFO_PROTOCOL-support-for-MBR.patch

Patch10:  USB-PD-TCPM-improvements.patch

Patch11:  rockchip-Enable-preboot-start-for-pci-usb.patch
Patch12:  rockchip-rk3568-nanopi-r5-Drop-duplicated-extra-sdhc.patch
Patch13:  rockchip-rk356x-Stop-overriding-sdhci-mmc-aliases.patch

Patch14:  p3450-fix-board.patch
Patch15:  JetsonTX2-Fix-upstream-device-tree-naming.patch

Patch16:  Allwinner-fix-booting-on-a-number-of-devices.patch

Patch20:  ARM-RPi5-Enable-PCIe.patch
Patch21:  0001-Add-bcm2712-compat.patch
Patch22:  ARM-RPi-PCIe-fixes.patch
Patch23:  raspberrypi-Add-quirk-for-RPi5-2Gb-rev-1.0.patch

Patch90:  openssl-no-engine.patch

Patch100: https://github.com/AsahiLinux/u-boot/commit/c38fe0da9ec361ad27392a5938780815365c97a7.patch#/asahi-c38fe0da9ec361ad27392a5938780815365c97a7.patch

Patch101: https://github.com/AsahiLinux/u-boot/commit/875354fcbfd9bf99884589499860fe0cda8d03fe.patch#/asahi-875354fcbfd9bf99884589499860fe0cda8d03fe.patch

Patch102: https://github.com/AsahiLinux/u-boot/commit/25c40c21c5befeb9abc44c36c3293666108d0170.patch#/asahi-25c40c21c5befeb9abc44c36c3293666108d0170.patch

Patch103: https://github.com/AsahiLinux/u-boot/commit/39ee4f12d547eb2bfc726c99f1af22f7b5fcfdf4.patch#/asahi-39ee4f12d547eb2bfc726c99f1af22f7b5fcfdf4.patch

Patch104: https://github.com/AsahiLinux/u-boot/commit/8087a722706c758bf9d94e324753029c4f6f80d8.patch#/asahi-8087a722706c758bf9d94e324753029c4f6f80d8.patch

Patch105: https://github.com/AsahiLinux/u-boot/commit/069ee0692959ee29c6fed077ca82012f30ce93ed.patch#/asahi-069ee0692959ee29c6fed077ca82012f30ce93ed.patch

Patch106: https://github.com/AsahiLinux/u-boot/commit/65ebb5d2ce9a9e0e58c57f4ceac153a233320f65.patch#/asahi-65ebb5d2ce9a9e0e58c57f4ceac153a233320f65.patch

Patch107: https://github.com/AsahiLinux/u-boot/commit/360ba4a4b3843b92438b62a9c5b9f02584821498.patch#/asahi-360ba4a4b3843b92438b62a9c5b9f02584821498.patch

Patch108: https://github.com/AsahiLinux/u-boot/commit/c183a8e502834d95831ae5b629b5eac4e7b65ccb.patch#/asahi-c183a8e502834d95831ae5b629b5eac4e7b65ccb.patch

Patch109: https://github.com/AsahiLinux/u-boot/commit/dea067f48029c437334de42aebe080540432eb09.patch#/asahi-dea067f48029c437334de42aebe080540432eb09.patch

Patch110: https://github.com/AsahiLinux/u-boot/commit/db27d8c07f0a574c4289b7d09bc5c7df2d7833af.patch#/asahi-db27d8c07f0a574c4289b7d09bc5c7df2d7833af.patch

Patch111: https://github.com/AsahiLinux/u-boot/commit/dd20f5e6cb98ee19aa0d73353df9d3c83e281c43.patch#/asahi-dd20f5e6cb98ee19aa0d73353df9d3c83e281c43.patch

Patch112: https://github.com/AsahiLinux/u-boot/commit/3b197c83142f643e73a1881eeaa2c69168cd7ade.patch#/asahi-3b197c83142f643e73a1881eeaa2c69168cd7ade.patch

Patch113: https://github.com/AsahiLinux/u-boot/commit/e18c2cc68ad3917dff37a15a69be06805c2ca792.patch#/asahi-e18c2cc68ad3917dff37a15a69be06805c2ca792.patch

Patch114: https://github.com/AsahiLinux/u-boot/commit/01878d7691bd2e8b4dc53bd7386b82ff231acc3b.patch#/asahi-01878d7691bd2e8b4dc53bd7386b82ff231acc3b.patch

Patch115: https://github.com/AsahiLinux/u-boot/commit/f9e0240c5693be7859e5d142a39ed59892a13576.patch#/asahi-f9e0240c5693be7859e5d142a39ed59892a13576.patch

Patch116: https://github.com/AsahiLinux/u-boot/commit/f5787c26ae35f5b10d808073e19b9c81ab4e93a7.patch#/asahi-f5787c26ae35f5b10d808073e19b9c81ab4e93a7.patch

Patch117: https://github.com/AsahiLinux/u-boot/commit/91ea578fe3ab3ef48b87d18607c015d7e280be5b.patch#/asahi-91ea578fe3ab3ef48b87d18607c015d7e280be5b.patch

Patch118: https://github.com/AsahiLinux/u-boot/commit/c659e88a7024a51ce898e64fc53073d94ae55d9b.patch#/asahi-c659e88a7024a51ce898e64fc53073d94ae55d9b.patch

Patch119: https://github.com/AsahiLinux/u-boot/commit/02c4a3d0a32f108200856948a9566a4138879698.patch#/asahi-02c4a3d0a32f108200856948a9566a4138879698.patch

Patch120: https://github.com/AsahiLinux/u-boot/commit/01382cc455b6fd9d8ae8bf3363523d9e6cebf61c.patch#/asahi-01382cc455b6fd9d8ae8bf3363523d9e6cebf61c.patch

Patch121: https://github.com/AsahiLinux/u-boot/commit/ce24899757a20a0cd1d0337527bf0b5916b4be3c.patch#/asahi-ce24899757a20a0cd1d0337527bf0b5916b4be3c.patch

Patch122: https://github.com/AsahiLinux/u-boot/commit/ba71e64f6f9619c7e896da94d7aeb4d9dfcad2eb.patch#/asahi-ba71e64f6f9619c7e896da94d7aeb4d9dfcad2eb.patch

Patch123: https://github.com/AsahiLinux/u-boot/commit/2c343e36671511c04683602db6f8f30200ccf7d2.patch#/asahi-2c343e36671511c04683602db6f8f30200ccf7d2.patch

Patch124: https://github.com/AsahiLinux/u-boot/commit/b85792fb5982acb1c6e8894fb23cce8e3b85d8d4.patch#/asahi-b85792fb5982acb1c6e8894fb23cce8e3b85d8d4.patch

Patch125: https://github.com/AsahiLinux/u-boot/commit/a68d8fb458b62c0ce10fc5dfc514f81eaf3672a9.patch#/asahi-a68d8fb458b62c0ce10fc5dfc514f81eaf3672a9.patch

Patch126: https://github.com/AsahiLinux/u-boot/commit/afc509b957da47872c98ddbe90f4a226a122f451.patch#/asahi-afc509b957da47872c98ddbe90f4a226a122f451.patch

Patch127: https://github.com/AsahiLinux/u-boot/commit/239fb952613ec04ff9f226aafd60aef8428e6acf.patch#/asahi-239fb952613ec04ff9f226aafd60aef8428e6acf.patch

Patch128: https://github.com/AsahiLinux/u-boot/commit/95c091294521f63845ed0018cafd1ae775e3543e.patch#/asahi-95c091294521f63845ed0018cafd1ae775e3543e.patch

Patch129: https://github.com/AsahiLinux/u-boot/commit/20d67f319421dcd955f146abdea8944b7946f407.patch#/asahi-20d67f319421dcd955f146abdea8944b7946f407.patch

Patch130: https://github.com/AsahiLinux/u-boot/commit/3aea66db69f0aca940e24aac172ecf27cd030228.patch#/asahi-3aea66db69f0aca940e24aac172ecf27cd030228.patch

Patch131: https://github.com/AsahiLinux/u-boot/commit/ab751ea6edc26fa86cbe6d4ed7eb9f240a9ebeec.patch#/asahi-ab751ea6edc26fa86cbe6d4ed7eb9f240a9ebeec.patch

Patch132: https://github.com/AsahiLinux/u-boot/commit/595eafa2bdcd249f80fd52041388ba69ab010777.patch#/asahi-595eafa2bdcd249f80fd52041388ba69ab010777.patch

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
rm -rf 'u-boot-2026.04'
rpmuncompress -x 'u-boot-2026.04.tar.bz2'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'u-boot-2026.04'
chmod -Rf a+rX,u+w,g-w,o-w .

rpmuncompress disable-VBE-by-default.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress enable-bootmenu-by-default.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress uefi-distro-load-FDT-from-any-partition-on-boot-device.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress uefi-Add-all-options-for-EFI-System-Partitions.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress 0001-Revert-efi_loader-install-device-tree-on-configurati.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress uefi-initial-find_fdt_location-for-finding-the-DT-on-disk.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress uefi-enable-SetVariableRT-with-volotile-storage.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress uefi-enable-https-boot-by-default.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress efi_loader-disk-Add-EFI_PARTITION_INFO_PROTOCOL-support-for-MBR.patch | 
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

rpmuncompress ARM-RPi5-Enable-PCIe.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress 0001-Add-bcm2712-compat.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress ARM-RPi-PCIe-fixes.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress raspberrypi-Add-quirk-for-RPi5-2Gb-rev-1.0.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress openssl-no-engine.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

echo 'Cannot read asahi-c38fe0da9ec361ad27392a5938780815365c97a7.patch'; exit 1;

echo 'Cannot read asahi-875354fcbfd9bf99884589499860fe0cda8d03fe.patch'; exit 1;

echo 'Cannot read asahi-25c40c21c5befeb9abc44c36c3293666108d0170.patch'; exit 1;

echo 'Cannot read asahi-39ee4f12d547eb2bfc726c99f1af22f7b5fcfdf4.patch'; exit 1;

echo 'Cannot read asahi-8087a722706c758bf9d94e324753029c4f6f80d8.patch'; exit 1;

echo 'Cannot read asahi-069ee0692959ee29c6fed077ca82012f30ce93ed.patch'; exit 1;

echo 'Cannot read asahi-65ebb5d2ce9a9e0e58c57f4ceac153a233320f65.patch'; exit 1;

echo 'Cannot read asahi-360ba4a4b3843b92438b62a9c5b9f02584821498.patch'; exit 1;

echo 'Cannot read asahi-c183a8e502834d95831ae5b629b5eac4e7b65ccb.patch'; exit 1;

echo 'Cannot read asahi-dea067f48029c437334de42aebe080540432eb09.patch'; exit 1;

echo 'Cannot read asahi-db27d8c07f0a574c4289b7d09bc5c7df2d7833af.patch'; exit 1;

echo 'Cannot read asahi-dd20f5e6cb98ee19aa0d73353df9d3c83e281c43.patch'; exit 1;

echo 'Cannot read asahi-3b197c83142f643e73a1881eeaa2c69168cd7ade.patch'; exit 1;

echo 'Cannot read asahi-e18c2cc68ad3917dff37a15a69be06805c2ca792.patch'; exit 1;

echo 'Cannot read asahi-01878d7691bd2e8b4dc53bd7386b82ff231acc3b.patch'; exit 1;

echo 'Cannot read asahi-f9e0240c5693be7859e5d142a39ed59892a13576.patch'; exit 1;

echo 'Cannot read asahi-f5787c26ae35f5b10d808073e19b9c81ab4e93a7.patch'; exit 1;

echo 'Cannot read asahi-91ea578fe3ab3ef48b87d18607c015d7e280be5b.patch'; exit 1;

echo 'Cannot read asahi-c659e88a7024a51ce898e64fc53073d94ae55d9b.patch'; exit 1;

echo 'Cannot read asahi-02c4a3d0a32f108200856948a9566a4138879698.patch'; exit 1;

echo 'Cannot read asahi-01382cc455b6fd9d8ae8bf3363523d9e6cebf61c.patch'; exit 1;

echo 'Cannot read asahi-ce24899757a20a0cd1d0337527bf0b5916b4be3c.patch'; exit 1;

echo 'Cannot read asahi-ba71e64f6f9619c7e896da94d7aeb4d9dfcad2eb.patch'; exit 1;

echo 'Cannot read asahi-2c343e36671511c04683602db6f8f30200ccf7d2.patch'; exit 1;

echo 'Cannot read asahi-b85792fb5982acb1c6e8894fb23cce8e3b85d8d4.patch'; exit 1;

echo 'Cannot read asahi-a68d8fb458b62c0ce10fc5dfc514f81eaf3672a9.patch'; exit 1;

echo 'Cannot read asahi-afc509b957da47872c98ddbe90f4a226a122f451.patch'; exit 1;

echo 'Cannot read asahi-239fb952613ec04ff9f226aafd60aef8428e6acf.patch'; exit 1;

echo 'Cannot read asahi-95c091294521f63845ed0018cafd1ae775e3543e.patch'; exit 1;

echo 'Cannot read asahi-20d67f319421dcd955f146abdea8944b7946f407.patch'; exit 1;

echo 'Cannot read asahi-3aea66db69f0aca940e24aac172ecf27cd030228.patch'; exit 1;

echo 'Cannot read asahi-ab751ea6edc26fa86cbe6d4ed7eb9f240a9ebeec.patch'; exit 1;

echo 'Cannot read asahi-595eafa2bdcd249f80fd52041388ba69ab010777.patch'; exit 1;

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

