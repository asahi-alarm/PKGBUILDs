
  Name:           rust-bankstown-lv2
  Version:        1.1.0
  Release:        1
  Summary:        Barebones, fast LV2 bass enhancement plugin

  License:        MIT
  URL:            https://crates.io/crates/bankstown-lv2
  Source:         %{crates_source}

  BuildRequires:  cargo-rpm-macros >= 24
  BuildRequires:  make

  ExcludeArch:    ppc64le s390x

  %description
  Bankstown is a barebones, fast LV2 bass enhancement plugin implementing
  halfway-decent three-stage psychoacoustic bass approximation.

  %package     -n lv2-bankstown
  Summary:        Barebones, fast LV2 bass enhancement plugin
  License:        MIT AND (MIT OR Apache-2.0)
  Requires:       lv2
  Provides:       bankstown-lv2 = 1.1.0-1
  Provides:       bankstown-lv2(aarch-64) = 1.1.0-1
  Obsoletes:      bankstown-lv2 < 1.0.0-2

  %description -n lv2-bankstown
  Bankstown is a barebones, fast LV2 bass enhancement plugin implementing
  halfway-decent three-stage psychoacoustic bass approximation.

prepare() {

  cd './'
  rm -rf 'bankstown-lv2-1.1.0'
  tar -xf '%{crates_source}'
  STATUS=$?
  if [ $STATUS -ne 0 ]; then
    exit $STATUS
  fi
  cd 'bankstown-lv2-1.1.0'
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
  /usr/bin/make install DESTDIR=fakeinstall INSTALL="install -p" LIBDIR="/usr/lib"

  #       -n lv2-bankstown
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/bankstown/ LICENSE
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/bankstown/ LICENSE.dependencies
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/bankstown/  README.md
  _install fakeinstall/usr/lib/lv2/bankstown.lv2/

}

check() {
  %cargo_test
}
