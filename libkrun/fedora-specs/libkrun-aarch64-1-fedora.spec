
Name:           libkrun
Version:        1.15.1
Release:        1
Summary:        Dynamic library providing Virtualization-based process isolation capabilities

License:        Apache-2.0
URL:            https://github.com/containers/libkrun
Source:         https://github.com/containers/libkrun/archive/refs/tags/v1.15.1.tar.gz

Patch0:         libkrun-remove-unused-deps.diff

Patch1:         libkrun-remove-nitro-deps.diff

Patch2:         libkrun-remove-tdx-deps.diff

Patch3:         libkrun-relax-bindgen-dep.diff

Patch4:         libkrun-remove-sev-deps.diff

ExclusiveArch:  x86_64 aarch64

Requires:  libkrunfw >= 4.0.0

BuildRequires:  rust-packaging >= 21
BuildRequires:  glibc-static
BuildRequires:  binutils
BuildRequires:  libepoxy-devel
BuildRequires:  libdrm-devel
BuildRequires:  virglrenderer-devel
BuildRequires:  pipewire-devel
BuildRequires:  clang-devel
BuildRequires:  openssl-devel
BuildRequires:  libcurl-devel

BuildRequires:  libfdt-devel

BuildRequires:  crate(libc/default) >= 0.2.39
BuildRequires:  crate(vm-memory/backend-mmap) >= 0.16.0
BuildRequires:  crate(vm-memory/default) >= 0.16.0
BuildRequires:  crate(kvm-bindings/default) >= 0.13.0
BuildRequires:  crate(kvm-bindings/fam-wrappers) >= 0.13.0
BuildRequires:  crate(kvm-ioctls/default) >= 0.23.0
BuildRequires:  crate(vmm-sys-util/default) >= 0.14.0
BuildRequires:  crate(vm-fdt/default) >= 0.2.0
BuildRequires:  (crate(virtio-bindings/default) >= 0.2.0 with crate(virtio-bindings/default) < 0.3.0~)
BuildRequires:  (crate(bitflags/default) >= 1.2.0 with crate(bitflags/default) < 2.0.0~)
BuildRequires:  (crate(env_logger/default) >= 0.11.0 with crate(env_logger/default) < 0.12.0~)
BuildRequires:  (crate(log/default) >= 0.4.0 with crate(log/default) < 0.5.0~)
BuildRequires:  (crate(nix/default) >= 0.24.1 with crate(nix/default) < 0.25.0~)
BuildRequires:  (crate(nix/default) >= 0.26.1 with crate(nix/default) < 0.27.0~)
BuildRequires:  (crate(nix/default) >= 0.27.1 with crate(nix/default) < 0.28.0~)
BuildRequires:  (crate(rand/default) >= 0.8.5 with crate(rand/default) < 0.9.0~)
BuildRequires:  (crate(rand/default) >= 0.9.2 with crate(rand/default) < 0.10.0~)
BuildRequires:  (crate(once_cell/default) >= 1.4.1 with crate(once_cell/default) < 2.0.0~)
BuildRequires:  (crate(crossbeam-channel/default) >= 0.5.0 with crate(crossbeam-channel/default) < 0.6.0~)
BuildRequires:  (crate(pipewire/default) >= 0.8.0 with crate(pipewire/default) < 0.9.0~)
BuildRequires:  (crate(zerocopy/default) >= 0.6.0 with crate(zerocopy/default) < 0.7.0~)
BuildRequires:  (crate(zerocopy/default) >= 0.7.0 with crate(zerocopy/default) < 0.8.0~)
BuildRequires:  (crate(remain/default) >= 0.2.0 with crate(remain/default) < 0.3.0~)
BuildRequires:  (crate(caps/default) >= 0.5.0 with crate(caps/default) < 0.6.0~)
BuildRequires:  (crate(imago/default) >= 0.1.0 with crate(imago/default) < 0.2.0~)
BuildRequires:  (crate(linux-loader/default) >= 0.13.0 with crate(linux-loader/default) < 0.14.0~)
BuildRequires:  (crate(bzip2/default) >= 0.5.0 with crate(bzip2/default) < 0.6.0~)
BuildRequires:  (crate(zstd/default) >= 0.13.0 with crate(zstd/default) < 0.14.0~)
BuildRequires:  (crate(flate2/default) >= 1.0.0 with crate(flate2/default) < 2.0.0~)
BuildRequires:  (crate(static_assertions/default) >= 1.1.0 with crate(static_assertions/default) < 2.0.0~)
BuildRequires:  (crate(thiserror/default) >= 2.0.0 with crate(thiserror/default) < 3.0.0~)

%description
Dynamic library providing Virtualization-based process isolation capabilities.

%package devel
Summary: Header files and libraries for libkrun development
Requires:       libkrun(aarch-64) = 1.15.1-1

%description devel
The libkrun-devel package containes the libraries and headers needed to
develop programs that use libkrun Virtualization-based process isolation
capabilities.

%prep
cd './'
rm -rf 'libkrun-%{version_no_tilde}'
rpmuncompress -x 'v1.15.1.tar.gz'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'libkrun-%{version_no_tilde}'
chmod -Rf a+rX,u+w,g-w,o-w .

echo "Patch #0 (libkrun-remove-unused-deps.diff):"
patch --no-backup-if-mismatch -f -p1  --fuzz=0 < libkrun-remove-unused-deps.diff

echo "Patch #1 (libkrun-remove-nitro-deps.diff):"
patch --no-backup-if-mismatch -f -p1  --fuzz=0 < libkrun-remove-nitro-deps.diff

echo "Patch #2 (libkrun-remove-tdx-deps.diff):"
patch --no-backup-if-mismatch -f -p1  --fuzz=0 < libkrun-remove-tdx-deps.diff

echo "Patch #3 (libkrun-relax-bindgen-dep.diff):"
patch --no-backup-if-mismatch -f -p1  --fuzz=0 < libkrun-relax-bindgen-dep.diff

echo "Patch #4 (libkrun-remove-sev-deps.diff):"
patch --no-backup-if-mismatch -f -p1  --fuzz=0 < libkrun-remove-sev-deps.diff

%cargo_prep

%build
/usr/bin/make -O -j${RPM_BUILD_NCPUS} V=1 VERBOSE=1 init/init
/usr/bin/make -O -j${RPM_BUILD_NCPUS} V=1 VERBOSE=1 libkrun.pc
/usr/bin/make -O -j${RPM_BUILD_NCPUS} V=1 VERBOSE=1 GPU=1 BLK=1 NET=1 SND=1

%install
/usr/bin/make install DESTDIR=fakeinstall INSTALL="install -p" PREFIX=/usr

%files
%license LICENSE
%doc README.md
/usr/lib/libkrun.so.1.15.1
/usr/lib/libkrun.so.1

%files devel
/usr/lib/libkrun.so
/usr/lib/pkgconfig/libkrun.pc
/usr/include/libkrun.h
/usr/include/libkrun_display.h

