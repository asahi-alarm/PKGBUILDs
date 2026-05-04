
  Summary: WPA/WPA2/IEEE 802.1X Supplicant
  Name: wpa_supplicant
  Epoch: 1
  Version: 2.11
  Release: 10
  License: BSD-3-Clause
  Source0: http://w1.fi/releases/wpa_supplicant-2.11.tar.gz
  Source1: wpa_supplicant.conf
  Source2: wpa_supplicant.service
  Source3: wpa_supplicant.sysconfig
  Source4: wpa_supplicant.logrotate

  Patch0: wpa_supplicant-defconfig-keep-options-we-ve-traditionally-used-enab.patch

  Patch1: wpa_supplicant-assoc-timeout.patch

  Patch2: wpa_supplicant-flush-debug-output.patch

  Patch3: wpa_supplicant-quiet-scan-results-message.patch

  Patch4: wpa_supplicant-gui-qt4.patch

  Patch6: wpa_supplicant-defconfig-keep-CONFIG_WEP-enabled.patch

  Patch7: wpa_supplicant-defconfig-enable-WPA-EAP-SUITE-B-192-ciphers.patch
  Patch8: wpa_supplicant-defconfig-enable-OCV-support.patch

  Patch9: wpa_supplicant-allow-legacy-renegotiation.patch

  Patch10: wpa_supplicant-Revert-Mark-authorization-completed-on-driver-indica.patch

  Patch11: wpa_supplicant-Send-signal-change-as-debug-msg.patch

  Patch12: wpa_supplicant-OpenSSL-Use-pkcs11-provider-when-OPENSSL_NO_ENGINE-i.patch

  Patch13: wpa_supplicant-OpenSSL-Support-PEM-encoded-chain-from-ca_cert-blob.patch

  URL: http://w1.fi/wpa_supplicant/

  BuildRequires: qt-devel >= 4.0

  BuildRequires: openssl-devel
  BuildRequires: readline-devel
  BuildRequires: dbus-devel
  BuildRequires: libnl3-devel
  BuildRequires: systemd-units
  BuildRequires: docbook-utils
  BuildRequires: gcc

  BuildRequires: openssl-devel-engine

  Requires(post): systemd-sysv
  Requires(post): systemd
  Requires(preun): systemd
  Requires(postun): systemd

  Obsoletes: libeap < 1:2.11-10
  Obsoletes: libeap-devel < 1:2.11-10

  %description
  wpa_supplicant is a WPA Supplicant for Linux, BSD and Windows with support
  for WPA and WPA2 (IEEE 802.11i / RSN). Supplicant is the IEEE 802.1X/WPA
  component that is used in the client stations. It implements key negotiation
  with a WPA Authenticator and it controls the roaming and IEEE 802.11
  authentication/association of the wlan driver.

  %package gui
  Summary: Graphical User Interface for wpa_supplicant

  %description gui
  Graphical User Interface for wpa_supplicant written using QT

prepare() {

  cd './'
  rm -rf 'wpa_supplicant-2.11'
  tar -xf 'wpa_supplicant-2.11.tar.gz'
  STATUS=$?
  if [ $STATUS -ne 0 ]; then
    exit $STATUS
  fi
  cd 'wpa_supplicant-2.11'
  chmod -Rf a+rX,u+w,g-w,o-w .

  cat wpa_supplicant-defconfig-keep-options-we-ve-traditionally-used-enab.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat wpa_supplicant-assoc-timeout.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat wpa_supplicant-flush-debug-output.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat wpa_supplicant-quiet-scan-results-message.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat wpa_supplicant-gui-qt4.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat wpa_supplicant-defconfig-keep-CONFIG_WEP-enabled.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat wpa_supplicant-defconfig-enable-WPA-EAP-SUITE-B-192-ciphers.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat wpa_supplicant-defconfig-enable-OCV-support.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat wpa_supplicant-allow-legacy-renegotiation.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat wpa_supplicant-Revert-Mark-authorization-completed-on-driver-indica.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat wpa_supplicant-Send-signal-change-as-debug-msg.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat wpa_supplicant-OpenSSL-Use-pkcs11-provider-when-OPENSSL_NO_ENGINE-i.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

  cat wpa_supplicant-OpenSSL-Support-PEM-encoded-chain-from-ca_cert-blob.patch | 
  patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

}

build() {
  pushd wpa_supplicant
    cp defconfig .config
    export CFLAGS="${CFLAGS:--O2 -g} -fPIE -DPIE"
    export CXXFLAGS="${CXXFLAGS:--O2 -g} -fPIE -DPIE"
    export LDFLAGS="${LDFLAGS:--O2 -g} -pie -Wl,-z,now"
    # yes, BINDIR=_sbindir
    export BINDIR="/usr/bin"
    export LIBDIR="/usr/lib"
    make -j${RPM_BUILD_NCPUS} V=1
    make wpa_gui-qt4 -j${RPM_BUILD_NCPUS} V=1 QTDIR=/usr/lib/qt4 \
      QMAKE='%{qmake_qt4}' LRELEASE='%{_qt4_bindir}/lrelease'
    make eapol_test V=1
    make -C doc/docbook man V=1
  popd

}

package() {
  # config
  install -D -m 0600 wpa_supplicant.conf fakeinstall/etc/wpa_supplicant/wpa_supplicant.conf

  # init scripts
  install -D -m 0644 wpa_supplicant.service fakeinstall/%{_unitdir}/wpa_supplicant.service
  install -D -m 0644 wpa_supplicant.sysconfig fakeinstall/etc/sysconfig/wpa_supplicant
  install -D -m 0644 wpa_supplicant.logrotate fakeinstall/etc/logrotate.d/wpa_supplicant

  # binary
  install -d fakeinstall/usr/bin
  install -m 0755 wpa_supplicant/wpa_passphrase fakeinstall/usr/bin
  install -m 0755 wpa_supplicant/wpa_cli fakeinstall/usr/bin
  install -m 0755 wpa_supplicant/wpa_supplicant fakeinstall/usr/bin
  install -m 0755 wpa_supplicant/eapol_test fakeinstall/usr/bin
  install -D -m 0644 wpa_supplicant/dbus/dbus-wpa_supplicant.conf \
    fakeinstall/usr/share/dbus-1/system.d/wpa_supplicant.conf
  install -D -m 0644 wpa_supplicant/dbus/fi.w1.wpa_supplicant1.service \
    fakeinstall/usr/share/dbus-1/system-services/fi.w1.wpa_supplicant1.service

  # gui
  install -d fakeinstall/usr/bin
  install -m 0755 wpa_supplicant/wpa_gui-qt4/wpa_gui fakeinstall/usr/bin

  # man pages
  install -d fakeinstall/usr/share/man/man{5,8}
  install -m 0644 wpa_supplicant/doc/docbook/*.8 fakeinstall/usr/share/man/man8
  install -m 0644 wpa_supplicant/doc/docbook/*.5 fakeinstall/usr/share/man/man5

  # some cleanup in docs and examples
  rm -f  wpa_supplicant/doc/.cvsignore
  rm -rf wpa_supplicant/doc/docbook
  chmod -R 0644 wpa_supplicant/examples/*.py

  %post
  %systemd_post wpa_supplicant.service

  %preun
  %systemd_preun wpa_supplicant.service

  %triggerun -- wpa_supplicant < 0.7.3-10
  # Save the current service runlevel info
  # User must manually run systemd-sysv-convert --apply wpa_supplicant
  # to migrate them to systemd targets
  /usr/bin/systemd-sysv-convert --save wpa_supplicant >/dev/null 2>&1 ||:

  # Run these because the SysV package being removed won't do them
  /sbin/chkconfig --del wpa_supplicant >/dev/null 2>&1 || :
  /bin/systemctl try-restart wpa_supplicant.service >/dev/null 2>&1 || :

  # A spec %files section (it could be that part of the next lines duplicate part of the package() function)
  %config(noreplace) /etc/wpa_supplicant/wpa_supplicant.conf
  %config(noreplace) /etc/sysconfig/wpa_supplicant
  install -m755 -d ${pkgdir}/etc/logrotate.d
  %config(noreplace) /etc/logrotate.d/wpa_supplicant
  %{_unitdir}/wpa_supplicant.service
  _install fakeinstall/usr/share/dbus-1/system.d/wpa_supplicant.conf
  _install fakeinstall/usr/share/dbus-1/system-services/fi.w1.wpa_supplicant1.service
  _install fakeinstall/usr/bin/wpa_passphrase
  _install fakeinstall/usr/bin/wpa_supplicant
  _install fakeinstall/usr/bin/wpa_cli
  _install fakeinstall/usr/bin/eapol_test
  install -m755 -d ${pkgdir}/etc/wpa_supplicant
  _install fakeinstall/usr/share/man/man8/wpa_supplicant.8.gz
  _install fakeinstall/usr/share/man/man8/wpa_priv.8.gz
  _install fakeinstall/usr/share/man/man8/wpa_passphrase.8.gz
  _install fakeinstall/usr/share/man/man8/wpa_cli.8.gz
  _install fakeinstall/usr/share/man/man8/wpa_background.8.gz
  _install fakeinstall/usr/share/man/man8/eapol_test.8.gz
  _install fakeinstall/usr/share/man/man5/*
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/wpa_supplicant/  README
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/wpa_supplicant/  wpa_supplicant/ChangeLog
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/wpa_supplicant/  wpa_supplicant/eap_testing.txt
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/wpa_supplicant/  wpa_supplicant/todo.txt
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/wpa_supplicant/  wpa_supplicant/wpa_supplicant.conf
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/wpa_supplicant/  wpa_supplicant/examples
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/wpa_supplicant/ COPYING

  # gui
  _install fakeinstall/usr/bin/wpa_gui
  _install fakeinstall/usr/share/man/man8/wpa_gui.8.gz
}
