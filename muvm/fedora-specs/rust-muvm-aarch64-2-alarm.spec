
  Name:           rust-muvm
  Version:        0.2.0
  Release:        1
  Summary:        Run programs from your system in a microVM

  License:        MIT
  URL:            https://crates.io/crates/muvm
  Source:         %{crates_source}
  Patch1:         0001-x11-Fix-XAUTHORITY-handling-for-wildcard-DISPLAY.patch

  BuildRequires:  cargo-rpm-macros >= 26

  ExclusiveArch:  x86_64 aarch64

  %description
  Run programs from your system in a microVM.

  %package     -n muvm
  Summary:        Run programs from your system in a microVM

  License:        Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)

  Obsoletes:      krun < 0.1.0-2

  Requires:       dhcp-client
  Requires:       libkrun >= 1.9.8-1
  Requires:       passt
  Requires:       socat
  Requires:       sommelier

  %description -n muvm
  Run programs from your system in a microVM.

prepare() {

  cd './'
  rm -rf 'muvm-0.2.0'
  tar -xf '%{crates_source}'
  STATUS=$?
  if [ $STATUS -ne 0 ]; then
    exit $STATUS
  fi
  cd 'muvm-0.2.0'
  chmod -Rf a+rX,u+w,g-w,o-w .

  cat 0001-x11-Fix-XAUTHORITY-handling-for-wildcard-DISPLAY.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

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

  #       -n muvm
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/muvm/ LICENSE
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/muvm/ LICENSE.dependencies
  _install fakeinstall/usr/bin/muvm
  _install fakeinstall/usr/bin/muvm-guest
  _install fakeinstall/usr/bin/muvm-hidpipe
  _install fakeinstall/usr/bin/muvm-server
  _install fakeinstall/usr/bin/muvm-x11bridge

}

check() {
  %cargo_test
}
