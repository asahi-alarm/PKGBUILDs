
Name:           rust-startup-disk
Version:        0.1.7
Release:        1
Summary:        Interface to choose the startup volume on Apple Silicon systems

License:        MIT
URL:            https://crates.io/crates/startup-disk
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  make

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
Startup Disk provides a simple interface to choose the startup volume on Apple
Silicon Macs running Asahi Linux.

%package     -n startup-disk
Summary:        Interface to choose the startup volume on Apple Silicon systems

License:        ((Apache-2.0 OR MIT) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT) AND Zlib

Requires:       hicolor-icon-theme
Requires:       polkit
Requires:       sudo

%description -n startup-disk
Startup Disk provides a simple interface to choose the startup volume on Apple
Silicon Macs running Asahi Linux.

%files       -n startup-disk
%license LICENSE
%license LICENSE.dependencies
%doc README.md
/usr/bin/startup-disk
/usr/share/applications/org.startup_disk.StartupDisk.desktop
/usr/share/icons/hicolor/scalable/apps/org.startup_disk.StartupDisk.svg
/usr/share/polkit-1/actions/org.startup_disk.StartupDisk.policy
/usr/share/metainfo/org.startup_disk.StartupDisk.metainfo.xml

%prep

cd './'
rm -rf 'startup-disk-0.1.7'
rpmuncompress -x '%{crates_source}'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'startup-disk-0.1.7'
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
make install-data DESTDIR="fakeinstall" DATADIR="/usr/share"

%check
%cargo_test
make check-data

