
Name:           rust-speakersafetyd
Version:        1.0.2
Release:        1
Summary:        Speaker protection daemon for embedded Linux systems

License:        MIT
URL:            https://crates.io/crates/speakersafetyd
Source:         %{crates_source}

Patch:          speakersafetyd-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  systemd-rpm-macros

%description
Speaker protection daemon for embedded Linux systems.

%package     -n speakersafetyd
Summary:        Speaker protection daemon for embedded Linux systems

License:        (Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (MIT OR LGPL-3.0-or-later) AND MPL-2.0

Requires:       systemd-udev

%description -n speakersafetyd
Speaker protection daemon for embedded Linux systems.

%files       -n speakersafetyd
%license LICENSE
%license LICENSE.dependencies
%doc README.md
/usr/bin/speakersafetyd
/usr/share/speakersafetyd/
%{_unitdir}/speakersafetyd.service
/usr/com/speakersafetyd/
%{_udevrulesdir}/95-speakersafetyd.rules

%post -n speakersafetyd
%systemd_post speakersafetyd.service

%preun -n speakersafetyd
%systemd_preun speakersafetyd.service

%postun -n speakersafetyd
%systemd_postun_with_restart speakersafetyd.service

%prep

cd './'
rm -rf 'speakersafetyd-1.0.2'
rpmuncompress -x '%{crates_source}'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'speakersafetyd-1.0.2'
chmod -Rf a+rX,u+w,g-w,o-w .

echo 'Cannot read speakersafetyd-fix-metadata.diff'; exit 1;

%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install
install -p -m 0644 -D speakersafetyd.service fakeinstall%{_unitdir}/speakersafetyd.service
install -p -m 0644 -D 95-speakersafetyd.rules fakeinstall%{_udevrulesdir}/95-speakersafetyd.rules
install -d -m 0755 fakeinstall/usr/share/speakersafetyd/apple
install -p -m 0644 -t fakeinstall/usr/share/speakersafetyd/apple conf/apple/*
install -d -m 0755 fakeinstall/usr/com/speakersafetyd/blackbox

%check
%cargo_test

