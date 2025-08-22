%global debug_package %{nil}

# Chainloading support requires the aarch64-unknown-none-softfloat rust target,
# which is only available on aarch64
%ifarch aarch64
%bcond chainloading 1
%else
%bcond chainloading 0
%endif

# We need to vendor fatfs because m1n1 stage1 relies on unreleased changes
# (notably, the lfn feature): https://github.com/rafalh/rust-fatfs/issues/81
%global fatfs_commit 87fc1ed5074a32b4e0344fcdde77359ef9e75432

%global _description %{expand:
m1n1 is the bootloader developed by the Asahi Linux project to bridge the Apple
(XNU) boot ecosystem to the Linux boot ecosystem.}

Name:           m1n1
Version:        1.5.0
Release:        %autorelease
Summary:        Bootloader and experimentation playground for Apple Silicon

# m1n1 proper is MIT licensed, but it relies on a number of vendored projects
# See the "License" section in README.md for the breakdown
License:        MIT AND CC0-1.0 AND OFL-1.1-RFN AND Zlib AND (BSD-2-Clause OR GPL-2.0-or-later) AND (BSD-3-Clause OR GPL-2.0-or-later)
URL:            https://github.com/AsahiLinux/m1n1
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source:         https://github.com/rafalh/rust-fatfs/archive/%{fatfs_commit}/rust-fatfs-%{fatfs_commit}.tar.gz
# Use distribution packages instead of the vendored ones
Patch:          m1n1-rust-deps.patch
# https://github.com/rafalh/rust-fatfs/commit/eb274ca10d035c176e5eac79420ca734c02613ae
Patch:          rust-fatfs-fix-build-log.patch

%ifarch aarch64
# On aarch64 m1n1 does a native build
BuildRequires:  gcc
%else
# On non-aarch64 m1n1 does a cross build
BuildRequires:  gcc-aarch64-linux-gnu
%endif

%global buildflags RELEASE=1
BuildRequires:  make

# For the bootloader logos and the framebuffer console
BuildRequires:  adobe-source-code-pro-fonts
BuildRequires:  coreutils
BuildRequires:  fontconfig
BuildRequires:  system-logos
BuildRequires:  ImageMagick

# For the udev rule
BuildRequires:  systemd-rpm-macros

%if %{with chainloading}
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  rust-std-static-aarch64-unknown-none-softfloat
%endif

# These are bundled, modified and statically linked into m1n1
Provides:       bundled(arm-trusted-firmware)
Provides:       bundled(dwc3)
Provides:       bundled(dlmalloc)
Provides:       bundled(PDCLib)
Provides:       bundled(libfdt)
Provides:       bundled(minilzlib)
Provides:       bundled(tinf)

%description    %_description

%if %{with chainloading}
%package        stage1
Summary:        %{summary}
# The following breakdown only covers the rust dependencies
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
License:        MIT AND CC0-1.0 AND OFL-1.1-RFN AND Zlib AND (BSD-2-Clause OR GPL-2.0-or-later) AND (BSD-3-Clause OR GPL-2.0-or-later) AND (Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0)
# LICENSE.dependencies contains a full license breakdown of the rust dependencies

# This is vendored and statically linked into m1n1 when building for stage 1
Provides:       bundled(crate(fatfs))= 0.4.0

%description    stage1 %_description

This package contains the stage1 build of m1n1 that is used by the Asahi Linux
Installer.
%endif

%package        tools
Summary:        Developer tools for m1n1
Requires:       %{name} = %{version}-%{release}
Requires:       python3
Requires:       python3dist(construct)
Requires:       python3dist(pyserial)
Requires:       systemd-udev
BuildArch:      noarch

%description    tools %_description

This package contains various developer tools for m1n1.

%prep
%autosetup -N

# Use our logos
pushd data
ln -s %{_datadir}/pixmaps/bootloader/bootlogo_128.png fedora_128.png
ln -s %{_datadir}/pixmaps/bootloader/bootlogo_256.png fedora_256.png
popd

# Use our fonts
font="$(fc-match "Source Code Pro:bold" 'file' | cut -d= -f2)"
if [ ! -e "$font" ]; then
    echo "Failed to find font"
    exit 1
fi

pushd font
rm SourceCodePro-Bold.ttf font.bin font_retina.bin
./makefont.sh 8 16 12 "$font" font.bin
./makefont.sh 16 32 25 "$font" font_retina.bin
popd

%if %{with chainloading}
tar -xf %{SOURCE1} -C rust/vendor/rust-fatfs --strip-components 1
%autopatch -p1

%cargo_prep

%generate_buildrequires
cd rust
%cargo_generate_buildrequires
%endif

%build
%if %{with chainloading}
%make_build %{buildflags} CHAINLOADING=1 LOGO=fedora
mv build build-stage1
pushd rust
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
popd
%endif

%make_build %{buildflags} LOGO=fedora

%install
install -Dpm0644 -t %{buildroot}%{_libdir}/%{name} \
  build/%{name}.{bin,macho} build/%{name}-asahi.bin
%if %{with chainloading}
install -Dpm0644 -t %{buildroot}%{_libdir}/%{name}-stage1 \
  build-stage1/%{name}.{bin,macho} build-stage1/%{name}-asahi.bin
%endif
install -Ddpm0755 %{buildroot}%{_libexecdir}/%{name}
cp -pr proxyclient tools %{buildroot}%{_libexecdir}/%{name}/
install -Dpm0644 -t %{buildroot}%{_udevrulesdir} udev/80-m1n1.rules
install -Dpm0644 m1n1.conf.example %{buildroot}%{_sysconfdir}/m1n1.conf

%files
%license LICENSE 3rdparty_licenses/LICENSE.*
%doc README.md
%doc m1n1.conf.example
%{_libdir}/%{name}
%config(noreplace) %{_sysconfdir}/m1n1.conf

%if %{with chainloading}
%files stage1
%license LICENSE 3rdparty_licenses/LICENSE.* rust/vendor/rust-fatfs/LICENSE.txt rust/LICENSE.dependencies
%doc README.md
%{_libdir}/%{name}-stage1
%endif

%files tools
%{_libexecdir}/%{name}
%{_udevrulesdir}/80-m1n1.rules

%changelog
%autochangelog
