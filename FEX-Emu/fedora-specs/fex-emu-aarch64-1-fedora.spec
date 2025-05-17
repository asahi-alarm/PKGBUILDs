
Name:       fex-emu
Version:    2505
Release:    1
Summary:    Fast usermode x86 and x86-64 emulator for ARM64

License:    MIT AND Apache-2.0 AND BSD-3-Clause AND GPL-2.0-only
URL:        https://fex-emu.com

Source0:    https://github.com/FEX-Emu/FEX/archive/FEX-2505/FEX-FEX-2505.tar.gz

Source1:    README.fedora

Source2:    fex-sysroot-macros.inc

Source3:    fex-sysroot-fc42-20250510.tar.gz
Source4:    toolchain_x86_32.cmake
Source5:    toolchain_x86_64.cmake
Source6:    build-fex-sysroot.sh
SourceLicense: MIT AND Apache-2.0 AND BSD-3-Clause AND GPL-2.0-only ( ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-2-Clause) AND ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-3-Clause) AND ((GPL-2.0-only WITH Linux-syscall-note) OR CDDL-1.0) AND ((GPL-2.0-only WITH Linux-syscall-note) OR Linux-OpenIB) AND ((GPL-2.0-only WITH Linux-syscall-note) OR MIT) AND ((GPL-2.0-or-later WITH Linux-syscall-note) OR BSD-3-Clause) AND ((GPL-2.0-or-later WITH Linux-syscall-note) OR MIT) AND BSD-3-Clause AND (GPL-1.0-or-later WITH Linux-syscall-note) AND GPL-2.0-only AND (GPL-2.0-only WITH Linux-syscall-note) AND (GPL-2.0-or-later WITH Linux-syscall-note) AND (LGPL-2.0-or-later WITH Linux-syscall-note) AND (LGPL-2.1-only WITH Linux-syscall-note) AND (LGPL-2.1-or-later WITH Linux-syscall-note) AND MIT ) AND( GPL-3.0-or-later AND LGPL-3.0-or-later AND (GPL-3.0-or-later WITH GCC-exception-3.1) AND (GPL-3.0-or-later WITH Texinfo-exception) AND (LGPL-2.1-or-later WITH GCC-exception-2.0) AND (GPL-2.0-or-later WITH GCC-exception-2.0) AND (GPL-2.0-or-later WITH GNU-compiler-exception) AND BSL-1.0 AND GFDL-1.3-or-later AND Linux-man-pages-copyleft-2-para AND SunPro AND BSD-1-Clause AND BSD-2-Clause AND BSD-2-Clause-Views AND BSD-3-Clause AND BSD-4-Clause AND BSD-Source-Code AND Zlib AND MIT AND Apache-2.0 AND (Apache-2.0 WITH LLVM-Exception) AND ZPL-2.1 AND ISC AND LicenseRef-Fedora-Public-Domain AND HP-1986 AND curl AND Martin-Birgmeier AND HPND-Markus-Kuhn AND dtoa AND SMLNJ AND AMD-newlib AND OAR AND HPND-merchantability-variant AND HPND-Intel ) AND( LGPL-2.1-or-later AND SunPro AND LGPL-2.1-or-later WITH GCC-exception-2.0 AND BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later WITH GNU-compiler-exception AND GPL-2.0-only AND ISC AND LicenseRef-Fedora-Public-Domain AND HPND AND CMU-Mach AND LGPL-2.0-or-later AND Unicode-3.0 AND GFDL-1.1-or-later AND GPL-1.0-or-later AND FSFUL AND MIT AND Inner-Net-2.0 AND X11 AND GPL-2.0-or-later WITH GCC-exception-2.0 AND GFDL-1.3-only AND GFDL-1.1-only )

Source101: https://github.com/Sonicadvance1/cpp-optparse/archive/9f94388/cpp-optparse-9f94388.tar.gz
Provides: bundled(cpp-optparse) = 0
Source102: https://github.com/FEX-Emu/drm-headers/archive/0675d2f/drm-headers-0675d2f.tar.gz
Provides: bundled(kernel) = 6.13
Source103: https://github.com/FEX-Emu/jemalloc/archive/02ca52b/jemalloc-02ca52b.tar.gz
Provides: bundled(jemalloc) = 5.3.0
Source104: https://github.com/FEX-Emu/jemalloc/archive/4043539/jemalloc-4043539.tar.gz
Provides: bundled(jemalloc) = 5.3.0
Source105: https://github.com/FEX-Emu/robin-map/archive/d5683d9/robin-map-d5683d9.tar.gz
Provides: bundled(robin-map) = 1.3.0
Source106: https://github.com/KhronosGroup/Vulkan-Headers/archive/cacef30/Vulkan-Headers-cacef30.tar.gz
Provides: bundled(vulkan-headers) = 1.4.310

Patch:          https://github.com/FEX-Emu/FEX/commit/a37def2c22e528477f64296747228400ddc40222.patch

Patch:          https://github.com/FEX-Emu/FEX/commit/8eaf45414c05c9e7ef6f74a323d95fe7e0d883c1.patch

Patch:          https://github.com/FEX-Emu/FEX/commit/c326e2d669fd5e9356f6107e188413a449cc1fd7.patch

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

BuildRequires:  catch2-devel
BuildRequires:  fmt-devel
BuildRequires:  libepoxy-devel
BuildRequires:  SDL2-devel
BuildRequires:  xxhash-devel

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
Requires:       fex-emu-filesystem = 2505-1

Recommends:     fex-emu-thunks = 2505-1

Recommends:     fex-emu-rootfs-fedora
Recommends:     erofs-fuse
Recommends:     erofs-utils
Recommends:     squashfs-tools
Recommends:     squashfuse

Obsoletes:      fex-emu-gdb < 2409-4
Provides:       fex-emu-gdb = 2505-1

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
Requires:       fex-emu(aarch-64) = 2505-1

%description    devel
This package provides development headers and libraries for fex-emu.

%package        utils
Summary:        Utility tools for fex-emu
Requires:       fex-emu(aarch-64) = 2505-1

%description    utils
This package provides utility tools for fex-emu for advanced users.

%package        thunks
Summary:        Thunk libraries for fex-emu
Requires:       fex-emu(aarch-64) = 2505-1

%description    thunks
This package provides host library thunks for fex-emu.

%prep
cd './'
rm -rf 'FEX-FEX-2505'
rpmuncompress -x 'FEX-FEX-2505.tar.gz'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'FEX-FEX-2505'
chmod -Rf a+rX,u+w,g-w,o-w .

# Copy in our README.fedora

# Unpack bundled libraries
mkdir -p External/../Source/Common/cpp-optparse
tar -xzf cpp-optparse-9f94388.tar.gz --strip-components=1 -C External/../Source/Common/cpp-optparse
mkdir -p External/drm-headers
tar -xzf drm-headers-0675d2f.tar.gz --strip-components=1 -C External/drm-headers
mkdir -p External/jemalloc
tar -xzf jemalloc-02ca52b.tar.gz --strip-components=1 -C External/jemalloc
mkdir -p External/jemalloc_glibc
tar -xzf jemalloc-4043539.tar.gz --strip-components=1 -C External/jemalloc_glibc
mkdir -p External/robin-map
tar -xzf robin-map-d5683d9.tar.gz --strip-components=1 -C External/robin-map
mkdir -p External/Vulkan-Headers
tar -xzf Vulkan-Headers-cacef30.tar.gz --strip-components=1 -C External/Vulkan-Headers

# This is done after so we can patch the bundled libraries if needed

rpmuncompress a37def2c22e528477f64296747228400ddc40222.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress 8eaf45414c05c9e7ef6f74a323d95fe7e0d883c1.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress c326e2d669fd5e9356f6107e188413a449cc1fd7.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

# Ensure library soversion is set
sed -i FEXCore/Source/CMakeLists.txt \
  -e '/PROPERTIES OUTPUT_NAME/aset_target_properties(${Name} PROPERTIES VERSION 2505)'

# Set up sysroot and toolchain files

  # Unpack and prepare sysroot
  tar xzf fex-sysroot-fc42-20250510.tar.gz
  cp -p toolchain_x86_32.cmake toolchain_x86_64.cmake .
  CPPINC="/$(cd sysroot; ls -d usr/include/c++/*)"
  sed -i "s,%CPPINC%,$CPPINC,g" toolchain_*.cmake

%build
%cmake -G Ninja \
    -DENABLE_OFFLINE_TELEMETRY=OFF \
    -DBUILD_THUNKS=ON \
    -DENABLE_CLANG_THUNKS=ON \
    -DBUILD_TESTS=OFF \
    -DBUILD_FEX_LINUX_TESTS=OFF \
    -DX86_DEV_ROOTFS=$PWD/sysroot \
    -DX86_32_TOOLCHAIN_FILE=$PWD/toolchain_x86_32.cmake \
    -DX86_64_TOOLCHAIN_FILE=$PWD/toolchain_x86_64.cmake \

%cmake_build

%install
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

%files
%license LICENSE
%doc Readme.md README.fedora docs
/usr/bin/FEXBash
/usr/bin/FEXGetConfig
/usr/bin/FEXInterpreter
/usr/bin/FEXLoader
/usr/bin/FEXpidof
/usr/bin/FEXServer
/usr/lib/libFEXCore.so.2505
%{_binfmtdir}/FEX-x86.conf
%{_binfmtdir}/FEX-x86_64.conf
/usr/share/fex-emu/AppConfig/
/usr/share/man/man1/FEX.1*

%files filesystem
%dir /usr/share/fex-emu/
%dir /usr/share/fex-emu/RootFS
%dir /usr/share/fex-emu/overlays

%files devel
/usr/include/FEXCore/
/usr/lib/libFEXCore.so

%files utils
/usr/bin/FEXConfig
/usr/bin/FEXRootFSFetcher

%files thunks
/usr/lib/fex-emu/HostThunks/
/usr/lib/fex-emu/HostThunks_32/
/usr/share/fex-emu/ThunksDB.json
/usr/share/fex-emu/GuestThunks/
/usr/share/fex-emu/GuestThunks_32/

