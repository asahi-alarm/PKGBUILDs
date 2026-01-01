
Name:           rust-tiny-dfr
Version:        0.3.5
Release:        1
Summary:        Most basic dynamic function row daemon possible

License:        MIT AND Apache-2.0
URL:            https://crates.io/crates/tiny-dfr
Source:         %{crates_source}

Patch:          tiny-dfr-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  systemd-rpm-macros

ExcludeArch: i386 i486 i586 i686 pentium3 pentium4 athlon geode

%description
The most basic dynamic function row daemon possible.

%package     -n tiny-dfr
Summary:        Most basic dynamic function row daemon possible

License:        (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND ISC AND MIT AND (MIT AND Apache-2.0) AND (MIT OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)

%description -n tiny-dfr
The most basic dynamic function row daemon possible.

%files       -n tiny-dfr
%license LICENSE
%license LICENSE.material
%license LICENSE.dependencies
%doc README.md
/usr/bin/tiny-dfr
/usr/share/tiny-dfr/
%{_udevrulesdir}/*.rules
%{_unitdir}/tiny-dfr.service
%dir /etc/tiny-dfr/
%config(noreplace) %ghost /etc/tiny-dfr/config.toml

%prep

cd './'
rm -rf 'tiny-dfr-0.3.5'
rpmuncompress -x '%{crates_source}'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'tiny-dfr-0.3.5'
chmod -Rf a+rX,u+w,g-w,o-w .

rpmuncompress tiny-dfr-fix-metadata.diff | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install
install -Dpm0644 -t fakeinstall/usr/share/tiny-dfr share/tiny-dfr/*.svg share/tiny-dfr/config.toml
install -Ddpm0755 fakeinstall/etc/tiny-dfr
touch fakeinstall/etc/tiny-dfr/config.toml
install -Dpm0644 -t fakeinstall%{_udevrulesdir} etc/udev/rules.d/*.rules
install -Dpm0644 -t fakeinstall%{_unitdir} etc/systemd/system/tiny-dfr.service

%post -n tiny-dfr
%systemd_post tiny-dfr.service

%preun -n tiny-dfr
%systemd_preun tiny-dfr.service

%postun -n tiny-dfr
%systemd_postun_with_restart tiny-dfr.service

%check
%cargo_test

