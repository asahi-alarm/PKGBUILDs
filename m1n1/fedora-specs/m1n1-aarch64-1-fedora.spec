
Name:           m1n1
Version:        1.4.21
Release:        1
Summary:        Bootloader and experimentation playground for Apple Silicon

License:        MIT AND CC0-1.0 AND OFL-1.1-RFN AND Zlib AND (BSD-2-Clause OR GPL-2.0-or-later) AND (BSD-3-Clause OR GPL-2.0-or-later)
URL:            https://github.com/AsahiLinux/m1n1
Source:         https://github.com/AsahiLinux/m1n1/archive/v1.4.21/m1n1-1.4.21.tar.gz
Source:         https://github.com/rafalh/rust-fatfs/archive/87fc1ed5074a32b4e0344fcdde77359ef9e75432/rust-fatfs-87fc1ed5074a32b4e0344fcdde77359ef9e75432.tar.gz

Patch:          m1n1-rust-deps.patch

Patch:          rust-fatfs-fix-build-log.patch

BuildRequires:  gcc

BuildRequires:  make

BuildRequires:  adobe-source-code-pro-fonts
BuildRequires:  coreutils
BuildRequires:  fontconfig
BuildRequires:  system-logos
BuildRequires:  ImageMagick

BuildRequires:  systemd-rpm-macros

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  rust-std-static-aarch64-unknown-none-softfloat

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
Requires:       m1n1 = 1.4.21-1
Requires:       python3
Requires:       python3dist(construct)
Requires:       python3dist(pyserial)
Requires:       systemd-udev
BuildArch:      noarch

%description    tools
m1n1 is the bootloader developed by the Asahi Linux project to bridge the Apple
(XNU) boot ecosystem to the Linux boot ecosystem.

This package contains various developer tools for m1n1.

%prep

cd './'
rm -rf 'm1n1-1.4.21'
rpmuncompress -x 'm1n1-1.4.21.tar.gz'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'm1n1-1.4.21'
chmod -Rf a+rX,u+w,g-w,o-w .

# Use our logos
pushd data
rm bootlogo_{128,256}.{bin,png}
ln -s /usr/share/pixmaps/bootloader/bootlogo_{128,256}.png .
./makelogo.sh
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

tar -xf rust-fatfs-87fc1ed5074a32b4e0344fcdde77359ef9e75432.tar.gz -C rust/vendor/rust-fatfs --strip-components 1

echo 'Cannot read m1n1-rust-deps.patch'; exit 1;

echo 'Cannot read rust-fatfs-fix-build-log.patch'; exit 1;

%cargo_prep

%generate_buildrequires
cd rust
%cargo_generate_buildrequires

%build
/usr/bin/make -O -j${RPM_BUILD_NCPUS} V=1 VERBOSE=1 RELEASE=1 CHAINLOADING=1
mv build build-stage1
pushd rust
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
popd

/usr/bin/make -O -j${RPM_BUILD_NCPUS} V=1 VERBOSE=1 RELEASE=1

%install
install -Dpm0644 -t fakeinstall/usr/lib/m1n1 build/m1n1.{bin,macho}
install -Dpm0644 -t fakeinstall/usr/lib/m1n1-stage1 \
  build-stage1/m1n1.{bin,macho}
install -Ddpm0755 fakeinstall/usr/lib/m1n1/m1n1
cp -pr proxyclient tools fakeinstall/usr/lib/m1n1/m1n1/
install -Dpm0644 -t fakeinstall%{_udevrulesdir} udev/80-m1n1.rules
install -Dpm0644 m1n1.conf.example fakeinstall/etc/m1n1.conf

%files
%license LICENSE 3rdparty_licenses/LICENSE.*
%doc README.md
%doc m1n1.conf.example
/usr/lib/m1n1
%config(noreplace) /etc/m1n1.conf

%files stage1
%license LICENSE 3rdparty_licenses/LICENSE.* rust/vendor/rust-fatfs/LICENSE.txt rust/LICENSE.dependencies
%doc README.md
/usr/lib/m1n1-stage1

%files tools
/usr/lib/m1n1/m1n1
%{_udevrulesdir}/80-m1n1.rules

