%global srcname alsa-ucm-conf-asahi
#global date 20231209
#global commit 334f21ccd388dbe292338b2942950dfeadfb3c83
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}

Name:           alsa-ucm-asahi
Version:        8%{?commit:^%{date}git%{shortcommit}}
Release:        %autorelease
Summary:        ALSA Use Case Manager configuration (and topologies) for Apple silicon devices
License:        BSD-3-Clause

URL:            https://github.com/AsahiLinux/alsa-ucm-conf-asahi
%if %{defined commit}
Source:         %{url}/archive/%{commit}/%{srcname}-%{commit}.tar.gz
%else
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
%endif

BuildArch:      noarch

Requires:       alsa-ucm >= 1.2.7.2

%description
The ALSA Use Case Manager configuration (and topologies) for Apple silicon devices.

%prep
%if %{defined commit}
%autosetup -n %{srcname}-%{commit}
%else
%autosetup -n %{srcname}-%{version}
%endif

%install
install -dm 755 %{buildroot}%{_datadir}/alsa/ucm2/conf.d/
cp -a ucm2/conf.d/aop_audio/ %{buildroot}%{_datadir}/alsa/ucm2/conf.d/
cp -a ucm2/conf.d/macaudio/ %{buildroot}%{_datadir}/alsa/ucm2/conf.d/

%files
%license LICENSE.asahi
%doc README.asahi
%{_datadir}/alsa/ucm2/conf.d/aop_audio/
%{_datadir}/alsa/ucm2/conf.d/macaudio/

%changelog
%autochangelog
