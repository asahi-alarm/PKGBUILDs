
  Name:           rust-triforce-lv2
  Version:        0.3.0
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

  Provides:       triforce-lv2 = 0.3.0-1
  Provides:       triforce-lv2(aarch-64) = 0.3.0-1
  Obsoletes:      triforce-lv2 < 0.1.1-2

  %description -n lv2-triforce
  Minimum variance distortionless response beamformer for Apple mic
  arrays.

prepare() {

  cd './'
  rm -rf 'triforce-lv2-0.3.0'
  tar -xf '%{crates_source}'
  STATUS=$?
  if [ $STATUS -ne 0 ]; then
    exit $STATUS
  fi
  cd 'triforce-lv2-0.3.0'
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
  /usr/bin/make install DESTDIR=fakeinstall INSTALL="install -p" LIBDIR=/usr/lib

  #       -n lv2-triforce
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/triforce-lv2/ LICENCE.txt
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/triforce-lv2/ LICENSE.dependencies
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/triforce-lv2/  README.md
  _install fakeinstall/usr/lib/lv2/triforce.lv2/manifest.ttl
  _install fakeinstall/usr/lib/lv2/triforce.lv2/triforce.ttl
  _install fakeinstall/usr/lib/lv2/triforce.lv2/triforce.so

}

check() {
  %cargo_test
}
