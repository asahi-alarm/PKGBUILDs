Name:           calamares-firstboot-config
Version:        20240509
Release:        6
Summary:        Fedora Asahi Calamares firstboot configs

License:        MIT
URL:            https://pagure.io/fedora-asahi/calamares-firstboot-config
Source:         calamares-firstboot-config-20240509.tar.gz

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

cd './'
rm -rf 'calamares-firstboot-config-20240509'
rpmuncompress -x 'calamares-firstboot-config-20240509.tar.gz'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'calamares-firstboot-config-20240509'
chmod -Rf a+rX,u+w,g-w,o-w .

%build
# Nothing to build

%install
install -p -m 0644 -D calamares-firstboot.service fakeinstall%{_unitdir}/calamares-firstboot.service
install -p -m 0755 -D setup.sh fakeinstall/usr/lib/asahi-calamares-configs/calamares-firstboot/setup.sh
install -d fakeinstall/usr/share/calamares-asahi/
cp -a calamares/* fakeinstall/usr/share/calamares-asahi/

%post
%systemd_post calamares-firstboot.service

%preun
%systemd_preun calamares-firstboot.service

%postun
%systemd_postun calamares-firstboot.service

%files
%license LICENSE
%{_unitdir}/calamares-firstboot.service
/usr/lib/asahi-calamares-configs/calamares-firstboot/
/usr/share/calamares-asahi/

