
Summary:    X Keyboard Extension configuration data
Name:       xkeyboard-config
Version:    2.46
Release:    1
License:    HPND AND HPND-sell-variant AND X11 AND X11-distribute-modifications-variant AND MIT AND MIT-open-group AND xkeyboard-config-Zinoviev
URL:        http://www.freedesktop.org/wiki/Software/XKeyboardConfig

Source0:    http://xorg.freedesktop.org/archive/individual/data/xkeyboard-config/xkeyboard-config-2.46.tar.xz

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
Requires:   xkeyboard-config = 2.46-1
Requires:   pkgconfig

%description devel
Development files for xkeyboard-config.

%prep

cd './'
rm -rf 'xkeyboard-config-2.46'
rpmuncompress -x 'xkeyboard-config-2.46.tar.xz'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'xkeyboard-config-2.46'
chmod -Rf a+rX,u+w,g-w,o-w .

/usr/bin/git init -q
/usr/bin/git config user.name "rpm-build"
/usr/bin/git config user.email "<rpm-build>"
/usr/bin/git config gc.auto 0
/usr/bin/git add --force .
GIT_COMMITTER_DATE=@${SOURCE_DATE_EPOCH:-${RPM_BUILD_TIME:?}} GIT_AUTHOR_DATE=@${SOURCE_DATE_EPOCH:-${RPM_BUILD_TIME:?}}\
	/usr/bin/git commit -q --allow-empty -a\
	--author "rpm-build <rpm-build>" -m "xkeyboard-config-2.46 base"
/usr/bin/git checkout --track -b rpm-build

%build
%meson -Dcompat-rules=true -Dxorg-rules-symlinks=true
%meson_build

%install
%meson_install

# Replace with relative symlink
rm $RPM_BUILD_ROOT/usr/share/X11/xkb
ln -srf $RPM_BUILD_ROOT/usr/share/xkeyboard-config-2 $RPM_BUILD_ROOT/usr/share/X11/xkb

/usr/lib/rpm/find-lang.sh fakeinstall xkeyboard-config-2
/usr/lib/rpm/find-lang.sh fakeinstall xkeyboard-config

# Note: 2.45 changed the install location from the decades-old /usr/share/X11/xkb
# to a package-specific /usr/share/xkeyboard-config-2. Upstream installs a symlink
# for /usr/share/X11/xkb since those two dirctories are guaranteed to be the same.
#
# The "official" script [1] is buggy if an .rpmmoved directory already exists so
# this is an approximation taken from OpenSuSE [2]
# [1] https://fedoraproject.org/wiki/Packaging:Directory_Replacement#Replacing_a_symlink_with_a_directory_or_a_directory_with_any_type_of_file
# [2] https://build.opensuse.org/request/show/1294803
%pretrans -p <lua>
-- Define the path to directory being replaced below.
-- DO NOT add a trailing slash at the end.
local path = "/usr/share/X11/xkb"
local st = posix.stat(path)

if st and st.type == "directory" then
  local target = path .. ".rpmmoved"
  local suffix = 1

  while posix.stat(target) do
    suffix = suffix + 1
    target = path .. ".rpmmoved" .. suffix
  end

  os.rename(path, target)
end

%files -f xkeyboard-config-2.lang -f xkeyboard-config.lang
%doc AUTHORS README.md COPYING docs/README.* docs/HOWTO.*
/usr/share/man/man7/xkeyboard-config.*
/usr/share/man/man7/xkeyboard-config-2.*
/usr/share/X11/xkb
/usr/share/xkeyboard-config-2/
%ghost %attr(0755, root, root) %dir /usr/share/X11/xkb.rpmmoved

%files devel
/usr/share/pkgconfig/xkeyboard-config-2.pc
/usr/share/pkgconfig/xkeyboard-config.pc

