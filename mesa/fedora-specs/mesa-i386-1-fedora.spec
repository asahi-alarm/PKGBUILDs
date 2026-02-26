
Name:           mesa
Summary:        Mesa graphics libraries

Version:        25.3.6
Release:        0.1
License:        MIT AND BSD-3-Clause AND SGI-B-2.0
URL:            https://mesa3d.org

Source0:        https://archive.mesa3d.org/mesa-25.3.6.tar.xz

Source1:        Mesa-MLAA-License-Clarification-Email.txt

Source10:       https://crates.io/api/v1/crates/paste/1.0.15/download#/paste-1.0.15.tar.gz
Source11:       https://crates.io/api/v1/crates/proc-macro2/1.0.101/download#/proc-macro2-1.0.101.tar.gz
Source12:       https://crates.io/api/v1/crates/quote/1.0.40/download#/quote-1.0.40.tar.gz
Source13:       https://crates.io/api/v1/crates/syn/2.0.106/download#/syn-2.0.106.tar.gz
Source14:       https://crates.io/api/v1/crates/unicode-ident/1.0.18/download#/unicode-ident-1.0.18.tar.gz
Source15:       https://crates.io/api/v1/crates/rustc-hash/2.1.1/download#/rustc-hash-2.1.1.tar.gz

BuildRequires:  meson >= 1.3.0
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
BuildRequires:  pkgconfig(wayland-protocols) >= 1.34
BuildRequires:  pkgconfig(wayland-client) >= 1.11
BuildRequires:  pkgconfig(wayland-server) >= 1.11
BuildRequires:  pkgconfig(wayland-egl-backend) >= 3
BuildRequires:  pkgconfig(libdisplay-info)
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

BuildRequires:  pkgconfig(libva) >= 0.38.0

BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libglvnd) >= 1.3.2
BuildRequires:  llvm-devel >= 7.0.0

BuildRequires:  clang-devel
BuildRequires:  pkgconfig(libclc)
BuildRequires:  pkgconfig(SPIRV-Tools)
BuildRequires:  pkgconfig(LLVMSPIRVLib)

BuildRequires:  bindgen

BuildRequires:  cargo-rpm-macros

BuildRequires:  cbindgen

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
Provides:       mesa-dri-filesystem = 25.3.6-0.1
Obsoletes:      mesa-omx-drivers < 25.3.6-0.1
Obsoletes:      mesa-libd3d < 25.3.6-0.1
Obsoletes:      mesa-libd3d-devel < 25.3.6-0.1
Obsoletes:      mesa-vdpau-drivers < 25.3.6-0.1

%description filesystem
Mesa driver filesystem.

%package libGL
Summary:        Mesa libGL runtime libraries
Requires:       libglvnd-glx(x86-32) >= 1:1.3.2
Requires:       mesa-dri-drivers(x86-32) = 25.3.6-0.1
Obsoletes:      mesa-libOSMesa < 25.1.0~rc2-1

%description libGL
Mesa libGL runtime libraries.

%package libGL-devel
Summary:        Mesa libGL development package
Requires:       (mesa-libGL(x86-32) = 25.3.6-0.1 if mesa-libGL(x86-32))
Requires:       libglvnd-devel(x86-32) >= 1:1.3.2
Provides:       libGL-devel = 25.3.6-0.1
Provides:       libGL-devel(x86-32) = 25.3.6-0.1
Recommends:     gl-manpages
Obsoletes:      mesa-libOSMesa-devel < 25.1.0~rc2-1

%description libGL-devel
Mesa libGL development package.

%package libEGL
Summary:        Mesa libEGL runtime libraries
Requires:       libglvnd-egl(x86-32) >= 1:1.3.2
Requires:       mesa-libgbm(x86-32) = 25.3.6-0.1
Requires:       mesa-dri-drivers(x86-32) = 25.3.6-0.1

%description libEGL
Mesa libEGL runtime libraries.

%package libEGL-devel
Summary:        Mesa libEGL development package
Requires:       (mesa-libEGL(x86-32) = 25.3.6-0.1 if mesa-libEGL(x86-32))
Requires:       libglvnd-devel(x86-32) >= 1:1.3.2
Requires:       mesa-khr-devel(x86-32)
Provides:       libEGL-devel = 25.3.6-0.1
Provides:       libEGL-devel(x86-32) = 25.3.6-0.1

%description libEGL-devel
Mesa libEGL development package.

%package dri-drivers
Summary:        Mesa-based DRI drivers
Requires:       mesa-filesystem(x86-32) = 25.3.6-0.1

Recommends:     mesa-va-drivers(x86-32)

Obsoletes:      mesa-libglapi < 25.0.0~rc2-1
Provides:       mesa-libglapi >= 25.0.0~rc2-1

%description dri-drivers
Mesa-based DRI drivers.

%package        va-drivers
Summary:        Mesa-based VA-API video acceleration drivers
Requires:       mesa-filesystem(x86-32) = 25.3.6-0.1
Obsoletes:      mesa-vaapi-drivers < 22.2.0-5

%description va-drivers
Mesa-based VA-API video acceleration drivers.

%package libgbm
Summary:        Mesa gbm runtime library
Provides:       libgbm = 25.3.6-0.1
Provides:       libgbm(x86-32) = 25.3.6-0.1
Recommends:     mesa-dri-drivers(x86-32) = 25.3.6-0.1

Requires:       (mesa-dri-drivers(x86-32) = 25.3.6-0.1 if mesa-dri-drivers(x86-32))

%description libgbm
Mesa gbm runtime library.

%package libgbm-devel
Summary:        Mesa libgbm development package
Requires:       mesa-libgbm(x86-32) = 25.3.6-0.1
Provides:       libgbm-devel = 25.3.6-0.1
Provides:       libgbm-devel(x86-32) = 25.3.6-0.1

%description libgbm-devel
Mesa libgbm development package.

%package libOpenCL
Summary:        Mesa OpenCL runtime library
Requires:       (ocl-icd(x86-32) or OpenCL-ICD-Loader(x86-32))
Requires:       libclc(x86-32)
Requires:       mesa-libgbm(x86-32) = 25.3.6-0.1
Requires:       opencl-filesystem

%description libOpenCL
Mesa OpenCL runtime library.

%package libOpenCL-devel
Summary:        Mesa OpenCL development package
Requires:       mesa-libOpenCL(x86-32) = 25.3.6-0.1

%description libOpenCL-devel
Mesa OpenCL development package.

%package vulkan-drivers
Summary:        Mesa Vulkan drivers
Requires:       vulkan(x86-32)
Requires:       mesa-filesystem(x86-32) = 25.3.6-0.1
Obsoletes:      mesa-vulkan-devel < 25.3.6-0.1
Obsoletes:      VK_hdr_layer < 1

%description vulkan-drivers
The drivers with support for the Vulkan API.

%prep

cd './'
rm -rf 'mesa-25.3.6'
rpmuncompress -x 'mesa-25.3.6.tar.xz'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'mesa-25.3.6'
chmod -Rf a+rX,u+w,g-w,o-w .

cp Mesa-MLAA-License-Clarification-Email.txt docs/

# Extract Rust crates meson cache directory

cat > Cargo.toml <<_EOF
[package]
name = "mesa"
version = "25.3.6"
edition = "2021"

[lib]
path = "src/nouveau/nil/lib.rs"

# only direct dependencies need to be listed here
[dependencies]
paste = "$(grep ^directory subprojects/paste*.wrap | sed 's|.*-||')"
syn = { version = "$(grep ^directory subprojects/syn*.wrap | sed 's|.*-||')", features = ["clone-impls"] }
rustc-hash = "$(grep ^directory subprojects/rustc-hash*.wrap | sed 's|.*-||')"
_EOF
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
# ensure standard Rust compiler flags are set
export RUSTFLAGS="%build_rustflags"

# So... Meson can't actually find them without tweaks
export MESON_PACKAGE_CACHE_DIR="%{cargo_registry}/"

# This function rewrites a mesa .wrap file:
# - Removes the lines that start with "source"
# - Replaces the "directory =" with the MESON_PACKAGE_CACHE_DIR
#
# Example: An upstream .wrap file like this (proc-macro2-1-rs.wrap):
#
# [wrap-file]
# directory = proc-macro2-1.0.86
# source_url = https://crates.io/api/v1/crates/proc-macro2/1.0.86/download
# source_filename = proc-macro2-1.0.86.tar.gz
# source_hash = 5e719e8df665df0d1c8fbfd238015744736151d4445ec0836b8e628aae103b77
# patch_directory = proc-macro2-1-rs
#
# Will be transformed to:
#
# [wrap-file]
# directory = meson-package-cache-dir
# patch_directory = proc-macro2-1-rs
rewrite_wrap_file() {
  sed -e "/source.*/d" -e "s/^directory = ${1}-.*/directory = $(basename ${MESON_PACKAGE_CACHE_DIR:-subprojects/packagecache}/${1}-*)/" -i subprojects/${1}*.wrap
}

rewrite_wrap_file proc-macro2
rewrite_wrap_file quote
rewrite_wrap_file syn
rewrite_wrap_file unicode-ident
rewrite_wrap_file paste
rewrite_wrap_file rustc-hash

%meson \
  -Dplatforms=x11,wayland \
  -Dgallium-drivers=llvmpipe,virgl,nouveau,r300,crocus,i915,iris,svga,radeonsi,r600,asahi,freedreno,etnaviv,tegra,vc4,v3d,lima,panfrost,zink \
  -Dgallium-va=enabled \
  -Dgallium-mediafoundation=disabled \
  -Dteflon=false \
  -Dgallium-rusticl=true \
  -Dvulkan-drivers=swrast,amd,intel,intel_hasvk,asahi,broadcom,freedreno,panfrost,imagination,nouveau,virtio \
  -Dvulkan-layers=device-select \
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
  -Dspirv-tools=enabled \

%meson_build

%cargo_license_summary
%{cargo_license} > LICENSE.dependencies

%install
%meson_install

# likewise glvnd
rm -vf fakeinstall/usr/lib32/libGLX_mesa.so
rm -vf fakeinstall/usr/lib32/libEGL_mesa.so
# XXX can we just not build this
rm -vf fakeinstall/usr/lib32/libGLES*

# glvnd needs a default provider for indirect rendering where it cannot
# determine the vendor
ln -s /usr/lib32/libGLX_mesa.so.0 fakeinstall/usr/lib32/libGLX_system.so.0

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

/usr/lib32/dri/r300_dri.so
/usr/lib32/dri/r600_dri.so
/usr/lib32/dri/radeonsi_dri.so
/usr/lib32/dri/crocus_dri.so
/usr/lib32/dri/iris_dri.so
/usr/lib32/dri/i915_dri.so
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
/usr/lib32/dri/vc4_dri.so
/usr/lib32/dri/v3d_dri.so
/usr/lib32/dri/kgsl_dri.so
/usr/lib32/dri/msm_dri.so
/usr/lib32/dri/etnaviv_dri.so
/usr/lib32/dri/tegra_dri.so
/usr/lib32/dri/lima_dri.so
/usr/lib32/dri/panfrost_dri.so
/usr/lib32/dri/panthor_dri.so
/usr/lib32/dri/nouveau_dri.so
/usr/lib32/dri/vmwgfx_dri.so
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
/usr/lib32/dri/nouveau_drv_video.so
/usr/lib32/dri/r600_drv_video.so
/usr/lib32/dri/radeonsi_drv_video.so
/usr/lib32/dri/virtio_gpu_drv_video.so

%files vulkan-drivers
%license LICENSE.dependencies
/usr/lib32/libvulkan_lvp.so
/usr/share/vulkan/icd.d/lvp_icd.*.json
/usr/lib32/libVkLayer_MESA_device_select.so
/usr/share/vulkan/implicit_layer.d/VkLayer_MESA_device_select.json
/usr/lib32/libvulkan_virtio.so
/usr/share/vulkan/icd.d/virtio_icd.*.json
/usr/lib32/libvulkan_radeon.so
/usr/share/drirc.d/00-radv-defaults.conf
/usr/share/vulkan/icd.d/radeon_icd.*.json
/usr/lib32/libvulkan_nouveau.so
/usr/share/vulkan/icd.d/nouveau_icd.*.json
/usr/lib32/libvulkan_intel.so
/usr/share/vulkan/icd.d/intel_icd.*.json
/usr/lib32/libvulkan_intel_hasvk.so
/usr/share/vulkan/icd.d/intel_hasvk_icd.*.json
/usr/lib32/libvulkan_asahi.so
/usr/share/vulkan/icd.d/asahi_icd.*.json
/usr/lib32/libvulkan_broadcom.so
/usr/share/vulkan/icd.d/broadcom_icd.*.json
/usr/lib32/libvulkan_freedreno.so
/usr/share/vulkan/icd.d/freedreno_icd.*.json
/usr/lib32/libvulkan_panfrost.so
/usr/share/vulkan/icd.d/panfrost_icd.*.json
/usr/lib32/libvulkan_powervr_mesa.so
/usr/share/vulkan/icd.d/powervr_mesa_icd.*.json

