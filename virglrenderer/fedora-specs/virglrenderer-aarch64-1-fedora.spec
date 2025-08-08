
Name:		virglrenderer
Version:	1.1.1^git20250806.b997bc1
Release:	1

Summary:	Virgl Rendering library.
License:	MIT

Source0: https://gitlab.freedesktop.org/virgl/virglrenderer/-/archive/b997bc18fafdcb8e563b7b07b54412ea61e12082/virglrenderer-b997bc18fafdcb8e563b7b07b54412ea61e12082.tar.bz2

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

Requires: virglrenderer(aarch-64) = 1.1.1^git20250806.b997bc1-1

%description devel
Virgil3D renderer development files, used by
qemu to build against.

%package test-server
Summary: Virgil3D renderer testing server

Requires: virglrenderer(aarch-64) = 1.1.1^git20250806.b997bc1-1

%description test-server
Virgil3D renderer testing server is a server
that can be used along with the mesa virgl
driver to test virgl rendering without GL.

%prep

cd './'
rm -rf 'virglrenderer-b997bc18fafdcb8e563b7b07b54412ea61e12082'
rpmuncompress -x 'virglrenderer-b997bc18fafdcb8e563b7b07b54412ea61e12082.tar.bz2'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'virglrenderer-b997bc18fafdcb8e563b7b07b54412ea61e12082'
chmod -Rf a+rX,u+w,g-w,o-w .

%build
%meson -Dvideo=true -Ddrm-renderers=asahi -Dvenus=true
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%license COPYING
/usr/lib/lib*.so.*
/usr/lib/virglrenderer/virgl_render_server

%files devel
%dir /usr/include/virgl/
/usr/include/virgl/*
/usr/lib/lib*.so
/usr/lib/pkgconfig/*.pc

%files test-server
/usr/bin/virgl_test_server

