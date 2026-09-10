Name:           asahi-fix27
Version:        0.1.0
Release:        1
Summary:        Fix macOS 27 bootability flag from linux side

SourceLicense:  GPL-2.0-only

License:        GPL-2.0-only AND MIT AND (Apache-2.0 OR MIT)

URL:            https://github.com/AsahiLinux/asahi-fix27
Source0:        https://github.com/AsahiLinux/asahi-fix27/archive/0.1.0/asahi-fix27-0.1.0.tar.gz

Source1:        asahi-fix27.1

ExcludeArch:    i386 i486 i586 i686 pentium3 pentium4 athlon geode

BuildRequires:  cargo-rpm-macros

%description
Fix macOS 27 bootability flag from linux side.

%prep

cd './'
rm -rf 'asahi-fix27-0.1.0'
rpmuncompress -x 'asahi-fix27-0.1.0.tar.gz'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'asahi-fix27-0.1.0'
chmod -Rf a+rX,u+w,g-w,o-w .

%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -t

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
install -D --preserve-timestamps --mode=0755 \
    --target='fakeinstall/usr/bin' target/rpm/asahi-fix27
install -D --preserve-timestamps --mode=0644 \
    --target='fakeinstall/usr/share/man/man1' 'asahi-fix27.1'

%check
%cargo_test

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
/usr/bin/asahi-fix27
/usr/share/man/man1/asahi-fix27.1*

