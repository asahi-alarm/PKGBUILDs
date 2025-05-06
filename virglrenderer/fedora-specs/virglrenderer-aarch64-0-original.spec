%global asahi_virglrenderer_ver 20250424
%global tag asahi-%{asahi_virglrenderer_ver}
%global baseversion 1.1.1

Name:		virglrenderer
Version:	%{baseversion}^asahipost%{asahi_virglrenderer_ver}
Release:	1%{?dist}

Summary:	Virgl Rendering library.
License:	MIT

Source0: https://gitlab.freedesktop.org/asahi/virglrenderer/-/archive/%{tag}/virglrenderer-%{tag}.tar.bz2

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:	libepoxy-devel
BuildRequires:	mesa-libgbm-devel
BuildRequires:	mesa-libEGL-devel
BuildRequires:	python3
BuildRequires:	python3-pyyaml
BuildRequires:	libdrm-devel
BuildRequires:  libva-devel
BuildRequires:  vulkan-loader-devel
Provides:       virglrenderer(asahi)

%description
The virgil3d rendering library is a library used by
qemu to implement 3D GPU support for the virtio GPU.

%package devel
Summary: Virgil3D renderer development files

Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Virgil3D renderer development files, used by
qemu to build against.

%package test-server
Summary: Virgil3D renderer testing server

Requires: %{name}%{?_isa} = %{version}-%{release}

%description test-server
Virgil3D renderer testing server is a server
that can be used along with the mesa virgl
driver to test virgl rendering without GL.

%prep
%autosetup -n %{name}-%{tag} -p1
%build
%meson -Dvideo=true -Ddrm-renderers=asahi-experimental
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%dir %{_includedir}/virgl/
%{_includedir}/virgl/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%files test-server
%{_bindir}/virgl_test_server

%changelog
* Wed Dec 04 2024 Asahi Lina <lina@asahilina.net> - 1.0.1^asahipost20241205.2-1
- Bump to virglrenderer-asahi-20241205.2

* Wed Dec 04 2024 Asahi Lina <lina@asahilina.net> - 1.0.1^asahipost20241205.1-1
- Bump to virglrenderer-asahi-20241205.1

* Wed Dec 04 2024 Asahi Lina <lina@asahilina.net> - 1.0.1^asahipost20241205-1
- Bump to virglrenderer-asahi-20241205

* Wed Dec 04 2024 Asahi Lina <lina@asahilina.net> - 1.0.1^asahipost20241204-1
- Bump to virglrenderer-asahi-20241204

* Thu Nov 28 2024 Asahi Lina <lina@asahilina.net> - 1.0.1^asahipost20241129-1
- Bump to virglrenderer-asahi-20241129

* Thu Nov 28 2024 Asahi Lina <lina@asahilina.net> - 1.0.1^asahipost20241128-2
- Bump release to clean up COPR builds

* Thu Nov 28 2024 Asahi Lina <lina@asahilina.net> - 1.0.1^asahipost20241128-1
- Bump to virglrenderer-asahi-20241128

* Wed Oct 09 2024 Janne Grunau <janne-fdr@jannau.net> - 1.0.1^asahipost20240925-2
- Provide virglrenderer(asahi) so that steam can depend on it

* Thu Sep 26 2024 Janne Grunau <j@jannau.net> - 1.0.1^asahipost20240925-1
- Bump to virglrenderer-asahi-20240925

* Sun Sep 01 2024 Davide Cavalca <dcavalca@fedoraproject.org> - 1.0.1^asahipost20240831-1
- Update version and source for Asahi

* Tue Aug 06 2024 Sandro Bonazzola <sbonazzo@redhat.com> - 1.0.1-4
- Drop xorg-x11-util-macros dependency as it's not needed anymore

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1 (#2257772)

* Tue Sep 19 2023 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.0.0-1
- new version

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-3.20230104git88b9fe3b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-2.20230104git88b9fe3b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.10.4-1.20230104git88b9fe3b
- new version

* Mon Sep 12 2022 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.10.1-1.20220912git19dc97a2
- new version, fixes upstream #286 "Virglrenderer 0.10.1 broke Firefox WebGL rendering in VM"
  Fixes: https://bugzilla.redhat.com/show_bug.cgi?id=2125160

* Tue Sep 06 2022 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.10.0-2.20220906git62cb845b
- new version, fixes upstream #285 "0.10.0 has issues with fedora 36, hangs the VM"

* Mon Sep 05 2022 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.10.0-1.20220905gitf70a6640
- new version

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4.20210420git36391559
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3.20210420git36391559
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2.20210420git36391559
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 20 2021 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.9.1-1.20210420git36391559
- Upstream release 0.9.1. rhbz#1945999

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3.20200212git7d204f39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2.20200212git7d204f39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 12 2020 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.8.2-1.20200212git7d204f39
- Upstream release 0.8.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2.20191220git66c57963
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.8.1-1.20191220git66c57963
- Upstream release 0.8.1

* Thu Oct 03 2019 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.8.0-1.20191002git4ac3a04c
- Latest upstream git snapshot

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4.20190424gitd1758cc09
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Dave Airlie <airlied@redhat.com> - 0.7.0-3.20190424gitd1758cc09
- Latest upstream git snapshot

* Wed Apr 10 2019 Dave Airlie <airlied@redhat.com> - 0.7.0-3.20180919git402c22886
- build debug package properly, fix make commands

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2.20180919git402c22886
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Dave Airlie <airlied@redhat.com> - 0.7.0-1.20180919git402c22886
- upstream 0.7.0 release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6.20170210git76b3da97b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.0-5.20170210git76b3da97b
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4.20170210git76b3da97b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3.20170210git76b3da97b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2.20170210git76b3da97b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Dave Airlie <airlied@redhat.com> - 0.6.0-1.git
- upstream 0.6.0 release

* Mon Apr 11 2016 Dave Airlie <airlied@redhat.com> 0.5.0-1.git
- upstream 0.5.0 release

* Thu Feb 18 2016 Dave Airlie <airlied@redhat.com> 0.4.1-1.git
- fix regression in last build

* Wed Feb 17 2016 Dave Airlie <airlied@redhat.com> 0.4.0-1.git
- latest git snapshot with new API

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3.20151215gite9d3c0c27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Dave Airlie <airlied@redhat.com> 0.3.0-2.gite9d3c0c27
- latest upstream to fix gnome-shell rendering bugs

* Fri Oct 23 2015 Dave Airlie <airlied@redhat.com> 0.3.0-1.20151023git9ce005e5a
- update to latest upstream to fix shader issue

* Fri Oct 23 2015 Dave Airlie <airlied@redhat.com> 0.2.0-1.20151023git5bfba5190
- update to latest upstream

* Thu Jul 09 2015 Dave Airlie <airlied@redhat.com> 0.0.1-0.20150420gitc4fb40201.2
- fix FTBFS (#1240041)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-0.20150420gitc4fb40201.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 01 2015 Dave Airlie <airlied@redhat.com> 0.0.1-0.20150401gita9ba2c442
- initial virglrenderer spec
