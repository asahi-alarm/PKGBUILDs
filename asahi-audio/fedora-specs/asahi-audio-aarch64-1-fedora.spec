
Name:           asahi-audio
Version:        3.4
Release:        1
Summary:        PipeWire DSP profiles for Apple Silicon machines
License:        MIT
URL:            https://github.com/AsahiLinux/asahi-audio

Source:         https://github.com/AsahiLinux/asahi-audio/archive/v3.4/asahi-audio-3.4.tar.gz

BuildArch:      noarch

BuildRequires:  make
Requires:       pipewire >= 1.0
Requires:       wireplumber >= 0.5.1-2
Requires:       pipewire-module-filter-chain-lv2
Requires:       lsp-plugins-lv2 >= 1.2.13-2
Requires:       lv2-bankstown >= 1.1.0

Requires:       lv2-triforce >= 0.2.0

Recommends:     speakersafetyd

%description
PipeWire and WirePlumber DSP profiles and configurations to
drive the speaker arrays in Apple Silicon laptops and desktops.

%prep

cd './'
rm -rf 'asahi-audio-3.4'
rpmuncompress -x 'asahi-audio-3.4.tar.gz'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'asahi-audio-3.4'
chmod -Rf a+rX,u+w,g-w,o-w .

%build
/usr/bin/make -O -j${RPM_BUILD_NCPUS} V=1 VERBOSE=1

%install
/usr/bin/make install DESTDIR=fakeinstall INSTALL="install -p" PREFIX=/usr DATA_DIR=/usr/share

%files
%license LICENSE
%doc README.md
/usr/share/asahi-audio/
/usr/share/wireplumber/scripts/device/asahi-limit-volume.lua
/usr/share/wireplumber/wireplumber.conf.d/99-asahi.conf
/usr/share/pipewire/pipewire.conf.d/99-asahi.conf
/usr/share/pipewire/pipewire-pulse.conf.d/99-asahi.conf

