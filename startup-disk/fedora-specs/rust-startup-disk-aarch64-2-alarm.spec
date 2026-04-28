
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

prepare() {

  cd './'
  rm -rf 'startup-disk-0.1.7'
  tar -xf '%{crates_source}'
  STATUS=$?
  if [ $STATUS -ne 0 ]; then
    exit $STATUS
  fi
  cd 'startup-disk-0.1.7'
  chmod -Rf a+rX,u+w,g-w,o-w .

  %cargo_prep

  %generate_buildrequires
  %cargo_generate_buildrequires

}

build() {
  %cargo_build
  %{cargo_license_summary}
  %{cargo_license} > LICENSE.dependencies

}

package() {
  %cargo_install
  make install-data DESTDIR="fakeinstall" DATADIR="/usr/share"

  #       -n startup-disk
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/startup-disk/ LICENSE
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/startup-disk/ LICENSE.dependencies
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/startup-disk/  README.md
  _install fakeinstall/usr/bin/startup-disk
  _install fakeinstall/usr/share/applications/org.startup_disk.StartupDisk.desktop
  _install fakeinstall/usr/share/icons/hicolor/scalable/apps/org.startup_disk.StartupDisk.svg
  _install fakeinstall/usr/share/polkit-1/actions/org.startup_disk.StartupDisk.policy
  _install fakeinstall/usr/share/metainfo/org.startup_disk.StartupDisk.metainfo.xml

}

check() {
  %cargo_test
  make check-data
}
