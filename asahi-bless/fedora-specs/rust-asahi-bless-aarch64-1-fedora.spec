
Name:           rust-asahi-bless
Version:        0.4.2
Release:        1
Summary:        Tool to select active boot partition on ARM Macs

License:        MIT
URL:            https://crates.io/crates/asahi-bless
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%description
A tool to select active boot partition on ARM Macs.

%package     -n asahi-bless
Summary:        Tool to select active boot partition on ARM Macs

License:        MIT AND Zlib AND (Apache-2.0 OR MIT)

%description -n asahi-bless
A tool to select active boot partition on ARM Macs.

%files       -n asahi-bless
%license LICENSE
%license LICENSE.dependencies
/usr/bin/asahi-bless

%package        devel
Summary:        Tool to select active boot partition on ARM Macs
BuildArch:      noarch

%description    devel
A tool to select active boot partition on ARM Macs.

This package contains library source intended for building other packages which
use the "asahi-bless" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%{crate_instdir}/

%package     -n rust-asahi-bless+default-devel
Summary:        Tool to select active boot partition on ARM Macs
BuildArch:      noarch

%description -n rust-asahi-bless+default-devel
A tool to select active boot partition on ARM Macs.

This package contains library source intended for building other packages which
use the "default" feature of the "asahi-bless" crate.

%files       -n rust-asahi-bless+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep

cd './'
rm -rf 'asahi-bless-0.4.2'
rpmuncompress -x '%{crates_source}'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'asahi-bless-0.4.2'
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

%check
%cargo_test

