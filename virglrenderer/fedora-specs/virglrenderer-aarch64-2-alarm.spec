
  Name:		virglrenderer
  Version:	1.2.0
  Release:	1.1

  Summary:	Virgl Rendering library.
  License:	MIT

  Source:         https://gitlab.freedesktop.org/virgl/virglrenderer/-/archive/1.2.0/virglrenderer-1.2.0.tar.bz2

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

  Requires: virglrenderer(aarch-64) = 1.2.0-1.1

  %description devel
  Virgil3D renderer development files, used by
  qemu to build against.

  %package test-server
  Summary: Virgil3D renderer testing server

  Requires: virglrenderer(aarch-64) = 1.2.0-1.1

  %description test-server
  Virgil3D renderer testing server is a server
  that can be used along with the mesa virgl
  driver to test virgl rendering without GL.

prepare() {

  cd './'
  rm -rf 'virglrenderer-1.2.0'
  tar -xf 'virglrenderer-1.2.0.tar.bz2'
  STATUS=$?
  if [ $STATUS -ne 0 ]; then
    exit $STATUS
  fi
  cd 'virglrenderer-1.2.0'
  chmod -Rf a+rX,u+w,g-w,o-w .

}

build() {
  %meson \
    -Ddrm-renderers=asahi,msm \
    -Dvideo=true \
    -Dvenus=true

}

package() {

  # A spec %files section (it could be that part of the next lines duplicate part of the package() function)
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/virglrenderer/ COPYING
  _install fakeinstall/usr/lib/libvirglrenderer.so.1{,.*}
  _install fakeinstall/usr/lib/virglrenderer/virgl_render_server

  # devel
  install -m755 -d ${pkgdir}/usr/include/virgl/
  _install fakeinstall/usr/include/virgl/*
  _install fakeinstall/usr/lib/libvirglrenderer.so
  _install fakeinstall/usr/lib/pkgconfig/virglrenderer.pc

  # test-server
  _install fakeinstall/usr/bin/virgl_test_server
}
