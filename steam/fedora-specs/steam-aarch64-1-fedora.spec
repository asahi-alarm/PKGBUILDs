Name:           steam
Version:        0
Release:        14
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

cd './'
rm -rf 'steam-0'
mkdir -p 'steam-0'
cd 'steam-0'
chmod -Rf a+rX,u+w,g-w,o-w .

%build
# Nothing to do here

%install
install -Dpm0755 shim.py fakeinstall/usr/bin/steam
desktop-file-install --dir=fakeinstall/usr/share/applications steam.desktop
install -Dpm0644 -t fakeinstall/usr/share/icons/hicolor/scalable/apps/ \
  steam.svg
install -Dpm0644 -t fakeinstall/usr/share/metainfo/ io.pagure.fedora_asahi.steam.metainfo.xml

%check
appstream-util validate-relax --nonet \
  fakeinstall/usr/share/metainfo/io.pagure.fedora_asahi.steam.metainfo.xml

%files
%license LICENSE
%doc README.md
/usr/bin/steam
/usr/share/applications/steam.desktop
/usr/share/icons/hicolor/scalable/apps/steam.svg
/usr/share/metainfo/io.pagure.fedora_asahi.steam.metainfo.xml

