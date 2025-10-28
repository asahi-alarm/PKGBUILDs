
  Summary:    X Keyboard Extension configuration data
  Name:       xkeyboard-config
  Version:    2.44
  Release:    1
  License:    HPND AND HPND-sell-variant AND X11 AND X11-distribute-modifications-variant AND MIT AND MIT-open-group AND xkeyboard-config-Zinoviev
  URL:        http://www.freedesktop.org/wiki/Software/XKeyboardConfig

  Source0:    http://xorg.freedesktop.org/archive/individual/data/xkeyboard-config/xkeyboard-config-2.44.tar.xz

  BuildArch:  noarch

  BuildRequires:  gettext gettext-devel
  BuildRequires:  meson
  BuildRequires:  libxslt
  BuildRequires:  perl(XML::Parser)
  BuildRequires:  pkgconfig(glib-2.0)
  BuildRequires:  pkgconfig(x11) >= 1.4.3
  BuildRequires:  pkgconfig(xorg-macros) >= 1.12
  BuildRequires:  pkgconfig(xproto) >= 7.0.20
  BuildRequires:  xkbcomp
  BuildRequires:  git-core

  %description
  This package contains configuration data used by the X Keyboard Extension (XKB),
  which allows selection of keyboard layouts when using a graphical interface.

  %package devel
  Summary:    Development files for xkeyboard-config
  Requires:   xkeyboard-config = 2.44-1
  Requires:   pkgconfig

  %description devel
  Development files for xkeyboard-config.

prepare() {

  cd './'
  rm -rf 'xkeyboard-config-2.44'
  tar -xf 'xkeyboard-config-2.44.tar.xz'
  STATUS=$?
  if [ $STATUS -ne 0 ]; then
    exit $STATUS
  fi
  cd 'xkeyboard-config-2.44'
  chmod -Rf a+rX,u+w,g-w,o-w .

  /usr/bin/git init -q
  /usr/bin/git config user.name "rpm-build"
  /usr/bin/git config user.email "<rpm-build>"
  /usr/bin/git config gc.auto 0
  /usr/bin/git add --force .
  GIT_COMMITTER_DATE=@${SOURCE_DATE_EPOCH:-${RPM_BUILD_TIME:?}} GIT_AUTHOR_DATE=@${SOURCE_DATE_EPOCH:-${RPM_BUILD_TIME:?}}\
  	/usr/bin/git commit -q --allow-empty -a\
  	--author "rpm-build <rpm-build>" -m "xkeyboard-config-2.44 base"
  /usr/bin/git checkout --track -b rpm-build

}

build() {
  %meson -Dcompat-rules=true -Dxorg-rules-symlinks=true

}

package() {

  # Remove unnecessary symlink
  rm -f $RPM_BUILD_ROOT/usr/share/X11/xkb/compiled
  /usr/lib/rpm/find-lang.sh fakeinstall xkeyboard-config

  # Create filelist
  {
     FILESLIST=${PWD}/files.list
     pushd $RPM_BUILD_ROOT
     find ./usr/share/X11/xkb -type d | sed -e "s/^\./%dir /g" > $FILESLIST
     find ./usr/share/X11/xkb -type f | sed -e "s/^\.//g" >> $FILESLIST
     popd
  }

  # -f files.list -f xkeyboard-config.lang
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/xkeyboard-config/  AUTHORS README.md COPYING docs/README.* docs/HOWTO.*
  _install fakeinstall/usr/share/man/man7/xkeyboard-config.*
  _install fakeinstall/usr/share/X11/xkb/rules/xorg
  _install fakeinstall/usr/share/X11/xkb/rules/xorg.lst
  _install fakeinstall/usr/share/X11/xkb/rules/xorg.xml

  # devel
  _install fakeinstall/usr/share/pkgconfig/xkeyboard-config.pc
}
