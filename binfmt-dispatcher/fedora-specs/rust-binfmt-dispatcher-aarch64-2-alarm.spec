
  Name:           rust-binfmt-dispatcher
  Version:        0.1.2
  Release:        1
  Summary:        Smart dispatcher for binfmt_misc

  License:        MIT
  URL:            https://crates.io/crates/binfmt-dispatcher
  Source:         %{crates_source}

  BuildRequires:  cargo-rpm-macros >= 24
  BuildRequires:  make
  BuildRequires:  systemd-rpm-macros

  %description
  binfmt-dispatcher is a simple dispatcher for binfmt_misc that dynamically picks the best interpreter to use at runtime.

  %package     -n binfmt-dispatcher
  Summary:        Smart dispatcher for binfmt_misc

  License:        ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND ISC AND MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)

  Requires:       polkit
  Requires:       systemd
  Recommends:     xdg-terminal-exec
  Recommends:     zenity

  %description -n binfmt-dispatcher
  binfmt-dispatcher is a simple dispatcher for binfmt_misc that dynamically picks the best interpreter to use at runtime.

prepare() {

  cd './'
  rm -rf 'binfmt-dispatcher-0.1.2'
  tar -xf '%{crates_source}'
  STATUS=$?
  if [ $STATUS -ne 0 ]; then
    exit $STATUS
  fi
  cd 'binfmt-dispatcher-0.1.2'
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
  make install-data DESTDIR="fakeinstall"
  install -Ddpm0755 fakeinstall/usr/lib/binfmt-dispatcher.d
  for f in fakeinstall%{_binfmtdir}/binfmt-dispatcher-*.conf; do mv "$f" "$(dirname "$f")/zz-$(basename "$f")"; done
  mv fakeinstall/usr/lib/binfmt-dispatcher.d/00-default.toml

  %postun      -n binfmt-dispatcher
  if [ $1 -eq 0 ]; then
  /bin/systemctl try-restart systemd-binfmt.service
  fi

  #       -n binfmt-dispatcher
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/binfmt-dispatcher/ LICENSE
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/binfmt-dispatcher/ LICENSE.dependencies
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/binfmt-dispatcher/  README.md
  _install fakeinstall/usr/bin/binfmt-dispatcher
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/binfmt-dispatcher/ binfmt-dispatcher.toml.example
  install -m755 -d ${pkgdir}/usr/lib/binfmt-dispatcher.d/
  %{_binfmtdir}/zz-binfmt-dispatcher-*.conf
  _install fakeinstall/usr/lib/binfmt-dispatcher.d/*.toml
  _install fakeinstall/usr/share/polkit-1/actions/org.AsahiLinux.binfmt_dispatcher.policy
  %config(noreplace) %ghost /etc/binfmt-dispatcher.toml

}

check() {
  %cargo_test
}
