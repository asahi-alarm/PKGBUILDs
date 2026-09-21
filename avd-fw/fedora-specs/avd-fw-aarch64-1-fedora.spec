
Name:     avd-fw
Version:  0.1
Release:  1
Summary:  Firmware for Apple/Asahi AVD video decoder V4L2 driver
License:  MIT
URL:      https://github.com/AsahiLinux/avd-fw
Source:   https://github.com/AsahiLinux/avd-fw/archive/v0.1/avd-fw-0.1.tar.gz

BuildRequires:  meson >= 1.3.0
BuildRequires:  arm-none-eabi-gcc-cs
BuildRequires:  arm-none-eabi-binutils-cs

BuildArch:      noarch

%description
Firmware for Apple/Asahi AVD video decoder V4L2 driver while the driver
is only in the downstream kernel and the firmware can't yet submitted to
linux-firmware.

%prep

cd './'
rm -rf 'avd-fw-0.1'
rpmuncompress -x 'avd-fw-0.1.tar.gz'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'avd-fw-0.1'
chmod -Rf a+rX,u+w,g-w,o-w .

%build
%meson \
  --libdir=lib \
  -Dfirmwaredir=firmware/updates \
  --cross-file=./arm-none-eabi-gcc.ini \

%meson_build

%install
%meson_install

%files
/usr/lib/firmware/updates/apple

