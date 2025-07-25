  Name:           asahi-scripts
  Version:        20250713
  Release:        1
  Summary:        Miscellaneous admin scripts for Asahi Linux

  License:        MIT
  URL:            https://github.com/AsahiLinux/asahi-scripts
  Source:         https://github.com/AsahiLinux/asahi-scripts/archive/20250713/asahi-scripts-20250713.tar.gz
  Source:         update-m1n1.sysconfig
  Source2:        15-update-m1n1.install

  BuildArch:      noarch

  BuildRequires:  make
  BuildRequires:  sed
  BuildRequires:  systemd-rpm-macros

  Requires:       bash
  Requires:       coreutils
  Requires:       grep
  Requires:       sed
  Requires:       systemd-udev
  Requires:       util-linux-core

  %description
  This package contains miscellaneous admin scripts for the Asahi Linux reference
  distro.

  %package -n     asahi-fwupdate
  Summary:        Asahi Linux firmware extractor

  Requires:       asahi-scripts = 20250713-1

  Requires:       python3-asahi_firmware >= 0.5.4

  %description -n asahi-fwupdate
  Asahi Linux firmware updater.

  %package -n     dracut-asahi
  Summary:        Dracut config for Apple Silicon Macs

  Requires:       dracut
  Requires:       linux-firmware-vendor = 20250713-1

  %description -n dracut-asahi
  Dracut config for Apple Silicon Macs.

  %package -n     linux-firmware-vendor
  Summary:        Ensure /lib/firmware/vendor exists for firmware handoff
  Requires:       linux-firmware

  %description -n linux-firmware-vendor
  This package ensures /lib/firmware/vendor exists so that firmware can be handed
  over properly from the initramfs.

  %package -n     update-m1n1
  Summary:        Keep m1n1 up to date

  Requires:       asahi-scripts = 20250713-1
  Requires:       bash
  Requires:       gzip
  Requires:       m1n1
  Requires:       uboot-images-armv8

  Requires:       grubby

  %description -n update-m1n1
  Keep m1n1 up to date on Apple Silicon systems.

  %package -n     asahi-battery
  Summary:        Asahi Linux battery charge control scripts

  Requires:       asahi-scripts = 20250713-1
  Requires:       systemd
  Requires:       systemd-udev

  %description -n asahi-battery
  Asahi Linux battery charge control scripts restore charge_control_end_threshold
  on system start.

prepare() {

  cd './'
  rm -rf 'asahi-scripts-20250713'
  tar -xf 'asahi-scripts-20250713.tar.gz'
  STATUS=$?
  if [ $STATUS -ne 0 ]; then
    exit $STATUS
  fi
  cd 'asahi-scripts-20250713'
  chmod -Rf a+rX,u+w,g-w,o-w .

}

build() {
  # nothing to do here

}

package() {
  /usr/bin/make install DESTDIR=fakeinstall INSTALL="install -p" install-fedora \
    PREFIX="/usr" \
    BIN_DIR="/usr/bin" \
    CONFIG_DIR="/etc/sysconfig"

  install -Ddpm0755 fakeinstall/usr/lib/firmware/vendor
  install -Dpm0644 update-m1n1.sysconfig fakeinstall/etc/sysconfig/update-m1n1
  # Install kernel-install script
  install -Dpm0755 -t fakeinstall%{_kernel_install_dir} 15-update-m1n1.install

  %transfiletriggerin -n asahi-fwupdate -- /usr/bin/asahi-fwupdate /usr/bin/asahi-fwextract
  /usr/bin/asahi-fwupdate || :

  # This needs to be a separate trigger because we can't use python3_sitearch here
  %transfiletriggerin -n asahi-fwupdate -- /usr/lib/python
  grep -q 'asahi_firmware' && /usr/bin/asahi-fwupdate || :

  # We can't use _libdir here because it gets incorrectly expanded to /usr/lib
  %transfiletriggerin -n update-m1n1 -- /usr/lib/m1n1 /usr/lib64/m1n1 /usr/share/uboot/apple_m1 /etc/m1n1.conf
  /usr/bin/update-m1n1 || :

  # A spec %files section (it could be that part of the next lines duplicate part of the package() function)
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/asahi-scripts/ LICENSE
  _install fakeinstall/usr/share/asahi-scripts/
  _install fakeinstall/usr/bin/asahi-diagnose
  %{_udevhwdbdir}/65-autosuspend-override-asahi-sdhci.hwdb

  # -n asahi-fwupdate
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/asahi-scripts/ LICENSE
  _install fakeinstall/usr/bin/asahi-fwupdate

  # -n dracut-asahi
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/asahi-scripts/ LICENSE
  _install fakeinstall/usr/lib/dracut/dracut.conf.d/10-asahi.conf
  _install fakeinstall/usr/lib/dracut/modules.d/91kernel-modules-asahi/
  _install fakeinstall/usr/lib/dracut/modules.d/99asahi-firmware/

  # -n linux-firmware-vendor
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/asahi-scripts/ LICENSE
  install -m755 -d ${pkgdir}/usr/lib/firmware/vendor

  # -n update-m1n1
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/asahi-scripts/ LICENSE
  %config(noreplace) /etc/sysconfig/update-m1n1
  %{_kernel_install_dir}/15-update-m1n1.install
  _install fakeinstall/usr/bin/update-m1n1

  # -n asahi-battery
  %{_unitdir}/macsmc-battery-charge-control-end-threshold.path
  %{_unitdir}/macsmc-battery-charge-control-end-threshold.service
  %{_udevrulesdir}/93-macsmc-battery-charge-control.rules
  %ghost %config(noreplace) /etc/udev/macsmc-battery.conf
}
