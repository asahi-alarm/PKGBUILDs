
  Name:           alsa-ucm-asahi
  Version:        8
  Release:        1
  Summary:        ALSA Use Case Manager configuration (and topologies) for Apple silicon devices
  License:        BSD-3-Clause

  URL:            https://github.com/AsahiLinux/alsa-ucm-conf-asahi

  Source:         https://github.com/AsahiLinux/alsa-ucm-conf-asahi/archive/v8/alsa-ucm-conf-asahi-8.tar.gz

  BuildArch:      noarch

  Requires:       alsa-ucm >= 1.2.7.2

  %description
  The ALSA Use Case Manager configuration (and topologies) for Apple silicon devices.

prepare() {

  cd './'
  rm -rf 'alsa-ucm-conf-asahi-8'
  tar -xf 'alsa-ucm-conf-asahi-8.tar.gz'
  STATUS=$?
  if [ $STATUS -ne 0 ]; then
    exit $STATUS
  fi
  cd 'alsa-ucm-conf-asahi-8'
  chmod -Rf a+rX,u+w,g-w,o-w .

}

package() {
  install -dm 755 fakeinstall/usr/share/alsa/ucm2/conf.d/
  cp -a ucm2/conf.d/aop_audio/ fakeinstall/usr/share/alsa/ucm2/conf.d/
  cp -a ucm2/conf.d/macaudio/ fakeinstall/usr/share/alsa/ucm2/conf.d/

  # A spec %files section (it could be that part of the next lines duplicate part of the package() function)
  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/alsa-ucm-conf-asahi/ LICENSE.asahi
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/alsa-ucm-conf-asahi/  README.asahi
  _install fakeinstall/usr/share/alsa/ucm2/conf.d/aop_audio/
  _install fakeinstall/usr/share/alsa/ucm2/conf.d/macaudio/
}
