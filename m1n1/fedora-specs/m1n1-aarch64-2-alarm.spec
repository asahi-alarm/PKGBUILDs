
  Name:           m1n1
  Version:        1.5.0
  Release:        1
  Summary:        Bootloader and experimentation playground for Apple Silicon

  License:        MIT AND CC0-1.0 AND OFL-1.1-RFN AND Zlib AND (BSD-2-Clause OR GPL-2.0-or-later) AND (BSD-3-Clause OR GPL-2.0-or-later)
  URL:            https://github.com/AsahiLinux/m1n1
  Source:         https://github.com/AsahiLinux/m1n1/archive/v1.5.0/m1n1-1.5.0.tar.gz
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
  Requires:       m1n1 = 1.5.0-1
  Requires:       python3
  Requires:       python3dist(construct)
  Requires:       python3dist(pyserial)
  Requires:       systemd-udev
  BuildArch:      noarch

  %description    tools
  m1n1 is the bootloader developed by the Asahi Linux project to bridge the Apple
  (XNU) boot ecosystem to the Linux boot ecosystem.

  This package contains various developer tools for m1n1.

prepare() {

  cd './'
  rm -rf 'm1n1-1.5.0'
  tar -xf 'm1n1-1.5.0.tar.gz'
  STATUS=$?
  if [ $STATUS -ne 0 ]; then
    exit $STATUS
  fi
  cd 'm1n1-1.5.0'
  chmod -Rf a+rX,u+w,g-w,o-w .

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

  tar -xf rust-fatfs-87fc1ed5074a32b4e0344fcdde77359ef9e75432.tar.gz -C rust/vendor/rust-fatfs --strip-components 1

  echo 'Cannot read m1n1-rust-deps.patch'; exit 1;

  echo 'Cannot read rust-fatfs-fix-build-log.patch'; exit 1;

  %cargo_prep

  %generate_buildrequires
  cd rust
  %cargo_generate_buildrequires

}

build() {
  /usr/bin/make -O -j${RPM_BUILD_NCPUS} V=1 VERBOSE=1 RELEASE=1 CHAINLOADING=1 LOGO=fedora
  mv build build-stage1
  pushd rust
  %{cargo_license_summary}
  %{cargo_license} > LICENSE.dependencies
  popd

  /usr/bin/make -O -j${RPM_BUILD_NCPUS} V=1 VERBOSE=1 RELEASE=1 LOGO=fedora

}

package() {
  install -Dpm0644 -t fakeinstall/usr/lib/m1n1 \
    build/m1n1.{bin,macho} build/m1n1-asahi.bin
  install -Dpm0644 -t fakeinstall/usr/lib/m1n1-stage1 \
    build-stage1/m1n1.{bin,macho} build-stage1/m1n1-asahi.bin
  install -Ddpm0755 fakeinstall/usr/lib/m1n1/m1n1
  cp -pr proxyclient tools fakeinstall/usr/lib/m1n1/m1n1/
  install -Dpm0644 -t fakeinstall%{_udevrulesdir} udev/80-m1n1.rules
  install -Dpm0644 m1n1.conf.example fakeinstall/etc/m1n1.conf

  # A spec %files section (it could be that part of the next lines duplicate part of the package() function)
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/m1n1/ LICENSE 3rdparty_licenses/LICENSE.*
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/m1n1/  README.md
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/m1n1/  m1n1.conf.example
  _install fakeinstall/usr/lib/m1n1
  %config(noreplace) /etc/m1n1.conf

  # stage1
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/m1n1/ LICENSE 3rdparty_licenses/LICENSE.* rust/vendor/rust-fatfs/LICENSE.txt rust/LICENSE.dependencies
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/m1n1/  README.md
  _install fakeinstall/usr/lib/m1n1-stage1

  # tools
  _install fakeinstall/usr/lib/m1n1/m1n1
  %{_udevrulesdir}/80-m1n1.rules
}
