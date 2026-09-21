%undefine _auto_set_build_flags
# Undefining _auto_set_build_flags does not appear to work. Instead define
# the duild flags to nil.
%global build_cflags %{nil}
%global build_ldflags %{nil}

Name:     avd-fw
Version:  0.1
Release:  %autorelease
Summary:  Firmware for Apple/Asahi AVD video decoder V4L2 driver
License:  MIT
URL:      https://github.com/AsahiLinux/avd-fw
Source:   https://github.com/AsahiLinux/avd-fw/archive/v%{version}/avd-fw-%{version}.tar.gz

BuildRequires:  meson >= 1.3.0
BuildRequires:  arm-none-eabi-gcc-cs
BuildRequires:  arm-none-eabi-binutils-cs

BuildArch:      noarch

%global debug_package %{nil}

%description
Firmware for Apple/Asahi AVD video decoder V4L2 driver while the driver
is only in the downstream kernel and the firmware can't yet submitted to
linux-firmware.

%prep
%autosetup -N -n %{name}-%{version}

%build
%meson \
  --libdir=lib \
  -Dfirmwaredir=firmware/updates \
  --cross-file=./arm-none-eabi-gcc.ini \
  %{nil}
%meson_build

%install
%meson_install

%files
%{_prefix}/lib/firmware/updates/apple

%changelog
%autochangelog
