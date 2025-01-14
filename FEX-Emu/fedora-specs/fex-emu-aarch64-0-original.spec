#global date 20240816
#global commit 226f5e2f235909170a5e2214a4e8ce0402af61b9
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}

%global srcname FEX
%global forgeurl https://github.com/FEX-Emu/FEX

# FEX upstream only supports building with clang
%global toolchain clang

# We do not want to run integration tests in Fedora
%bcond integration 0

%if %{with integration}
%bcond check 1
%else
# Tests don't work for now
%bcond check 0
%endif

%if (0%{?fedora} && 0%{?fedora} >= 41)
%global has_sysroot 1
%bcond thunks 1
%else
%bcond thunks 0
%endif

# FEX does not support x86_64 hosts in production, only enable this when
# testing local builds for development
%bcond x86_debug 0

Name:       fex-emu
Version:    2412%{?commit:^%{date}git%{commit}}
Release:    %autorelease
Summary:    Fast usermode x86 and x86-64 emulator for ARM64

# FEX itself is MIT, see below for the bundled libraries
%global fex_license MIT AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND GPL-2.0-only AND GPL-2.0-or-later
License:    %{fex_license}
URL:        https://fex-emu.com
%if %{defined commit}
Source0:    %{forgeurl}/commit/%{commit}/%{srcname}-%{commit}.tar.gz
%else
Source0:    %{forgeurl}/archive/%{srcname}-%{version}/%{srcname}-%{srcname}-%{version}.tar.gz
Source1:    README.fedora
%endif

%if 0%{?has_sysroot}
Source2:    fex-sysroot-macros.inc
%include    %SOURCE2
Source3:    fex-sysroot-%{sysroot_version}.tar.gz
Source4:    toolchain_x86_32.cmake
Source5:    toolchain_x86_64.cmake
SourceLicense: %{fex_license} %{sysroot_license}
%endif

# Fix thunk build
Patch0:     0001-Thunks-gen-Add-support-for-compiling-against-clang-1.patch
Patch1:     0001-Library-Forwarding-Allow-reading-standard-library-he.patch

# Bundled dependencies managed as git submodules upstream
# These are too entangled with the build system to unbundle for now
# https://github.com/FEX-Emu/FEX/issues/2996
%{lua:
local externals = {
  { name="Catch2", ref="8ac8190", owner="catchorg", version="3.5.3", license="BSL-1.0", bcond="check" },
  { name="cpp-optparse", ref="eab4212", owner="Sonicadvance1", path="../Source/Common/cpp-optparse", license="MIT" },
  { name="drm-headers", ref="8efb6dc", owner="FEX-Emu", package="kernel", version="6.11", license="GPL-2.0-only" },
  --Exclude these altogether for now, as they're prebuilt binaries only needed for the integration tests
  --{ name="fex-gcc-target-tests-bins", ref="442678a", owner="FEX-Emu", license="GPL-2.0-or-later", bcond="integration" },
  --{ name="fex-gvisor-tests-bins", ref="71349ae", owner="FEX-Emu", license="Apache-2.0", bcond="integration" },
  --{ name="fex-posixtest-bins", ref="9ae2963", owner="FEX-Emu", package="posixtest", version="1.5.2", license="GPL-2.0-or-later", bcond="integration" },
  { name="fmt", ref="0c9fce2", owner="fmtlib", version="11.0.2", license="MIT" },
  --Excluded as we use the FEXConfig Qt backend instead
  --{ name="imgui", ref="4c986ec", owner="Sonicadvance1", version="1.73", license="MIT" },
  { name="jemalloc", ref="02ca52b", owner="FEX-Emu", version="5.3.0", license="MIT" },
  { name="jemalloc", ref="4043539", owner="FEX-Emu", path="jemalloc_glibc", version="5.3.0", license="MIT" },
  { name="robin-map", ref="d5683d9", owner="FEX-Emu", version="1.3.0", license="MIT" },
  { name="vixl", ref="a90f5d5", owner="FEX-Emu", version="5.1.0", license="BSD-3-Clause" },
  { name="Vulkan-Headers", ref="29f979e", owner="KhronosGroup", package="vulkan-headers", version="1.3.296", license="Apache-2.0" },
  { name="xbyak", ref="c68cc53", owner="herumi", version="7.09", license="BSD-3-Clause", bcond="x86_debug" },
  { name="xxhash", ref="bbb27a5", owner="Cyan4973", version="0.8.2", license="BSD-2-Clause" },
}

for i, s in ipairs(externals) do
  si = 100 + i
  print(string.format("Source%d: https://github.com/%s/%s/archive/%s/%s-%s.tar.gz", si, s.owner, s.name, s.ref, s.name, s.ref).."\n")
  if s.bcond and not rpm.isdefined(string.format("with_%s", s.bcond)) then goto continue1 end
  print(string.format("Provides: bundled(%s) = %s", (s.package or s.name), (s.version or "0")).."\n")
  ::continue1::
end

function print_setup_externals()
  for i, s in ipairs(externals) do
    si = 100 + i
    if s.bcond and not rpm.isdefined(string.format("with_%s", s.bcond)) then goto continue2 end
    print(string.format("mkdir -p External/%s", (s.path or s.name)).."\n")
    print(string.format("tar -xzf %s --strip-components=1 -C External/%s", rpm.expand("%{SOURCE"..si.."}"), (s.path or s.name)).."\n")
    ::continue2::
  end
end
}

# FEX upstream only supports these architectures
%if %{with x86_debug}
ExclusiveArch:  %{arm64} %{x86_64}
%else
ExclusiveArch:  %{arm64}
%endif

BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  git-core
BuildRequires:  lld
BuildRequires:  llvm
BuildRequires:  ninja-build
BuildRequires:  python3
%ifarch %{arm64}
BuildRequires:  python3-setuptools
%endif
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
%if %{with check}
BuildRequires:  nasm
BuildRequires:  python3-clang
%endif

BuildRequires:  libepoxy-devel
BuildRequires:  SDL2-devel
%if %{with thunks}
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
%endif

BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)

Requires:       systemd-udev
Requires:       %{name}-filesystem = %{version}-%{release}
%if %{with thunks}
Recommends:     %{name}-thunks = %{version}-%{release}
%endif

Recommends:     fex-emu-rootfs-fedora
Recommends:     erofs-fuse
Recommends:     erofs-utils
Recommends:     squashfs-tools
Recommends:     squashfuse

# Drop once f42 is retired
Obsoletes:      fex-emu-gdb < 2409-4
Provides:       fex-emu-gdb = %{version}-%{release}

# Do not check guest thunks for requires, since these are x86-64 binaries that link against libs in the FEX RootFS.
%global __requires_exclude_from ^%{_datadir}/fex-emu/GuestThunks.*$

# Do not check guest and host thunks for provides, since these are not general system libraries on the host.
%global __provides_exclude_from ^(%{_datadir}/fex-emu/GuestThunks.*|%{_libdir}/fex-emu/HostThunks.*)$

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
%{summary}.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package provides development headers and libraries for %{name}.

%package        utils
Summary:        Utility tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
This package provides utility tools for %{name} for advanced users.

%if %{with thunks}
%package        thunks
Summary:        Thunk libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    thunks
This package provides host library thunks for %{name}.
%endif

%prep
%if %{defined commit}
%setup -q -n %{srcname}-%{commit}
%else
%setup -q -n %{srcname}-%{srcname}-%{version}
%endif

# Copy in our README.fedora
cp -p %SOURCE1 .

# Unpack bundled libraries
%{lua: print_setup_externals()}

# This is done after so we can patch the bundled libraries if needed
%autopatch -p1

# Ensure library soversion is set
sed -i FEXCore/Source/CMakeLists.txt \
  -e '/PROPERTIES OUTPUT_NAME/aset_target_properties(${Name} PROPERTIES VERSION %{version})'

# Set up sysroot and toolchain files

%if 0%{?has_sysroot}
  # Unpack and prepare sysroot
  tar xzf %SOURCE3
  cp -p %SOURCE4 %SOURCE5 .
  CPPINC="/$(cd sysroot; ls -d usr/include/c++/*)"
  sed -i "s,%%CPPINC%%,$CPPINC,g" toolchain_*.cmake
%endif

%build
%cmake -G Ninja \
    -DUSE_FEXCONFIG_TOOLKIT=qt \
    -DENABLE_OFFLINE_TELEMETRY=OFF \
%ifarch %{x86_64}
    -DENABLE_X86_HOST_DEBUG=ON \
%endif
%if %{with thunks}
    -DBUILD_THUNKS=ON \
    -DENABLE_CLANG_THUNKS=ON \
%endif
%if %{with check}
    -DBUILD_TESTS=ON \
%else
    -DBUILD_TESTS=OFF \
%endif
%if %{with integration}
    -DBUILD_FEX_LINUX_TESTS=ON \
%else
    -DBUILD_FEX_LINUX_TESTS=OFF \
%endif
%if 0%{?has_sysroot}
    -DX86_DEV_ROOTFS=$PWD/sysroot \
    -DX86_32_TOOLCHAIN_FILE=$PWD/toolchain_x86_32.cmake \
    -DX86_64_TOOLCHAIN_FILE=$PWD/toolchain_x86_64.cmake \
%endif
    %{nil}

%cmake_build

%install
%cmake_install

# These are used to store RootFS and overlays for FEX that will be provided
# by other packages
install -Ddpm0755 %{buildroot}%{_datadir}/fex-emu/RootFS/
install -Ddpm0755 %{buildroot}%{_datadir}/fex-emu/overlays/

%if %{with thunks}
# This is for running tests only (and gets installed into the wrong libdir)
rm %{buildroot}/usr/lib/libfex_thunk_test.so
%else
# Not useful without thunks
rm %{buildroot}%{_datadir}/fex-emu/ThunksDB.json
%endif

%postun
if [ $1 -eq 0 ]; then
/bin/systemctl try-restart systemd-binfmt.service
fi

%if %{with check}
%check
%ctest
%endif

%files
%license LICENSE
%doc Readme.md README.fedora docs
%{_bindir}/FEXBash
%{_bindir}/FEXGetConfig
%{_bindir}/FEXInterpreter
%{_bindir}/FEXLoader
%{_bindir}/FEXpidof
%{_bindir}/FEXServer
%{_libdir}/libFEXCore.so.%{version}
%{_binfmtdir}/FEX-x86.conf
%{_binfmtdir}/FEX-x86_64.conf
%{_datadir}/fex-emu/AppConfig/
%{_mandir}/man1/FEX.1*

%files filesystem
%dir %{_datadir}/fex-emu/
%dir %{_datadir}/fex-emu/RootFS
%dir %{_datadir}/fex-emu/overlays

%files devel
%{_includedir}/FEXCore/
%{_libdir}/libFEXCore.so

%files utils
%{_bindir}/FEXConfig
%{_bindir}/FEXRootFSFetcher

%if %{with thunks}
%files thunks
%{_libdir}/fex-emu/HostThunks/
%{_libdir}/fex-emu/HostThunks_32/
%{_datadir}/fex-emu/ThunksDB.json
%{_datadir}/fex-emu/GuestThunks/
%{_datadir}/fex-emu/GuestThunks_32/
%endif

%changelog
%autochangelog
