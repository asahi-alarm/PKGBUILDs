
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

BuildRequires:  flatbuffers-devel
BuildRequires:  flatbuffers-compiler
BuildRequires:  xtensor-devel

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
Requires:       libglvnd-glx(aarch-64) >= 1:1.3.2
Requires:       mesa-dri-drivers(aarch-64) = 25.2.4-0.101
Obsoletes:      mesa-libOSMesa < 25.1.0~rc2-1

%description libGL
Mesa libGL runtime libraries.

%package libGL-devel
Summary:        Mesa libGL development package
Requires:       (mesa-libGL(aarch-64) = 25.2.4-0.101 if mesa-libGL(aarch-64))
Requires:       libglvnd-devel(aarch-64) >= 1:1.3.2
Provides:       libGL-devel
Provides:       libGL-devel(aarch-64)
Recommends:     gl-manpages
Obsoletes:      mesa-libOSMesa-devel < 25.1.0~rc2-1

%description libGL-devel
Mesa libGL development package.

%package libEGL
Summary:        Mesa libEGL runtime libraries
Requires:       libglvnd-egl(aarch-64) >= 1:1.3.2
Requires:       mesa-libgbm(aarch-64) = 25.2.4-0.101
Requires:       mesa-dri-drivers(aarch-64) = 25.2.4-0.101

%description libEGL
Mesa libEGL runtime libraries.

%package libEGL-devel
Summary:        Mesa libEGL development package
Requires:       (mesa-libEGL(aarch-64) = 25.2.4-0.101 if mesa-libEGL(aarch-64))
Requires:       libglvnd-devel(aarch-64) >= 1:1.3.2
Requires:       mesa-khr-devel(aarch-64)
Provides:       libEGL-devel
Provides:       libEGL-devel(aarch-64)

%description libEGL-devel
Mesa libEGL development package.

%package dri-drivers
Summary:        Mesa-based DRI drivers
Requires:       mesa-filesystem(aarch-64) = 25.2.4-0.101

Recommends:     mesa-va-drivers(aarch-64)

Obsoletes:      mesa-libglapi < 25.0.0~rc2-1
Provides:       mesa-libglapi >= 25.0.0~rc2-1

%description dri-drivers
Mesa-based DRI drivers.

%package        va-drivers
Summary:        Mesa-based VA-API video acceleration drivers
Requires:       mesa-filesystem(aarch-64) = 25.2.4-0.101
Obsoletes:      mesa-vaapi-drivers < 22.2.0-5

%description va-drivers
Mesa-based VA-API video acceleration drivers.

%package        vdpau-drivers
Summary:        Mesa-based VDPAU drivers
Requires:       mesa-filesystem(aarch-64) = 25.2.4-0.101

%description vdpau-drivers
Mesa-based VDPAU drivers.

%package libgbm
Summary:        Mesa gbm runtime library
Provides:       libgbm
Provides:       libgbm(aarch-64)
Recommends:     mesa-dri-drivers(aarch-64) = 25.2.4-0.101

Requires:       (mesa-dri-drivers(aarch-64) = 25.2.4-0.101 if mesa-dri-drivers(aarch-64))

%description libgbm
Mesa gbm runtime library.

%package libgbm-devel
Summary:        Mesa libgbm development package
Requires:       mesa-libgbm(aarch-64) = 25.2.4-0.101
Provides:       libgbm-devel
Provides:       libgbm-devel(aarch-64)

%description libgbm-devel
Mesa libgbm development package.

%package libOpenCL
Summary:        Mesa OpenCL runtime library
Requires:       (ocl-icd(aarch-64) or OpenCL-ICD-Loader(aarch-64))
Requires:       libclc(aarch-64)
Requires:       mesa-libgbm(aarch-64) = 25.2.4-0.101
Requires:       opencl-filesystem

%description libOpenCL
Mesa OpenCL runtime library.

%package libOpenCL-devel
Summary:        Mesa OpenCL development package
Requires:       mesa-libOpenCL(aarch-64) = 25.2.4-0.101

%description libOpenCL-devel
Mesa OpenCL development package.

%package libTeflon
Summary:        Mesa TensorFlow Lite delegate

%description libTeflon
Mesa TensorFlow Lite delegate.

%package vulkan-drivers
Summary:        Mesa Vulkan drivers
Requires:       vulkan(aarch-64)
Requires:       mesa-filesystem(aarch-64) = 25.2.4-0.101
Obsoletes:      mesa-vulkan-devel < 25.2.4-0.101

%description vulkan-drivers
The drivers with support for the Vulkan API.

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
  -Dteflon=true \
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

%meson_build

%install
%meson_install

# libvdpau opens the versioned name, don't bother including the unversioned
rm -vf fakeinstall/usr/lib/vdpau/*.so
# likewise glvnd
rm -vf fakeinstall/usr/lib/libGLX_mesa.so
rm -vf fakeinstall/usr/lib/libEGL_mesa.so
# XXX can we just not build this
rm -vf fakeinstall/usr/lib/libGLES*

# glvnd needs a default provider for indirect rendering where it cannot
# determine the vendor
ln -s /usr/lib/libGLX_mesa.so.0 fakeinstall/usr/lib/libGLX_system.so.0

# this keeps breaking, check it early.  note that the exit from eu-ftr is odd.
pushd fakeinstall/usr/lib
for i in libGL.so ; do
    eu-findtextrel $i && exit 1
done
popd

%files filesystem
%doc docs/Mesa-MLAA-License-Clarification-Email.txt
%dir /usr/lib/dri
%dir /usr/share/drirc.d

%files libGL
/usr/lib/libGLX_mesa.so.0*
/usr/lib/libGLX_system.so.0*
%files libGL-devel
%dir /usr/include/GL
%dir /usr/include/GL/internal
/usr/include/GL/internal/dri_interface.h
/usr/lib/pkgconfig/dri.pc

%files libEGL
/usr/share/glvnd/egl_vendor.d/50_mesa.json
/usr/lib/libEGL_mesa.so.0*
%files libEGL-devel
%dir /usr/include/EGL
/usr/include/EGL/eglext_angle.h
/usr/include/EGL/eglmesaext.h

%files libgbm
/usr/lib/libgbm.so.1
/usr/lib/libgbm.so.1.*
%files libgbm-devel
/usr/lib/libgbm.so
/usr/include/gbm.h
/usr/include/gbm_backend_abi.h
/usr/lib/pkgconfig/gbm.pc

%files libTeflon
/usr/lib/libteflon.so

%files libOpenCL
/usr/lib/libRusticlOpenCL.so.*
/etc/OpenCL/vendors/rusticl.icd

%files libOpenCL-devel
/usr/lib/libRusticlOpenCL.so

%files dri-drivers
/usr/share/drirc.d/00-mesa-defaults.conf
/usr/lib/libgallium-*.so
/usr/lib/gbm/dri_gbm.so
/usr/lib/dri/kms_swrast_dri.so
/usr/lib/dri/libdril_dri.so
/usr/lib/dri/swrast_dri.so
/usr/lib/dri/virtio_gpu_dri.so

/usr/lib/dri/apple_dri.so
/usr/lib/dri/asahi_dri.so
/usr/lib/dri/ingenic-drm_dri.so
/usr/lib/dri/imx-drm_dri.so
/usr/lib/dri/imx-lcdif_dri.so
/usr/lib/dri/kirin_dri.so
/usr/lib/dri/komeda_dri.so
/usr/lib/dri/mali-dp_dri.so
/usr/lib/dri/mcde_dri.so
/usr/lib/dri/mxsfb-drm_dri.so
/usr/lib/dri/rcar-du_dri.so
/usr/lib/dri/stm_dri.so
/usr/lib/dri/armada-drm_dri.so
/usr/lib/dri/exynos_dri.so
/usr/lib/dri/gm12u320_dri.so
/usr/lib/dri/hdlcd_dri.so
/usr/lib/dri/hx8357d_dri.so
/usr/lib/dri/ili9163_dri.so
/usr/lib/dri/ili9225_dri.so
/usr/lib/dri/ili9341_dri.so
/usr/lib/dri/ili9486_dri.so
/usr/lib/dri/imx-dcss_dri.so
/usr/lib/dri/mediatek_dri.so
/usr/lib/dri/meson_dri.so
/usr/lib/dri/mi0283qt_dri.so
/usr/lib/dri/panel-mipi-dbi_dri.so
/usr/lib/dri/pl111_dri.so
/usr/lib/dri/repaper_dri.so
/usr/lib/dri/rockchip_dri.so
/usr/lib/dri/rzg2l-du_dri.so
/usr/lib/dri/ssd130x_dri.so
/usr/lib/dri/st7586_dri.so
/usr/lib/dri/st7735r_dri.so
/usr/lib/dri/sti_dri.so
/usr/lib/dri/sun4i-drm_dri.so
/usr/lib/dri/udl_dri.so
/usr/lib/dri/vkms_dri.so
/usr/lib/dri/zynqmp-dpsub_dri.so
/usr/lib/dri/zink_dri.so

%files va-drivers
/usr/lib/dri/virtio_gpu_drv_video.so

%files vdpau-drivers
%dir /usr/lib/vdpau
/usr/lib/vdpau/libvdpau_virtio_gpu.so.1*

%files vulkan-drivers
/usr/lib/libvulkan_lvp.so
/usr/share/vulkan/icd.d/lvp_icd.*.json
/usr/lib/libVkLayer_MESA_device_select.so
/usr/share/vulkan/implicit_layer.d/VkLayer_MESA_device_select.json
/usr/lib/libvulkan_virtio.so
/usr/share/vulkan/icd.d/virtio_icd.*.json
/usr/lib/libvulkan_asahi.so
/usr/share/vulkan/icd.d/asahi_icd.*.json

