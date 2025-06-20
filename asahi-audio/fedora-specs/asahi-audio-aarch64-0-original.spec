#global date 20231209
#global commit 35311b68945f25c10397f4e894e7045f8359143a
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}

Name:           asahi-audio
Version:        3.4%{?commit:^%{date}git%{shortcommit}}
Release:        %autorelease
Summary:        PipeWire DSP profiles for Apple Silicon machines
License:        MIT
URL:            https://github.com/AsahiLinux/asahi-audio
%if %{defined commit}
Source:         %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
%else
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
%endif

BuildArch:      noarch

BuildRequires:  make
Requires:       pipewire >= 1.0
Requires:       wireplumber >= 0.5.1-2
Requires:       pipewire-module-filter-chain-lv2
Requires:       lsp-plugins-lv2 >= 1.2.13-2
Requires:       lv2-bankstown >= 1.1.0
# https://bugzilla.redhat.com/show_bug.cgi?id=2361562
%if 0%{?fedora}
Requires:       lv2-triforce >= 0.2.0
%endif
Recommends:     speakersafetyd

%description
PipeWire and WirePlumber DSP profiles and configurations to
drive the speaker arrays in Apple Silicon laptops and desktops.

%prep
%autosetup %{?commit:-n %{name}-%{commit}}

%build
%make_build

%install
%make_install PREFIX=%{_prefix} DATA_DIR=%{_datadir}

%files
%license LICENSE
%doc README.md
%{_datadir}/asahi-audio/
%{_datadir}/wireplumber/scripts/device/asahi-limit-volume.lua
%{_datadir}/wireplumber/wireplumber.conf.d/99-asahi.conf
%{_datadir}/pipewire/pipewire.conf.d/99-asahi.conf
%{_datadir}/pipewire/pipewire-pulse.conf.d/99-asahi.conf

%changelog
%autochangelog
