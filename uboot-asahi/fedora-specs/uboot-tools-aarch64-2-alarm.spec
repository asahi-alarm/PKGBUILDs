
  Name:     uboot-tools
  Version:  2023.07
  Release:  5
  Summary:  U-Boot utilities
  License:  GPLv2+ BSD LGPL-2.1+ LGPL-2.0+
  URL:      http://www.denx.de/wiki/U-Boot

  ExcludeArch: s390x
  Source0:  https://ftp.denx.de/pub/u-boot/u-boot-2023.07.tar.bz2
  Source1:  aarch64-boards

  Patch2:   smbios-Simplify-reporting-of-unknown-values.patch
  Patch3:   0001-disable-NFS-support-by-default.patch
  Patch4:   fix-release-rev.patch

  Patch5:   rpi-Enable-using-the-DT-provided-by-the-Raspberry-Pi.patch

  Patch6:   rockchip-Add-initial-support-for-the-PinePhone-Pro.patch
  Patch7:   0001-Revert-rockchip-rockpro64-Build-u-boot-rockchip-spi..patch

  Patch100: https://github.com/AsahiLinux/u-boot/commit/f28906758d6ae5edfd265df75e94697e50ba973e.patch#/asahi-f28906758d6ae5edfd265df75e94697e50ba973e.patch

  Patch101: https://github.com/AsahiLinux/u-boot/commit/d2afe04bc7fe1db4ff4323822f07ab36400ba902.patch#/asahi-d2afe04bc7fe1db4ff4323822f07ab36400ba902.patch

  Patch102: https://github.com/AsahiLinux/u-boot/commit/403e6561b81e465863e980844f71a2c64a672492.patch#/asahi-403e6561b81e465863e980844f71a2c64a672492.patch

  Patch103: https://github.com/AsahiLinux/u-boot/commit/ae41d19a39a7f1eff327d6e0eaef3a31cf44b055.patch#/asahi-ae41d19a39a7f1eff327d6e0eaef3a31cf44b055.patch

  Patch104: https://github.com/AsahiLinux/u-boot/commit/8ee5429c68beae7a8bfa6fd019fec017093d4483.patch#/asahi-8ee5429c68beae7a8bfa6fd019fec017093d4483.patch

  Patch105: https://github.com/AsahiLinux/u-boot/commit/89f1801b1a53b2cfd668f9dd92305a7b2410c9e2.patch#/asahi-89f1801b1a53b2cfd668f9dd92305a7b2410c9e2.patch

  Patch106: https://github.com/AsahiLinux/u-boot/commit/ee317f3f2f00f9a6e29b09b6c8fc981dbeba51c6.patch#/asahi-ee317f3f2f00f9a6e29b09b6c8fc981dbeba51c6.patch

  Patch107: https://github.com/AsahiLinux/u-boot/commit/07e39c5e717c917187091687c17f6b8e2f6b18c5.patch#/asahi-07e39c5e717c917187091687c17f6b8e2f6b18c5.patch

  Patch108: https://github.com/AsahiLinux/u-boot/commit/dae9ae738e9489bfbd19e57a5d71d5365eb893b8.patch#/asahi-dae9ae738e9489bfbd19e57a5d71d5365eb893b8.patch

  Patch109: https://github.com/AsahiLinux/u-boot/commit/eb7a3b52c7ddcbb7641b85f63783240964c30d06.patch#/asahi-eb7a3b52c7ddcbb7641b85f63783240964c30d06.patch

  Patch110: https://github.com/AsahiLinux/u-boot/commit/be836c7e251ef6617b773740bdfe1e682144320c.patch#/asahi-be836c7e251ef6617b773740bdfe1e682144320c.patch

  Patch111: https://github.com/AsahiLinux/u-boot/commit/3eaded9904190e322975ed936f5396726107ec20.patch#/asahi-3eaded9904190e322975ed936f5396726107ec20.patch

  Patch112: https://github.com/AsahiLinux/u-boot/commit/c782e304a068b65e8c9926a974f2e3ae248a5d81.patch#/asahi-c782e304a068b65e8c9926a974f2e3ae248a5d81.patch

  Patch113: https://github.com/AsahiLinux/u-boot/commit/de4de7a2d9132da92ad5cfc7cd71cdfb514b4b6f.patch#/asahi-de4de7a2d9132da92ad5cfc7cd71cdfb514b4b6f.patch

  Patch114: https://github.com/AsahiLinux/u-boot/commit/38eae1d40a21019238b6b39be1ac648a737624e4.patch#/asahi-38eae1d40a21019238b6b39be1ac648a737624e4.patch

  Patch115: https://github.com/AsahiLinux/u-boot/commit/71345875f8f49f1ed1b5d4a183adeee77ab62e62.patch#/asahi-71345875f8f49f1ed1b5d4a183adeee77ab62e62.patch

  Patch116: https://github.com/AsahiLinux/u-boot/commit/3d4ff95b859111da800f937f27be8775907d88c2.patch#/asahi-3d4ff95b859111da800f937f27be8775907d88c2.patch

  Patch117: https://github.com/AsahiLinux/u-boot/commit/b9926890b37ecd2269858f7771b11932ae8b2ea2.patch#/asahi-b9926890b37ecd2269858f7771b11932ae8b2ea2.patch

  Patch118: https://github.com/AsahiLinux/u-boot/commit/3a6996e261a698d33627460efd1604deb44dde90.patch#/asahi-3a6996e261a698d33627460efd1604deb44dde90.patch

  Patch119: https://github.com/AsahiLinux/u-boot/commit/46d6873a2428a9e037660312d756c0ca412b1bdf.patch#/asahi-46d6873a2428a9e037660312d756c0ca412b1bdf.patch

  Patch120: https://github.com/AsahiLinux/u-boot/commit/a79ee83e71a28825425cbe8ec9af8d2609367683.patch#/asahi-a79ee83e71a28825425cbe8ec9af8d2609367683.patch

  Patch121: https://github.com/AsahiLinux/u-boot/commit/20df54a0355bbbc30b682f00d0648183734bf0bd.patch#/asahi-20df54a0355bbbc30b682f00d0648183734bf0bd.patch

  Patch122: https://github.com/AsahiLinux/u-boot/commit/ce490b6f0502cdba56004838f0b52bb5c942da1f.patch#/asahi-ce490b6f0502cdba56004838f0b52bb5c942da1f.patch

  Patch123: https://github.com/AsahiLinux/u-boot/commit/8079fe5d87267868381dd1928c70e3d95042f7da.patch#/asahi-8079fe5d87267868381dd1928c70e3d95042f7da.patch

  Patch124: https://github.com/AsahiLinux/u-boot/commit/405aa60ef20a9cbaf770b1edc7ed1fc5feb1056e.patch#/asahi-405aa60ef20a9cbaf770b1edc7ed1fc5feb1056e.patch

  Patch125: https://github.com/AsahiLinux/u-boot/commit/fca97b0c02d6d6e6a2a03631772369d5044756f8.patch#/asahi-fca97b0c02d6d6e6a2a03631772369d5044756f8.patch

  Patch126: https://github.com/AsahiLinux/u-boot/commit/8b8a56cb1e8465a1a9ce40d329b70e83af485026.patch#/asahi-8b8a56cb1e8465a1a9ce40d329b70e83af485026.patch

  Patch127: https://github.com/AsahiLinux/u-boot/commit/ad398d3dbf53703fea52dd3f144c64d1fb51fe09.patch#/asahi-ad398d3dbf53703fea52dd3f144c64d1fb51fe09.patch

  Patch128: https://github.com/AsahiLinux/u-boot/commit/d797bf2643013840f5247ae8a0511d38e7eacb00.patch#/asahi-d797bf2643013840f5247ae8a0511d38e7eacb00.patch

  Patch129: https://github.com/AsahiLinux/u-boot/commit/ae6fe5bd9ad88dfe4bb40e35f79508e2de5d2a8d.patch#/asahi-ae6fe5bd9ad88dfe4bb40e35f79508e2de5d2a8d.patch

  Patch130: https://github.com/AsahiLinux/u-boot/commit/d063fc77c802a2ec4f1679cd1f8d95871e96e75c.patch#/asahi-d063fc77c802a2ec4f1679cd1f8d95871e96e75c.patch

  Patch131: https://github.com/AsahiLinux/u-boot/commit/40d8c4d337e5c1a1bf55ded9eba3e2ce3a38dd6e.patch#/asahi-40d8c4d337e5c1a1bf55ded9eba3e2ce3a38dd6e.patch

  Patch132: https://github.com/AsahiLinux/u-boot/commit/311d4fe3b468dccb62cca8b49b648b30afeeacf0.patch#/asahi-311d4fe3b468dccb62cca8b49b648b30afeeacf0.patch

  Patch133: https://github.com/AsahiLinux/u-boot/commit/efc46536d89374c0bf07c95c95c597fecf366b38.patch#/asahi-efc46536d89374c0bf07c95c95c597fecf366b38.patch

  Patch134: https://github.com/AsahiLinux/u-boot/commit/d4ef6c148d5152500ba11ad0d9c451fe46d8f693.patch#/asahi-d4ef6c148d5152500ba11ad0d9c451fe46d8f693.patch

  Patch135: https://github.com/AsahiLinux/u-boot/commit/039791d6bc96194defda3c4d6daffad11d64e2a1.patch#/asahi-039791d6bc96194defda3c4d6daffad11d64e2a1.patch

  Patch136: https://github.com/AsahiLinux/u-boot/commit/d63c269a019b15a4143957d20e162a8e460056b3.patch#/asahi-d63c269a019b15a4143957d20e162a8e460056b3.patch

  Patch137: https://github.com/AsahiLinux/u-boot/commit/97bb2192361741021a4291d19f88a2bb69ad2f32.patch#/asahi-97bb2192361741021a4291d19f88a2bb69ad2f32.patch

  Patch138: https://github.com/AsahiLinux/u-boot/commit/b7cc8dac8646c91690adcccb4d065135ff540684.patch#/asahi-b7cc8dac8646c91690adcccb4d065135ff540684.patch

  Patch139: https://github.com/AsahiLinux/u-boot/commit/b4cc61d057065794933120215d8b60f8a83380a2.patch#/asahi-b4cc61d057065794933120215d8b60f8a83380a2.patch

  Patch140: https://github.com/AsahiLinux/u-boot/commit/0190c00f5687ef54817f75b86cec8595b736c3f8.patch#/asahi-0190c00f5687ef54817f75b86cec8595b736c3f8.patch

  Patch141: https://github.com/AsahiLinux/u-boot/commit/35693e4799c9cd61f3c970aaad920b9b143959dd.patch#/asahi-35693e4799c9cd61f3c970aaad920b9b143959dd.patch

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

  BuildRequires:  arm-trusted-firmware-armv8
  BuildRequires:  python3-pyelftools

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
  rm -rf 'u-boot-2023.07'
  tar -xf 'u-boot-2023.07.tar.bz2'
  STATUS=$?
  if [ $STATUS -ne 0 ]; then
    exit $STATUS
  fi
  cd 'u-boot-2023.07'
  chmod -Rf a+rX,u+w,g-w,o-w .

  echo 'Cannot read smbios-Simplify-reporting-of-unknown-values.patch'; exit 1;

  echo 'Cannot read 0001-disable-NFS-support-by-default.patch'; exit 1;

  echo 'Cannot read fix-release-rev.patch'; exit 1;

  echo 'Cannot read rpi-Enable-using-the-DT-provided-by-the-Raspberry-Pi.patch'; exit 1;

  echo 'Cannot read rockchip-Add-initial-support-for-the-PinePhone-Pro.patch'; exit 1;

  echo 'Cannot read 0001-Revert-rockchip-rockpro64-Build-u-boot-rockchip-spi..patch'; exit 1;

  echo 'Cannot read asahi-f28906758d6ae5edfd265df75e94697e50ba973e.patch'; exit 1;

  echo 'Cannot read asahi-d2afe04bc7fe1db4ff4323822f07ab36400ba902.patch'; exit 1;

  echo 'Cannot read asahi-403e6561b81e465863e980844f71a2c64a672492.patch'; exit 1;

  echo 'Cannot read asahi-ae41d19a39a7f1eff327d6e0eaef3a31cf44b055.patch'; exit 1;

  echo 'Cannot read asahi-8ee5429c68beae7a8bfa6fd019fec017093d4483.patch'; exit 1;

  echo 'Cannot read asahi-89f1801b1a53b2cfd668f9dd92305a7b2410c9e2.patch'; exit 1;

  echo 'Cannot read asahi-ee317f3f2f00f9a6e29b09b6c8fc981dbeba51c6.patch'; exit 1;

  echo 'Cannot read asahi-07e39c5e717c917187091687c17f6b8e2f6b18c5.patch'; exit 1;

  echo 'Cannot read asahi-dae9ae738e9489bfbd19e57a5d71d5365eb893b8.patch'; exit 1;

  echo 'Cannot read asahi-eb7a3b52c7ddcbb7641b85f63783240964c30d06.patch'; exit 1;

  echo 'Cannot read asahi-be836c7e251ef6617b773740bdfe1e682144320c.patch'; exit 1;

  echo 'Cannot read asahi-3eaded9904190e322975ed936f5396726107ec20.patch'; exit 1;

  echo 'Cannot read asahi-c782e304a068b65e8c9926a974f2e3ae248a5d81.patch'; exit 1;

  echo 'Cannot read asahi-de4de7a2d9132da92ad5cfc7cd71cdfb514b4b6f.patch'; exit 1;

  echo 'Cannot read asahi-38eae1d40a21019238b6b39be1ac648a737624e4.patch'; exit 1;

  echo 'Cannot read asahi-71345875f8f49f1ed1b5d4a183adeee77ab62e62.patch'; exit 1;

  echo 'Cannot read asahi-3d4ff95b859111da800f937f27be8775907d88c2.patch'; exit 1;

  echo 'Cannot read asahi-b9926890b37ecd2269858f7771b11932ae8b2ea2.patch'; exit 1;

  echo 'Cannot read asahi-3a6996e261a698d33627460efd1604deb44dde90.patch'; exit 1;

  echo 'Cannot read asahi-46d6873a2428a9e037660312d756c0ca412b1bdf.patch'; exit 1;

  echo 'Cannot read asahi-a79ee83e71a28825425cbe8ec9af8d2609367683.patch'; exit 1;

  echo 'Cannot read asahi-20df54a0355bbbc30b682f00d0648183734bf0bd.patch'; exit 1;

  echo 'Cannot read asahi-ce490b6f0502cdba56004838f0b52bb5c942da1f.patch'; exit 1;

  echo 'Cannot read asahi-8079fe5d87267868381dd1928c70e3d95042f7da.patch'; exit 1;

  echo 'Cannot read asahi-405aa60ef20a9cbaf770b1edc7ed1fc5feb1056e.patch'; exit 1;

  echo 'Cannot read asahi-fca97b0c02d6d6e6a2a03631772369d5044756f8.patch'; exit 1;

  echo 'Cannot read asahi-8b8a56cb1e8465a1a9ce40d329b70e83af485026.patch'; exit 1;

  echo 'Cannot read asahi-ad398d3dbf53703fea52dd3f144c64d1fb51fe09.patch'; exit 1;

  echo 'Cannot read asahi-d797bf2643013840f5247ae8a0511d38e7eacb00.patch'; exit 1;

  echo 'Cannot read asahi-ae6fe5bd9ad88dfe4bb40e35f79508e2de5d2a8d.patch'; exit 1;

  echo 'Cannot read asahi-d063fc77c802a2ec4f1679cd1f8d95871e96e75c.patch'; exit 1;

  echo 'Cannot read asahi-40d8c4d337e5c1a1bf55ded9eba3e2ce3a38dd6e.patch'; exit 1;

  echo 'Cannot read asahi-311d4fe3b468dccb62cca8b49b648b30afeeacf0.patch'; exit 1;

  echo 'Cannot read asahi-efc46536d89374c0bf07c95c95c597fecf366b38.patch'; exit 1;

  echo 'Cannot read asahi-d4ef6c148d5152500ba11ad0d9c451fe46d8f693.patch'; exit 1;

  echo 'Cannot read asahi-039791d6bc96194defda3c4d6daffad11d64e2a1.patch'; exit 1;

  echo 'Cannot read asahi-d63c269a019b15a4143957d20e162a8e460056b3.patch'; exit 1;

  echo 'Cannot read asahi-97bb2192361741021a4291d19f88a2bb69ad2f32.patch'; exit 1;

  echo 'Cannot read asahi-b7cc8dac8646c91690adcccb4d065135ff540684.patch'; exit 1;

  echo 'Cannot read asahi-b4cc61d057065794933120215d8b60f8a83380a2.patch'; exit 1;

  echo 'Cannot read asahi-0190c00f5687ef54817f75b86cec8595b736c3f8.patch'; exit 1;

  echo 'Cannot read asahi-35693e4799c9cd61f3c970aaad920b9b143959dd.patch'; exit 1;

  echo 'Cannot read asahi-0203fd3d70b229ea2e50abe40b85ae8adc5c49f3.patch'; exit 1;

}

build() {
  mkdir builds

  /usr/bin/make -O -j${RPM_BUILD_NCPUS} V=1 VERBOSE=1 HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="" tools-only_defconfig O=builds/
  /usr/bin/make -O -j${RPM_BUILD_NCPUS} V=1 VERBOSE=1 HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="" tools-all O=builds/

  for board in $(cat aarch64-boards)
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
    BINMAN_ALLOW_MISSING=1 /usr/bin/make -O -j${RPM_BUILD_NCPUS} V=1 VERBOSE=1 HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="" O=builds/$(echo $board)/

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

}

package() {
  mkdir -p fakeinstall/usr/bin
  mkdir -p fakeinstall/usr/share/man/man1
  mkdir -p fakeinstall/usr/share/uboot/

  for board in $(ls builds)
  do
   mkdir -p fakeinstall/usr/share/uboot/$(echo $board)/
   for file in u-boot.bin u-boot.dtb u-boot.img u-boot-dtb.img u-boot.itb u-boot-sunxi-with-spl.bin u-boot-rockchip.bin idbloader.img idbloader.spi spl/boot.bin spl/sunxi-spl.bin
   do
    if [ -f builds/$(echo $board)/$(echo $file) ]; then
      install -p -m 0644 builds/$(echo $board)/$(echo $file) fakeinstall/usr/share/uboot/$(echo $board)/
    fi
   done
  done

  # For Apple M1 we also need the nodtb variant
  install -p -m 0644 builds/apple_m1/u-boot-nodtb.bin fakeinstall/usr/share/uboot/apple_m1/u-boot-nodtb.bin

  # Bit of a hack to remove binaries we don't use as they're large
  for board in $(ls builds)
  do
    rm -f fakeinstall/usr/share/uboot/$(echo $board)/u-boot.dtb
    if [ -f fakeinstall/usr/share/uboot/$(echo $board)/u-boot-sunxi-with-spl.bin ]; then
      rm -f fakeinstall/usr/share/uboot/$(echo $board)/u-boot{,-dtb}.*
    fi
    if [ -f fakeinstall/usr/share/uboot/$(echo $board)/MLO ]; then
      rm -f fakeinstall/usr/share/uboot/$(echo $board)/u-boot.bin
    fi
    if [ -f fakeinstall/usr/share/uboot/$(echo $board)/SPL ]; then
      rm -f fakeinstall/usr/share/uboot/$(echo $board)/u-boot.bin
    fi
    if [ -f fakeinstall/usr/share/uboot/$(echo $board)/u-boot.imx ]; then
      rm -f fakeinstall/usr/share/uboot/$(echo $board)/u-boot.bin
    fi
    if [ -f fakeinstall/usr/share/uboot/$(echo $board)/u-boot-spl.kwb ]; then
      rm -f fakeinstall/usr/share/uboot/$(echo $board)/u-boot.*
      rm -f fakeinstall/usr/share/uboot/$(echo $board)/u-boot-spl.bin
    fi
    if [ -f fakeinstall/usr/share/uboot/$(echo $board)/idbloader.img ]; then
      rm -f fakeinstall/usr/share/uboot/$(echo $board)/u-boot.bin
      rm -f fakeinstall/usr/share/uboot/$(echo $board)/u-boot{,-dtb}.img
    fi
  done

  for tool in dumpimage env/fw_printenv fit_check_sign fit_info gdb/gdbcont gdb/gdbsend gen_eth_addr gen_ethaddr_crc ifwitool img2srec kwboot mkeficapsule mkenvimage mkimage mksunxiboot ncb proftool sunxi-spl-image-builder
  do
  install -p -m 0755 builds/tools/$tool fakeinstall/usr/bin
  done
  install -p -m 0644 doc/mkimage.1 fakeinstall/usr/share/man/man1

  install -p -m 0755 builds/tools/env/fw_printenv fakeinstall/usr/bin
  ( cd fakeinstall/usr/bin; ln -sf fw_printenv fw_setenv )

  # Copy some useful docs over
  mkdir -p builds/docs
  cp -p board/hisilicon/hikey/README builds/docs/README.hikey
  cp -p board/rockchip/evb_rk3399/README builds/docs/README.evb_rk3399
  cp -p board/sunxi/README.sunxi64 builds/docs/README.sunxi64
  cp -p board/sunxi/README.nand builds/docs/README.sunxi-nand

  # A spec %files section (it could be that part of the next lines duplicate part of the package() function)
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/uboot-asahi/  README doc/develop/distro.rst doc/README.gpt
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/uboot-asahi/  doc/README.rockchip doc/develop/uefi doc/usage doc/arch/arm64.rst
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/uboot-asahi/  builds/docs/* doc/board/amlogic/ doc/board/rockchip/
  _install fakeinstall/usr/bin/*
  _install fakeinstall/usr/share/man/man1/mkimage.1*
  install -m755 -d ${pkgdir}/usr/share/uboot/

  # -n uboot-images-armv8
  _install fakeinstall/usr/share/uboot/*
}
