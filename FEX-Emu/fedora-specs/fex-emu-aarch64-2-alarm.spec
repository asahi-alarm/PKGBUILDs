
  Name:       fex-emu
  Version:    2412
  Release:    1
  Summary:    Fast usermode x86 and x86-64 emulator for ARM64

  License:    MIT AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND GPL-2.0-only AND GPL-2.0-or-later
  URL:        https://fex-emu.com

  Source0:    https://github.com/FEX-Emu/FEX/archive/FEX-2412/FEX-FEX-2412.tar.gz
  Source1:    README.fedora

  Source2:    fex-sysroot-macros.inc

  Source3:    fex-sysroot-fc41-20241221.tar.gz
  Source4:    toolchain_x86_32.cmake
  Source5:    toolchain_x86_64.cmake
  SourceLicense: MIT AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND GPL-2.0-only AND GPL-2.0-or-later ( ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-2-Clause) AND ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-3-Clause) AND ((GPL-2.0-only WITH Linux-syscall-note) OR CDDL-1.0) AND ((GPL-2.0-only WITH Linux-syscall-note) OR Linux-OpenIB) AND ((GPL-2.0-only WITH Linux-syscall-note) OR MIT) AND ((GPL-2.0-or-later WITH Linux-syscall-note) OR BSD-3-Clause) AND ((GPL-2.0-or-later WITH Linux-syscall-note) OR MIT) AND BSD-3-Clause AND (GPL-1.0-or-later WITH Linux-syscall-note) AND GPL-2.0-only AND (GPL-2.0-only WITH Linux-syscall-note) AND (GPL-2.0-or-later WITH Linux-syscall-note) AND (LGPL-2.0-or-later WITH Linux-syscall-note) AND (LGPL-2.1-only WITH Linux-syscall-note) AND (LGPL-2.1-or-later WITH Linux-syscall-note) AND MIT ) AND( GPL-3.0-or-later AND LGPL-3.0-or-later AND (GPL-3.0-or-later WITH GCC-exception-3.1) AND (GPL-3.0-or-later WITH Texinfo-exception) AND (LGPL-2.1-or-later WITH GCC-exception-2.0) AND (GPL-2.0-or-later WITH GCC-exception-2.0) AND (GPL-2.0-or-later WITH GNU-compiler-exception) AND BSL-1.0 AND GFDL-1.3-or-later AND Linux-man-pages-copyleft-2-para AND SunPro AND BSD-1-Clause AND BSD-2-Clause AND BSD-2-Clause-Views AND BSD-3-Clause AND BSD-4-Clause AND BSD-Source-Code AND Zlib AND MIT AND Apache-2.0 AND (Apache-2.0 WITH LLVM-Exception) AND ZPL-2.1 AND ISC AND LicenseRef-Fedora-Public-Domain AND HP-1986 AND curl AND Martin-Birgmeier AND HPND-Markus-Kuhn AND dtoa AND SMLNJ AND AMD-newlib AND OAR AND HPND-merchantability-variant AND HPND-Intel ) AND( LGPL-2.1-or-later AND SunPro AND LGPL-2.1-or-later WITH GCC-exception-2.0 AND BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later WITH GNU-compiler-exception AND GPL-2.0-only AND ISC AND LicenseRef-Fedora-Public-Domain AND HPND AND CMU-Mach AND LGPL-2.0-or-later AND Unicode-3.0 AND GFDL-1.1-or-later AND GPL-1.0-or-later AND FSFUL AND MIT AND Inner-Net-2.0 AND X11 AND GPL-2.0-or-later WITH GCC-exception-2.0 AND GFDL-1.3-only AND GFDL-1.1-only )

  Patch0:     0001-Thunks-gen-Add-support-for-compiling-against-clang-1.patch
  Patch1:     0001-Library-Forwarding-Allow-reading-standard-library-he.patch

  Source101: https://github.com/catchorg/Catch2/archive/8ac8190/Catch2-8ac8190.tar.gz
  Source102: https://github.com/Sonicadvance1/cpp-optparse/archive/eab4212/cpp-optparse-eab4212.tar.gz
  Provides: bundled(cpp-optparse) = 0
  Source103: https://github.com/FEX-Emu/drm-headers/archive/8efb6dc/drm-headers-8efb6dc.tar.gz
  Provides: bundled(kernel) = 6.11
  Source104: https://github.com/fmtlib/fmt/archive/0c9fce2/fmt-0c9fce2.tar.gz
  Provides: bundled(fmt) = 11.0.2
  Source105: https://github.com/FEX-Emu/jemalloc/archive/02ca52b/jemalloc-02ca52b.tar.gz
  Provides: bundled(jemalloc) = 5.3.0
  Source106: https://github.com/FEX-Emu/jemalloc/archive/4043539/jemalloc-4043539.tar.gz
  Provides: bundled(jemalloc) = 5.3.0
  Source107: https://github.com/FEX-Emu/robin-map/archive/d5683d9/robin-map-d5683d9.tar.gz
  Provides: bundled(robin-map) = 1.3.0
  Source108: https://github.com/FEX-Emu/vixl/archive/a90f5d5/vixl-a90f5d5.tar.gz
  Provides: bundled(vixl) = 5.1.0
  Source109: https://github.com/KhronosGroup/Vulkan-Headers/archive/29f979e/Vulkan-Headers-29f979e.tar.gz
  Provides: bundled(vulkan-headers) = 1.3.296
  Source110: https://github.com/herumi/xbyak/archive/c68cc53/xbyak-c68cc53.tar.gz
  Source111: https://github.com/Cyan4973/xxhash/archive/bbb27a5/xxhash-bbb27a5.tar.gz
  Provides: bundled(xxhash) = 0.8.2

  ExclusiveArch:  aarch64

  BuildRequires:  cmake
  BuildRequires:  clang
  BuildRequires:  git-core
  BuildRequires:  lld
  BuildRequires:  llvm
  BuildRequires:  ninja-build
  BuildRequires:  python3

  BuildRequires:  python3-setuptools

  BuildRequires:  sed
  BuildRequires:  systemd-rpm-macros

  BuildRequires:  libepoxy-devel
  BuildRequires:  SDL2-devel

  BuildRequires:  alsa-lib-devel
  BuildRequires:  clang-devel
  BuildRequires:  libdrm-devel
  BuildRequires:  libglvnd-devel
  BuildRequires:  libX11-devel
  BuildRequires:  libXrandr-devel
  BuildRequires:  llvm-devel
  BuildRequires:  openssl-devel
  BuildRequires:  wayland-devel
  BuildRequires:  zlib-devel

  BuildRequires:  cmake(Qt6Qml)
  BuildRequires:  cmake(Qt6Quick)
  BuildRequires:  cmake(Qt6Widgets)

  Requires:       systemd-udev
  Requires:       fex-emu-filesystem = 2412-1

  Recommends:     fex-emu-thunks = 2412-1

  Recommends:     fex-emu-rootfs-fedora
  Recommends:     erofs-fuse
  Recommends:     erofs-utils
  Recommends:     squashfs-tools
  Recommends:     squashfuse

  Obsoletes:      fex-emu-gdb < 2409-4
  Provides:       fex-emu-gdb = 2412-1

  %description
  FEX allows you to run x86 and x86-64 binaries on an AArch64 host, similar to
  qemu-user and box86. It has native support for a rootfs overlay, so you don't
  need to chroot, as well as some thunklibs so it can forward things like GL to
  the host. FEX presents a Linux 5.0+ interface to the guest, and supports only
  AArch64 as a host. FEX is very much work in progress, so expect things to
  change.

  %package        filesystem
  Summary:        FEX rootfs and overlay filesystem
  BuildArch:      noarch

  %description    filesystem
  FEX rootfs and overlay filesystem.

  %package        devel
  Summary:        Development headers and libraries for fex-emu
  Requires:       fex-emu(aarch-64) = 2412-1

  %description    devel
  This package provides development headers and libraries for fex-emu.

  %package        utils
  Summary:        Utility tools for fex-emu
  Requires:       fex-emu(aarch-64) = 2412-1

  %description    utils
  This package provides utility tools for fex-emu for advanced users.

  %package        thunks
  Summary:        Thunk libraries for fex-emu
  Requires:       fex-emu(aarch-64) = 2412-1

  %description    thunks
  This package provides host library thunks for fex-emu.

prepare() {
  cd './'
  rm -rf 'FEX-FEX-2412'
  tar -xf 'FEX-FEX-2412.tar.gz'
  STATUS=$?
  if [ $STATUS -ne 0 ]; then
    exit $STATUS
  fi
  cd 'FEX-FEX-2412'
  chmod -Rf a+rX,u+w,g-w,o-w .

  # Copy in our README.fedora

  # Unpack bundled libraries
  mkdir -p External/../Source/Common/cpp-optparse
  tar -xzf cpp-optparse-eab4212.tar.gz --strip-components=1 -C External/../Source/Common/cpp-optparse
  mkdir -p External/drm-headers
  tar -xzf drm-headers-8efb6dc.tar.gz --strip-components=1 -C External/drm-headers
  mkdir -p External/fmt
  tar -xzf fmt-0c9fce2.tar.gz --strip-components=1 -C External/fmt
  mkdir -p External/jemalloc
  tar -xzf jemalloc-02ca52b.tar.gz --strip-components=1 -C External/jemalloc
  mkdir -p External/jemalloc_glibc
  tar -xzf jemalloc-4043539.tar.gz --strip-components=1 -C External/jemalloc_glibc
  mkdir -p External/robin-map
  tar -xzf robin-map-d5683d9.tar.gz --strip-components=1 -C External/robin-map
  mkdir -p External/vixl
  tar -xzf vixl-a90f5d5.tar.gz --strip-components=1 -C External/vixl
  mkdir -p External/Vulkan-Headers
  tar -xzf Vulkan-Headers-29f979e.tar.gz --strip-components=1 -C External/Vulkan-Headers
  mkdir -p External/xxhash
  tar -xzf xxhash-bbb27a5.tar.gz --strip-components=1 -C External/xxhash

  # This is done after so we can patch the bundled libraries if needed

  cat 0001-Thunks-gen-Add-support-for-compiling-against-clang-1.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat 0001-Library-Forwarding-Allow-reading-standard-library-he.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  # Ensure library soversion is set
  sed -i FEXCore/Source/CMakeLists.txt \
    -e '/PROPERTIES OUTPUT_NAME/aset_target_properties(${Name} PROPERTIES VERSION 2412)'

  # Set up sysroot and toolchain files

    # Unpack and prepare sysroot
    tar xzf fex-sysroot-fc41-20241221.tar.gz
    cp -p toolchain_x86_32.cmake toolchain_x86_64.cmake .
    CPPINC="/$(cd sysroot; ls -d usr/include/c++/*)"
    sed -i "s,%CPPINC%,$CPPINC,g" toolchain_*.cmake

}

build() {
  %cmake -G Ninja \
      -DUSE_FEXCONFIG_TOOLKIT=qt \
      -DENABLE_OFFLINE_TELEMETRY=OFF \
      -DBUILD_THUNKS=ON \
      -DENABLE_CLANG_THUNKS=ON \
      -DBUILD_TESTS=OFF \
      -DBUILD_FEX_LINUX_TESTS=OFF \
      -DX86_DEV_ROOTFS=$PWD/sysroot \
      -DX86_32_TOOLCHAIN_FILE=$PWD/toolchain_x86_32.cmake \
      -DX86_64_TOOLCHAIN_FILE=$PWD/toolchain_x86_64.cmake \

  %cmake_build

}

package() {
  %cmake_install

  # These are used to store RootFS and overlays for FEX that will be provided
  # by other packages
  install -Ddpm0755 fakeinstall/usr/share/fex-emu/RootFS/
  install -Ddpm0755 fakeinstall/usr/share/fex-emu/overlays/

  # This is for running tests only (and gets installed into the wrong libdir)
  rm fakeinstall/usr/lib/libfex_thunk_test.so

  %postun
  if [ $1 -eq 0 ]; then
  /bin/systemctl try-restart systemd-binfmt.service
  fi

  # A spec %files section (it could be that part of the next lines duplicate part of the package() function)
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/FEX-Emu/ LICENSE
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/FEX-Emu/  Readme.md README.fedora docs
  _install fakeinstall/usr/bin/FEXBash
  _install fakeinstall/usr/bin/FEXGetConfig
  _install fakeinstall/usr/bin/FEXInterpreter
  _install fakeinstall/usr/bin/FEXLoader
  _install fakeinstall/usr/bin/FEXpidof
  _install fakeinstall/usr/bin/FEXServer
  _install fakeinstall/usr/lib/libFEXCore.so.2412
  %{_binfmtdir}/FEX-x86.conf
  %{_binfmtdir}/FEX-x86_64.conf
  _install fakeinstall/usr/share/fex-emu/AppConfig/
  _install fakeinstall/usr/share/man/man1/FEX.1*

  # filesystem
  install -m755 -d ${pkgdir}/usr/share/fex-emu/
  install -m755 -d ${pkgdir}/usr/share/fex-emu/RootFS
  install -m755 -d ${pkgdir}/usr/share/fex-emu/overlays

  # devel
  _install fakeinstall/usr/include/FEXCore/
  _install fakeinstall/usr/lib/libFEXCore.so

  # utils
  _install fakeinstall/usr/bin/FEXConfig
  _install fakeinstall/usr/bin/FEXRootFSFetcher

  # thunks
  _install fakeinstall/usr/lib/fex-emu/HostThunks/
  _install fakeinstall/usr/lib/fex-emu/HostThunks_32/
  _install fakeinstall/usr/share/fex-emu/ThunksDB.json
  _install fakeinstall/usr/share/fex-emu/GuestThunks/
  _install fakeinstall/usr/share/fex-emu/GuestThunks_32/
}
