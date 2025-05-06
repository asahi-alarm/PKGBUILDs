
Name:           rust-muvm
Version:        0.4.1
Release:        1
Summary:        Run programs from your system in a microVM

License:        MIT
URL:            https://crates.io/crates/muvm
Source:         %{crates_source}
Source2:        50-muvm-access.conf
Source3:        access-muvm.lua

BuildRequires:  cargo-rpm-macros >= 26

ExclusiveArch:  x86_64 aarch64

%description
Run programs from your system in a microVM.

%package     -n muvm
Summary:        Run programs from your system in a microVM

License:        Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)

Obsoletes:      krun < 0.1.0-2

Requires:       libkrun >= 1.9.8-1
Requires:       passt
Requires:       socat
Requires:       (wireplumber if pipewire)

%description -n muvm
Run programs from your system in a microVM.

%files       -n muvm
%license LICENSE
%license LICENSE.dependencies
/usr/bin/muvm
/usr/bin/muvm-guest
/usr/share/wireplumber/wireplumber.conf.d/50-muvm-access.conf
/usr/share/wireplumber/scripts/client/access-muvm.lua

%prep

cd './'
rm -rf 'muvm-0.4.1'
rpmuncompress -x '%{crates_source}'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'muvm-0.4.1'
chmod -Rf a+rX,u+w,g-w,o-w .

%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install
mkdir -p fakeinstall/usr/share/wireplumber/wireplumber.conf.d
mkdir -p fakeinstall/usr/share/wireplumber/scripts/client
cp -p 50-muvm-access.conf fakeinstall/usr/share/wireplumber/wireplumber.conf.d
cp -p access-muvm.lua fakeinstall/usr/share/wireplumber/scripts/client

%check
%cargo_test

