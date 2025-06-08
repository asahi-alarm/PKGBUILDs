
Name:           rust-triforce-lv2
Version:        0.3.2
Release:        1
Summary:        Minimum variance distortionless response beamformer for Apple mic arrays

License:        GPL-2.0-or-later
URL:            https://crates.io/crates/triforce-lv2
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  make

ExcludeArch:    ppc64le s390x

%description
Minimum variance distortionless response beamformer for Apple mic
arrays.

%package     -n lv2-triforce
Summary:        Minimum variance distortionless response beamformer for Apple mic arrays

License:        Apache-2.0 AND GPL-2.0-or-later AND MIT AND (MIT OR Apache-2.0) AND (Zlib OR Apache-2.0 OR MIT)

Requires:       lv2

Provides:       triforce-lv2 = 0.3.2-1
Provides:       triforce-lv2(aarch-64) = 0.3.2-1
Obsoletes:      triforce-lv2 < 0.1.1-2

%description -n lv2-triforce
Minimum variance distortionless response beamformer for Apple mic
arrays.

%files       -n lv2-triforce
%license LICENCE.txt
%license LICENSE.dependencies
%doc README.md
/usr/lib/lv2/triforce.lv2/manifest.ttl
/usr/lib/lv2/triforce.lv2/triforce.ttl
/usr/lib/lv2/triforce.lv2/triforce.so

%prep

cd './'
rm -rf 'triforce-lv2-0.3.2'
rpmuncompress -x '%{crates_source}'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'triforce-lv2-0.3.2'
chmod -Rf a+rX,u+w,g-w,o-w .

%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
/usr/bin/make install DESTDIR=fakeinstall INSTALL="install -p" LIBDIR=/usr/lib

%check
%cargo_test

