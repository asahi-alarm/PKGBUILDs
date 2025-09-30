Name:           steam
Version:        0
Release:        14%{?dist}
Summary:        Steam wrapper for Fedora Asahi Remix

License:        MIT
URL:            https://pagure.io/fedora-asahi/steam
Source0:        shim.py
Source1:        LICENSE
Source2:        README.md
Source3:        steam.desktop
Source4:        steam.svg
Source5:        io.pagure.fedora_asahi.steam.metainfo.xml

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       bash
Requires:       dbus-x11
Requires:       fex-emu
Requires:       grep
Requires:       hicolor-icon-theme
Requires:       lsb_release
Requires:       muvm >= 0.2
Requires:       python3
Requires:       xwininfo
%if 0%{?fedora} && 0%{?fedora} < 43
Requires:       mesa-fex-emu-overlay-i386
Requires:       mesa-fex-emu-overlay-x86_64
%endif
Requires:       virglrenderer > 1.2.0-1
Requires:       zenity

Requires:       python3dist(pyqt6)
Requires:       python3dist(pexpect)
Requires:       python3dist(requests)
Requires:       python3dist(pyxdg)

%description
This package provides a wrapper to download, install and run Steam on Fedora
Asahi Remix.

%prep
%autosetup -c -T

cp -p %SOURCE1 %SOURCE2 .

%build
# Nothing to do here

%install
install -Dpm0755 %SOURCE0 %{buildroot}%{_bindir}/steam
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %SOURCE3
install -Dpm0644 -t %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/ \
  %SOURCE4
install -Dpm0644 -t %{buildroot}%{_metainfodir}/ %SOURCE5

%check
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/io.pagure.fedora_asahi.steam.metainfo.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/steam
%{_datadir}/applications/steam.desktop
%{_datadir}/icons/hicolor/scalable/apps/steam.svg
%{_metainfodir}/io.pagure.fedora_asahi.steam.metainfo.xml

%changelog
* Thu Sep 18 2025 Janne Grunau <j@jannau.net> - 0-14
- Depend on upstream virglrenderer 1.2.0 with asahi DRM native context support (F43)
- Do not depend on mesa overlays for F43. Mesa 25.2.2 will be in the rootfs

* Wed Dec 04 2024 Asahi Lina <lina@asahilina.net> - 0-13
- Start up in non-big-picture mode if muvm is new enough
- Drop CEF workarounds if muvm is new enough
- Fix bug with the launcher window remaining up after Steam

* Tue Nov 12 2024 Asahi Lina <lina@asahilina.net> - 0-12
- Depend on zenity (which Steam uses)

* Thu Oct 10 2024 Janne Grunau <janne-fdr@jannau.net> - 0-11
- shim: Prevent running as root

* Wed Oct 09 2024 Janne Grunau <janne-fdr@jannau.net> - 0-10
- Require virglrenderer(asahi) to avoid incompatible packages

* Wed Oct 09 2024 Alyssa Rosenzweig <alyssa@rosenzweig.io> - 0-9
- Start hidpipe-server manually

* Wed Oct 09 2024 Janne Grunau <j@jannau.net> - 0-8
- hidpipe: Fail gracefully if hidpipe is not running

* Wed Oct 9 2024 Alyssa Rosenzweig <alyssa@rosenzweig.io> - 0-7
- Hack to fix gamepads

* Sun Oct 6 2024 Alyssa Rosenzweig <alyssa@rosenzweig.io> - 0-6
- Fix obnoxious font size
- Pull in Mesa overlay explicitly

* Fri Oct 4 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 0-5
- Add missing dependencies

* Tue Oct 1 2024 Alyssa Rosenzweig <alyssa@rosenzweig.io> - 0-4
- Rename krun to muvm

* Sun Sep 29 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 0-3
- Install the icon in the right place

* Thu Sep 26 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 0-2
- Add desktop launcher, icon and metadata

* Wed Sep 25 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 0-1
- Initial version
