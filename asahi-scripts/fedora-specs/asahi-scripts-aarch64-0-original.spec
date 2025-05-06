Name:           asahi-scripts
Version:        20250426.1
Release:        %autorelease
Summary:        Miscellaneous admin scripts for Asahi Linux

License:        MIT
URL:            https://github.com/AsahiLinux/asahi-scripts
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source:         update-m1n1.sysconfig

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

Requires:       %{name} = %{version}-%{release}
# Not using python3dist(asahi-firmware) because its version is fixed
Requires:       python3-asahi_firmware >= 0.5.4

%description -n asahi-fwupdate
Asahi Linux firmware updater.

%package -n     dracut-asahi
Summary:        Dracut config for Apple Silicon Macs

Requires:       dracut
Requires:       linux-firmware-vendor = %{version}-%{release}

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

Requires:       %{name} = %{version}-%{release}
Requires:       bash
Requires:       gzip
Requires:       m1n1
Requires:       uboot-images-armv8

%description -n update-m1n1
Keep m1n1 up to date on Apple Silicon systems.

%package -n     asahi-battery
Summary:        Asahi Linux battery charge control scripts

Requires:       %{name} = %{version}-%{release}
Requires:       systemd
Requires:       systemd-udev

%description -n asahi-battery
Asahi Linux battery charge control scripts restore charge_control_end_threshold
on system start.

%prep
%autosetup -p1

%build
# nothing to do here

%install
%make_install install-fedora \
  PREFIX="%{_prefix}" \
  BIN_DIR="%{_sbindir}" \
  CONFIG_DIR="%{_sysconfdir}/sysconfig"

install -Ddpm0755 %{buildroot}%{_prefix}/lib/firmware/vendor
install -Dpm0644 %SOURCE1 %{buildroot}%{_sysconfdir}/sysconfig/update-m1n1

%transfiletriggerin -n asahi-fwupdate -- %{_sbindir}/asahi-fwupdate %{_bindir}/asahi-fwextract
%{_sbindir}/asahi-fwupdate || :

# This needs to be a separate trigger because we can't use python3_sitearch here
%transfiletriggerin -n asahi-fwupdate -- /usr/lib/python
grep -q 'asahi_firmware' && %{_sbindir}/asahi-fwupdate || :

# We can't use _libdir here because it gets incorrectly expanded to /usr/lib
%transfiletriggerin -n update-m1n1 -- /usr/lib/m1n1 /usr/lib64/m1n1 /usr/share/uboot/apple_m1 /boot/dtb- /etc/m1n1.conf
%{_sbindir}/update-m1n1 || :

%files
%license LICENSE
%{_datadir}/%{name}/
%{_sbindir}/asahi-diagnose
%{_udevhwdbdir}/65-autosuspend-override-asahi-sdhci.hwdb

%files -n asahi-fwupdate
%license LICENSE
%{_sbindir}/asahi-fwupdate

%files -n dracut-asahi
%license LICENSE
%{_prefix}/lib/dracut/dracut.conf.d/10-asahi.conf
%{_prefix}/lib/dracut/modules.d/91kernel-modules-asahi/
%{_prefix}/lib/dracut/modules.d/99asahi-firmware/

%files -n linux-firmware-vendor
%license LICENSE
%dir %{_prefix}/lib/firmware/vendor

%files -n update-m1n1
%license LICENSE
%config(noreplace) %{_sysconfdir}/sysconfig/update-m1n1
%{_sbindir}/update-m1n1

%files -n asahi-battery
%{_unitdir}/macsmc-battery-charge-control-end-threshold.path
%{_unitdir}/macsmc-battery-charge-control-end-threshold.service
%{_udevrulesdir}/93-macsmc-battery-charge-control.rules

%changelog
%autochangelog
