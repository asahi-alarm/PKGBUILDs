
Name:           m1n1
Version:        1.6.1
Release:        1
Summary:        Bootloader and experimentation playground for Apple Silicon

License:        MIT AND CC0-1.0 AND OFL-1.1-RFN AND Zlib AND (BSD-2-Clause OR GPL-2.0-or-later) AND (BSD-3-Clause OR GPL-2.0-or-later) AND MIT AND (MIT OR Apache-2.0)
URL:            https://github.com/AsahiLinux/m1n1
Source:         https://github.com/AsahiLinux/m1n1/archive/v1.6.1/m1n1-1.6.1.tar.gz
Source:         https://github.com/rafalh/rust-fatfs/archive/4eccb50d011146fbed20e133d33b22f3c27292e7/rust-fatfs-4eccb50d011146fbed20e133d33b22f3c27292e7.tar.gz

Patch:          m1n1-1.6.1-rust-deps.patch

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  adobe-source-code-pro-fonts
BuildRequires:  coreutils
BuildRequires:  fontconfig
BuildRequires:  system-logos
BuildRequires:  ImageMagick >= 7

BuildRequires:  systemd-rpm-macros

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  rust-std-static-aarch64-unknown-none-softfloat

BuildArch:      noarch

ExclusiveArch:  aarch64 noarch

Obsoletes:      m1n1 < 1.5.2-3

Provides:       bundled(arm-trusted-firmware)
Provides:       bundled(dwc3)
Provides:       bundled(dlmalloc)
Provides:       bundled(PDCLib)
Provides:       bundled(libfdt)
Provides:       bundled(minilzlib)
Provides:       bundled(tinf)

%description
m1n1 is the bootloader developed by the Asahi Linux project to bridge the Apple
(XNU) boot ecosystem to the Linux boot ecosystem.

%package        stage1
Summary:        Bootloader and experimentation playground for Apple Silicon

License:        MIT AND CC0-1.0 AND OFL-1.1-RFN AND Zlib AND (BSD-2-Clause OR GPL-2.0-or-later) AND (BSD-3-Clause OR GPL-2.0-or-later) AND (Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0)

Provides:       bundled(crate(fatfs))= 0.4.0

%description    stage1
m1n1 is the bootloader developed by the Asahi Linux project to bridge the Apple
(XNU) boot ecosystem to the Linux boot ecosystem.

This package contains the stage1 build of m1n1 that is used by the Asahi Linux
Installer.

%package        tools
Summary:        Developer tools for m1n1
License:        MIT
Requires:       m1n1 = 1.6.1-1
Requires:       python3
Requires:       python3dist(construct)
Requires:       python3dist(pyserial)
Requires:       systemd-udev

%description    tools
m1n1 is the bootloader developed by the Asahi Linux project to bridge the Apple
(XNU) boot ecosystem to the Linux boot ecosystem.

This package contains various developer tools for m1n1.

%prep

cd './'
rm -rf 'm1n1-1.6.1'
rpmuncompress -x 'm1n1-1.6.1.tar.gz'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'm1n1-1.6.1'
chmod -Rf a+rX,u+w,g-w,o-w .

mkdir -p rust/vendor/rust-fatfs
tar -xf rust-fatfs-4eccb50d011146fbed20e133d33b22f3c27292e7.tar.gz -C rust/vendor/rust-fatfs --strip-components 1

rpmuncompress m1n1-1.6.1-rust-deps.patch | 
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f

/usr/bin/rm -f rust/Cargo.lock
sed -ie 's;\(^build/$(RUST_LIB):.*\) rust/Cargo.lock$;\1;' Makefile

# Use our logos
pushd data
ln -s /usr/share/pixmaps/bootloader/bootlogo_128.png fedora_128.png
ln -s /usr/share/pixmaps/bootloader/bootlogo_256.png fedora_256.png
popd

# Use our fonts
font="$(fc-match "Source Code Pro:bold" 'file' | cut -d= -f2)"
if [ ! -e "$font" ]; then
    echo "Failed to find font"
    exit 1
fi

pushd font
rm SourceCodePro-Bold.ttf font.bin font_retina.bin
./makefont.sh 8 16 12 "$font" font.bin
./makefont.sh 16 32 25 "$font" font_retina.bin
popd

# Generate rust dependencies
%cargo_prep

%generate_buildrequires
cd rust
%cargo_generate_buildrequires -f chainload

%build
/usr/bin/make -O -j${RPM_BUILD_NCPUS} V=1 VERBOSE=1 RELEASE=1 LOGO=fedora CHAINLOADING=1
mv build build-stage1
pushd rust
%{cargo_license_summary} -f chainload
%{cargo_license} -f chainload > ../build-stage1/LICENSE.dependencies
popd

/usr/bin/make -O -j${RPM_BUILD_NCPUS} V=1 VERBOSE=1 RELEASE=1 LOGO=fedora
pushd rust
%{cargo_license_summary}
%{cargo_license} > ../build/LICENSE.dependencies
popd

%install
install -Dpm0644 -t fakeinstall/usr/lib/m1n1 \
  build/m1n1.{bin,macho} build/m1n1-asahi.bin
# install backwards compatibility symlink since update-m1n1 hardcodes
# `/usr/lib64/m1n1/m1n1.bin` as m1n1 binary
# check if the dir exists since /usr/lib expands to "/usr/lib64" for
# aarch64 builds in mock
if [ ! -d fakeinstall/usr/lib64/m1n1 ]; then
  mkdir -p fakeinstall/usr/lib64/m1n1
  ln -s /usr/lib/m1n1/m1n1.bin \
    fakeinstall/usr/lib64/m1n1/m1n1.bin
fi
install -Dpm0644 -t fakeinstall/usr/lib/m1n1-stage1 \
  build-stage1/m1n1.{bin,macho} build-stage1/m1n1-asahi.bin
install -Ddpm0755 fakeinstall/usr/lib/m1n1/m1n1
cp -pr proxyclient tools fakeinstall/usr/lib/m1n1/m1n1/
install -Dpm0644 -t fakeinstall%{_udevrulesdir} udev/80-m1n1.rules
install -Dpm0644 m1n1.conf.example fakeinstall/etc/m1n1.conf

%files
%license LICENSE 3rdparty_licenses/LICENSE.* build/LICENSE.dependencies
%doc README.md
%doc m1n1.conf.example
/usr/lib/m1n1/
/usr/lib64/m1n1
%config(noreplace) /etc/m1n1.conf

%files stage1
%license LICENSE 3rdparty_licenses/LICENSE.* rust/vendor/rust-fatfs/LICENSE.txt build-stage1/LICENSE.dependencies
%doc README.md
/usr/lib/m1n1-stage1/

%files tools
/usr/lib/m1n1/m1n1/
%{_udevrulesdir}/80-m1n1.rules

