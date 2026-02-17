
  Name:     uboot-tools
  Version:  2025.10
  Release:  101
  Epoch:    1
  Summary:  U-Boot utilities

  License:  GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LGPL-2.1-or-later AND LGPL-2.0-or-later
  URL:      http://www.denx.de/wiki/U-Boot
  ExcludeArch: s390x
  Source0:  https://ftp.denx.de/pub/u-boot/u-boot-2025.10.tar.bz2
  Source1:  aarch64-boards
  Source2:  riscv64-boards

  Patch1:   disable-VBE-by-default.patch
  Patch2:   enable-bootmenu-by-default.patch

  Patch3:   uefi-distro-load-FDT-from-any-partition-on-boot-device.patch

  Patch4:   uefi-Add-all-options-for-EFI-System-Partitions.patch

  Patch5:   0001-Revert-efi_loader-install-device-tree-on-configurati.patch

  Patch6:   uefi-initial-find_fdt_location-for-finding-the-DT-on-disk.patch

  Patch7:   uefi-enable-SetVariableRT-with-volotile-storage.patch

  Patch8:   uefi-enable-https-boot-by-default.patch

  Patch10:  USB-PD-TCPM-improvements.patch

  Patch11:  rockchip-Enable-preboot-start-for-pci-usb.patch
  Patch13:  Initial-MNT-Reform2-support.patch

  Patch14:  p3450-fix-board.patch
  Patch15:  JetsonTX2-Fix-upstream-device-tree-naming.patch

  Patch16:  Allwinner-fix-booting-on-a-number-of-devices.patch

  Patch17:  Improve-RaspBerry-Pi-5-support-part1-Fixes.patch

  Patch90:  openssl-no-engine.patch

  Patch100: https://github.com/AsahiLinux/u-boot/commit/29a672b04d658a1204cd5ada7bebe1435d909eb6.patch#/asahi-29a672b04d658a1204cd5ada7bebe1435d909eb6.patch

  Patch101: https://github.com/AsahiLinux/u-boot/commit/56e691cfe3e38e6f1d3cdd5605dda10be4f0f9df.patch#/asahi-56e691cfe3e38e6f1d3cdd5605dda10be4f0f9df.patch

  Patch102: https://github.com/AsahiLinux/u-boot/commit/030d43481db4590c755560187c501bdad3d519cd.patch#/asahi-030d43481db4590c755560187c501bdad3d519cd.patch

  Patch103: https://github.com/AsahiLinux/u-boot/commit/5f0bda0d9a422b7c19e91789eeb6957eea80438c.patch#/asahi-5f0bda0d9a422b7c19e91789eeb6957eea80438c.patch

  Patch104: https://github.com/AsahiLinux/u-boot/commit/b67328259e1fd89646b3e59b3f03febe1c30b409.patch#/asahi-b67328259e1fd89646b3e59b3f03febe1c30b409.patch

  Patch105: https://github.com/AsahiLinux/u-boot/commit/7b2fe0b9aff232f7f62d4b741fc9f8c9834ce1f2.patch#/asahi-7b2fe0b9aff232f7f62d4b741fc9f8c9834ce1f2.patch

  Patch106: https://github.com/AsahiLinux/u-boot/commit/976376ad06ac4133ac22dd1794889beda8ebd2f6.patch#/asahi-976376ad06ac4133ac22dd1794889beda8ebd2f6.patch

  Patch107: https://github.com/AsahiLinux/u-boot/commit/a0790507c9fdfe05022087728c8e47b6f0005937.patch#/asahi-a0790507c9fdfe05022087728c8e47b6f0005937.patch

  Patch108: https://github.com/AsahiLinux/u-boot/commit/655fc2f4be49460624df16bdda14bffdb524d07e.patch#/asahi-655fc2f4be49460624df16bdda14bffdb524d07e.patch

  Patch109: https://github.com/AsahiLinux/u-boot/commit/459b45aa5ead20ac4f364a54bc2ec10ca2fe6a89.patch#/asahi-459b45aa5ead20ac4f364a54bc2ec10ca2fe6a89.patch

  Patch110: https://github.com/AsahiLinux/u-boot/commit/44a39842f92eb2be2a238da909d6ed3510621d36.patch#/asahi-44a39842f92eb2be2a238da909d6ed3510621d36.patch

  Patch111: https://github.com/AsahiLinux/u-boot/commit/21e2b962e438b761a448bb6f4ab36ab5549a739f.patch#/asahi-21e2b962e438b761a448bb6f4ab36ab5549a739f.patch

  Patch112: https://github.com/AsahiLinux/u-boot/commit/9d50956a6674b2883f64345e2c8816b0c30e4df2.patch#/asahi-9d50956a6674b2883f64345e2c8816b0c30e4df2.patch

  Patch113: https://github.com/AsahiLinux/u-boot/commit/8aa706b2daa49b64102e44067d8514de8a26dc42.patch#/asahi-8aa706b2daa49b64102e44067d8514de8a26dc42.patch

  Patch114: https://github.com/AsahiLinux/u-boot/commit/b66d7bc5b0ce0d625436766c887400a9e6c0f2f1.patch#/asahi-b66d7bc5b0ce0d625436766c887400a9e6c0f2f1.patch

  Patch115: https://github.com/AsahiLinux/u-boot/commit/8cdc16f7da5175ac09a67caa05dd73c204ed9ef9.patch#/asahi-8cdc16f7da5175ac09a67caa05dd73c204ed9ef9.patch

  Patch116: https://github.com/AsahiLinux/u-boot/commit/50b02ee98bf104873351bf1a40a5d09e4ed3ba52.patch#/asahi-50b02ee98bf104873351bf1a40a5d09e4ed3ba52.patch

  Patch117: https://github.com/AsahiLinux/u-boot/commit/cc66189884fd09d00b3b0113c08687f2274a8e15.patch#/asahi-cc66189884fd09d00b3b0113c08687f2274a8e15.patch

  Patch118: https://github.com/AsahiLinux/u-boot/commit/5eddf1994b2812e86f0ff550daec0c19335a05a7.patch#/asahi-5eddf1994b2812e86f0ff550daec0c19335a05a7.patch

  Patch119: https://github.com/AsahiLinux/u-boot/commit/bef5ffc28080e2cfea5300347757855c0d3c8955.patch#/asahi-bef5ffc28080e2cfea5300347757855c0d3c8955.patch

  Patch120: https://github.com/AsahiLinux/u-boot/commit/045e48531efcfbb5e058a5515a931fdde996092d.patch#/asahi-045e48531efcfbb5e058a5515a931fdde996092d.patch

  Patch121: https://github.com/AsahiLinux/u-boot/commit/e71bce920193087c04c18217434538a3f374c87f.patch#/asahi-e71bce920193087c04c18217434538a3f374c87f.patch

  Patch122: https://github.com/AsahiLinux/u-boot/commit/f3845a541a924d2596f06f4dfcf504f9786b1145.patch#/asahi-f3845a541a924d2596f06f4dfcf504f9786b1145.patch

  Patch123: https://github.com/AsahiLinux/u-boot/commit/c8f2183def80ff59aaefb3ea4cec8200ad88bd2e.patch#/asahi-c8f2183def80ff59aaefb3ea4cec8200ad88bd2e.patch

  Patch124: https://github.com/AsahiLinux/u-boot/commit/0ed8eedee5bf4447bca8d26c5ecc693e7aed4aad.patch#/asahi-0ed8eedee5bf4447bca8d26c5ecc693e7aed4aad.patch

  Patch125: https://github.com/AsahiLinux/u-boot/commit/24675d697e32b3b85e72dae9e70325e8a63fba33.patch#/asahi-24675d697e32b3b85e72dae9e70325e8a63fba33.patch

  Patch126: https://github.com/AsahiLinux/u-boot/commit/8d259ae7a33e317fa04f590c3d2fe548e4e62c57.patch#/asahi-8d259ae7a33e317fa04f590c3d2fe548e4e62c57.patch

  Patch127: https://github.com/AsahiLinux/u-boot/commit/32e5c782a67af41306f3169000b527277860c44f.patch#/asahi-32e5c782a67af41306f3169000b527277860c44f.patch

  Patch128: https://github.com/AsahiLinux/u-boot/commit/5191f0e2ceb6901289a1bb2c627890dbf8432f18.patch#/asahi-5191f0e2ceb6901289a1bb2c627890dbf8432f18.patch

  Patch129: https://github.com/AsahiLinux/u-boot/commit/4411224f218ee67526f74d10cd3b3a7cd70ff2ad.patch#/asahi-4411224f218ee67526f74d10cd3b3a7cd70ff2ad.patch

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

prepare() {

  cd './'
  rm -rf 'u-boot-2025.10'
  tar -xf 'u-boot-2025.10.tar.bz2'
  STATUS=$?
  if [ $STATUS -ne 0 ]; then
    exit $STATUS
  fi
  cd 'u-boot-2025.10'
  chmod -Rf a+rX,u+w,g-w,o-w .

  cat disable-VBE-by-default.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat enable-bootmenu-by-default.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat uefi-distro-load-FDT-from-any-partition-on-boot-device.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat uefi-Add-all-options-for-EFI-System-Partitions.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat 0001-Revert-efi_loader-install-device-tree-on-configurati.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat uefi-initial-find_fdt_location-for-finding-the-DT-on-disk.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat uefi-enable-SetVariableRT-with-volotile-storage.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat uefi-enable-https-boot-by-default.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat USB-PD-TCPM-improvements.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat rockchip-Enable-preboot-start-for-pci-usb.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat Initial-MNT-Reform2-support.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat p3450-fix-board.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat JetsonTX2-Fix-upstream-device-tree-naming.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat Allwinner-fix-booting-on-a-number-of-devices.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat Improve-RaspBerry-Pi-5-support-part1-Fixes.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat openssl-no-engine.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  echo 'Cannot read asahi-29a672b04d658a1204cd5ada7bebe1435d909eb6.patch'; exit 1;

  echo 'Cannot read asahi-56e691cfe3e38e6f1d3cdd5605dda10be4f0f9df.patch'; exit 1;

  echo 'Cannot read asahi-030d43481db4590c755560187c501bdad3d519cd.patch'; exit 1;

  echo 'Cannot read asahi-5f0bda0d9a422b7c19e91789eeb6957eea80438c.patch'; exit 1;

  echo 'Cannot read asahi-b67328259e1fd89646b3e59b3f03febe1c30b409.patch'; exit 1;

  echo 'Cannot read asahi-7b2fe0b9aff232f7f62d4b741fc9f8c9834ce1f2.patch'; exit 1;

  echo 'Cannot read asahi-976376ad06ac4133ac22dd1794889beda8ebd2f6.patch'; exit 1;

  echo 'Cannot read asahi-a0790507c9fdfe05022087728c8e47b6f0005937.patch'; exit 1;

  echo 'Cannot read asahi-655fc2f4be49460624df16bdda14bffdb524d07e.patch'; exit 1;

  echo 'Cannot read asahi-459b45aa5ead20ac4f364a54bc2ec10ca2fe6a89.patch'; exit 1;

  echo 'Cannot read asahi-44a39842f92eb2be2a238da909d6ed3510621d36.patch'; exit 1;

  echo 'Cannot read asahi-21e2b962e438b761a448bb6f4ab36ab5549a739f.patch'; exit 1;

  echo 'Cannot read asahi-9d50956a6674b2883f64345e2c8816b0c30e4df2.patch'; exit 1;

  echo 'Cannot read asahi-8aa706b2daa49b64102e44067d8514de8a26dc42.patch'; exit 1;

  echo 'Cannot read asahi-b66d7bc5b0ce0d625436766c887400a9e6c0f2f1.patch'; exit 1;

  echo 'Cannot read asahi-8cdc16f7da5175ac09a67caa05dd73c204ed9ef9.patch'; exit 1;

  echo 'Cannot read asahi-50b02ee98bf104873351bf1a40a5d09e4ed3ba52.patch'; exit 1;

  echo 'Cannot read asahi-cc66189884fd09d00b3b0113c08687f2274a8e15.patch'; exit 1;

  echo 'Cannot read asahi-5eddf1994b2812e86f0ff550daec0c19335a05a7.patch'; exit 1;

  echo 'Cannot read asahi-bef5ffc28080e2cfea5300347757855c0d3c8955.patch'; exit 1;

  echo 'Cannot read asahi-045e48531efcfbb5e058a5515a931fdde996092d.patch'; exit 1;

  echo 'Cannot read asahi-e71bce920193087c04c18217434538a3f374c87f.patch'; exit 1;

  echo 'Cannot read asahi-f3845a541a924d2596f06f4dfcf504f9786b1145.patch'; exit 1;

  echo 'Cannot read asahi-c8f2183def80ff59aaefb3ea4cec8200ad88bd2e.patch'; exit 1;

  echo 'Cannot read asahi-0ed8eedee5bf4447bca8d26c5ecc693e7aed4aad.patch'; exit 1;

  echo 'Cannot read asahi-24675d697e32b3b85e72dae9e70325e8a63fba33.patch'; exit 1;

  echo 'Cannot read asahi-8d259ae7a33e317fa04f590c3d2fe548e4e62c57.patch'; exit 1;

  echo 'Cannot read asahi-32e5c782a67af41306f3169000b527277860c44f.patch'; exit 1;

  echo 'Cannot read asahi-5191f0e2ceb6901289a1bb2c627890dbf8432f18.patch'; exit 1;

  echo 'Cannot read asahi-4411224f218ee67526f74d10cd3b3a7cd70ff2ad.patch'; exit 1;

}

build() {
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

}

package() {
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

  # A spec %files section (it could be that part of the next lines duplicate part of the package() function)
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/uboot-asahi/ Licenses/*
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/uboot-asahi/  README doc/develop/distro.rst doc/README.gpt
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/uboot-asahi/  doc/develop/uefi doc/usage doc/arch/arm64.rst
  _install fakeinstall/usr/bin/*
  _install fakeinstall/usr/share/man/man1/dumpimage.1*
  _install fakeinstall/usr/share/man/man1/kwboot.1*
  _install fakeinstall/usr/share/man/man1/mkeficapsule.1*
  _install fakeinstall/usr/share/man/man1/mkimage.1*

  # -n uboot-images-armv8
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/uboot-asahi/ Licenses/*
  install -m755 -d ${pkgdir}/usr/share/uboot/
  _install fakeinstall/usr/share/uboot/*
}
