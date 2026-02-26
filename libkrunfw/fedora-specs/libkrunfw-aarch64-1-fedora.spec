
Name:           libkrunfw
Version:        5.2.1
Release:        1
Summary:        A dynamic library bundling the guest payload consumed by libkrun
License:        LGPL-2.1-only AND GPL-2.0-only
URL:            https://github.com/containers/libkrunfw
Source0:        https://github.com/containers/libkrunfw/archive/refs/tags/v5.2.1.tar.gz

Source1:        https://www.kernel.org/pub/linux/kernel/v6.x/linux-6.12.68.tar.xz

ExclusiveArch:  x86_64 aarch64 riscv64

BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  python3-pyelftools
BuildRequires:  openssl-devel

BuildRequires:  bc
BuildRequires:  bison
BuildRequires:  elfutils-devel
BuildRequires:  flex

BuildRequires:  perl-interpreter

%description
A dynamic library bundling the guest payload consumed by libkrun

%package devel
Summary: Header files and libraries for libkrunfw development
Requires: libkrunfw(aarch-64) = 5.2.1-1

%description devel
The libkrunfw-devel package contains the libraries needed to develop
programs that consume the guest payload integrated in libkrunfw.

%prep

cd './'
rm -rf 'libkrunfw-5.2.1'
rpmuncompress -x 'v5.2.1.tar.gz'
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
cd 'libkrunfw-5.2.1'
chmod -Rf a+rX,u+w,g-w,o-w .

/usr/bin/git init -q
/usr/bin/git config user.name "rpm-build"
/usr/bin/git config user.email "<rpm-build>"
/usr/bin/git config gc.auto 0
/usr/bin/git add --force .
GIT_COMMITTER_DATE=@${SOURCE_DATE_EPOCH:-${RPM_BUILD_TIME:?}} GIT_AUTHOR_DATE=@${SOURCE_DATE_EPOCH:-${RPM_BUILD_TIME:?}}\
	/usr/bin/git commit -q --no-gpg-sign --allow-empty -a\
	--author "rpm-build <rpm-build>" -m "libkrunfw-5.2.1 base"
/usr/bin/git checkout --track -b rpm-build

mkdir tarballs
cp linux-6.12.68.tar.xz tarballs/

%build
/usr/bin/make -O -j${RPM_BUILD_NCPUS} V=1 VERBOSE=1

%install
/usr/bin/make install DESTDIR=fakeinstall INSTALL="install -p" PREFIX=/usr

%files
/usr/lib/libkrunfw.so.5
/usr/lib/libkrunfw.so.5.2.1

%files devel
/usr/lib/libkrunfw.so

