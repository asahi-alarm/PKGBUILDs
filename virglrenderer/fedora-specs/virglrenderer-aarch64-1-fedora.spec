
Name:		virglrenderer
Version:	1.2.0
Release:	1.5

Summary:	Virgl Rendering library.
License:	MIT

Source:         https://gitlab.freedesktop.org/virgl/virglrenderer/-/archive/1.2.0/virglrenderer-1.2.0.tar.bz2
Patch0000:      0001-c11-threads-fix-build-on-c23.patch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:	libepoxy-devel
BuildRequires:	mesa-libgbm-devel
BuildRequires:	mesa-libEGL-devel
BuildRequires:	python3
BuildRequires:	libdrm-devel
BuildRequires:  libva-devel
BuildRequires:  vulkan-loader-devel
BuildRequires:  python3-pyyaml
Provides:       virglrenderer(asahi)

%description
The virgil3d rendering library is a library used by
qemu to implement 3D GPU support for the virtio GPU.

%package devel
Summary: Virgil3D renderer development files

Requires: virglrenderer(aarch-64) = 1.2.0-1.5

%description devel
Virgil3D renderer development files, used by
qemu to build against.

%package test-server
Summary: Virgil3D renderer testing server

Requires: virglrenderer(aarch-64) = 1.2.0-1.5

%description test-server
Virgil3D renderer testing server is a server
that can be used along with the mesa virgl
driver to test virgl rendering without GL.

%prep

cd './'
rm -rf 'virglrenderer-1.2.0'
rpmuncompress -x 'virglrenderer-1.2.0.tar.bz2'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'virglrenderer-1.2.0'
chmod -Rf a+rX,u+w,g-w,o-w .

rpmuncompress 0001-c11-threads-fix-build-on-c23.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

%build
%meson \
  -Ddrm-renderers=asahi,msm \
  -Dvideo=true \
  -Dvenus=true
%meson_build

%install
%meson_install

%files
%license COPYING
/usr/lib/libvirglrenderer.so.1{,.*}
/usr/lib/virglrenderer/virgl_render_server

%files devel
%dir /usr/include/virgl/
/usr/include/virgl/*
/usr/lib/libvirglrenderer.so
/usr/lib/pkgconfig/virglrenderer.pc

%files test-server
/usr/bin/virgl_test_server

