
Name:           mesa
Summary:        Mesa graphics libraries

Version:        25.2.4

Release:        0.101
License:        MIT AND BSD-3-Clause AND SGI-B-2.0
URL:            http://www.mesa3d.org

Source0:        https://archive.mesa3d.org/mesa-25.2.4.tar.xz

Source1:        Mesa-MLAA-License-Clarification-Email.txt

Patch10:        gnome-shell-glthread-disable.patch

Patch20:        meson_1.5_rust_build.patch
Patch21:        do_not_use_wl_display_dispatch_queue_timeout.diff
Patch22:        mr_37655_hk_host_cached.patch

BuildRequires:  meson >= 1.7.0

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext

BuildRequires:  kernel-headers
BuildRequires:  systemd-devel

BuildRequires:  pkgconfig(libdrm) >= 2.4.122

BuildRequires:  pkgconfig(libunwind)

BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(zlib) >= 1.2.3
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.41
BuildRequires:  pkgconfig(wayland-client) >= 1.11
BuildRequires:  pkgconfig(wayland-server) >= 1.11
BuildRequires:  pkgconfig(wayland-egl-backend) >= 3
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xdamage) >= 1.1
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xcb-glx) >= 1.8.1
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-dri2) >= 1.8
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xshmfence) >= 1.1
BuildRequires:  pkgconfig(dri2proto) >= 2.8
BuildRequires:  pkgconfig(glproto) >= 1.4.14
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xrandr) >= 1.3
BuildRequires:  bison
BuildRequires:  flex

BuildRequires:  lm_sensors-devel

BuildRequires:  pkgconfig(vdpau) >= 1.1

BuildRequires:  pkgconfig(libva) >= 0.38.0

BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libglvnd) >= 1.3.2
BuildRequires:  llvm-devel >= 7.0.0

BuildRequires:  clang-devel
BuildRequires:  pkgconfig(libclc)
BuildRequires:  pkgconfig(SPIRV-Tools)
BuildRequires:  pkgconfig(LLVMSPIRVLib)

BuildRequires:  bindgen
BuildRequires:  rust-packaging

BuildRequires:  python3-devel
BuildRequires:  python3-mako
BuildRequires:  python3-pycparser
BuildRequires:  python3-pyyaml
BuildRequires:  vulkan-headers
BuildRequires:  glslang

BuildRequires:  pkgconfig(vulkan)

%description
Mesa graphics libraries.

%package filesystem
Summary:        Mesa driver filesystem
Provides:       mesa-dri-filesystem = 25.2.4-0.101
Obsoletes:      mesa-omx-drivers < 25.2.4-0.101

%description filesystem
Mesa driver filesystem.

%package libGL
Summary:        Mesa libGL runtime libraries
Requires:       libglvnd-glx(x86-32) >= 1:1.3.2
Requires:       mesa-dri-drivers(x86-32) = 25.2.4-0.101
Obsoletes:      mesa-libOSMesa < 25.1.0~rc2-1

%description libGL
Mesa libGL runtime libraries.

%package libGL-devel
Summary:        Mesa libGL development package
Requires:       (mesa-libGL(x86-32) = 25.2.4-0.101 if mesa-libGL(x86-32))
Requires:       libglvnd-devel(x86-32) >= 1:1.3.2
Provides:       libGL-devel
Provides:       libGL-devel(x86-32)
Recommends:     gl-manpages
Obsoletes:      mesa-libOSMesa-devel < 25.1.0~rc2-1

%description libGL-devel
Mesa libGL development package.

%package libEGL
Summary:        Mesa libEGL runtime libraries
Requires:       libglvnd-egl(x86-32) >= 1:1.3.2
Requires:       mesa-libgbm(x86-32) = 25.2.4-0.101
Requires:       mesa-dri-drivers(x86-32) = 25.2.4-0.101

%description libEGL
Mesa libEGL runtime libraries.

%package libEGL-devel
Summary:        Mesa libEGL development package
Requires:       (mesa-libEGL(x86-32) = 25.2.4-0.101 if mesa-libEGL(x86-32))
Requires:       libglvnd-devel(x86-32) >= 1:1.3.2
Requires:       mesa-khr-devel(x86-32)
Provides:       libEGL-devel
Provides:       libEGL-devel(x86-32)

%description libEGL-devel
Mesa libEGL development package.

%package dri-drivers
Summary:        Mesa-based DRI drivers
Requires:       mesa-filesystem(x86-32) = 25.2.4-0.101

Recommends:     mesa-va-drivers(x86-32)

Obsoletes:      mesa-libglapi < 25.0.0~rc2-1
Provides:       mesa-libglapi >= 25.0.0~rc2-1

%description dri-drivers
Mesa-based DRI drivers.

%package        va-drivers
Summary:        Mesa-based VA-API video acceleration drivers
Requires:       mesa-filesystem(x86-32) = 25.2.4-0.101
Obsoletes:      mesa-vaapi-drivers < 22.2.0-5

%description va-drivers
Mesa-based VA-API video acceleration drivers.

%package        vdpau-drivers
Summary:        Mesa-based VDPAU drivers
Requires:       mesa-filesystem(x86-32) = 25.2.4-0.101

%description vdpau-drivers
Mesa-based VDPAU drivers.

%package libgbm
Summary:        Mesa gbm runtime library
Provides:       libgbm
Provides:       libgbm(x86-32)
Recommends:     mesa-dri-drivers(x86-32) = 25.2.4-0.101

Requires:       (mesa-dri-drivers(x86-32) = 25.2.4-0.101 if mesa-dri-drivers(x86-32))

%description libgbm
Mesa gbm runtime library.

%package libgbm-devel
Summary:        Mesa libgbm development package
Requires:       mesa-libgbm(x86-32) = 25.2.4-0.101
Provides:       libgbm-devel
Provides:       libgbm-devel(x86-32)

%description libgbm-devel
Mesa libgbm development package.

%package libOpenCL
Summary:        Mesa OpenCL runtime library
Requires:       (ocl-icd(x86-32) or OpenCL-ICD-Loader(x86-32))
Requires:       libclc(x86-32)
Requires:       mesa-libgbm(x86-32) = 25.2.4-0.101
Requires:       opencl-filesystem

%description libOpenCL
Mesa OpenCL runtime library.

%package libOpenCL-devel
Summary:        Mesa OpenCL development package
Requires:       mesa-libOpenCL(x86-32) = 25.2.4-0.101

%description libOpenCL-devel
Mesa OpenCL development package.

%package vulkan-drivers
Summary:        Mesa Vulkan drivers
Requires:       vulkan(x86-32)
Requires:       mesa-filesystem(x86-32) = 25.2.4-0.101
Obsoletes:      mesa-vulkan-devel < 25.2.4-0.101

%description vulkan-drivers
The drivers with support for the Vulkan API.

%package fex-emu-overlay-i386
Summary:        Mesa driver overlay for FEX-emu
BuildArch: noarch
BuildRequires:  erofs-utils
BuildRequires:  patchelf
Requires:       fex-emu
Supplements:    fex-emu-rootfs-fedora
Provides:       fex-emu-overlay(i386)(mesa) = 25.2.4-0.101
Provides:       bundled(mesa) = 25.2.4-0.101

%description fex-emu-overlay-i386
Mesa EGL/GL libraries and Gallium/OpenCL/Vulkan drivers for FEX-emu roots file system images.

%prep

cd './'
rm -rf 'mesa-25.2.4'
rpmuncompress -x 'mesa-25.2.4.tar.xz'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'mesa-25.2.4'
chmod -Rf a+rX,u+w,g-w,o-w .

rpmuncompress gnome-shell-glthread-disable.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

echo 'Cannot read meson_1.5_rust_build.patch'; exit 1;

rpmuncompress do_not_use_wl_display_dispatch_queue_timeout.diff | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

rpmuncompress mr_37655_hk_host_cached.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

cp Mesa-MLAA-License-Clarification-Email.txt docs/

%build
# ensure standard Rust compiler flags are set
export RUSTFLAGS="%build_rustflags"

# We've gotten a report that enabling LTO for mesa breaks some games. See
# https://bugzilla.redhat.com/show_bug.cgi?id=1862771 for details.
# Disable LTO for now

%meson \
  -Dplatforms=x11,wayland \
  -Dgallium-drivers=llvmpipe,virgl,asahi,zink \
  -Dgallium-vdpau=enabled \
  -Dgallium-va=enabled \
  -Dgallium-mediafoundation=disabled \
  -Dteflon=false \
  -Dgallium-rusticl=true \
  -Dvulkan-drivers=swrast,virtio,asahi \
  -Dvulkan-layers=device-select \
  -Dshared-glapi=enabled \
  -Dgles1=enabled \
  -Dgles2=enabled \
  -Dopengl=true \
  -Dgbm=enabled \
  -Dglx=dri \
  -Degl=enabled \
  -Dglvnd=enabled \
  -Dintel-rt=disabled \
  -Dmicrosoft-clc=disabled \
  -Dllvm=enabled \
  -Dshared-llvm=enabled \
  -Dvalgrind=disabled \
  -Dbuild-tests=false \
  -Dandroid-libbacktrace=disabled \
  -Dglx-read-only-text=true \

%meson_build

%install
%meson_install

# libvdpau opens the versioned name, don't bother including the unversioned
rm -vf fakeinstall/usr/lib32/vdpau/*.so
# likewise glvnd
rm -vf fakeinstall/usr/lib32/libGLX_mesa.so
rm -vf fakeinstall/usr/lib32/libEGL_mesa.so
# XXX can we just not build this
rm -vf fakeinstall/usr/lib32/libGLES*

# glvnd needs a default provider for indirect rendering where it cannot
# determine the vendor
ln -s /usr/lib32/libGLX_mesa.so.0 fakeinstall/usr/lib32/libGLX_system.so.0

# this keeps breaking, check it early.  note that the exit from eu-ftr is odd.
pushd fakeinstall/usr/lib32
for i in libGL.so ; do
    eu-findtextrel $i && exit 1
done
popd

mkdir -p fexov

# Note: In order to effectively white-out the underlying RootFS Mesa's
# drivers, we install files into alternately named sub-directories and
# then symlink them to the original name. This hides the entire original
# directory in the underlying RootFS.

install -Dpm0755 -s -t "fexov/usr/lib32/" \
  fakeinstall/usr/lib32/libgallium-*.so
install -Dpm0755 -s -t "fexov/usr/lib32/ovl_dri/" \
  fakeinstall/usr/lib32/dri/libdril_dri.so
ln -s libdril_dri.so "fexov/usr/lib32/ovl_dri/apple_dri.so"
ln -s libdril_dri.so "fexov/usr/lib32/ovl_dri/asahi_dri.so"
ln -s ovl_dri "fexov/usr/lib32/dri"

install -Dpm0755 -s -t "fexov/usr/lib32/" \
  fakeinstall/usr/lib32/libEGL_mesa.so.0.0.0 \
  fakeinstall/usr/lib32/libGLX_mesa.so.0.0.0
ln -s libEGL_mesa.so.0.0.0 "fexov/usr/lib32/libEGL_mesa.so.0"
ln -s libGLX_mesa.so.0.0.0 "fexov/usr/lib32/libGLX_mesa.so.0"
ln -s libGLX_mesa.so.0 "fexov/usr/lib32/libGLX_system.so.0"

install -Dpm0755 -s -t "fexov/usr/lib32/" \
  fakeinstall/usr/lib32/libRusticlOpenCL.so.1.0.0
ln -s libRusticlOpenCL.so.1.0.0 fexov/usr/lib32/libRusticlOpenCL.so.1
install -Dpm0644 -t "fexov/etc/OpenCL/ovl_vendors/" \
  fakeinstall/etc/OpenCL/vendors/rusticl.icd
ln -s ovl_vendors "fexov/etc/OpenCL/vendors"

install -Dpm0755 -s -t "fexov/usr/lib32/" \
  fakeinstall/usr/lib32/libvulkan_asahi.so \
  fakeinstall/usr/lib32/libVkLayer_MESA_device_select.so

install -Dpm0644 -t "fexov/usr/share/vulkan/ovl_icd.d/" \
  fakeinstall/usr/share/vulkan/icd.d/asahi_icd.*.json
install -Dpm0644 -t "fexov/usr/share/vulkan/implicit_layer.d/" \
  fakeinstall/usr/share/vulkan/implicit_layer.d/VkLayer_MESA_device_select.json
ln -s ovl_icd.d "fexov/usr/share/vulkan/icd.d"

install -Dpm0755 -s -t "fexov/usr/lib32/" \
  fakeinstall/usr/lib32/libgbm.so.1.0.0
install -Dpm0755 -s -t "fexov/usr/lib32/gbm/" \
  fakeinstall/usr/lib32/gbm/dri_gbm.so
install -Dpm0644 -t "fexov/usr/share/glvnd/ovl_egl_vendor.d/" \
  fakeinstall/usr/share/glvnd/egl_vendor.d/50_mesa.json
ln -s ovl_egl_vendor.d "fexov/usr/share/glvnd/egl_vendor.d"

# Hack to work around libcapsule bug:
# https://github.com/ValveSoftware/steam-runtime/issues/704
#
# The FEX overlays do not update ld.so.cache, so ld.so falls back
# to the system library paths. This works fine for ld.so since
# the dependencies are indeed in /usr/lib[64], but libcapsule
# has the fallback harcoded to /lib:/usr/lib, which fails on
# x86_64 systems.
patchelf --add-rpath /usr/lib32 "fexov/usr/lib32/gbm/dri_gbm.so"
patchelf --add-rpath /usr/lib32 "fexov/usr/lib32/libGLX_mesa.so.0.0.0"
patchelf --add-rpath /usr/lib32 "fexov/usr/lib32/libEGL_mesa.so.0.0.0"
patchelf --add-rpath /usr/lib32 "fexov/usr/lib32/libRusticlOpenCL.so.1.0.0"

#dnl erofs  ----------------------------
mkfs.erofs -z lz4 mesa-i386.erofs fexov

install -Dpm0644 -t fakeinstall/usr/share/fex-emu/overlays/ mesa-i386.erofs

%files filesystem
%doc docs/Mesa-MLAA-License-Clarification-Email.txt
%dir /usr/lib32/dri
%dir /usr/share/drirc.d

%files libGL
/usr/lib32/libGLX_mesa.so.0*
/usr/lib32/libGLX_system.so.0*
%files libGL-devel
%dir /usr/include/GL
%dir /usr/include/GL/internal
/usr/include/GL/internal/dri_interface.h
/usr/lib32/pkgconfig/dri.pc

%files libEGL
/usr/share/glvnd/egl_vendor.d/50_mesa.json
/usr/lib32/libEGL_mesa.so.0*
%files libEGL-devel
%dir /usr/include/EGL
/usr/include/EGL/eglext_angle.h
/usr/include/EGL/eglmesaext.h

%files libgbm
/usr/lib32/libgbm.so.1
/usr/lib32/libgbm.so.1.*
%files libgbm-devel
/usr/lib32/libgbm.so
/usr/include/gbm.h
/usr/include/gbm_backend_abi.h
/usr/lib32/pkgconfig/gbm.pc

%files libOpenCL
/usr/lib32/libRusticlOpenCL.so.*
/etc/OpenCL/vendors/rusticl.icd

%files libOpenCL-devel
/usr/lib32/libRusticlOpenCL.so

%files dri-drivers
/usr/share/drirc.d/00-mesa-defaults.conf
/usr/lib32/libgallium-*.so
/usr/lib32/gbm/dri_gbm.so
/usr/lib32/dri/kms_swrast_dri.so
/usr/lib32/dri/libdril_dri.so
/usr/lib32/dri/swrast_dri.so
/usr/lib32/dri/virtio_gpu_dri.so

/usr/lib32/dri/apple_dri.so
/usr/lib32/dri/asahi_dri.so
/usr/lib32/dri/ingenic-drm_dri.so
/usr/lib32/dri/imx-drm_dri.so
/usr/lib32/dri/imx-lcdif_dri.so
/usr/lib32/dri/kirin_dri.so
/usr/lib32/dri/komeda_dri.so
/usr/lib32/dri/mali-dp_dri.so
/usr/lib32/dri/mcde_dri.so
/usr/lib32/dri/mxsfb-drm_dri.so
/usr/lib32/dri/rcar-du_dri.so
/usr/lib32/dri/stm_dri.so
/usr/lib32/dri/armada-drm_dri.so
/usr/lib32/dri/exynos_dri.so
/usr/lib32/dri/gm12u320_dri.so
/usr/lib32/dri/hdlcd_dri.so
/usr/lib32/dri/hx8357d_dri.so
/usr/lib32/dri/ili9163_dri.so
/usr/lib32/dri/ili9225_dri.so
/usr/lib32/dri/ili9341_dri.so
/usr/lib32/dri/ili9486_dri.so
/usr/lib32/dri/imx-dcss_dri.so
/usr/lib32/dri/mediatek_dri.so
/usr/lib32/dri/meson_dri.so
/usr/lib32/dri/mi0283qt_dri.so
/usr/lib32/dri/panel-mipi-dbi_dri.so
/usr/lib32/dri/pl111_dri.so
/usr/lib32/dri/repaper_dri.so
/usr/lib32/dri/rockchip_dri.so
/usr/lib32/dri/rzg2l-du_dri.so
/usr/lib32/dri/ssd130x_dri.so
/usr/lib32/dri/st7586_dri.so
/usr/lib32/dri/st7735r_dri.so
/usr/lib32/dri/sti_dri.so
/usr/lib32/dri/sun4i-drm_dri.so
/usr/lib32/dri/udl_dri.so
/usr/lib32/dri/vkms_dri.so
/usr/lib32/dri/zynqmp-dpsub_dri.so
/usr/lib32/dri/zink_dri.so

%files va-drivers
/usr/lib32/dri/virtio_gpu_drv_video.so

%files vdpau-drivers
%dir /usr/lib32/vdpau
/usr/lib32/vdpau/libvdpau_virtio_gpu.so.1*

%files vulkan-drivers
/usr/lib32/libvulkan_lvp.so
/usr/share/vulkan/icd.d/lvp_icd.*.json
/usr/lib32/libVkLayer_MESA_device_select.so
/usr/share/vulkan/implicit_layer.d/VkLayer_MESA_device_select.json
/usr/lib32/libvulkan_virtio.so
/usr/share/vulkan/icd.d/virtio_icd.*.json
/usr/lib32/libvulkan_asahi.so
/usr/share/vulkan/icd.d/asahi_icd.*.json

%files fex-emu-overlay-i386
/usr/share/fex-emu/overlays/mesa-i386.erofs
%doc docs/Mesa-MLAA-License-Clarification-Email.txt

