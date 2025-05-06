Name:           calamares-firstboot-config
Version:        20240509
Release:        6%{?dist}
Summary:        Fedora Asahi Calamares firstboot configs

License:        MIT
URL:            https://pagure.io/fedora-asahi/calamares-firstboot-config
Source:         %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  systemd-rpm-macros
Requires:       libkscreen-qt5
Requires:       plasma-workspace
Requires:       calamares
Requires:       desktop-backgrounds-compat
Requires:       util-linux
Requires:       console-setup
Requires:       kwin-wayland
Requires:       findutils
Requires:       xxd
Requires:       systemd

%description
Calamares first-boot wizard configuration and launch scripts
for Fedora Asahi Remix.

%prep
%autosetup

%build
# Nothing to build

%install
install -p -m 0644 -D calamares-firstboot.service %{buildroot}%{_unitdir}/calamares-firstboot.service
install -p -m 0755 -D setup.sh %{buildroot}%{_libexecdir}/calamares-firstboot/setup.sh
install -d %{buildroot}%{_datadir}/calamares-asahi/
cp -a calamares/* %{buildroot}%{_datadir}/calamares-asahi/

%post
%systemd_post calamares-firstboot.service

%preun
%systemd_preun calamares-firstboot.service

%postun
%systemd_postun calamares-firstboot.service

%files
%license LICENSE
%{_unitdir}/calamares-firstboot.service
%{_libexecdir}/calamares-firstboot/
%{_datadir}/calamares-asahi/

%changelog
* Sat Mar 01 2025 Davide Cavalca <dcavalca@fedoraproject.org> - 20240509-6
- Try a different approach for the existence tests in the setup script
- Fix some shellcheck warnings
- More robust GPU detection

* Sat Mar 01 2025 NoisyCoil <noisycoil@tutanota.com> - 20240509-5
- Do not use globs for existence tests in setup script

* Sat Mar 01 2025 Davide Cavalca <dcavalca@fedoraproject.org> - 20240509-4
- Add missing changelog entries

* Sat Mar 01 2025 Janne Grunau <j@jannau.net> - 20240509-4
- Fix typo in setup script

* Mon Feb 03 2025 Hector Martin <marcan@fedoraproject.org> - 20240509-3
- Enable a11y

* Thu May 09 2024 Hector Martin <marcan@fedoraproject.org> - 20240509-2
- Fix sidebar on F40+

* Thu May 09 2024 Hector Martin <marcan@marcan.st> - 20240509-1
- Fix SDDM scale on F40+

* Sat Apr 20 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 20231010-2
- Rebuild for Fedora Linux 40

* Tue Oct 10 2023 Hector Martin <marcan@marcan.st> - 20231010-1
- Add workaround for KDE bug #475435

* Sun Oct 08 2023 Hector Martin <marcan@marcan.st> - 20231008-1
- Fix HiDPI detection (wildcard DRM device ID)

* Tue Sep 05 2023 Davide Cavalca <dcavalca@fedoraproject.org> - 20230905-2
- Add missing Requires

* Tue Sep 05 2023 Davide Cavalca <dcavalca@fedoraproject.org> - 20230905-1
- Misc systemd service fixes
- Add missing changelog entries

* Mon Sep 04 2023 Hector Martin <marcan@marcan.st> - 20230904.1-1
- Use kscreen to set display scale, switch to plasmashell

* Mon Sep 04 2023 Hector Martin <marcan@marcan.st> - 20230904-1
- welcome: Add dummy RAM check
- branding: Double the SVG native size for the welcome laptop

* Sun Sep 03 2023 Hector Martin <marcan@marcan.st> - 20230903-1
- Initial revision
