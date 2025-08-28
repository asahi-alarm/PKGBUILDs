
  Summary: The Linux kernel

  Name: kernel
  License: ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-2-Clause) AND ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-3-Clause) AND ((GPL-2.0-only WITH Linux-syscall-note) OR CDDL-1.0) AND ((GPL-2.0-only WITH Linux-syscall-note) OR Linux-OpenIB) AND ((GPL-2.0-only WITH Linux-syscall-note) OR MIT) AND ((GPL-2.0-or-later WITH Linux-syscall-note) OR BSD-3-Clause) AND ((GPL-2.0-or-later WITH Linux-syscall-note) OR MIT) AND 0BSD AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0) AND BSD-3-Clause AND BSD-3-Clause-Clear AND CC0-1.0 AND GFDL-1.1-no-invariants-or-later AND GPL-1.0-or-later AND (GPL-1.0-or-later OR BSD-3-Clause) AND (GPL-1.0-or-later WITH Linux-syscall-note) AND GPL-2.0-only AND (GPL-2.0-only OR Apache-2.0) AND (GPL-2.0-only OR BSD-2-Clause) AND (GPL-2.0-only OR BSD-3-Clause) AND (GPL-2.0-only OR CDDL-1.0) AND (GPL-2.0-only OR GFDL-1.1-no-invariants-or-later) AND (GPL-2.0-only OR GFDL-1.2-no-invariants-only) AND (GPL-2.0-only OR GFDL-1.2-no-invariants-or-later) AND (GPL-2.0-only WITH Linux-syscall-note) AND GPL-2.0-or-later AND (GPL-2.0-or-later OR BSD-2-Clause) AND (GPL-2.0-or-later OR BSD-3-Clause) AND (GPL-2.0-or-later OR CC-BY-4.0) AND (GPL-2.0-or-later WITH GCC-exception-2.0) AND (GPL-2.0-or-later WITH Linux-syscall-note) AND ISC AND LGPL-2.0-or-later AND (LGPL-2.0-or-later OR BSD-2-Clause) AND (LGPL-2.0-or-later WITH Linux-syscall-note) AND LGPL-2.1-only AND (LGPL-2.1-only OR BSD-2-Clause) AND (LGPL-2.1-only WITH Linux-syscall-note) AND LGPL-2.1-or-later AND (LGPL-2.1-or-later WITH Linux-syscall-note) AND (Linux-OpenIB OR GPL-2.0-only) AND (Linux-OpenIB OR GPL-2.0-only OR BSD-2-Clause) AND Linux-man-pages-copyleft AND MIT AND (MIT OR Apache-2.0) AND (MIT OR GPL-2.0-only) AND (MIT OR GPL-2.0-or-later) AND (MIT OR LGPL-2.1-only) AND (MPL-1.1 OR GPL-2.0-only) AND (X11 OR GPL-2.0-only) AND (X11 OR GPL-2.0-or-later) AND Zlib AND (copyleft-next-0.3.1 OR GPL-2.0-or-later)
  URL: https://www.kernel.org/
  Version: 6.15.10
  Release: 402.asahi

  ExclusiveArch: noarch x86_64 s390x aarch64 ppc64le riscv64

  ExclusiveOS: Linux

  Requires: kernel-core-uname-r = 6.15.10-402.asahi.aarch64
  Requires: kernel-modules-uname-r = 6.15.10-402.asahi.aarch64
  Requires: kernel-modules-core-uname-r = 6.15.10-402.asahi.aarch64
  Requires: ((kernel-modules-extra-uname-r = 6.15.10-402.asahi.aarch64) if kernel-modules-extra-matched)
  Provides: installonlypkg(kernel)

  BuildRequires: kmod, bash, coreutils, tar, git-core, which
  BuildRequires: bzip2, xz, findutils, m4, perl-interpreter, perl-Carp, perl-devel, perl-generators, make, diffutils, gawk, xz

  BuildRequires: zstd

  BuildRequires: gcc, binutils, redhat-rpm-config, hmaccalc, bison, flex, gcc-c++
  BuildRequires: rust, rust-src, bindgen, rustfmt, clippy
  BuildRequires: net-tools, hostname, bc, elfutils-devel
  BuildRequires: dwarves
  BuildRequires: python3
  BuildRequires: python3-devel
  BuildRequires: python3-pyyaml
  BuildRequires: kernel-rpm-macros

  BuildRequires: glibc-static

  BuildRequires: rsync

  BuildRequires: zlib-devel binutils-devel newt-devel perl(ExtUtils::Embed) bison flex xz-devel
  BuildRequires: audit-libs-devel python3-setuptools
  BuildRequires: java-devel
  BuildRequires: libbpf-devel >= 0.6.0-1
  BuildRequires: libbabeltrace-devel
  BuildRequires: libtraceevent-devel

  BuildRequires: numactl-devel

  BuildRequires: opencsd-devel >= 1.0.0

  BuildRequires: python3-docutils
  BuildRequires: gettext ncurses-devel
  BuildRequires: libcap-devel libcap-ng-devel

  BuildRequires: python3-docutils
  BuildRequires: libtraceevent-devel
  BuildRequires: libtracefs-devel
  BuildRequires: libbpf-devel
  BuildRequires: bpftool
  BuildRequires: clang

  BuildRequires: pciutils-devel

  BuildRequires: python3-pyyaml python3-jsonschema python3-pip python3-setuptools >= 61
  BuildRequires: (python3-wheel if python3-setuptools < 70)

  BuildRequires: openssl-devel

  BuildRequires: clang llvm-devel fuse-devel zlib-devel binutils-devel python3-docutils python3-jsonschema

  BuildRequires: libcap-devel libcap-ng-devel rsync libmnl-devel
  BuildRequires: numactl-devel

  BuildConflicts: rhbuildsys(DiskFree) < 500Mb

  BuildRequires: rpm-build, elfutils
  BuildConflicts: rpm < 4.13.0.1-19
  BuildConflicts: dwarves < 1.13

  BuildRequires: openssl

  BuildRequires: xmlto

  BuildRequires: asciidoc

  BuildRequires: dracut

  BuildRequires: binutils

  BuildRequires: lvm2
  BuildRequires: systemd-boot-unsigned

  BuildRequires: systemd-udev >= 252-1

  BuildRequires: systemd-ukify

  BuildRequires: tpm2-tools

  Source0: linux-6.15.10.tar.xz

  Source1: Makefile.rhelver
  Source2: kernel.changelog

  Source10: redhatsecurebootca5.cer
  Source13: redhatsecureboot501.cer

  Source20: mod-denylist.sh
  Source21: mod-sign.sh
  Source22: filtermods.py

  Source23: x509.genkey.rhel

  Source24: kernel-aarch64-rhel.config
  Source25: kernel-aarch64-debug-rhel.config

  Source27: kernel-ppc64le-rhel.config
  Source28: kernel-ppc64le-debug-rhel.config
  Source29: kernel-s390x-rhel.config
  Source30: kernel-s390x-debug-rhel.config
  Source31: kernel-s390x-zfcpdump-rhel.config
  Source32: kernel-x86_64-rhel.config
  Source33: kernel-x86_64-debug-rhel.config

  Source34: def_variants.yaml.rhel

  Source41: x509.genkey.centos

  Source42: kernel-aarch64-64k-rhel.config
  Source43: kernel-aarch64-64k-debug-rhel.config

  Source50: x509.genkey.fedora

  Source52: kernel-aarch64-fedora.config
  Source53: kernel-aarch64-debug-fedora.config
  Source54: kernel-aarch64-16k-fedora.config
  Source55: kernel-aarch64-16k-debug-fedora.config
  Source56: kernel-ppc64le-fedora.config
  Source57: kernel-ppc64le-debug-fedora.config
  Source58: kernel-s390x-fedora.config
  Source59: kernel-s390x-debug-fedora.config
  Source60: kernel-x86_64-fedora.config
  Source61: kernel-x86_64-debug-fedora.config
  Source700: kernel-riscv64-fedora.config
  Source701: kernel-riscv64-debug-fedora.config

  Source62: def_variants.yaml.fedora

  Source70: partial-kgcov-snip.config
  Source71: partial-kgcov-debug-snip.config
  Source72: partial-clang-snip.config
  Source73: partial-clang-debug-snip.config
  Source74: partial-clang_lto-x86_64-snip.config
  Source75: partial-clang_lto-x86_64-debug-snip.config
  Source76: partial-clang_lto-aarch64-snip.config
  Source77: partial-clang_lto-aarch64-debug-snip.config
  Source80: generate_all_configs.sh
  Source81: process_configs.sh

  Source86: dracut-virt.conf

  Source87: flavors

  Source151: uki_create_addons.py
  Source152: uki_addons.json

  Source100: rheldup3.x509
  Source101: rhelkpatch1.x509
  Source102: nvidiagpuoot001.x509
  Source103: rhelimaca1.x509
  Source104: rhelima.x509
  Source105: rhelima_centos.x509
  Source106: fedoraimaca.x509

  Source200: check-kabi

  Source201: Module.kabi_aarch64
  Source202: Module.kabi_ppc64le
  Source203: Module.kabi_s390x
  Source204: Module.kabi_x86_64
  Source205: Module.kabi_riscv64

  Source210: Module.kabi_dup_aarch64
  Source211: Module.kabi_dup_ppc64le
  Source212: Module.kabi_dup_s390x
  Source213: Module.kabi_dup_x86_64
  Source214: Module.kabi_dup_riscv64

  Source300: kernel-abi-stablelists-6.15.10.tar.xz
  Source301: kernel-kabi-dw-6.15.10.tar.xz

  Source474: kernel-aarch64-rt-rhel.config
  Source475: kernel-aarch64-rt-debug-rhel.config
  Source476: kernel-aarch64-rt-64k-rhel.config
  Source477: kernel-aarch64-rt-64k-debug-rhel.config
  Source478: kernel-x86_64-rt-rhel.config
  Source479: kernel-x86_64-rt-debug-rhel.config

  Source480: kernel-aarch64-rt-fedora.config
  Source481: kernel-aarch64-rt-debug-fedora.config
  Source482: kernel-aarch64-rt-64k-fedora.config
  Source483: kernel-aarch64-rt-64k-debug-fedora.config
  Source484: kernel-x86_64-rt-fedora.config
  Source485: kernel-x86_64-rt-debug-fedora.config
  Source486: kernel-riscv64-rt-fedora.config
  Source487: kernel-riscv64-rt-debug-fedora.config

  Source488: kernel-aarch64-automotive-rhel.config
  Source489: kernel-aarch64-automotive-debug-rhel.config
  Source490: kernel-x86_64-automotive-rhel.config
  Source491: kernel-x86_64-automotive-debug-rhel.config

  Source2002: kvm_stat.logrotate

  Source3000: merge.py
  Source3001: kernel-local

  Source3002: Patchlist.changelog

  Source4000: README.rst
  Source4001: rpminspect.yaml
  Source4002: gating.yaml

  Patch1: patch-6.15-redhat.patch

  Patch999999: linux-kernel-test.patch

  %description
  The kernel meta package

  %package doc
  Summary: Various documentation bits found in the kernel source
  Group: Documentation
  %description doc
  This package contains documentation files from the kernel
  source. Various bits of information about the Linux kernel and the
  device drivers shipped with it are documented in these files.

  You'll want to install this package if you need a reference to the
  options that can be passed to Linux kernel modules at load time.

  %package headers
  Summary: Header files for the Linux kernel for use by glibc
  Obsoletes: glibc-kernheaders < 3.0-46
  Provides: glibc-kernheaders = 3.0-46

  %description headers
  Kernel-headers includes the C header files that specify the interface
  between the Linux kernel and userspace libraries and programs.  The
  header files define structures and constants that are needed for
  building most standard programs and are also needed for rebuilding the
  glibc package.

  %package cross-headers
  Summary: Header files for the Linux kernel for use by cross-glibc

  %description cross-headers
  Kernel-cross-headers includes the C header files that specify the interface
  between the Linux kernel and userspace libraries and programs.  The
  header files define structures and constants that are needed for
  building most standard programs and are also needed for rebuilding the
  cross-glibc package.

  %package debuginfo-common-aarch64
  Summary: Kernel source files used by kernel-debuginfo packages
  Provides: installonlypkg(kernel)
  %description debuginfo-common-aarch64
  This package is required by kernel-debuginfo subpackages.
  It provides the kernel source files common to all builds.

  %package -n perf

  Summary: Performance monitoring for the Linux kernel
  Requires: bzip2
  %description -n perf
  This package contains the perf tool, which enables performance monitoring
  of the Linux kernel.

  %package -n perf-debuginfo

  Summary: Debug information for package perf
  Requires: kernel-debuginfo-common-aarch64 = 6.15.10-402.asahi
  AutoReqProv: no
  %description -n perf-debuginfo
  This package provides debug information for the perf package.

  %package -n python3-perf

  Summary: Python bindings for apps which will manipulate perf events
  %description -n python3-perf
  The python3-perf package contains a module that permits applications
  written in the Python programming language to use the interface
  to manipulate perf events.

  %package -n python3-perf-debuginfo

  Summary: Debug information for package perf python bindings
  Requires: kernel-debuginfo-common-aarch64 = 6.15.10-402.asahi
  AutoReqProv: no
  %description -n python3-perf-debuginfo
  This package provides debug information for the perf python bindings.

  %package -n libperf
  Summary: The perf library from kernel source
  %description -n libperf
  This package contains the kernel source perf library.

  %package -n libperf-devel
  Summary: Developement files for the perf library from kernel source
  Requires: libperf = 6.15.10-402.asahi
  %description -n libperf-devel
  This package includes libraries and header files needed for development
  of applications which use perf library from kernel source.

  %package -n libperf-debuginfo
  Summary: Debug information for package libperf
  Group: Development/Debug
  Requires: kernel-debuginfo-common-aarch64 = 6.15.10-402.asahi
  AutoReqProv: no
  %description -n libperf-debuginfo
  This package provides debug information for the libperf package.

  %package -n kernel-tools
  Summary: Assortment of tools for the Linux kernel

  Provides:  cpupowerutils = 1:009-0.6.p1
  Obsoletes: cpupowerutils < 1:009-0.6.p1
  Provides:  cpufreq-utils = 1:009-0.6.p1
  Provides:  cpufrequtils = 1:009-0.6.p1
  Obsoletes: cpufreq-utils < 1:009-0.6.p1
  Obsoletes: cpufrequtils < 1:009-0.6.p1
  Obsoletes: cpuspeed < 1:1.5-16
  Requires: kernel-tools-libs = 6.15.10-402.asahi

  %description -n kernel-tools
  This package contains the tools/ directory from the kernel source
  and the supporting documentation.

  %package -n kernel-tools-libs
  Summary: Libraries for the kernels-tools
  %description -n kernel-tools-libs
  This package contains the libraries built from the tools/ directory
  from the kernel source.

  %package -n kernel-tools-libs-devel
  Summary: Assortment of tools for the Linux kernel
  Requires: kernel-tools = 6.15.10-402.asahi

  Provides:  cpupowerutils-devel = 1:009-0.6.p1
  Obsoletes: cpupowerutils-devel < 1:009-0.6.p1

  Requires: kernel-tools-libs = 6.15.10-402.asahi
  Provides: kernel-tools-devel
  %description -n kernel-tools-libs-devel
  This package contains the development files for the tools/ directory from
  the kernel source.

  %package -n kernel-tools-debuginfo
  Summary: Debug information for package kernel-tools
  Requires: kernel-debuginfo-common-aarch64 = 6.15.10-402.asahi
  AutoReqProv: no
  %description -n kernel-tools-debuginfo
  This package provides debug information for package kernel-tools.

  %package -n rtla

  Summary: Real-Time Linux Analysis tools
  Requires: libtraceevent
  Requires: libtracefs
  Requires: libbpf

  Requires: kernel-tools-libs = 6.15.10-402.asahi

  %description -n rtla
  The rtla meta-tool includes a set of commands that aims to analyze
  the real-time properties of Linux. Instead of testing Linux as a black box,
  rtla leverages kernel tracing capabilities to provide precise information
  about the properties and root causes of unexpected results.

  %package -n rv
  Summary: RV: Runtime Verification
  %description -n rv
  Runtime Verification (RV) is a lightweight (yet rigorous) method that
  complements classical exhaustive verification techniques (such as model
  checking and theorem proving) with a more practical approach for
  complex systems.
  The rv tool is the interface for a collection of monitors that aim
  analysing the logical and timing behavior of Linux.

  %package selftests-internal
  Summary: Kernel samples and selftests
  Requires: binutils, bpftool, fuse-libs, iproute-tc, iputils, keyutils, nmap-ncat, python3
  %description selftests-internal
  Kernel sample programs and selftests.

  %package -n kernel-abi-stablelists
  Summary: The Red Hat Enterprise Linux kernel ABI symbol stablelists
  AutoReqProv: no
  %description -n kernel-abi-stablelists
  The kABI package contains information pertaining to the Red Hat Enterprise
  Linux kernel ABI, including lists of kernel symbols that are needed by
  external Linux kernel modules, and a yum plugin to aid enforcement.

  %package 16k-core
  Summary: The Linux kernel compiled for 16k pagesize usage
  Provides: kernel-16k-core-uname-r = 6.15.10-402.asahi.aarch64++16k
  Provides: installonlypkg(kernel)

  Provides: kernel = 6.15.10-402.asahi

  Provides: kernel-aarch64 = 6.15.10-402.asahi++16k
  Provides: kernel-uname-r = 6.15.10-402.asahi.aarch64++16k
  Requires: kernel-16k-modules-core-uname-r = 6.15.10-402.asahi.aarch64++16k
  Requires(pre): coreutils, systemd >= 203-2, /usr/bin/kernel-install
  Requires(pre): dracut >= 027
  Requires(pre): ((linux-firmware >= 20150904-56.git6ebf5d57) if linux-firmware)
  Recommends: linux-firmware
  Requires(preun): systemd >= 200
  Conflicts: xfsprogs < 4.3.0-1
  Conflicts: xorg-x11-drv-vmmouse < 13.0.99

  AutoReq: no
  AutoProv: yes

  %package 16k
  summary: kernel meta-package for the 16k kernel
  Requires: kernel-16k-core-uname-r = 6.15.10-402.asahi.aarch64+16k
  Requires: kernel-16k-modules-uname-r = 6.15.10-402.asahi.aarch64+16k
  Requires: kernel-16k-modules-core-uname-r = 6.15.10-402.asahi.aarch64+16k
  Requires: ((kernel-16k-modules-extra-uname-r = 6.15.10-402.asahi.aarch64+16k) if kernel-modules-extra-matched)

  Provides: installonlypkg(kernel)
  %description 16k
  The meta-package for the 16k kernel

  %package 16k-devel
  Summary: Development package for building kernel modules to match the kernel
  Provides: kernel-16k-devel-aarch64 = 6.15.10-402.asahi
  Provides: kernel-devel-aarch64 = 6.15.10-402.asahi++16k
  Provides: kernel-devel-uname-r = 6.15.10-402.asahi.aarch64++16k
  Provides: installonlypkg(kernel)
  AutoReqProv: no
  Requires(pre): findutils
  Requires: findutils
  Requires: perl-interpreter
  Requires: openssl-devel
  Requires: elfutils-libelf-devel
  Requires: bison
  Requires: flex
  Requires: make
  Requires: gcc

  %description 16k-devel
  This package provides kernel headers and makefiles sufficient to build modules
  against the kernel package.

  %package 16k-devel-matched
  Summary: Meta package to install matching core and devel packages for a given kernel
  Requires: kernel-16k-devel = 6.15.10-402.asahi
  Requires: kernel-16k-core = 6.15.10-402.asahi
  %description 16k-devel-matched
  This meta package is used to install matching core and devel packages for a given kernel.

  %package 16k-modules
  Summary: kernel modules to match the core kernel
  Provides: kernel-16k-modules-aarch64 = 6.15.10-402.asahi
  Provides: kernel-modules-aarch64 = 6.15.10-402.asahi++16k
  Provides: kernel-modules = 6.15.10-402.asahi++16k
  Provides: installonlypkg(kernel-module)
  Provides: kernel-16k-modules-uname-r = 6.15.10-402.asahi.aarch64++16k
  Requires: kernel-uname-r = 6.15.10-402.asahi.aarch64++16k
  Requires: kernel-16k-modules-core-uname-r = 6.15.10-402.asahi.aarch64++16k

  AutoReq: no
  AutoProv: yes
  %description 16k-modules
  This package provides commonly used kernel modules for the core kernel package.

  %package 16k-modules-core
  Summary: Core kernel modules to match the core kernel
  Provides: kernel-16k-modules-core-aarch64 = 6.15.10-402.asahi
  Provides: kernel-modules-core-aarch64 = 6.15.10-402.asahi++16k
  Provides: kernel-modules-core = 6.15.10-402.asahi++16k
  Provides: installonlypkg(kernel-module)
  Provides: kernel-16k-modules-core-uname-r = 6.15.10-402.asahi.aarch64++16k
  Requires: kernel-uname-r = 6.15.10-402.asahi.aarch64++16k

  AutoReq: no
  AutoProv: yes
  %description 16k-modules-core
  This package provides essential kernel modules for the core kernel package.

  %package 16k-modules-extra
  Summary: Extra kernel modules to match the kernel
  Provides: kernel-16k-modules-extra-aarch64 = 6.15.10-402.asahi
  Provides: kernel-16k-modules-extra-aarch64 = 6.15.10-402.asahi++16k
  Provides: kernel-16k-modules-extra = 6.15.10-402.asahi++16k
  Provides: installonlypkg(kernel-module)
  Provides: kernel-16k-modules-extra-uname-r = 6.15.10-402.asahi.aarch64++16k
  Requires: kernel-uname-r = 6.15.10-402.asahi.aarch64++16k
  Requires: kernel-16k-modules-uname-r = 6.15.10-402.asahi.aarch64++16k
  Requires: kernel-16k-modules-core-uname-r = 6.15.10-402.asahi.aarch64++16k

  AutoReq: no
  AutoProv: yes
  %description 16k-modules-extra
  This package provides less commonly used kernel modules for the kernel package.

  %package 16k-modules-internal
  Summary: Extra kernel modules to match the kernel
  Group: System Environment/Kernel
  Provides: kernel-16k-modules-internal-aarch64 = 6.15.10-402.asahi
  Provides: kernel-16k-modules-internal-aarch64 = 6.15.10-402.asahi++16k
  Provides: kernel-16k-modules-internal = 6.15.10-402.asahi++16k
  Provides: installonlypkg(kernel-module)
  Provides: kernel-16k-modules-internal-uname-r = 6.15.10-402.asahi.aarch64++16k
  Requires: kernel-uname-r = 6.15.10-402.asahi.aarch64++16k
  Requires: kernel-16k-modules-uname-r = 6.15.10-402.asahi.aarch64++16k
  Requires: kernel-16k-modules-core-uname-r = 6.15.10-402.asahi.aarch64++16k
  AutoReq: no
  AutoProv: yes
  %description 16k-modules-internal
  This package provides kernel modules for the kernel package for Red Hat internal usage.

  %package 16k-debuginfo
  Summary: Debug information for package kernel-16k
  Requires: kernel-debuginfo-common-aarch64 = 6.15.10-402.asahi
  Provides: kernel-16k-debuginfo-aarch64 = 6.15.10-402.asahi
  Provides: installonlypkg(kernel)
  AutoReqProv: no
  %description 16k-debuginfo
  This package provides debug information for package kernel-16k.
  This is required to use SystemTap with kernel-16k-6.15.10-402.asahi.aarch64.

  %package 16k-uki-virt
  Summary: The Linux kernel compiled for 16k pagesize usage unified kernel image for virtual machines
  Provides: installonlypkg(kernel)
  Provides: kernel-uname-r = 6.15.10-402.asahi.aarch64++16k
  Requires: kernel-16k-modules-core-uname-r = 6.15.10-402.asahi.aarch64++16k
  Requires(pre): coreutils, systemd >= 203-2, /usr/bin/kernel-install
  Requires(pre): systemd >= 254-1
  Recommends: uki-direct
  %package 16k-uki-virt-addons
  Summary: The Linux kernel compiled for 16k pagesize usage unified kernel image addons for virtual machines
  Provides: installonlypkg(kernel)
  Requires: kernel-16k-uki-virt = 6.15.10-402.asahi
  Requires(pre): systemd >= 254-1

  %description 16k-core
  The kernel package contains a variant of the ARM64 Linux kernel using
  a 16K page size.

  %package 16k-debug-core
  Summary: The Linux kernel compiled with extra debugging enabled
  Provides: kernel-16k-debug-core-uname-r = 6.15.10-402.asahi.aarch64++16k_debug
  Provides: installonlypkg(kernel)

  Provides: kernel = 6.15.10-402.asahi

  Provides: kernel-aarch64 = 6.15.10-402.asahi++16k_debug
  Provides: kernel-uname-r = 6.15.10-402.asahi.aarch64++16k_debug
  Requires: kernel-16k-debug-modules-core-uname-r = 6.15.10-402.asahi.aarch64++16k_debug
  Requires(pre): coreutils, systemd >= 203-2, /usr/bin/kernel-install
  Requires(pre): dracut >= 027
  Requires(pre): ((linux-firmware >= 20150904-56.git6ebf5d57) if linux-firmware)
  Recommends: linux-firmware
  Requires(preun): systemd >= 200
  Conflicts: xfsprogs < 4.3.0-1
  Conflicts: xorg-x11-drv-vmmouse < 13.0.99

  AutoReq: no
  AutoProv: yes

  %package 16k-debug
  summary: kernel meta-package for the 16k-debug kernel
  Requires: kernel-16k-debug-core-uname-r = 6.15.10-402.asahi.aarch64+16k_debug
  Requires: kernel-16k-debug-modules-uname-r = 6.15.10-402.asahi.aarch64+16k_debug
  Requires: kernel-16k-debug-modules-core-uname-r = 6.15.10-402.asahi.aarch64+16k_debug
  Requires: ((kernel-16k-debug-modules-extra-uname-r = 6.15.10-402.asahi.aarch64+16k_debug) if kernel-modules-extra-matched)

  Provides: installonlypkg(kernel)
  %description 16k-debug
  The meta-package for the 16k-debug kernel

  %package 16k-debug-devel
  Summary: Development package for building kernel modules to match the kernel
  Provides: kernel-16k-debug-devel-aarch64 = 6.15.10-402.asahi
  Provides: kernel-devel-aarch64 = 6.15.10-402.asahi++16k_debug
  Provides: kernel-devel-uname-r = 6.15.10-402.asahi.aarch64++16k_debug
  Provides: installonlypkg(kernel)
  AutoReqProv: no
  Requires(pre): findutils
  Requires: findutils
  Requires: perl-interpreter
  Requires: openssl-devel
  Requires: elfutils-libelf-devel
  Requires: bison
  Requires: flex
  Requires: make
  Requires: gcc

  %description 16k-debug-devel
  This package provides kernel headers and makefiles sufficient to build modules
  against the kernel package.

  %package 16k-debug-devel-matched
  Summary: Meta package to install matching core and devel packages for a given kernel
  Requires: kernel-16k-debug-devel = 6.15.10-402.asahi
  Requires: kernel-16k-debug-core = 6.15.10-402.asahi
  %description 16k-debug-devel-matched
  This meta package is used to install matching core and devel packages for a given kernel.

  %package 16k-debug-modules
  Summary: kernel modules to match the core kernel
  Provides: kernel-16k-debug-modules-aarch64 = 6.15.10-402.asahi
  Provides: kernel-modules-aarch64 = 6.15.10-402.asahi++16k_debug
  Provides: kernel-modules = 6.15.10-402.asahi++16k_debug
  Provides: installonlypkg(kernel-module)
  Provides: kernel-16k-debug-modules-uname-r = 6.15.10-402.asahi.aarch64++16k_debug
  Requires: kernel-uname-r = 6.15.10-402.asahi.aarch64++16k_debug
  Requires: kernel-16k-debug-modules-core-uname-r = 6.15.10-402.asahi.aarch64++16k_debug

  AutoReq: no
  AutoProv: yes
  %description 16k-debug-modules
  This package provides commonly used kernel modules for the core kernel package.

  %package 16k-debug-modules-core
  Summary: Core kernel modules to match the core kernel
  Provides: kernel-16k-debug-modules-core-aarch64 = 6.15.10-402.asahi
  Provides: kernel-modules-core-aarch64 = 6.15.10-402.asahi++16k_debug
  Provides: kernel-modules-core = 6.15.10-402.asahi++16k_debug
  Provides: installonlypkg(kernel-module)
  Provides: kernel-16k-debug-modules-core-uname-r = 6.15.10-402.asahi.aarch64++16k_debug
  Requires: kernel-uname-r = 6.15.10-402.asahi.aarch64++16k_debug

  AutoReq: no
  AutoProv: yes
  %description 16k-debug-modules-core
  This package provides essential kernel modules for the core kernel package.

  %package 16k-debug-modules-extra
  Summary: Extra kernel modules to match the kernel
  Provides: kernel-16k-debug-modules-extra-aarch64 = 6.15.10-402.asahi
  Provides: kernel-16k-debug-modules-extra-aarch64 = 6.15.10-402.asahi++16k_debug
  Provides: kernel-16k-debug-modules-extra = 6.15.10-402.asahi++16k_debug
  Provides: installonlypkg(kernel-module)
  Provides: kernel-16k-debug-modules-extra-uname-r = 6.15.10-402.asahi.aarch64++16k_debug
  Requires: kernel-uname-r = 6.15.10-402.asahi.aarch64++16k_debug
  Requires: kernel-16k-debug-modules-uname-r = 6.15.10-402.asahi.aarch64++16k_debug
  Requires: kernel-16k-debug-modules-core-uname-r = 6.15.10-402.asahi.aarch64++16k_debug

  AutoReq: no
  AutoProv: yes
  %description 16k-debug-modules-extra
  This package provides less commonly used kernel modules for the kernel package.

  %package 16k-debug-modules-internal
  Summary: Extra kernel modules to match the kernel
  Group: System Environment/Kernel
  Provides: kernel-16k-debug-modules-internal-aarch64 = 6.15.10-402.asahi
  Provides: kernel-16k-debug-modules-internal-aarch64 = 6.15.10-402.asahi++16k_debug
  Provides: kernel-16k-debug-modules-internal = 6.15.10-402.asahi++16k_debug
  Provides: installonlypkg(kernel-module)
  Provides: kernel-16k-debug-modules-internal-uname-r = 6.15.10-402.asahi.aarch64++16k_debug
  Requires: kernel-uname-r = 6.15.10-402.asahi.aarch64++16k_debug
  Requires: kernel-16k-debug-modules-uname-r = 6.15.10-402.asahi.aarch64++16k_debug
  Requires: kernel-16k-debug-modules-core-uname-r = 6.15.10-402.asahi.aarch64++16k_debug
  AutoReq: no
  AutoProv: yes
  %description 16k-debug-modules-internal
  This package provides kernel modules for the kernel package for Red Hat internal usage.

  %package 16k-debug-debuginfo
  Summary: Debug information for package kernel-16k-debug
  Requires: kernel-debuginfo-common-aarch64 = 6.15.10-402.asahi
  Provides: kernel-16k-debug-debuginfo-aarch64 = 6.15.10-402.asahi
  Provides: installonlypkg(kernel)
  AutoReqProv: no
  %description 16k-debug-debuginfo
  This package provides debug information for package kernel-16k-debug.
  This is required to use SystemTap with kernel-16k-debug-6.15.10-402.asahi.aarch64.

  %package 16k-debug-uki-virt
  Summary: The Linux kernel compiled with extra debugging enabled unified kernel image for virtual machines
  Provides: installonlypkg(kernel)
  Provides: kernel-uname-r = 6.15.10-402.asahi.aarch64++16k_debug
  Requires: kernel-16k-debug-modules-core-uname-r = 6.15.10-402.asahi.aarch64++16k_debug
  Requires(pre): coreutils, systemd >= 203-2, /usr/bin/kernel-install
  Requires(pre): systemd >= 254-1
  Recommends: uki-direct
  %package 16k-debug-uki-virt-addons
  Summary: The Linux kernel compiled with extra debugging enabled unified kernel image addons for virtual machines
  Provides: installonlypkg(kernel)
  Requires: kernel-16k-debug-uki-virt = 6.15.10-402.asahi
  Requires(pre): systemd >= 254-1

  %description 16k-debug-core
  The debug kernel package contains a variant of the ARM64 Linux kernel using
  a 16K page size.
  This variant of the kernel has numerous debugging options enabled.
  It should only be installed when trying to gather additional information
  on kernel bugs, as some of these options impact performance noticably.

  %package debug-core
  Summary: The Linux kernel compiled with extra debugging enabled
  Provides: kernel-debug-core-uname-r = 6.15.10-402.asahi.aarch64++debug
  Provides: installonlypkg(kernel)

  Provides: kernel = 6.15.10-402.asahi

  Provides: kernel-aarch64 = 6.15.10-402.asahi++debug
  Provides: kernel-uname-r = 6.15.10-402.asahi.aarch64++debug
  Requires: kernel-debug-modules-core-uname-r = 6.15.10-402.asahi.aarch64++debug
  Requires(pre): coreutils, systemd >= 203-2, /usr/bin/kernel-install
  Requires(pre): dracut >= 027
  Requires(pre): ((linux-firmware >= 20150904-56.git6ebf5d57) if linux-firmware)
  Recommends: linux-firmware
  Requires(preun): systemd >= 200
  Conflicts: xfsprogs < 4.3.0-1
  Conflicts: xorg-x11-drv-vmmouse < 13.0.99

  AutoReq: no
  AutoProv: yes

  %package debug
  summary: kernel meta-package for the debug kernel
  Requires: kernel-debug-core-uname-r = 6.15.10-402.asahi.aarch64+debug
  Requires: kernel-debug-modules-uname-r = 6.15.10-402.asahi.aarch64+debug
  Requires: kernel-debug-modules-core-uname-r = 6.15.10-402.asahi.aarch64+debug
  Requires: ((kernel-debug-modules-extra-uname-r = 6.15.10-402.asahi.aarch64+debug) if kernel-modules-extra-matched)

  Provides: installonlypkg(kernel)
  %description debug
  The meta-package for the debug kernel

  %package debug-devel
  Summary: Development package for building kernel modules to match the kernel
  Provides: kernel-debug-devel-aarch64 = 6.15.10-402.asahi
  Provides: kernel-devel-aarch64 = 6.15.10-402.asahi++debug
  Provides: kernel-devel-uname-r = 6.15.10-402.asahi.aarch64++debug
  Provides: installonlypkg(kernel)
  AutoReqProv: no
  Requires(pre): findutils
  Requires: findutils
  Requires: perl-interpreter
  Requires: openssl-devel
  Requires: elfutils-libelf-devel
  Requires: bison
  Requires: flex
  Requires: make
  Requires: gcc

  %description debug-devel
  This package provides kernel headers and makefiles sufficient to build modules
  against the kernel package.

  %package debug-devel-matched
  Summary: Meta package to install matching core and devel packages for a given kernel
  Requires: kernel-debug-devel = 6.15.10-402.asahi
  Requires: kernel-debug-core = 6.15.10-402.asahi
  %description debug-devel-matched
  This meta package is used to install matching core and devel packages for a given kernel.

  %package debug-modules
  Summary: kernel modules to match the core kernel
  Provides: kernel-debug-modules-aarch64 = 6.15.10-402.asahi
  Provides: kernel-modules-aarch64 = 6.15.10-402.asahi++debug
  Provides: kernel-modules = 6.15.10-402.asahi++debug
  Provides: installonlypkg(kernel-module)
  Provides: kernel-debug-modules-uname-r = 6.15.10-402.asahi.aarch64++debug
  Requires: kernel-uname-r = 6.15.10-402.asahi.aarch64++debug
  Requires: kernel-debug-modules-core-uname-r = 6.15.10-402.asahi.aarch64++debug

  AutoReq: no
  AutoProv: yes
  %description debug-modules
  This package provides commonly used kernel modules for the core kernel package.

  %package debug-modules-core
  Summary: Core kernel modules to match the core kernel
  Provides: kernel-debug-modules-core-aarch64 = 6.15.10-402.asahi
  Provides: kernel-modules-core-aarch64 = 6.15.10-402.asahi++debug
  Provides: kernel-modules-core = 6.15.10-402.asahi++debug
  Provides: installonlypkg(kernel-module)
  Provides: kernel-debug-modules-core-uname-r = 6.15.10-402.asahi.aarch64++debug
  Requires: kernel-uname-r = 6.15.10-402.asahi.aarch64++debug

  AutoReq: no
  AutoProv: yes
  %description debug-modules-core
  This package provides essential kernel modules for the core kernel package.

  %package debug-modules-extra
  Summary: Extra kernel modules to match the kernel
  Provides: kernel-debug-modules-extra-aarch64 = 6.15.10-402.asahi
  Provides: kernel-debug-modules-extra-aarch64 = 6.15.10-402.asahi++debug
  Provides: kernel-debug-modules-extra = 6.15.10-402.asahi++debug
  Provides: installonlypkg(kernel-module)
  Provides: kernel-debug-modules-extra-uname-r = 6.15.10-402.asahi.aarch64++debug
  Requires: kernel-uname-r = 6.15.10-402.asahi.aarch64++debug
  Requires: kernel-debug-modules-uname-r = 6.15.10-402.asahi.aarch64++debug
  Requires: kernel-debug-modules-core-uname-r = 6.15.10-402.asahi.aarch64++debug

  AutoReq: no
  AutoProv: yes
  %description debug-modules-extra
  This package provides less commonly used kernel modules for the kernel package.

  %package debug-modules-internal
  Summary: Extra kernel modules to match the kernel
  Group: System Environment/Kernel
  Provides: kernel-debug-modules-internal-aarch64 = 6.15.10-402.asahi
  Provides: kernel-debug-modules-internal-aarch64 = 6.15.10-402.asahi++debug
  Provides: kernel-debug-modules-internal = 6.15.10-402.asahi++debug
  Provides: installonlypkg(kernel-module)
  Provides: kernel-debug-modules-internal-uname-r = 6.15.10-402.asahi.aarch64++debug
  Requires: kernel-uname-r = 6.15.10-402.asahi.aarch64++debug
  Requires: kernel-debug-modules-uname-r = 6.15.10-402.asahi.aarch64++debug
  Requires: kernel-debug-modules-core-uname-r = 6.15.10-402.asahi.aarch64++debug
  AutoReq: no
  AutoProv: yes
  %description debug-modules-internal
  This package provides kernel modules for the kernel package for Red Hat internal usage.

  %package debug-debuginfo
  Summary: Debug information for package kernel-debug
  Requires: kernel-debuginfo-common-aarch64 = 6.15.10-402.asahi
  Provides: kernel-debug-debuginfo-aarch64 = 6.15.10-402.asahi
  Provides: installonlypkg(kernel)
  AutoReqProv: no
  %description debug-debuginfo
  This package provides debug information for package kernel-debug.
  This is required to use SystemTap with kernel-debug-6.15.10-402.asahi.aarch64.

  %package debug-uki-virt
  Summary: The Linux kernel compiled with extra debugging enabled unified kernel image for virtual machines
  Provides: installonlypkg(kernel)
  Provides: kernel-uname-r = 6.15.10-402.asahi.aarch64++debug
  Requires: kernel-debug-modules-core-uname-r = 6.15.10-402.asahi.aarch64++debug
  Requires(pre): coreutils, systemd >= 203-2, /usr/bin/kernel-install
  Requires(pre): systemd >= 254-1
  Recommends: uki-direct
  %package debug-uki-virt-addons
  Summary: The Linux kernel compiled with extra debugging enabled unified kernel image addons for virtual machines
  Provides: installonlypkg(kernel)
  Requires: kernel-debug-uki-virt = 6.15.10-402.asahi
  Requires(pre): systemd >= 254-1

  %description debug-core
  The kernel package contains the Linux kernel (vmlinuz), the core of any
  Linux operating system.  The kernel handles the basic functions
  of the operating system:  memory allocation, process allocation, device
  input and output, etc.

  This variant of the kernel has numerous debugging options enabled.
  It should only be installed when trying to gather additional information
  on kernel bugs, as some of these options impact performance noticably.

  %package core
  Summary: The Linux kernel
  Provides: kernel-core-uname-r = 6.15.10-402.asahi.aarch64
  Provides: installonlypkg(kernel)

  Provides: kernel = 6.15.10-402.asahi

  Provides: kernel-aarch64 = 6.15.10-402.asahi
  Provides: kernel-uname-r = 6.15.10-402.asahi.aarch64
  Requires: kernel-modules-core-uname-r = 6.15.10-402.asahi.aarch64
  Requires(pre): coreutils, systemd >= 203-2, /usr/bin/kernel-install
  Requires(pre): dracut >= 027
  Requires(pre): ((linux-firmware >= 20150904-56.git6ebf5d57) if linux-firmware)
  Recommends: linux-firmware
  Requires(preun): systemd >= 200
  Conflicts: xfsprogs < 4.3.0-1
  Conflicts: xorg-x11-drv-vmmouse < 13.0.99

  AutoReq: no
  AutoProv: yes

  %package devel
  Summary: Development package for building kernel modules to match the kernel
  Provides: kernel-devel-aarch64 = 6.15.10-402.asahi
  Provides: kernel-devel-aarch64 = 6.15.10-402.asahi
  Provides: kernel-devel-uname-r = 6.15.10-402.asahi.aarch64
  Provides: installonlypkg(kernel)
  AutoReqProv: no
  Requires(pre): findutils
  Requires: findutils
  Requires: perl-interpreter
  Requires: openssl-devel
  Requires: elfutils-libelf-devel
  Requires: bison
  Requires: flex
  Requires: make
  Requires: gcc

  %description devel
  This package provides kernel headers and makefiles sufficient to build modules
  against the kernel package.

  %package devel-matched
  Summary: Meta package to install matching core and devel packages for a given kernel
  Requires: kernel-devel = 6.15.10-402.asahi
  Requires: kernel-core = 6.15.10-402.asahi
  %description devel-matched
  This meta package is used to install matching core and devel packages for a given kernel.

  %package modules
  Summary: kernel modules to match the core kernel
  Provides: kernel-modules-aarch64 = 6.15.10-402.asahi
  Provides: kernel-modules-aarch64 = 6.15.10-402.asahi
  Provides: kernel-modules = 6.15.10-402.asahi
  Provides: installonlypkg(kernel-module)
  Provides: kernel-modules-uname-r = 6.15.10-402.asahi.aarch64
  Requires: kernel-uname-r = 6.15.10-402.asahi.aarch64
  Requires: kernel-modules-core-uname-r = 6.15.10-402.asahi.aarch64

  AutoReq: no
  AutoProv: yes
  %description modules
  This package provides commonly used kernel modules for the core kernel package.

  %package modules-core
  Summary: Core kernel modules to match the core kernel
  Provides: kernel-modules-core-aarch64 = 6.15.10-402.asahi
  Provides: kernel-modules-core-aarch64 = 6.15.10-402.asahi
  Provides: kernel-modules-core = 6.15.10-402.asahi
  Provides: installonlypkg(kernel-module)
  Provides: kernel-modules-core-uname-r = 6.15.10-402.asahi.aarch64
  Requires: kernel-uname-r = 6.15.10-402.asahi.aarch64

  AutoReq: no
  AutoProv: yes
  %description modules-core
  This package provides essential kernel modules for the core kernel package.

  %package modules-extra
  Summary: Extra kernel modules to match the kernel
  Provides: kernel-modules-extra-aarch64 = 6.15.10-402.asahi
  Provides: kernel-modules-extra-aarch64 = 6.15.10-402.asahi
  Provides: kernel-modules-extra = 6.15.10-402.asahi
  Provides: installonlypkg(kernel-module)
  Provides: kernel-modules-extra-uname-r = 6.15.10-402.asahi.aarch64
  Requires: kernel-uname-r = 6.15.10-402.asahi.aarch64
  Requires: kernel-modules-uname-r = 6.15.10-402.asahi.aarch64
  Requires: kernel-modules-core-uname-r = 6.15.10-402.asahi.aarch64

  AutoReq: no
  AutoProv: yes
  %description modules-extra
  This package provides less commonly used kernel modules for the kernel package.

  %package modules-internal
  Summary: Extra kernel modules to match the kernel
  Group: System Environment/Kernel
  Provides: kernel-modules-internal-aarch64 = 6.15.10-402.asahi
  Provides: kernel-modules-internal-aarch64 = 6.15.10-402.asahi
  Provides: kernel-modules-internal = 6.15.10-402.asahi
  Provides: installonlypkg(kernel-module)
  Provides: kernel-modules-internal-uname-r = 6.15.10-402.asahi.aarch64
  Requires: kernel-uname-r = 6.15.10-402.asahi.aarch64
  Requires: kernel-modules-uname-r = 6.15.10-402.asahi.aarch64
  Requires: kernel-modules-core-uname-r = 6.15.10-402.asahi.aarch64
  AutoReq: no
  AutoProv: yes
  %description modules-internal
  This package provides kernel modules for the kernel package for Red Hat internal usage.

  %package debuginfo
  Summary: Debug information for package kernel
  Requires: kernel-debuginfo-common-aarch64 = 6.15.10-402.asahi
  Provides: kernel-debuginfo-aarch64 = 6.15.10-402.asahi
  Provides: installonlypkg(kernel)
  AutoReqProv: no
  %description debuginfo
  This package provides debug information for package kernel.
  This is required to use SystemTap with kernel-6.15.10-402.asahi.aarch64.

  %package uki-virt
  Summary: The Linux kernel unified kernel image for virtual machines
  Provides: installonlypkg(kernel)
  Provides: kernel-uname-r = 6.15.10-402.asahi.aarch64
  Requires: kernel-modules-core-uname-r = 6.15.10-402.asahi.aarch64
  Requires(pre): coreutils, systemd >= 203-2, /usr/bin/kernel-install
  Requires(pre): systemd >= 254-1
  Recommends: uki-direct
  %package uki-virt-addons
  Summary: The Linux kernel unified kernel image addons for virtual machines
  Provides: installonlypkg(kernel)
  Requires: kernel-uki-virt = 6.15.10-402.asahi
  Requires(pre): systemd >= 254-1

  %description core
  The kernel package contains the Linux kernel (vmlinuz), the core of any
  Linux operating system.  The kernel handles the basic functions
  of the operating system: memory allocation, process allocation, device
  input and output, etc.

  %description debug-uki-virt
  Prebuilt debug unified kernel image for virtual machines.

  %description debug-uki-virt-addons
  Prebuilt debug unified kernel image addons for virtual machines.

  %description uki-virt
  Prebuilt default unified kernel image for virtual machines.

  %description uki-virt-addons
  Prebuilt default unified kernel image addons for virtual machines.

  %description 16k-debug-uki-virt
  Prebuilt 16k debug unified kernel image for virtual machines.

  %description 16k-debug-uki-virt-addons
  Prebuilt 16k debug unified kernel image addons for virtual machines.

  %description 16k-uki-virt
  Prebuilt 16k unified kernel image for virtual machines.

  %description 16k-uki-virt-addons
  Prebuilt 16k unified kernel image addons for virtual machines.

  %package modules-extra-matched
  Summary: Meta package which requires modules-extra to be installed for all kernels.
  %description modules-extra-matched
  This meta package provides a single reference that other packages can Require to have modules-extra installed for all kernels.

prepare() {

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Start of prep stage" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Start of prep stage"" 
  	set -x

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Sanity checks" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Sanity checks"" 
  	set -x

  # do a few sanity-checks for --with *only builds

  # more sanity checking; do it quietly
  if [ "'patch-6.15-redhat.patch' 'linux-kernel-test.patch' " != "%{patches}" ] ; then
    for patch in 'patch-6.15-redhat.patch' 'linux-kernel-test.patch'  ; do
      if [ ! -f $patch ] ; then

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "ERROR: Patch ${patch##/*/} listed in specfile but is missing" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "ERROR: Patch ${patch##/*/} listed in specfile but is missing"" 
  	set -x
        exit 1
      fi
    done
  fi 2>/dev/null

  patch_command='git --work-tree=. apply'
  ApplyPatch()
  {
    local patch=$1
    shift
    if [ ! -f $RPM_SOURCE_DIR/$patch ]; then
      exit 1
    fi
    if ! grep -E "^Patch[0-9]+: $patch\$" /SPECS/${RPM_PACKAGE_NAME}.spec ; then
      if [ "${patch:0:8}" != "patch-6." ] ; then

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "ERROR: Patch $patch not listed as a source patch in specfile" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "ERROR: Patch $patch not listed as a source patch in specfile"" 
  	set -x
        exit 1
      fi
    fi 2>/dev/null
    case "$patch" in
    *.bz2) bunzip2 < "$RPM_SOURCE_DIR/$patch" | $patch_command ${1+"$@"} ;;
    *.gz)  gunzip  < "$RPM_SOURCE_DIR/$patch" | $patch_command ${1+"$@"} ;;
    *.xz)  unxz    < "$RPM_SOURCE_DIR/$patch" | $patch_command ${1+"$@"} ;;
    *) $patch_command ${1+"$@"} < "$RPM_SOURCE_DIR/$patch" ;;
    esac
  }

  # don't apply patch if it's empty
  ApplyOptionalPatch()
  {
    local patch=$1
    shift

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "ApplyOptionalPatch: $1" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "ApplyOptionalPatch: $1"" 
  	set -x
    if [ ! -f $RPM_SOURCE_DIR/$patch ]; then
      exit 1
    fi
    local C=$(wc -l $RPM_SOURCE_DIR/$patch | awk '{print $1}')
    if [ "$C" -gt 9 ]; then
      ApplyPatch $patch ${1+"$@"}
    fi
  }

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Untar kernel tarball" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Untar kernel tarball"" 
  	set -x
  cd './'
  rm -rf 'kernel-6.15.10'
  mkdir -p 'kernel-6.15.10'
  cd 'kernel-6.15.10'
  tar -xf 'linux-6.15.10.tar.xz'
  STATUS=$?
  if [ $STATUS -ne 0 ]; then
    exit $STATUS
  fi
  chmod -Rf a+rX,u+w,g-w,o-w .

  mv linux-6.15.10 linux-6.15.10-402.asahi.aarch64

  cd linux-6.15.10-402.asahi.aarch64
  cp -a Makefile.rhelver .

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Start of patch applications" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Start of patch applications"" 
  	set -x

  ApplyOptionalPatch patch-6.15-redhat.patch

  ApplyOptionalPatch linux-kernel-test.patch

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "End of patch applications" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "End of patch applications"" 
  	set -x
  # END OF PATCH APPLICATIONS

  # Any further pre-build tree manipulations happen here.

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Pre-build tree manipulations" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Pre-build tree manipulations"" 
  	set -x
  chmod +x scripts/checkpatch.pl
  mv COPYING COPYING-6.15.10-402.asahi

  # on linux-next prevent scripts/setlocalversion from mucking with our version numbers
  rm -f localversion-next localversion-rt

  # Mangle /usr/bin/python shebangs to /usr/bin/python3
  # Mangle all Python shebangs to be Python 3 explicitly
  # -p preserves timestamps
  # -n prevents creating ~backup files
  # -i specifies the interpreter for the shebang
  # This fixes errors such as
  # *** ERROR: ambiguous python shebang in /usr/bin/kvm_stat: #!/usr/bin/python. Change it to python3 (or python2) explicitly.
  # We patch all sources below for which we got a report/error.

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Fixing Python shebangs..." /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Fixing Python shebangs..."" 
  	set -x
  %py3_shebang_fix \
  	tools/kvm/kvm_stat/kvm_stat \
  	scripts/show_delta \
  	scripts/diffconfig \
  	scripts/bloat-o-meter \
  	scripts/jobserver-exec \
  	tools \
  	Documentation \
  	scripts/clang-tools 2> /dev/null

  # only deal with configs if we are going to build for the arch

  if [ -L configs ]; then
  	rm -f configs
  fi
  mkdir configs
  cd configs

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Copy additional source files into buildroot" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Copy additional source files into buildroot"" 
  	set -x
  # Drop some necessary files from the source dir into the buildroot
  cp $RPM_SOURCE_DIR/kernel-*.config .
  cp generate_all_configs.sh .
  # merge.py
  cp merge.py .
  # kernel-local - rename and copy for partial snippet config process
  cp kernel-local partial-kernel-local-snip.config
  cp kernel-local partial-kernel-local-debug-snip.config
  FLAVOR=fedora SPECPACKAGE_NAME=kernel SPECVERSION=6.15.10 SPECRPMVERSION=6.15.10 ./generate_all_configs.sh 1

  # Collect custom defined config options

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Collect custom defined config options" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Collect custom defined config options"" 
  	set -x
  PARTIAL_CONFIGS=""
  PARTIAL_CONFIGS="$PARTIAL_CONFIGS partial-kernel-local-snip.config partial-kernel-local-debug-snip.config"

  GetArch()
  {
    case "$1" in
    *aarch64*) echo "aarch64" ;;
    *ppc64le*) echo "ppc64le" ;;
    *s390x*) echo "s390x" ;;
    *x86_64*) echo "x86_64" ;;
    *riscv64*) echo "riscv64" ;;
    # no arch, apply everywhere
    *) echo "" ;;
    esac
  }

  # Merge in any user-provided local config option changes

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Merge in any user-provided local config option changes" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Merge in any user-provided local config option changes"" 
  	set -x
  for i in kernel-6.15.10-*.config
  do
    kern_arch="$(GetArch $i)"
    kern_debug="$(echo $i | grep -q debug && echo "debug" || echo "")"

    for j in $PARTIAL_CONFIGS
    do
      part_arch="$(GetArch $j)"
      part_debug="$(echo $j | grep -q debug && echo "debug" || echo "")"

      # empty arch means apply to all arches
      if [ "$part_arch" == "" -o "$part_arch" == "$kern_arch" ] && [ "$part_debug" == "$kern_debug" ]
      then
        mv $i $i.tmp
        ./merge.py $j $i.tmp > $i
      fi
    done
    rm -f $i.tmp
  done

  # Add DUP and kpatch certificates to system trusted keys for RHEL

  openssl x509 -inform der -in fedoraimaca.x509 -out imaca.pem
  cat imaca.pem >> ../certs/rhel.pem

  for i in *.config; do
    sed -i 's@CONFIG_SYSTEM_TRUSTED_KEYS=""@CONFIG_SYSTEM_TRUSTED_KEYS="certs/rhel.pem"@' $i
  done

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Set process_configs.sh $OPTS" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Set process_configs.sh $OPTS"" 
  	set -x
  cp process_configs.sh .
  OPTS=""
  	OPTS="$OPTS -w -n -c"

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Generate redhat configs" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Generate redhat configs"" 
  	set -x
  RHJOBS=$RPM_BUILD_NCPUS SPECPACKAGE_NAME=kernel ./process_configs.sh $OPTS 6.15.10

  # We may want to override files from the primary target in case of building
  # against a flavour of it (eg. centos not rhel), thus override it here if
  # necessary
  update_scripts() {
  	TARGET="$1"

  	for i in "$RPM_SOURCE_DIR"/*."$TARGET"; do
  		NEW=${i%."$TARGET"}
  		cp "$i" "$(basename "$NEW")"
  	done
  }

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Set scripts/SOURCES targets" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Set scripts/SOURCES targets"" 
  	set -x
  update_target=fedora
  if [ "fedora" == "rhel" ]; then
  : # no-op to avoid empty if-fi error
  fi
  update_scripts $update_target

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "End of kernel config" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "End of kernel config"" 
  	set -x
  cd ..
  # # End of Configs stuff

  # get rid of unwanted files resulting from patch fuzz
  find . \( -name "*.orig" -o -name "*~" \) -delete >/dev/null

  # remove unnecessary SCM files
  find . -name .gitignore -delete >/dev/null

  cd ..

  ###
  ### build
  ###
}

build() {

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Start of build stage" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Start of build stage"" 
  	set -x

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "General arch build configuration" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "General arch build configuration"" 
  	set -x
  rm -rf .//root_unstripped || true
  mkdir -p .//root_unstripped

  cp_vmlinux()
  {
    eu-strip --remove-comment -o "$2" "$1"
  }

  # Note we need to disable these flags for cross builds because the flags
  # from redhat-rpm-config assume that host == target so target arch
  # flags cause issues with the host compiler.

  InitBuildVars() {

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "InitBuildVars for $1" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "InitBuildVars for $1"" 
  	set -x

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "InitBuildVars: Initialize build variables" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "InitBuildVars: Initialize build variables"" 
  	set -x
      # Initialize the kernel .config file and create some variables that are
      # needed for the actual build process.

      Variant=$1

      # Pick the right kernel config file
      Config=kernel-6.15.10-aarch64${Variant:+-${Variant}}.config
      DevelDir=/usr/src/kernels/6.15.10-402.asahi.aarch64${Variant:++${Variant}}

      KernelVer=6.15.10-402.asahi.aarch64${Variant:++${Variant}}

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "InitBuildVars: Update Makefile" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "InitBuildVars: Update Makefile"" 
  	set -x
      # make sure EXTRAVERSION says what we want it to say
      # Trim the release if this is a CI build, since KERNELVERSION is limited to 64 characters
      ShortRel=$(perl -e "print \"402.asahi\" =~ s/\.pr\.[0-9A-Fa-f]{32}//r")
      perl -p -i -e "s/^EXTRAVERSION.*/EXTRAVERSION = -${ShortRel}.aarch64${Variant:++${Variant}}/" Makefile

      # if pre-rc1 devel kernel, must fix up PATCHLEVEL for our versioning scheme
      # if we are post rc1 this should match anyway so this won't matter
      perl -p -i -e 's/^PATCHLEVEL.*/PATCHLEVEL = 15/' Makefile

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "InitBuildVars: Copy files" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "InitBuildVars: Copy files"" 
  	set -x
      /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" -j${RPM_BUILD_NCPUS} mrproper
      cp configs/$Config .config

      cp configs/x509.genkey certs/.

      Arch=`head -1 .config | cut -b 3-`

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "InitBuildVars: USING ARCH=$Arch" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "InitBuildVars: USING ARCH=$Arch"" 
  	set -x

      KCFLAGS=""
  }

  #Build bootstrap bpftool
  BuildBpftool(){
      export BPFBOOTSTRAP_CFLAGS=$(echo "%{__global_compiler_flags}" | sed -r "s/\-specs=[^\ ]+\/redhat-annobin-cc1//")
      export BPFBOOTSTRAP_LDFLAGS=$(echo "%{__global_ldflags}" | sed -r "s/\-specs=[^\ ]+\/redhat-annobin-cc1//")
      CFLAGS="" LDFLAGS="" make EXTRA_CFLAGS="${BPFBOOTSTRAP_CFLAGS}" EXTRA_CXXFLAGS="${BPFBOOTSTRAP_CFLAGS}" EXTRA_LDFLAGS="${BPFBOOTSTRAP_LDFLAGS}" V=1  V=1 -C tools/bpf/bpftool bootstrap
  }

  BuildKernel() {

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "BuildKernel for $4" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "BuildKernel for $4"" 
  	set -x
      MakeTarget=$1
      KernelImage=$2
      DoVDSO=$3
      Variant=$4
      InstallName=${5:-vmlinuz}

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Setup variables" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Setup variables"" 
  	set -x
      DoModules=1
      if [ "$Variant" = "zfcpdump" ]; then
  	    DoModules=0
      fi

      # When the bootable image is just the ELF kernel, strip it.
      # We already copy the unstripped file into the debuginfo package.
      if [ "$KernelImage" = vmlinux ]; then
        CopyKernel=cp_vmlinux
      else
        CopyKernel=cp
      fi

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Calling InitBuildVars for $Variant" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Calling InitBuildVars for $Variant"" 
  	set -x
      InitBuildVars $Variant

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "BUILDING A KERNEL FOR ${Variant} aarch64..." /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "BUILDING A KERNEL FOR ${Variant} aarch64..."" 
  	set -x

      /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" ARCH=$Arch olddefconfig >/dev/null

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Setup build-ids" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Setup build-ids"" 
  	set -x
      # This ensures build-ids are unique to allow parallel debuginfo
      perl -p -i -e "s/^CONFIG_BUILD_SALT.*/CONFIG_BUILD_SALT=\"6.15.10-402.asahi.aarch64\"/" .config
      /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" ARCH=$Arch KCFLAGS="$KCFLAGS" WITH_GCOV="0" -j${RPM_BUILD_NCPUS} $MakeTarget  
      if [ $DoModules -eq 1 ]; then
  	/usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" ARCH=$Arch KCFLAGS="$KCFLAGS" WITH_GCOV="0" -j${RPM_BUILD_NCPUS} modules  || exit 1
      fi

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Setup RPM_BUILD_ROOT directories" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Setup RPM_BUILD_ROOT directories"" 
  	set -x
      mkdir -p $RPM_BUILD_ROOT/boot
      mkdir -p $RPM_BUILD_ROOT/lib/modules/$KernelVer
      mkdir -p $RPM_BUILD_ROOT/lib/modules/$KernelVer/systemtap
      mkdir -p $RPM_BUILD_ROOT/usr/lib/debug/boot

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Build dtb kernel" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Build dtb kernel"" 
  	set -x
      /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" ARCH=$Arch dtbs INSTALL_DTBS_PATH=$RPM_BUILD_ROOT/boot/dtb-$KernelVer
      /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" ARCH=$Arch dtbs_install INSTALL_DTBS_PATH=$RPM_BUILD_ROOT/boot/dtb-$KernelVer
      cp -r $RPM_BUILD_ROOT/boot/dtb-$KernelVer $RPM_BUILD_ROOT/lib/modules/$KernelVer/dtb
      find arch/$Arch/boot/dts -name '*.dtb' -type f -delete

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Cleanup temp btf files" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Cleanup temp btf files"" 
  	set -x
      # Remove large intermediate files we no longer need to save space
      # (-f required for zfcpdump builds that do not enable BTF)
      rm -f vmlinux.o .tmp_vmlinux.btf

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Install files to RPM_BUILD_ROOT" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Install files to RPM_BUILD_ROOT"" 
  	set -x

      # Comment out specific config settings that may use resources not available
      # to the end user so that the packaged config file can be easily reused with
      # upstream make targets
        sed -i -e '/^CONFIG_SYSTEM_TRUSTED_KEYS/{
          i\# The kernel was built with
          s/^/# /
          a\# We are resetting this value to facilitate local builds
          a\CONFIG_SYSTEM_TRUSTED_KEYS=""
          }' .config

      # Start installing the results
      install -m 644 .config $RPM_BUILD_ROOT/boot/config-$KernelVer
      install -m 644 .config $RPM_BUILD_ROOT/lib/modules/$KernelVer/config
      install -m 644 System.map $RPM_BUILD_ROOT/boot/System.map-$KernelVer
      install -m 644 System.map $RPM_BUILD_ROOT/lib/modules/$KernelVer/System.map

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Reserving 40MB in boot for initramfs" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Reserving 40MB in boot for initramfs"" 
  	set -x
      # We estimate the size of the initramfs because rpm needs to take this size
      # into consideration when performing disk space calculations. (See bz #530778)
      dd if=/dev/zero of=$RPM_BUILD_ROOT/boot/initramfs-$KernelVer.img bs=1M count=40

      if [ -f arch/$Arch/boot/zImage.stub ]; then

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Copy zImage.stub to RPM_BUILD_ROOT" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Copy zImage.stub to RPM_BUILD_ROOT"" 
  	set -x
        cp arch/$Arch/boot/zImage.stub $RPM_BUILD_ROOT/boot/zImage.stub-$KernelVer || :
        cp arch/$Arch/boot/zImage.stub $RPM_BUILD_ROOT/lib/modules/$KernelVer/zImage.stub-$KernelVer || :
      fi

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "copy signed kernel" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "copy signed kernel"" 
  	set -x
      $CopyKernel $KernelImage \
                  $RPM_BUILD_ROOT/boot/$InstallName-$KernelVer
      chmod 755 $RPM_BUILD_ROOT/boot/$InstallName-$KernelVer
      cp $RPM_BUILD_ROOT/boot/$InstallName-$KernelVer $RPM_BUILD_ROOT/lib/modules/$KernelVer/$InstallName

      # hmac sign the kernel for FIPS

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "hmac sign the kernel for FIPS" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "hmac sign the kernel for FIPS"" 
  	set -x

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Creating hmac file: $RPM_BUILD_ROOT/boot/.vmlinuz-$KernelVer.hmac" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Creating hmac file: $RPM_BUILD_ROOT/boot/.vmlinuz-$KernelVer.hmac"" 
  	set -x
      ls -l $RPM_BUILD_ROOT/boot/$InstallName-$KernelVer
      (cd $RPM_BUILD_ROOT/boot && sha512hmac $InstallName-$KernelVer) > $RPM_BUILD_ROOT/boot/.vmlinuz-$KernelVer.hmac;
      cp $RPM_BUILD_ROOT/boot/.vmlinuz-$KernelVer.hmac $RPM_BUILD_ROOT/lib/modules/$KernelVer/.vmlinuz.hmac

      if [ $DoModules -eq 1 ]; then

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Install modules in RPM_BUILD_ROOT" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Install modules in RPM_BUILD_ROOT"" 
  	set -x
  	# Override $(mod-fw) because we don't want it to install any firmware
  	# we'll get it from the linux-firmware package and we don't want conflicts
  	/usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" -j${RPM_BUILD_NCPUS} ARCH=$Arch INSTALL_MOD_PATH=$RPM_BUILD_ROOT -j${RPM_BUILD_NCPUS} modules_install KERNELRELEASE=$KernelVer mod-fw=
      fi

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Add VDSO files" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Add VDSO files"" 
  	set -x
      # add an a noop %defattr statement 'cause rpm doesn't like empty file list files
      echo '%defattr(-,-,-)' > ../kernel${Variant:+-${Variant}}-ldsoconf.list
      if [ $DoVDSO -ne 0 ]; then
          /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" ARCH=$Arch INSTALL_MOD_PATH=$RPM_BUILD_ROOT vdso_install KERNELRELEASE=$KernelVer
          if [ -s ldconfig-kernel.conf ]; then
               install -D -m 444 ldconfig-kernel.conf \
                  $RPM_BUILD_ROOT/etc/ld.so.conf.d/kernel-$KernelVer.conf
  	     echo /etc/ld.so.conf.d/kernel-$KernelVer.conf >> ../kernel${Variant:+-${Variant}}-ldsoconf.list
          fi

          rm -rf $RPM_BUILD_ROOT/lib/modules/$KernelVer/vdso/.build-id
      fi

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Save headers/makefiles, etc. for kernel-headers" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Save headers/makefiles, etc. for kernel-headers"" 
  	set -x
      # And save the headers/makefiles etc for building modules against
      #
      # This all looks scary, but the end result is supposed to be:
      # * all arch relevant include/ files
      # * all Makefile/Kconfig files
      # * all script/ files

      rm -f $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      rm -f $RPM_BUILD_ROOT/lib/modules/$KernelVer/source
      mkdir -p $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      (cd $RPM_BUILD_ROOT/lib/modules/$KernelVer ; ln -s build source)
      # dirs for additional modules per module-init-tools, kbuild/modules.txt
      mkdir -p $RPM_BUILD_ROOT/lib/modules/$KernelVer/updates
      mkdir -p $RPM_BUILD_ROOT/lib/modules/$KernelVer/weak-updates
      # CONFIG_KERNEL_HEADER_TEST generates some extra files in the process of
      # testing so just delete
      find . -name *.h.s -delete
      # first copy everything
      cp --parents `find  -type f -name "Makefile*" -o -name "Kconfig*"` $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      if [ ! -e Module.symvers ]; then
          touch Module.symvers
      fi
      cp Module.symvers $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp System.map $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      if [ -s Module.markers ]; then
        cp Module.markers $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      fi

      # create the kABI metadata for use in packaging
      # NOTENOTE: the name symvers is used by the rpm backend
      # NOTENOTE: to discover and run the /usr/lib/rpm/fileattrs/kabi.attr
      # NOTENOTE: script which dynamically adds exported kernel symbol
      # NOTENOTE: checksums to the rpm metadata provides list.
      # NOTENOTE: if you change the symvers name, update the backend too

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "GENERATING kernel ABI metadata" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "GENERATING kernel ABI metadata"" 
  	set -x
      xz --stdout --compress --check=crc32 --lzma2=dict=1MiB < Module.symvers > $RPM_BUILD_ROOT/boot/symvers-$KernelVer.xz
      cp $RPM_BUILD_ROOT/boot/symvers-$KernelVer.xz $RPM_BUILD_ROOT/lib/modules/$KernelVer/symvers.xz

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Cleanup Makefiles/Kconfig files" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Cleanup Makefiles/Kconfig files"" 
  	set -x
      # then drop all but the needed Makefiles/Kconfig files
      rm -rf $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/scripts
      rm -rf $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/include
      cp .config $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp -a scripts $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      rm -rf $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/scripts/tracing
      rm -f $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/scripts/spdxcheck.py

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Copy additional files for make targets" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Copy additional files for make targets"" 
  	set -x
      # Files for 'make scripts' to succeed with kernel-devel.
      mkdir -p $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/security/selinux/include
      cp -a --parents security/selinux/include/classmap.h $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp -a --parents security/selinux/include/initial_sid_to_string.h $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      mkdir -p $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/tools/include/tools
      cp -a --parents tools/include/tools/be_byteshift.h $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp -a --parents tools/include/tools/le_byteshift.h $RPM_BUILD_ROOT/lib/modules/$KernelVer/build

      # Files for 'make prepare' to succeed with kernel-devel.
      cp -a --parents tools/include/linux/compiler* $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp -a --parents tools/include/linux/types.h $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp -a --parents tools/build/Build.include $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp --parents tools/build/fixdep.c $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp --parents tools/objtool/sync-check.sh $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp -a --parents tools/bpf/resolve_btfids $RPM_BUILD_ROOT/lib/modules/$KernelVer/build

      cp --parents security/selinux/include/policycap_names.h $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp --parents security/selinux/include/policycap.h $RPM_BUILD_ROOT/lib/modules/$KernelVer/build

      cp -a --parents tools/include/asm $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp -a --parents tools/include/asm-generic $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp -a --parents tools/include/linux $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp -a --parents tools/include/uapi/asm $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp -a --parents tools/include/uapi/asm-generic $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp -a --parents tools/include/uapi/linux $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp -a --parents tools/include/vdso $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp --parents tools/scripts/utilities.mak $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp -a --parents tools/lib/subcmd $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp --parents tools/lib/*.c $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp --parents tools/objtool/*.[ch] $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp --parents tools/objtool/Build $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp --parents tools/objtool/include/objtool/*.h $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp -a --parents tools/lib/bpf $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      cp --parents tools/lib/bpf/Build $RPM_BUILD_ROOT/lib/modules/$KernelVer/build

      if [ -f tools/objtool/objtool ]; then
        cp -a tools/objtool/objtool $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/tools/objtool/ || :
      fi
      if [ -f tools/objtool/fixdep ]; then
        cp -a tools/objtool/fixdep $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/tools/objtool/ || :
      fi
      if [ -d arch/$Arch/scripts ]; then
        cp -a arch/$Arch/scripts $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/arch/aarch64 || :
      fi
      if [ -f arch/$Arch/*lds ]; then
        cp -a arch/$Arch/*lds $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/arch/aarch64/ || :
      fi
      if [ -f arch/arm64/kernel/module.lds ]; then
        cp -a --parents arch/arm64/kernel/module.lds $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
      fi
      find $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/scripts \( -iname "*.o" -o -iname "*.cmd" \) -exec rm -f {} +
      if [ -d arch/arm64/include ]; then
        cp -a --parents arch/arm64/include $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
      fi
      if [ -d tools/arch/arm64/include ]; then
        cp -a --parents tools/arch/arm64/include $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
      fi
      # arch/arm64/include/asm/xen references arch/arm
      cp -a --parents arch/arm/include/asm/xen $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
      # arch/arm64/include/asm/opcodes.h references arch/arm
      cp -a --parents arch/arm/include/asm/opcodes.h $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
      cp -a include $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/include
      # Cross-reference from include/perf/events/sof.h
      cp -a sound/soc/sof/sof-audio.h $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/sound/soc/sof

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Clean up intermediate tools files" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Clean up intermediate tools files"" 
  	set -x
      # Clean up intermediate tools files
      find $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/tools \( -iname "*.o" -o -iname "*.cmd" \) -exec rm -f {} +

      # Make sure the Makefile, version.h, and auto.conf have a matching
      # timestamp so that external modules can be built
      touch -r $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/Makefile \
          $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/include/generated/uapi/linux/version.h \
          $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/include/config/auto.conf

      eu-readelf -n vmlinux | grep "Build ID" | awk '{print $NF}' > vmlinux.id
      cp vmlinux.id $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/vmlinux.id

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Copy additional files for kernel-debuginfo rpm" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Copy additional files for kernel-debuginfo rpm"" 
  	set -x
      #
      # save the vmlinux file for kernel debugging into the kernel-debuginfo rpm
      # (use mv + symlink instead of cp to reduce disk space requirements)
      #
      mkdir -p $RPM_BUILD_ROOT/usr/lib/debug/lib/modules/$KernelVer
      mv vmlinux $RPM_BUILD_ROOT/usr/lib/debug/lib/modules/$KernelVer
      ln -s $RPM_BUILD_ROOT/usr/lib/debug/lib/modules/$KernelVer/vmlinux vmlinux
      if [ -n "" ]; then
  	    eu-readelf -n  %{vmlinux_decompressor} | grep "Build ID" | awk '{print $NF}' > vmlinux.decompressor.id
  	    # Without build-id the build will fail. But for s390 the build-id
  	    # wasn't added before 5.11. In case it is missing prefer not
  	    # packaging the debuginfo over a build failure.
  	    if [ -s vmlinux.decompressor.id ]; then
  		    cp vmlinux.decompressor.id $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/vmlinux.decompressor.id
  		    cp %{vmlinux_decompressor} $RPM_BUILD_ROOT/usr/lib/debug/lib/modules/$KernelVer/vmlinux.decompressor
  	    fi
      fi

      # build and copy the vmlinux-gdb plugin files into kernel-debuginfo
      /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" ARCH=$Arch -j${RPM_BUILD_NCPUS} scripts_gdb
      cp -a --parents scripts/gdb/{,linux/}*.py $RPM_BUILD_ROOT/usr/lib/debug/lib/modules/$KernelVer
      # this should be a relative symlink (Kbuild creates an absolute one)
      ln -s scripts/gdb/vmlinux-gdb.py $RPM_BUILD_ROOT/usr/lib/debug/lib/modules/$KernelVer/vmlinux-gdb.py
      %py_byte_compile %{python3} $RPM_BUILD_ROOT/usr/lib/debug/lib/modules/$KernelVer/scripts/gdb

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Create modnames" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Create modnames"" 
  	set -x
      find $RPM_BUILD_ROOT/lib/modules/$KernelVer -name "*.ko" -type f >modnames

      # mark modules executable so that strip-to-file can strip them
      xargs --no-run-if-empty chmod u+x < modnames

      # Generate a list of modules for block and networking.

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Generate a list of modules for block and networking" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Generate a list of modules for block and networking"" 
  	set -x
      grep -F /drivers/ modnames | xargs --no-run-if-empty nm -upA |
      sed -n 's,^.*/\([^/]*\.ko\):  *U \(.*\)$,\1 \2,p' > drivers.undef

      collect_modules_list()
      {
        sed -r -n -e "s/^([^ ]+) \\.?($2)\$/\\1/p" drivers.undef |
          LC_ALL=C sort -u > $RPM_BUILD_ROOT/lib/modules/$KernelVer/modules.$1
        if [ ! -z "$3" ]; then
          sed -r -e "/^($3)\$/d" -i $RPM_BUILD_ROOT/lib/modules/$KernelVer/modules.$1
        fi
      }

      collect_modules_list networking \
        'register_netdev|ieee80211_register_hw|usbnet_probe|phy_driver_register|rt(l_|2x00)(pci|usb)_probe|register_netdevice'
      collect_modules_list block \
        'ata_scsi_ioctl|scsi_add_host|scsi_add_host_with_dma|blk_alloc_queue|blk_init_queue|register_mtd_blktrans|scsi_esp_register|scsi_register_device_handler|blk_queue_physical_block_size' 'pktcdvd.ko|dm-mod.ko'
      collect_modules_list drm \
        'drm_open|drm_init'
      collect_modules_list modesetting \
        'drm_crtc_init'

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "detect missing or incorrect license tags" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "detect missing or incorrect license tags"" 
  	set -x
      # detect missing or incorrect license tags
      ( find $RPM_BUILD_ROOT/lib/modules/$KernelVer -name '*.ko' | xargs /sbin/modinfo -l | \
          grep -E -v 'GPL( v2)?$|Dual BSD/GPL$|Dual MPL/GPL$|GPL and additional rights$' ) && exit 1

      if [ $DoModules -eq 0 ]; then

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Create empty files for RPM packaging" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Create empty files for RPM packaging"" 
  	set -x
          # Ensure important files/directories exist to let the packaging succeed
          echo '%defattr(-,-,-)' > ../kernel${Variant:+-${Variant}}-modules-core.list
          echo '%defattr(-,-,-)' > ../kernel${Variant:+-${Variant}}-modules.list
          echo '%defattr(-,-,-)' > ../kernel${Variant:+-${Variant}}-modules-extra.list
          echo '%defattr(-,-,-)' > ../kernel${Variant:+-${Variant}}-modules-internal.list
          echo '%defattr(-,-,-)' > ../kernel${Variant:+-${Variant}}-modules-partner.list
          mkdir -p $RPM_BUILD_ROOT/lib/modules/$KernelVer/kernel
          # Add files usually created by make modules, needed to prevent errors
          # thrown by depmod during package installation
          touch $RPM_BUILD_ROOT/lib/modules/$KernelVer/modules.order
          touch $RPM_BUILD_ROOT/lib/modules/$KernelVer/modules.builtin
      fi

      # Copy the System.map file for depmod to use
      cp System.map $RPM_BUILD_ROOT/.

      if [[ "$Variant" == "rt" || "$Variant" == "rt-debug" || "$Variant" == "rt-64k" || "$Variant" == "rt-64k-debug" || "$Variant" == "automotive" || "$Variant" == "automotive-debug" ]]; then

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Skipping efiuki build" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Skipping efiuki build"" 
  	set -x
      else

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Setup the EFI UKI kernel" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Setup the EFI UKI kernel"" 
  	set -x

          # RHEL/CentOS specific .SBAT entries
          SBATsuffix="fedora"
          SBAT=$(cat <<- EOF
  	linux,1,Red Hat,linux,$KernelVer,mailto:secalert@redhat.com
  	linux.$SBATsuffix,1,Red Hat,linux,$KernelVer,mailto:secalert@redhat.com
  	kernel-uki-virt.$SBATsuffix,1,Red Hat,kernel-uki-virt,$KernelVer,mailto:secalert@redhat.com
  	EOF
  	)

          ADDONS_SBAT=$(cat <<- EOF
  	sbat,1,SBAT Version,sbat,1,https://github.com/rhboot/shim/blob/main/SBAT.md
  	kernel-uki-virt-addons.$SBATsuffix,1,Red Hat,kernel-uki-virt-addons,$KernelVer,mailto:secalert@redhat.com
  	EOF
  	)

  	KernelUnifiedImageDir="$RPM_BUILD_ROOT/lib/modules/$KernelVer"
      	KernelUnifiedImage="$KernelUnifiedImageDir/$InstallName-virt.efi"

      	mkdir -p $KernelUnifiedImageDir

      	dracut --conf=dracut-virt.conf \
             --confdir=$(mktemp -d) \
             --verbose \
             --kver "$KernelVer" \
             --kmoddir "$RPM_BUILD_ROOT/lib/modules/$KernelVer/" \
             --logfile=$(mktemp) \
             --uefi \
             --kernel-image $(realpath $KernelImage) \
             --kernel-cmdline 'console=tty0 console=ttyS0' \
  	   $KernelUnifiedImage

    KernelAddonsDirOut="$KernelUnifiedImage.extra.d"
    mkdir -p $KernelAddonsDirOut
    python3 uki_create_addons.py uki_addons.json $KernelAddonsDirOut virt fedora aarch64 "$ADDONS_SBAT"

      # hmac sign the UKI for FIPS
      KernelUnifiedImageHMAC="$KernelUnifiedImageDir/.$InstallName-virt.efi.hmac"

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "hmac sign the UKI for FIPS" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "hmac sign the UKI for FIPS"" 
  	set -x

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Creating hmac file: $KernelUnifiedImageHMAC" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Creating hmac file: $KernelUnifiedImageHMAC"" 
  	set -x
      (cd $KernelUnifiedImageDir && sha512hmac $InstallName-virt.efi) > $KernelUnifiedImageHMAC;

  # with_efiuki
  	:  # in case of empty block
      fi # "$Variant" == "rt" || "$Variant" == "rt-debug" || "$Variant" == "automotive" || "$Variant" == "automotive-debug"

      #
      # Generate the modules files lists
      #
      move_kmod_list()
      {
          local module_list="$1"
          local subdir_name="$2"

          mkdir -p "$RPM_BUILD_ROOT/lib/modules/$KernelVer/$subdir_name"

          set +x
          while read -r kmod; do
              local target_file="$RPM_BUILD_ROOT/lib/modules/$KernelVer/$subdir_name/$kmod"
              local target_dir="${target_file%/*}"
              mkdir -p "$target_dir"
              mv "$RPM_BUILD_ROOT/lib/modules/$KernelVer/kernel/$kmod" "$target_dir"
          done < <(sed -e 's|^kernel/||' "$module_list")
          set -x
      }

      create_module_file_list()
      {
          # subdirectory within /lib/modules/$KernelVer where kmods should go
          local module_subdir="$1"
          # kmod list with relative paths produced by filtermods.py
          local relative_kmod_list="$2"
          # list with absolute paths to kmods and other files to be included
          local absolute_file_list="$3"
          # if 1, this adds also all kmod directories to absolute_file_list
          local add_all_dirs="$4"
          local run_mod_deny="$5"

          if [ "$module_subdir" != "kernel" ]; then
              # move kmods into subdirs if needed (internal, partner, extra,..)
              move_kmod_list $relative_kmod_list $module_subdir
          fi

          # make kmod paths absolute
          sed -e 's|^kernel/|/lib/modules/'$KernelVer'/'$module_subdir'/|' $relative_kmod_list > $absolute_file_list

  	if [ "$run_mod_deny" -eq 1 ]; then
              # run deny-mod script, this adds blacklist-* files to absolute_file_list
              mod-denylist.sh "$RPM_BUILD_ROOT" lib/modules/$KernelVer $absolute_file_list
  	fi

          # deny-mod script works with kmods as they are now (not compressed),
          # but if they will be we need to add compext to all
          sed -i -e 's/.ko$/.ko.xz/' $absolute_file_list
          # add also dir for the case when there are no kmods
          # "kernel" subdir is covered in %files section, skip it here
          if [ "$module_subdir" != "kernel" ]; then
                  echo "%dir /lib/modules/$KernelVer/$module_subdir" >> $absolute_file_list
          fi

          if [ "$add_all_dirs" -eq 1 ]; then
              (cd $RPM_BUILD_ROOT; find lib/modules/$KernelVer/kernel -mindepth 1 -type d | sort -n) > ../module-dirs.list
              sed -e 's|^lib|%dir /lib|' ../module-dirs.list >> $absolute_file_list
          fi
      }

      if [ $DoModules -eq 1 ]; then
          # save modules.dep for debugging
          cp $RPM_BUILD_ROOT/lib/modules/$KernelVer/modules.dep ../

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Create module list files for all kernel variants" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Create module list files for all kernel variants"" 
  	set -x
          variants_param=""
          if [[ "$Variant" == "rt" || "$Variant" == "rt-debug" ]]; then
              variants_param="-r rt"
          fi
          if [[ "$Variant" == "rt-64k" || "$Variant" == "rt-64k-debug" ]]; then
              variants_param="-r rt-64k"
          fi
          if [[ "$Variant" == "automotive" || "$Variant" == "automotive-debug" ]]; then
              variants_param="-r automotive"
          fi
          # this creates ../modules-*.list output, where each kmod path is as it
          # appears in modules.dep (relative to lib/modules/$KernelVer)
          ret=0
          filtermods.py -l "../filtermods-$KernelVer.log" sort -d $RPM_BUILD_ROOT/lib/modules/$KernelVer/modules.dep -c configs/def_variants.yaml $variants_param -o .. || ret=$?
          if [ $ret -ne 0 ]; then
              echo "8< --- filtermods-$KernelVer.log ---"
              cat "../filtermods-$KernelVer.log"
              echo "--- filtermods-$KernelVer.log --- >8"

              echo "8< --- modules.dep ---"
              cat $RPM_BUILD_ROOT/lib/modules/$KernelVer/modules.dep
              echo "--- modules.dep --- >8"
              exit 1
          fi

          create_module_file_list "kernel" ../modules-core.list ../kernel${Variant:+-${Variant}}-modules-core.list 1 0
          create_module_file_list "kernel" ../modules.list ../kernel${Variant:+-${Variant}}-modules.list 0 0
          create_module_file_list "internal" ../modules-internal.list ../kernel${Variant:+-${Variant}}-modules-internal.list 0 1
          create_module_file_list "kernel" ../modules-extra.list ../kernel${Variant:+-${Variant}}-modules-extra.list 0 1
      fi # $DoModules -eq 1

      remove_depmod_files()
      {
          # remove files that will be auto generated by depmod at rpm -i time
          pushd $RPM_BUILD_ROOT/lib/modules/$KernelVer/
              # in case below list needs to be extended, remember to add a
              # matching ghost entry in the files section as well
              rm -f modules.{alias,alias.bin,builtin.alias.bin,builtin.bin} \
                    modules.{dep,dep.bin,devname,softdep,symbols,symbols.bin,weakdep}
          popd
      }

      # Cleanup

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Cleanup build files" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Cleanup build files"" 
  	set -x
      rm -f $RPM_BUILD_ROOT/System.map

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Remove depmod files" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Remove depmod files"" 
  	set -x
      remove_depmod_files

      # Move the devel headers out of the root file system

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Move the devel headers to RPM_BUILD_ROOT" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Move the devel headers to RPM_BUILD_ROOT"" 
  	set -x
      mkdir -p $RPM_BUILD_ROOT/usr/src/kernels
      mv $RPM_BUILD_ROOT/lib/modules/$KernelVer/build $RPM_BUILD_ROOT/$DevelDir

      # This is going to create a broken link during the build, but we don't use
      # it after this point.  We need the link to actually point to something
      # when kernel-devel is installed, and a relative link doesn't work across
      # the F17 UsrMove feature.
      ln -sf $DevelDir $RPM_BUILD_ROOT/lib/modules/$KernelVer/build

      # Generate vmlinux.h and put it to kernel-devel path
      # zfcpdump build does not have btf anymore
      if [ "$Variant" != "zfcpdump" ]; then

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Build the bootstrap bpftool to generate vmlinux.h" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Build the bootstrap bpftool to generate vmlinux.h"" 
  	set -x
          # Build the bootstrap bpftool to generate vmlinux.h
          BuildBpftool
          tools/bpf/bpftool/bootstrap/bpftool btf dump file vmlinux format c > $RPM_BUILD_ROOT/$DevelDir/vmlinux.h
      fi

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Cleanup kernel-devel and kernel-debuginfo files" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Cleanup kernel-devel and kernel-debuginfo files"" 
  	set -x
      # prune junk from kernel-devel
      find $RPM_BUILD_ROOT/usr/src/kernels -name ".*.cmd" -delete
      # prune junk from kernel-debuginfo
      find $RPM_BUILD_ROOT/usr/src/kernels -name "*.mod.c" -delete

      # Red Hat UEFI Secure Boot CA cert, which can be used to authenticate the kernel

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Install certs" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Install certs"" 
  	set -x
      mkdir -p $RPM_BUILD_ROOT/usr/share/doc/kernel-keys/$KernelVer

      if [ $DoModules -eq 1 ]; then
          # Save the signing keys so we can sign the modules in __modsign_install_post
          cp certs/signing_key.pem certs/signing_key.pem.sign${Variant:++${Variant}}
          cp certs/signing_key.x509 certs/signing_key.x509.sign${Variant:++${Variant}}
      fi

  }

  ###
  # DO it...
  ###

  # prepare directories
  rm -rf $RPM_BUILD_ROOT
  mkdir -p $RPM_BUILD_ROOT/boot
  mkdir -p $RPM_BUILD_ROOT/usr/lib/linux-asahi

  cd linux-6.15.10-402.asahi.aarch64

  BuildKernel vmlinuz.efi arch/arm64/boot/vmlinuz.efi 1 16k-debug

  BuildKernel vmlinuz.efi arch/arm64/boot/vmlinuz.efi 1 debug

  BuildKernel vmlinuz.efi arch/arm64/boot/vmlinuz.efi 1 16k

  BuildKernel vmlinuz.efi arch/arm64/boot/vmlinuz.efi 1

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "Build perf" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "Build perf"" 
  	set -x
  # perf
  # make sure check-headers.sh is executable
  chmod +x tools/perf/check-headers.sh

    /usr/bin/make V=1 EXTRA_CFLAGS="${RPM_OPT_FLAGS}" EXTRA_CXXFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags} -Wl,-E"  -C tools/perf V=1 NO_PERF_READ_VDSO32=1 NO_PERF_READ_VDSOX32=1 WERROR=0 NO_LIBUNWIND=1 HAVE_CPLUS_DEMANGLE=1 NO_GTK2=1 NO_STRLCPY=1 NO_BIONIC=1 LIBBPF_DYNAMIC=1 LIBTRACEEVENT_DYNAMIC=1 CORESIGHT=1 prefix=/usr PYTHON=%{__python3} DESTDIR=$RPM_BUILD_ROOT all

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "build libperf" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "build libperf"" 
  	set -x

    /usr/bin/make V=1 EXTRA_CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}"  -C tools/lib/perf V=1 DESTDIR=$RPM_BUILD_ROOT

      # link against in-tree libcpupower for idle state support

  pushd tools/net/ynl
  export PIP_CONFIG_FILE=/tmp/pip.config
  cat <<EOF > $PIP_CONFIG_FILE
  [install]
  no-index = true
  no-build-isolation = false
  EOF

    CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" EXTRA_CFLAGS="${RPM_OPT_FLAGS}" /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" V=1 -j${RPM_BUILD_NCPUS} DESTDIR=$RPM_BUILD_ROOT install
  popd

  # cpupower
  # make sure version-gen.sh is executable.
  chmod +x tools/power/cpupower/utils/version-gen.sh

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "build cpupower" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "build cpupower"" 
  	set -x

    CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" EXTRA_CFLAGS="${RPM_OPT_FLAGS}" /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" V=1 -j${RPM_BUILD_NCPUS} -C tools/power/cpupower CPUFREQ_BENCH=false DEBUG=false
  pushd tools/thermal/tmon/

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "build tmon" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "build tmon"" 
  	set -x

    CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" EXTRA_CFLAGS="${RPM_OPT_FLAGS}" /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" V=1
  popd
  pushd tools/bootconfig/

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "build bootconfig" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "build bootconfig"" 
  	set -x

    CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" EXTRA_CFLAGS="${RPM_OPT_FLAGS}" /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" V=1
  popd
  pushd tools/iio/

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "build iio" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "build iio"" 
  	set -x

    CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" EXTRA_CFLAGS="${RPM_OPT_FLAGS}" /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" V=1
  popd
  pushd tools/gpio/

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "build gpio" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "build gpio"" 
  	set -x

    CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" EXTRA_CFLAGS="${RPM_OPT_FLAGS}" /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" V=1
  popd
  # build VM tools
  pushd tools/mm/

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "build slabinfo page_owner_sort" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "build slabinfo page_owner_sort"" 
  	set -x

    CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" EXTRA_CFLAGS="${RPM_OPT_FLAGS}" /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" V=1 slabinfo page_owner_sort
  popd
  pushd tools/verification/rv/

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "build rv" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "build rv"" 
  	set -x

    CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" EXTRA_CFLAGS="${RPM_OPT_FLAGS}" /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" V=1
  popd
  pushd tools/tracing/rtla

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "build rtla" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "build rtla"" 
  	set -x

    CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" EXTRA_CFLAGS="${RPM_OPT_FLAGS}" /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" V=1 LDFLAGS="%{__global_ldflags} -L../../power/cpupower" INCLUDES="-I../../power/cpupower/lib"
  popd

  #set RPM_VMLINUX_H
  if [ -f $RPM_BUILD_ROOT/$DevelDir/vmlinux.h ]; then
    RPM_VMLINUX_H=$RPM_BUILD_ROOT/$DevelDir/vmlinux.h
  elif [ -f $DevelDir/vmlinux.h ]; then
    RPM_VMLINUX_H=$DevelDir/vmlinux.h
  fi
  echo "${RPM_VMLINUX_H}" > ../vmlinux_h_path

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "start build selftests" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "start build selftests"" 
  	set -x
  # Unfortunately, samples/bpf/Makefile expects that the headers are installed
  # in the source tree. We installed them previously to $RPM_BUILD_ROOT/usr
  # but there's no way to tell the Makefile to take them from there.

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "install headers for selftests" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "install headers for selftests"" 
  	set -x
  /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" -j${RPM_BUILD_NCPUS} headers_install

  # If we re building only tools without kernel, we need to generate config
  # headers and prepare tree for modules building. The modules_prepare target
  # will cover both.
  if [ ! -f include/generated/autoconf.h ]; then

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "modules_prepare for selftests" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "modules_prepare for selftests"" 
  	set -x
     /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" -j${RPM_BUILD_NCPUS} modules_prepare
  fi

  # Build BPFtool for samples/bpf
  if [ ! -f tools/bpf/bpftool/bootstrap/bpftool ]; then
    BuildBpftool
  fi

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "build samples/bpf" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "build samples/bpf"" 
  	set -x
  /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" -j${RPM_BUILD_NCPUS} ARCH=$Arch BPFTOOL=$(pwd)/tools/bpf/bpftool/bootstrap/bpftool V=1 M=samples/bpf/ VMLINUX_H="${RPM_VMLINUX_H}" || true

  pushd tools/testing/selftests
  # We need to install here because we need to call make with ARCH set which
  # doesn't seem possible to do in the install section.
    force_targets=""

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "main selftests compile" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "main selftests compile"" 
  	set -x
  /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" -j${RPM_BUILD_NCPUS} ARCH=$Arch V=1 TARGETS="bpf cgroup mm net net/forwarding net/mptcp net/netfilter net/packetdrill tc-testing memfd drivers/net/bonding iommu cachestat pid_namespace rlimits" SKIP_TARGETS="" $force_targets INSTALL_PATH=fakeinstall/usr/lib/linux-asahi/kselftests VMLINUX_H="${RPM_VMLINUX_H}" install

  # 'make install' for bpf is broken and upstream refuses to fix it.
  # Install the needed files manually.

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "install selftests" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "install selftests"" 
  	set -x
  for dir in bpf bpf/no_alu32 bpf/progs; do
  	# In ARK, the rpm build continues even if some of the selftests
  	# cannot be built. It's not always possible to build selftests,
  	# as upstream sometimes dependens on too new llvm version or has
  	# other issues. If something did not get built, just skip it.
  	test -d $dir || continue
  	mkdir -p fakeinstall/usr/lib/linux-asahi/kselftests/$dir
  	find $dir -maxdepth 1 -type f \( -executable -o -name '*.py' -o -name settings -o \
  		-name 'btf_dump_test_case_*.c' -o -name '*.ko' -o \
  		-name '*.o' -exec sh -c 'readelf -h "{}" | grep -q "^  Machine:.*BPF"' \; \) -print0 | \
  	xargs -0 cp -t fakeinstall/usr/lib/linux-asahi/kselftests/$dir || true
  done

  (cd fakeinstall; cp -rav --parents -t .//root_unstripped/ "usr/libexec/kselftests/bpf/test_progs" || true) 

  (cd fakeinstall; cp -rav --parents -t .//root_unstripped/ "usr/libexec/kselftests/bpf/test_progs-no_alu32" || true) 

  popd

  	{ set +x; } 2>/dev/null 
  	_log_msglineno=$(grep -n "end build selftests" /SPECS/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) 
  	echo "kernel.spec:${_log_msglineno}: "end build selftests"" 
  	set -x

  # Module signing (modsign)
  #
  # This must be run _after_ find-debuginfo.sh runs, otherwise that will strip
  # the signature off of the modules.
  #
  # Don't sign modules for the zfcpdump variant as it is monolithic.

  ###
  ### Special hacks for debuginfo subpackages.
  ###

  # This macro is used by %install, so we must redefine it before that.

}

package() {

  cd linux-6.15.10-402.asahi.aarch64

  # re-define RPM_VMLINUX_H, because it doesn't carry over from %build
  RPM_VMLINUX_H="$(cat ../vmlinux_h_path)"

  # We have to do the headers install before the tools install because the
  # kernel headers_install will remove any header files in /usr/include that
  # it doesn't install itself.

  # Install kernel headers
  /usr/bin/make ARCH=arm64 INSTALL_HDR_PATH=$RPM_BUILD_ROOT/usr headers_install

  find $RPM_BUILD_ROOT/usr/include \
       \( -name .install -o -name .check -o \
          -name ..install.cmd -o -name ..check.cmd \) -delete

  # perf tool binary and supporting scripts/binaries

    /usr/bin/make V=1 EXTRA_CFLAGS="${RPM_OPT_FLAGS}" EXTRA_CXXFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags} -Wl,-E"  -C tools/perf V=1 NO_PERF_READ_VDSO32=1 NO_PERF_READ_VDSOX32=1 WERROR=0 NO_LIBUNWIND=1 HAVE_CPLUS_DEMANGLE=1 NO_GTK2=1 NO_STRLCPY=1 NO_BIONIC=1 LIBBPF_DYNAMIC=1 LIBTRACEEVENT_DYNAMIC=1 CORESIGHT=1 prefix=/usr PYTHON=%{__python3} DESTDIR=$RPM_BUILD_ROOT lib=lib install-bin
  # remove the 'trace' symlink.
  rm -f fakeinstall/usr/bin/trace

  # For both of the below, yes, this should be using a macro but right now
  # it's hard coded and we don't actually want it anyway right now.
  # Whoever wants examples can fix it up!

  # remove examples
  rm -rf fakeinstall/usr/lib/perf/examples
  rm -rf fakeinstall/usr/lib/perf/include

  # python-perf extension

    /usr/bin/make V=1 EXTRA_CFLAGS="${RPM_OPT_FLAGS}" EXTRA_CXXFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags} -Wl,-E"  -C tools/perf V=1 NO_PERF_READ_VDSO32=1 NO_PERF_READ_VDSOX32=1 WERROR=0 NO_LIBUNWIND=1 HAVE_CPLUS_DEMANGLE=1 NO_GTK2=1 NO_STRLCPY=1 NO_BIONIC=1 LIBBPF_DYNAMIC=1 LIBTRACEEVENT_DYNAMIC=1 CORESIGHT=1 prefix=/usr PYTHON=%{__python3} DESTDIR=$RPM_BUILD_ROOT install-python_ext

  # perf man pages (note: implicit rpm magic compresses them later)
  mkdir -p fakeinstall/usr/share/man/man1

    /usr/bin/make V=1 EXTRA_CFLAGS="${RPM_OPT_FLAGS}" EXTRA_CXXFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags} -Wl,-E"  -C tools/perf V=1 NO_PERF_READ_VDSO32=1 NO_PERF_READ_VDSOX32=1 WERROR=0 NO_LIBUNWIND=1 HAVE_CPLUS_DEMANGLE=1 NO_GTK2=1 NO_STRLCPY=1 NO_BIONIC=1 LIBBPF_DYNAMIC=1 LIBTRACEEVENT_DYNAMIC=1 CORESIGHT=1 prefix=/usr PYTHON=%{__python3} DESTDIR=$RPM_BUILD_ROOT install-man

  # remove any tracevent files, eg. its plugins still gets built and installed,
  # even if we build against system's libtracevent during perf build (by setting
  # LIBTRACEEVENT_DYNAMIC=1 above in perf_make macro). Those files should already
  # ship with libtraceevent package.
  rm -rf fakeinstall/usr/lib/traceevent

    /usr/bin/make V=1 EXTRA_CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}"  -C tools/lib/perf V=1 DESTDIR=fakeinstall prefix=/usr libdir=/usr/lib install install_headers
  # This is installed on some arches and we don't want to ship it
  rm -rf fakeinstall/usr/lib/libperf.a

  /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" -C tools/power/cpupower DESTDIR=$RPM_BUILD_ROOT libdir=/usr/lib mandir=/usr/share/man CPUFREQ_BENCH=false install
  /usr/lib/rpm/find-lang.sh fakeinstall cpupower
  mv cpupower.lang ../
  chmod 0755 fakeinstall/usr/lib/libcpupower.so*
  pushd tools/thermal/tmon

    CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" EXTRA_CFLAGS="${RPM_OPT_FLAGS}" /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" V=1 INSTALL_ROOT=fakeinstall install
  popd
  pushd tools/bootconfig

    CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" EXTRA_CFLAGS="${RPM_OPT_FLAGS}" /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" V=1 DESTDIR=fakeinstall install
  popd
  pushd tools/iio

    CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" EXTRA_CFLAGS="${RPM_OPT_FLAGS}" /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" V=1 DESTDIR=fakeinstall install
  popd
  pushd tools/gpio

    CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" EXTRA_CFLAGS="${RPM_OPT_FLAGS}" /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" V=1 DESTDIR=fakeinstall install
  popd
  install -m644 -D kvm_stat.logrotate fakeinstall/etc/logrotate.d/kvm_stat
  pushd tools/kvm/kvm_stat
  /usr/bin/make INSTALL_ROOT=fakeinstall install-tools
  /usr/bin/make INSTALL_ROOT=fakeinstall install-man
  install -m644 -D kvm_stat.service fakeinstall%{_unitdir}/kvm_stat.service
  popd
  # install VM tools
  pushd tools/mm/
  install -m755 slabinfo fakeinstall/usr/bin/slabinfo
  install -m755 page_owner_sort fakeinstall/usr/bin/page_owner_sort
  popd
  pushd tools/verification/rv/

    CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" EXTRA_CFLAGS="${RPM_OPT_FLAGS}" /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" V=1 DESTDIR=fakeinstall install
  popd
  pushd tools/tracing/rtla/

    CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" EXTRA_CFLAGS="${RPM_OPT_FLAGS}" /usr/bin/make  V=1 HOSTCFLAGS="-O2 -g" HOSTLDFLAGS="" V=1 DESTDIR=fakeinstall install
  rm -f fakeinstall/usr/bin/hwnoise
  rm -f fakeinstall/usr/bin/osnoise
  rm -f fakeinstall/usr/bin/timerlat
  (cd fakeinstall

          ln -sf rtla ./usr/bin/hwnoise
          ln -sf rtla ./usr/bin/osnoise
          ln -sf rtla ./usr/bin/timerlat
  )
  popd

  pushd samples
  install -d fakeinstall/usr/lib/linux-asahi/ksamples
  # install bpf samples
  pushd bpf
  install -d fakeinstall/usr/lib/linux-asahi/ksamples/bpf
  find -type f -executable -exec install -m755 {} fakeinstall/usr/lib/linux-asahi/ksamples/bpf \;
  install -m755 *.sh fakeinstall/usr/lib/linux-asahi/ksamples/bpf
  # test_lwt_bpf.sh compiles test_lwt_bpf.c when run; this works only from the
  # kernel tree. Just remove it.
  rm fakeinstall/usr/lib/linux-asahi/ksamples/bpf/test_lwt_bpf.sh
  install -m644 *_kern.o fakeinstall/usr/lib/linux-asahi/ksamples/bpf || true
  install -m644 tcp_bpf.readme fakeinstall/usr/lib/linux-asahi/ksamples/bpf
  popd
  # install pktgen samples
  pushd pktgen
  install -d fakeinstall/usr/lib/linux-asahi/ksamples/pktgen
  find . -type f -executable -exec install -m755 {} fakeinstall/usr/lib/linux-asahi/ksamples/pktgen/{} \;
  find . -type f ! -executable -exec install -m644 {} fakeinstall/usr/lib/linux-asahi/ksamples/pktgen/{} \;
  popd
  popd
  # install mm selftests
  pushd tools/testing/selftests/mm
  find -type d -exec install -d fakeinstall/usr/lib/linux-asahi/kselftests/mm/{} \;
  find -type f -executable -exec install -D -m755 {} fakeinstall/usr/lib/linux-asahi/kselftests/mm/{} \;
  find -type f ! -executable -exec install -D -m644 {} fakeinstall/usr/lib/linux-asahi/kselftests/mm/{} \;
  popd
  # install cgroup selftests
  pushd tools/testing/selftests/cgroup
  find -type d -exec install -d fakeinstall/usr/lib/linux-asahi/kselftests/cgroup/{} \;
  find -type f -executable -exec install -D -m755 {} fakeinstall/usr/lib/linux-asahi/kselftests/cgroup/{} \;
  find -type f ! -executable -exec install -D -m644 {} fakeinstall/usr/lib/linux-asahi/kselftests/cgroup/{} \;
  popd
  # install drivers/net/mlxsw selftests
  pushd tools/testing/selftests/drivers/net/mlxsw
  find -type d -exec install -d fakeinstall/usr/lib/linux-asahi/kselftests/drivers/net/mlxsw/{} \;
  find -type f -executable -exec install -D -m755 {} fakeinstall/usr/lib/linux-asahi/kselftests/drivers/net/mlxsw/{} \;
  find -type f ! -executable -exec install -D -m644 {} fakeinstall/usr/lib/linux-asahi/kselftests/drivers/net/mlxsw/{} \;
  popd
  # install drivers/net/netdevsim selftests
  pushd tools/testing/selftests/drivers/net/netdevsim
  find -type d -exec install -d fakeinstall/usr/lib/linux-asahi/kselftests/drivers/net/netdevsim/{} \;
  find -type f -executable -exec install -D -m755 {} fakeinstall/usr/lib/linux-asahi/kselftests/drivers/net/netdevsim/{} \;
  find -type f ! -executable -exec install -D -m644 {} fakeinstall/usr/lib/linux-asahi/kselftests/drivers/net/netdevsim/{} \;
  popd
  # install drivers/net/bonding selftests
  pushd tools/testing/selftests/drivers/net/bonding
  find -type d -exec install -d fakeinstall/usr/lib/linux-asahi/kselftests/drivers/net/bonding/{} \;
  find -type f -executable -exec install -D -m755 {} fakeinstall/usr/lib/linux-asahi/kselftests/drivers/net/bonding/{} \;
  find -type f ! -executable -exec install -D -m644 {} fakeinstall/usr/lib/linux-asahi/kselftests/drivers/net/bonding/{} \;
  popd
  # install net/forwarding selftests
  pushd tools/testing/selftests/net/forwarding
  find -type d -exec install -d fakeinstall/usr/lib/linux-asahi/kselftests/net/forwarding/{} \;
  find -type f -executable -exec install -D -m755 {} fakeinstall/usr/lib/linux-asahi/kselftests/net/forwarding/{} \;
  find -type f ! -executable -exec install -D -m644 {} fakeinstall/usr/lib/linux-asahi/kselftests/net/forwarding/{} \;
  popd
  # install net/mptcp selftests
  pushd tools/testing/selftests/net/mptcp
  find -type d -exec install -d fakeinstall/usr/lib/linux-asahi/kselftests/net/mptcp/{} \;
  find -type f -executable -exec install -D -m755 {} fakeinstall/usr/lib/linux-asahi/kselftests/net/mptcp/{} \;
  find -type f ! -executable -exec install -D -m644 {} fakeinstall/usr/lib/linux-asahi/kselftests/net/mptcp/{} \;
  popd
  # install tc-testing selftests
  pushd tools/testing/selftests/tc-testing
  find -type d -exec install -d fakeinstall/usr/lib/linux-asahi/kselftests/tc-testing/{} \;
  find -type f -executable -exec install -D -m755 {} fakeinstall/usr/lib/linux-asahi/kselftests/tc-testing/{} \;
  find -type f ! -executable -exec install -D -m644 {} fakeinstall/usr/lib/linux-asahi/kselftests/tc-testing/{} \;
  popd
  # install livepatch selftests
  pushd tools/testing/selftests/livepatch
  find -type d -exec install -d fakeinstall/usr/lib/linux-asahi/kselftests/livepatch/{} \;
  find -type f -executable -exec install -D -m755 {} fakeinstall/usr/lib/linux-asahi/kselftests/livepatch/{} \;
  find -type f ! -executable -exec install -D -m644 {} fakeinstall/usr/lib/linux-asahi/kselftests/livepatch/{} \;
  popd
  # install net/netfilter selftests
  pushd tools/testing/selftests/net/netfilter
  find -type d -exec install -d fakeinstall/usr/lib/linux-asahi/kselftests/net/netfilter/{} \;
  find -type f -executable -exec install -D -m755 {} fakeinstall/usr/lib/linux-asahi/kselftests/net/netfilter/{} \;
  find -type f ! -executable -exec install -D -m644 {} fakeinstall/usr/lib/linux-asahi/kselftests/net/netfilter/{} \;
  popd
  # install net/packetdrill selftests
  pushd tools/testing/selftests/net/packetdrill
  find -type d -exec install -d fakeinstall/usr/lib/linux-asahi/kselftests/net/packetdrill/{} \;
  find -type f -executable -exec install -D -m755 {} fakeinstall/usr/lib/linux-asahi/kselftests/net/packetdrill/{} \;
  find -type f ! -executable -exec install -D -m644 {} fakeinstall/usr/lib/linux-asahi/kselftests/net/packetdrill/{} \;
  popd

  # install memfd selftests
  pushd tools/testing/selftests/memfd
  find -type d -exec install -d fakeinstall/usr/lib/linux-asahi/kselftests/memfd/{} \;
  find -type f -executable -exec install -D -m755 {} fakeinstall/usr/lib/linux-asahi/kselftests/memfd/{} \;
  find -type f ! -executable -exec install -D -m644 {} fakeinstall/usr/lib/linux-asahi/kselftests/memfd/{} \;
  popd
  # install iommu selftests
  pushd tools/testing/selftests/iommu
  find -type d -exec install -d fakeinstall/usr/lib/linux-asahi/kselftests/iommu/{} \;
  find -type f -executable -exec install -D -m755 {} fakeinstall/usr/lib/linux-asahi/kselftests/iommu/{} \;
  find -type f ! -executable -exec install -D -m644 {} fakeinstall/usr/lib/linux-asahi/kselftests/iommu/{} \;
  popd
  # install rlimits selftests
  pushd tools/testing/selftests/rlimits
  find -type d -exec install -d fakeinstall/usr/lib/linux-asahi/kselftests/rlimits/{} \;
  find -type f -executable -exec install -D -m755 {} fakeinstall/usr/lib/linux-asahi/kselftests/rlimits/{} \;
  find -type f ! -executable -exec install -D -m644 {} fakeinstall/usr/lib/linux-asahi/kselftests/rlimits/{} \;
  popd
  # install pid_namespace selftests
  pushd tools/testing/selftests/pid_namespace
  find -type d -exec install -d fakeinstall/usr/lib/linux-asahi/kselftests/pid_namespace/{} \;
  find -type f -executable -exec install -D -m755 {} fakeinstall/usr/lib/linux-asahi/kselftests/pid_namespace/{} \;
  find -type f ! -executable -exec install -D -m644 {} fakeinstall/usr/lib/linux-asahi/kselftests/pid_namespace/{} \;
  popd

  ###
  ### clean
  ###

  ###
  ### scripts
  ###

  %post -n kernel-tools-libs
  /sbin/ldconfig

  %postun -n kernel-tools-libs
  /sbin/ldconfig

  #
  # This macro defines a %post script for a kernel*-devel package.
  #	%kernel_devel_post [<subpackage>]
  # Note we don't run hardlink if ostree is in use, as ostree is
  # a far more sophisticated hardlink implementation.
  # https://github.com/projectatomic/rpm-ostree/commit/58a79056a889be8814aa51f507b2c7a4dccee526
  #
  # The deletion of *.hardlink-temporary files is a temporary workaround
  # for this bug in the hardlink binary (fixed in util-linux 2.38):
  # https://github.com/util-linux/util-linux/issues/1602
  #

  #
  # This macro defines a %post script for a kernel*-modules-extra package.
  # It also defines a %postun script that does the same thing.
  #	%kernel_modules_extra_post [<subpackage>]
  #

  #
  # This macro defines a %post script for a kernel*-modules-internal package.
  # It also defines a %postun script that does the same thing.
  #	%kernel_modules_internal_post [<subpackage>]
  #

  #
  # This macro defines a %post script for a kernel*-modules-partner package.
  # It also defines a %postun script that does the same thing.
  #	%kernel_modules_partner_post [<subpackage>]
  #

  #
  # This macro defines a %post script for a kernel*-modules package.
  # It also defines a %postun script that does the same thing.
  #	%kernel_modules_post [<subpackage>]
  #

  #
  # This macro defines a %post script for a kernel*-modules-core package.
  #	%kernel_modules_core_post [<subpackage>]
  #

  # This macro defines a %posttrans script for a kernel package.
  #	%kernel_variant_posttrans [-v <subpackage>] [-u uki-suffix]
  # More text can follow to go at the end of this variant's %post.
  #

  #
  # This macro defines a %post script for a kernel package and its devel package.
  #	%kernel_variant_post [-v <subpackage>] [-r <replace>]
  # More text can follow to go at the end of this variant's %post.
  #

  #
  # This macro defines a %preun script for a kernel package.
  #	%kernel_variant_preun [-v <subpackage>] -u [uki-suffix]
  #

  %posttrans uki-virt
  rm -f /var/lib/rpm-state/kernel/installing_core_6.15.10-402.asahi.aarch64
  /bin/kernel-install add 6.15.10-402.asahi.aarch64 /lib/modules/6.15.10-402.asahi.aarch64/vmlinuz-virt.efi || exit $?
  if [[ ! -e "/boot/symvers-6.15.10-402.asahi.aarch64.xz" ]]; then
      cp "/lib/modules/6.15.10-402.asahi.aarch64/symvers.xz" "/boot/symvers-6.15.10-402.asahi.aarch64.xz"
      if command -v restorecon &>/dev/null; then
          restorecon "/boot/symvers-6.15.10-402.asahi.aarch64.xz"
      fi
  fi

  %preun uki-virt
  /bin/kernel-install remove 6.15.10-402.asahi.aarch64 || exit $?
  if [ -x /usr/bin/weak-modules ]
  then
      /usr/bin/weak-modules --remove-kernel 6.15.10-402.asahi.aarch64 || exit $?
  fi

  %preun core
  /bin/kernel-install remove 6.15.10-402.asahi.aarch64 || exit $?
  if [ -x /usr/bin/weak-modules ]
  then
      /usr/bin/weak-modules --remove-kernel 6.15.10-402.asahi.aarch64 || exit $?
  fi

  %post devel
  if [ -f /etc/sysconfig/kernel ]
  then
      . /etc/sysconfig/kernel || exit $?
  fi
  if [ "$HARDLINK" != "no" -a -x /usr/bin/hardlink -a ! -e /run/ostree-booted ] 
  then
      (cd /usr/src/kernels/6.15.10-402.asahi.aarch64 &&
       /usr/bin/find . -type f | while read f; do
         hardlink -c /usr/src/kernels/*.*/$f $f > /dev/null
       done;
       /usr/bin/find /usr/src/kernels -type f -name '*.hardlink-temporary' -delete
      )
  fi

  %post modules
  /sbin/depmod -a 6.15.10-402.asahi.aarch64
  if [ ! -f /var/lib/rpm-state/kernel/installing_core_6.15.10-402.asahi.aarch64 ]; then
  	mkdir -p /var/lib/rpm-state/kernel
  	touch /var/lib/rpm-state/kernel/need_to_run_dracut_6.15.10-402.asahi.aarch64
  fi

  %postun modules
  /sbin/depmod -a 6.15.10-402.asahi.aarch64

  %posttrans modules
  if [ -f /var/lib/rpm-state/kernel/need_to_run_dracut_6.15.10-402.asahi.aarch64 ]; then
  	rm -f /var/lib/rpm-state/kernel/need_to_run_dracut_6.15.10-402.asahi.aarch64
  	echo "Running: dracut -f --kver 6.15.10-402.asahi.aarch64"
  	dracut -f --kver "6.15.10-402.asahi.aarch64" || exit $?
  fi

  %posttrans modules-core
  /sbin/depmod -a 6.15.10-402.asahi.aarch64

  %post modules-extra
  /sbin/depmod -a 6.15.10-402.asahi.aarch64

  %postun modules-extra
  /sbin/depmod -a 6.15.10-402.asahi.aarch64

  %post modules-internal
  /sbin/depmod -a 6.15.10-402.asahi.aarch64

  %postun modules-internal
  /sbin/depmod -a 6.15.10-402.asahi.aarch64

  %posttrans core
  rm -f /var/lib/rpm-state/kernel/installing_core_6.15.10-402.asahi.aarch64
  /bin/kernel-install add 6.15.10-402.asahi.aarch64 /lib/modules/6.15.10-402.asahi.aarch64/vmlinuz || exit $?
  if [[ ! -e "/boot/symvers-6.15.10-402.asahi.aarch64.xz" ]]; then
      cp "/lib/modules/6.15.10-402.asahi.aarch64/symvers.xz" "/boot/symvers-6.15.10-402.asahi.aarch64.xz"
      if command -v restorecon &>/dev/null; then
          restorecon "/boot/symvers-6.15.10-402.asahi.aarch64.xz"
      fi
  fi

  %post core

  mkdir -p /var/lib/rpm-state/kernel
  touch /var/lib/rpm-state/kernel/installing_core_6.15.10-402.asahi.aarch64

  %posttrans debug-uki-virt
  rm -f /var/lib/rpm-state/kernel/installing_core_6.15.10-402.asahi.aarch64+debug
  /bin/kernel-install add 6.15.10-402.asahi.aarch64+debug /lib/modules/6.15.10-402.asahi.aarch64+debug/vmlinuz-virt.efi || exit $?
  if [[ ! -e "/boot/symvers-6.15.10-402.asahi.aarch64+debug.xz" ]]; then
      cp "/lib/modules/6.15.10-402.asahi.aarch64+debug/symvers.xz" "/boot/symvers-6.15.10-402.asahi.aarch64+debug.xz"
      if command -v restorecon &>/dev/null; then
          restorecon "/boot/symvers-6.15.10-402.asahi.aarch64+debug.xz"
      fi
  fi

  %preun debug-uki-virt
  /bin/kernel-install remove 6.15.10-402.asahi.aarch64+debug || exit $?
  if [ -x /usr/bin/weak-modules ]
  then
      /usr/bin/weak-modules --remove-kernel 6.15.10-402.asahi.aarch64+debug || exit $?
  fi

  %preun debug-core
  /bin/kernel-install remove 6.15.10-402.asahi.aarch64+debug || exit $?
  if [ -x /usr/bin/weak-modules ]
  then
      /usr/bin/weak-modules --remove-kernel 6.15.10-402.asahi.aarch64+debug || exit $?
  fi

  %post debug-devel
  if [ -f /etc/sysconfig/kernel ]
  then
      . /etc/sysconfig/kernel || exit $?
  fi
  if [ "$HARDLINK" != "no" -a -x /usr/bin/hardlink -a ! -e /run/ostree-booted ] 
  then
      (cd /usr/src/kernels/6.15.10-402.asahi.aarch64+debug &&
       /usr/bin/find . -type f | while read f; do
         hardlink -c /usr/src/kernels/*.*/$f $f > /dev/null
       done;
       /usr/bin/find /usr/src/kernels -type f -name '*.hardlink-temporary' -delete
      )
  fi

  %post debug-modules
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+debug
  if [ ! -f /var/lib/rpm-state/kernel/installing_core_6.15.10-402.asahi.aarch64+debug ]; then
  	mkdir -p /var/lib/rpm-state/kernel
  	touch /var/lib/rpm-state/kernel/need_to_run_dracut_6.15.10-402.asahi.aarch64+debug
  fi

  %postun debug-modules
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+debug

  %posttrans debug-modules
  if [ -f /var/lib/rpm-state/kernel/need_to_run_dracut_6.15.10-402.asahi.aarch64+debug ]; then
  	rm -f /var/lib/rpm-state/kernel/need_to_run_dracut_6.15.10-402.asahi.aarch64+debug
  	echo "Running: dracut -f --kver 6.15.10-402.asahi.aarch64+debug"
  	dracut -f --kver "6.15.10-402.asahi.aarch64+debug" || exit $?
  fi

  %posttrans debug-modules-core
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+debug

  %post debug-modules-extra
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+debug

  %postun debug-modules-extra
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+debug

  %post debug-modules-internal
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+debug

  %postun debug-modules-internal
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+debug

  %posttrans debug-core
  rm -f /var/lib/rpm-state/kernel/installing_core_6.15.10-402.asahi.aarch64+debug
  /bin/kernel-install add 6.15.10-402.asahi.aarch64+debug /lib/modules/6.15.10-402.asahi.aarch64+debug/vmlinuz || exit $?
  if [[ ! -e "/boot/symvers-6.15.10-402.asahi.aarch64+debug.xz" ]]; then
      cp "/lib/modules/6.15.10-402.asahi.aarch64+debug/symvers.xz" "/boot/symvers-6.15.10-402.asahi.aarch64+debug.xz"
      if command -v restorecon &>/dev/null; then
          restorecon "/boot/symvers-6.15.10-402.asahi.aarch64+debug.xz"
      fi
  fi

  %post debug-core

  mkdir -p /var/lib/rpm-state/kernel
  touch /var/lib/rpm-state/kernel/installing_core_6.15.10-402.asahi.aarch64+debug

  %preun 16k-core
  /bin/kernel-install remove 6.15.10-402.asahi.aarch64+16k || exit $?
  if [ -x /usr/bin/weak-modules ]
  then
      /usr/bin/weak-modules --remove-kernel 6.15.10-402.asahi.aarch64+16k || exit $?
  fi

  %post 16k-devel
  if [ -f /etc/sysconfig/kernel ]
  then
      . /etc/sysconfig/kernel || exit $?
  fi
  if [ "$HARDLINK" != "no" -a -x /usr/bin/hardlink -a ! -e /run/ostree-booted ] 
  then
      (cd /usr/src/kernels/6.15.10-402.asahi.aarch64+16k &&
       /usr/bin/find . -type f | while read f; do
         hardlink -c /usr/src/kernels/*.*/$f $f > /dev/null
       done;
       /usr/bin/find /usr/src/kernels -type f -name '*.hardlink-temporary' -delete
      )
  fi

  %post 16k-modules
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+16k
  if [ ! -f /var/lib/rpm-state/kernel/installing_core_6.15.10-402.asahi.aarch64+16k ]; then
  	mkdir -p /var/lib/rpm-state/kernel
  	touch /var/lib/rpm-state/kernel/need_to_run_dracut_6.15.10-402.asahi.aarch64+16k
  fi

  %postun 16k-modules
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+16k

  %posttrans 16k-modules
  if [ -f /var/lib/rpm-state/kernel/need_to_run_dracut_6.15.10-402.asahi.aarch64+16k ]; then
  	rm -f /var/lib/rpm-state/kernel/need_to_run_dracut_6.15.10-402.asahi.aarch64+16k
  	echo "Running: dracut -f --kver 6.15.10-402.asahi.aarch64+16k"
  	dracut -f --kver "6.15.10-402.asahi.aarch64+16k" || exit $?
  fi

  %posttrans 16k-modules-core
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+16k

  %post 16k-modules-extra
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+16k

  %postun 16k-modules-extra
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+16k

  %post 16k-modules-internal
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+16k

  %postun 16k-modules-internal
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+16k

  %posttrans 16k-core
  rm -f /var/lib/rpm-state/kernel/installing_core_6.15.10-402.asahi.aarch64+16k
  /bin/kernel-install add 6.15.10-402.asahi.aarch64+16k /lib/modules/6.15.10-402.asahi.aarch64+16k/vmlinuz || exit $?
  if [[ ! -e "/boot/symvers-6.15.10-402.asahi.aarch64+16k.xz" ]]; then
      cp "/lib/modules/6.15.10-402.asahi.aarch64+16k/symvers.xz" "/boot/symvers-6.15.10-402.asahi.aarch64+16k.xz"
      if command -v restorecon &>/dev/null; then
          restorecon "/boot/symvers-6.15.10-402.asahi.aarch64+16k.xz"
      fi
  fi

  %post 16k-core

  mkdir -p /var/lib/rpm-state/kernel
  touch /var/lib/rpm-state/kernel/installing_core_6.15.10-402.asahi.aarch64+16k

  %preun 16k-debug-core
  /bin/kernel-install remove 6.15.10-402.asahi.aarch64+16k-debug || exit $?
  if [ -x /usr/bin/weak-modules ]
  then
      /usr/bin/weak-modules --remove-kernel 6.15.10-402.asahi.aarch64+16k-debug || exit $?
  fi

  %post 16k-debug-devel
  if [ -f /etc/sysconfig/kernel ]
  then
      . /etc/sysconfig/kernel || exit $?
  fi
  if [ "$HARDLINK" != "no" -a -x /usr/bin/hardlink -a ! -e /run/ostree-booted ] 
  then
      (cd /usr/src/kernels/6.15.10-402.asahi.aarch64+16k-debug &&
       /usr/bin/find . -type f | while read f; do
         hardlink -c /usr/src/kernels/*.*/$f $f > /dev/null
       done;
       /usr/bin/find /usr/src/kernels -type f -name '*.hardlink-temporary' -delete
      )
  fi

  %post 16k-debug-modules
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+16k-debug
  if [ ! -f /var/lib/rpm-state/kernel/installing_core_6.15.10-402.asahi.aarch64+16k-debug ]; then
  	mkdir -p /var/lib/rpm-state/kernel
  	touch /var/lib/rpm-state/kernel/need_to_run_dracut_6.15.10-402.asahi.aarch64+16k-debug
  fi

  %postun 16k-debug-modules
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+16k-debug

  %posttrans 16k-debug-modules
  if [ -f /var/lib/rpm-state/kernel/need_to_run_dracut_6.15.10-402.asahi.aarch64+16k-debug ]; then
  	rm -f /var/lib/rpm-state/kernel/need_to_run_dracut_6.15.10-402.asahi.aarch64+16k-debug
  	echo "Running: dracut -f --kver 6.15.10-402.asahi.aarch64+16k-debug"
  	dracut -f --kver "6.15.10-402.asahi.aarch64+16k-debug" || exit $?
  fi

  %posttrans 16k-debug-modules-core
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+16k-debug

  %post 16k-debug-modules-extra
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+16k-debug

  %postun 16k-debug-modules-extra
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+16k-debug

  %post 16k-debug-modules-internal
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+16k-debug

  %postun 16k-debug-modules-internal
  /sbin/depmod -a 6.15.10-402.asahi.aarch64+16k-debug

  %posttrans 16k-debug-core
  rm -f /var/lib/rpm-state/kernel/installing_core_6.15.10-402.asahi.aarch64+16k-debug
  /bin/kernel-install add 6.15.10-402.asahi.aarch64+16k-debug /lib/modules/6.15.10-402.asahi.aarch64+16k-debug/vmlinuz || exit $?
  if [[ ! -e "/boot/symvers-6.15.10-402.asahi.aarch64+16k-debug.xz" ]]; then
      cp "/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/symvers.xz" "/boot/symvers-6.15.10-402.asahi.aarch64+16k-debug.xz"
      if command -v restorecon &>/dev/null; then
          restorecon "/boot/symvers-6.15.10-402.asahi.aarch64+16k-debug.xz"
      fi
  fi

  %post 16k-debug-core

  mkdir -p /var/lib/rpm-state/kernel
  touch /var/lib/rpm-state/kernel/installing_core_6.15.10-402.asahi.aarch64+16k-debug

  %posttrans 16k-debug-uki-virt
  rm -f /var/lib/rpm-state/kernel/installing_core_6.15.10-402.asahi.aarch64+16k-debug
  /bin/kernel-install add 6.15.10-402.asahi.aarch64+16k-debug /lib/modules/6.15.10-402.asahi.aarch64+16k-debug/vmlinuz-virt.efi || exit $?
  if [[ ! -e "/boot/symvers-6.15.10-402.asahi.aarch64+16k-debug.xz" ]]; then
      cp "/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/symvers.xz" "/boot/symvers-6.15.10-402.asahi.aarch64+16k-debug.xz"
      if command -v restorecon &>/dev/null; then
          restorecon "/boot/symvers-6.15.10-402.asahi.aarch64+16k-debug.xz"
      fi
  fi

  %preun 16k-debug-uki-virt
  /bin/kernel-install remove 6.15.10-402.asahi.aarch64+16k-debug || exit $?
  if [ -x /usr/bin/weak-modules ]
  then
      /usr/bin/weak-modules --remove-kernel 6.15.10-402.asahi.aarch64+16k-debug || exit $?
  fi

  %posttrans 16k-uki-virt
  rm -f /var/lib/rpm-state/kernel/installing_core_6.15.10-402.asahi.aarch64+16k
  /bin/kernel-install add 6.15.10-402.asahi.aarch64+16k /lib/modules/6.15.10-402.asahi.aarch64+16k/vmlinuz-virt.efi || exit $?
  if [[ ! -e "/boot/symvers-6.15.10-402.asahi.aarch64+16k.xz" ]]; then
      cp "/lib/modules/6.15.10-402.asahi.aarch64+16k/symvers.xz" "/boot/symvers-6.15.10-402.asahi.aarch64+16k.xz"
      if command -v restorecon &>/dev/null; then
          restorecon "/boot/symvers-6.15.10-402.asahi.aarch64+16k.xz"
      fi
  fi

  %preun 16k-uki-virt
  /bin/kernel-install remove 6.15.10-402.asahi.aarch64+16k || exit $?
  if [ -x /usr/bin/weak-modules ]
  then
      /usr/bin/weak-modules --remove-kernel 6.15.10-402.asahi.aarch64+16k || exit $?
  fi

  ###
  ### file lists
  ###

  # -f debugfiles.list debuginfo-common-aarch64

  # headers
  _install fakeinstall/usr/include/*
  %exclude /usr/include/cpufreq.h
  %exclude /usr/include/ynl

  # -n perf
  _install fakeinstall/usr/bin/perf
  _install fakeinstall/usr/lib/libperf-jvmti.so
  install -m755 -d ${pkgdir}/usr/lib/linux-asahi/perf-core
  _install fakeinstall/usr/lib/linux-asahi/perf-core/*
  _install fakeinstall/usr/share/man/man[1-8]/perf*
  _install fakeinstall/etc/bash_completion.d/perf
  install -Dpm0755 -t ${pkgdir}/usr/share/doc/linux-asahi/  linux-6.15.10-402.asahi.aarch64/tools/perf/Documentation/examples.txt
  _install fakeinstall/usr/share/doc/perf-tip/tips.txt
  _install fakeinstall/usr/include/perf/perf_dlfilter.h

  # -n python3-perf
  %{python3_sitearch}/*

  # -f perf-debuginfo.list -n perf-debuginfo

  # -f python3-perf-debuginfo.list -n python3-perf-debuginfo

  # -n libperf
  _install fakeinstall/usr/lib/libperf.so.0
  _install fakeinstall/usr/lib/libperf.so.0.0.1

  # -n libperf-devel
  _install fakeinstall/usr/lib/libperf.so
  _install fakeinstall/usr/lib/pkgconfig/libperf.pc
  _install fakeinstall/usr/include/internal/*.h
  _install fakeinstall/usr/include/perf/bpf_perf.h
  _install fakeinstall/usr/include/perf/core.h
  _install fakeinstall/usr/include/perf/cpumap.h
  _install fakeinstall/usr/include/perf/event.h
  _install fakeinstall/usr/include/perf/evlist.h
  _install fakeinstall/usr/include/perf/evsel.h
  _install fakeinstall/usr/include/perf/mmap.h
  _install fakeinstall/usr/include/perf/threadmap.h
  _install fakeinstall/usr/share/man/man3/libperf.3.gz
  _install fakeinstall/usr/share/man/man7/libperf-counting.7.gz
  _install fakeinstall/usr/share/man/man7/libperf-sampling.7.gz
  _install fakeinstall/usr/share/doc/libperf/examples/sampling.c
  _install fakeinstall/usr/share/doc/libperf/examples/counting.c
  _install fakeinstall/usr/share/doc/libperf/html/libperf.html
  _install fakeinstall/usr/share/doc/libperf/html/libperf-counting.html
  _install fakeinstall/usr/share/doc/libperf/html/libperf-sampling.html

  # -f libperf-debuginfo.list -n libperf-debuginfo

  # -n kernel-tools -f cpupower.lang
  _install fakeinstall/usr/bin/cpupower
  _install fakeinstall/usr/share/bash-completion/completions/cpupower
  _install fakeinstall/usr/share/man/man[1-8]/cpupower*
  _install fakeinstall/usr/bin/tmon
  _install fakeinstall/usr/bin/bootconfig
  _install fakeinstall/usr/bin/iio_event_monitor
  _install fakeinstall/usr/bin/iio_generic_buffer
  _install fakeinstall/usr/bin/lsiio
  _install fakeinstall/usr/bin/lsgpio
  _install fakeinstall/usr/bin/gpio-hammer
  _install fakeinstall/usr/bin/gpio-event-mon
  _install fakeinstall/usr/bin/gpio-watch
  _install fakeinstall/usr/share/man/man1/kvm_stat*
  _install fakeinstall/usr/bin/kvm_stat
  %{_unitdir}/kvm_stat.service
  %config(noreplace) /etc/logrotate.d/kvm_stat
  _install fakeinstall/usr/bin/page_owner_sort
  _install fakeinstall/usr/bin/slabinfo
  _install fakeinstall/usr/bin/ynl*
  _install fakeinstall/usr/share/doc/ynl
  _install fakeinstall/usr/share/ynl
  %{python3_sitelib}/pyynl*

  # -f kernel-tools-debuginfo.list -n kernel-tools-debuginfo

  # -n kernel-tools-libs
  _install fakeinstall/usr/lib/libcpupower.so.1
  _install fakeinstall/usr/lib/libcpupower.so.1.0.1

  # -n kernel-tools-libs-devel
  _install fakeinstall/usr/lib/libcpupower.so
  _install fakeinstall/usr/include/cpufreq.h
  _install fakeinstall/usr/include/cpuidle.h
  _install fakeinstall/usr/include/powercap.h
  _install fakeinstall/usr/lib/libynl*
  _install fakeinstall/usr/include/ynl

  # -n rtla
  _install fakeinstall/usr/bin/rtla
  _install fakeinstall/usr/bin/hwnoise
  _install fakeinstall/usr/bin/osnoise
  _install fakeinstall/usr/bin/timerlat
  _install fakeinstall/usr/share/man/man1/rtla-hwnoise.1.gz
  _install fakeinstall/usr/share/man/man1/rtla-osnoise-hist.1.gz
  _install fakeinstall/usr/share/man/man1/rtla-osnoise-top.1.gz
  _install fakeinstall/usr/share/man/man1/rtla-osnoise.1.gz
  _install fakeinstall/usr/share/man/man1/rtla-timerlat-hist.1.gz
  _install fakeinstall/usr/share/man/man1/rtla-timerlat-top.1.gz
  _install fakeinstall/usr/share/man/man1/rtla-timerlat.1.gz
  _install fakeinstall/usr/share/man/man1/rtla.1.gz

  # -n rv
  _install fakeinstall/usr/bin/rv
  _install fakeinstall/usr/share/man/man1/rv-list.1.gz
  _install fakeinstall/usr/share/man/man1/rv-mon-wip.1.gz
  _install fakeinstall/usr/share/man/man1/rv-mon-wwnr.1.gz
  _install fakeinstall/usr/share/man/man1/rv-mon.1.gz
  _install fakeinstall/usr/share/man/man1/rv-mon-sched.1.gz
  _install fakeinstall/usr/share/man/man1/rv.1.gz

  # selftests-internal
  _install fakeinstall/usr/lib/linux-asahi/ksamples
  _install fakeinstall/usr/lib/linux-asahi/kselftests

  # A spec %files section (it could be that part of the next lines duplicate part of the package() function)

  # -f kernel-ldsoconf.list core

  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/linux-asahi/ linux-6.15.10-402.asahi.aarch64/COPYING-6.15.10-402.asahi
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/vmlinuz
  %ghost /boot/vmlinuz-6.15.10-402.asahi.aarch64
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/.vmlinuz.hmac 
  %ghost /boot/.vmlinuz-6.15.10-402.asahi.aarch64.hmac 
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/dtb 
  %ghost /boot/dtb-6.15.10-402.asahi.aarch64 
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/System.map
  %ghost /boot/System.map-6.15.10-402.asahi.aarch64
  install -m755 -d ${pkgdir}/lib/modules
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/symvers.xz
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/config
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/modules.builtin*
  %ghost %attr(0644, root, root) /boot/symvers-6.15.10-402.asahi.aarch64.xz
  %ghost %attr(0600, root, root) /boot/initramfs-6.15.10-402.asahi.aarch64.img
  %ghost %attr(0644, root, root) /boot/config-6.15.10-402.asahi.aarch64
  # -f kernel-modules-core.list modules-core
  install -m755 -d ${pkgdir}/lib/modules
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64/kernel
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/build
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/source
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/updates
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/weak-updates
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/systemtap
  _install fakeinstall/usr/share/doc/kernel-keys/6.15.10-402.asahi.aarch64
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/vdso
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/modules.block
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/modules.drm
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/modules.modesetting
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/modules.networking
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/modules.order
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64/modules.alias
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64/modules.alias.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64/modules.builtin.alias.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64/modules.builtin.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64/modules.dep
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64/modules.dep.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64/modules.devname
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64/modules.softdep
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64/modules.symbols
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64/modules.symbols.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64/modules.weakdep
  # -f kernel-modules.list modules
  # devel
  %defverify(not mtime)
  _install fakeinstall/usr/src/kernels/6.15.10-402.asahi.aarch64
  # devel-matched
  # -f kernel-modules-extra.list modules-extra
  # -f kernel-modules-internal.list modules-internal
  # -f debuginfo.list debuginfo
  # uki-virt
  install -m755 -d ${pkgdir}/lib/modules
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/System.map
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/symvers.xz
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/config
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/modules.builtin*
  %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64/vmlinuz-virt.efi
  %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64/.vmlinuz-virt.efi.hmac
  %ghost /boot/efi/EFI/Linux/*-6.15.10-402.asahi.aarch64.efi
  # uki-virt-addons
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64/vmlinuz-virt.efi.extra.d/ 
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64/vmlinuz-virt.efi.extra.d/*.addon.efi

  # -f kernel-debug-ldsoconf.list debug-core

  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/linux-asahi/ linux-6.15.10-402.asahi.aarch64/COPYING-6.15.10-402.asahi
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/vmlinuz
  %ghost /boot/vmlinuz-6.15.10-402.asahi.aarch64+debug
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/.vmlinuz.hmac 
  %ghost /boot/.vmlinuz-6.15.10-402.asahi.aarch64+debug.hmac 
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/dtb 
  %ghost /boot/dtb-6.15.10-402.asahi.aarch64+debug 
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/System.map
  %ghost /boot/System.map-6.15.10-402.asahi.aarch64+debug
  install -m755 -d ${pkgdir}/lib/modules
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64+debug
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/symvers.xz
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/config
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/modules.builtin*
  %ghost %attr(0644, root, root) /boot/symvers-6.15.10-402.asahi.aarch64+debug.xz
  %ghost %attr(0600, root, root) /boot/initramfs-6.15.10-402.asahi.aarch64+debug.img
  %ghost %attr(0644, root, root) /boot/config-6.15.10-402.asahi.aarch64+debug
  # -f kernel-debug-modules-core.list debug-modules-core
  install -m755 -d ${pkgdir}/lib/modules
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64+debug
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64+debug/kernel
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/build
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/source
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/updates
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/weak-updates
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/systemtap
  _install fakeinstall/usr/share/doc/kernel-keys/6.15.10-402.asahi.aarch64+debug
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/vdso
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/modules.block
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/modules.drm
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/modules.modesetting
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/modules.networking
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/modules.order
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+debug/modules.alias
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+debug/modules.alias.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+debug/modules.builtin.alias.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+debug/modules.builtin.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+debug/modules.dep
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+debug/modules.dep.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+debug/modules.devname
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+debug/modules.softdep
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+debug/modules.symbols
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+debug/modules.symbols.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+debug/modules.weakdep
  # -f kernel-debug-modules.list debug-modules
  # debug-devel
  %defverify(not mtime)
  _install fakeinstall/usr/src/kernels/6.15.10-402.asahi.aarch64+debug
  # debug-devel-matched
  # -f kernel-debug-modules-extra.list debug-modules-extra
  # -f kernel-debug-modules-internal.list debug-modules-internal
  # -f debuginfodebug.list debug-debuginfo
  # debug-uki-virt
  install -m755 -d ${pkgdir}/lib/modules
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64+debug
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/System.map
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/symvers.xz
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/config
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/modules.builtin*
  %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+debug/vmlinuz-virt.efi
  %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+debug/.vmlinuz-virt.efi.hmac
  %ghost /boot/efi/EFI/Linux/*-6.15.10-402.asahi.aarch64+debug.efi
  # debug-uki-virt-addons
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64+debug/vmlinuz-virt.efi.extra.d/ 
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+debug/vmlinuz-virt.efi.extra.d/*.addon.efi
  # debug

  # -f kernel-16k-debug-ldsoconf.list 16k-debug-core

  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/linux-asahi/ linux-6.15.10-402.asahi.aarch64/COPYING-6.15.10-402.asahi
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/vmlinuz
  %ghost /boot/vmlinuz-6.15.10-402.asahi.aarch64+16k-debug
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/.vmlinuz.hmac 
  %ghost /boot/.vmlinuz-6.15.10-402.asahi.aarch64+16k-debug.hmac 
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/dtb 
  %ghost /boot/dtb-6.15.10-402.asahi.aarch64+16k-debug 
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/System.map
  %ghost /boot/System.map-6.15.10-402.asahi.aarch64+16k-debug
  install -m755 -d ${pkgdir}/lib/modules
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64+16k-debug
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/symvers.xz
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/config
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/modules.builtin*
  %ghost %attr(0644, root, root) /boot/symvers-6.15.10-402.asahi.aarch64+16k-debug.xz
  %ghost %attr(0600, root, root) /boot/initramfs-6.15.10-402.asahi.aarch64+16k-debug.img
  %ghost %attr(0644, root, root) /boot/config-6.15.10-402.asahi.aarch64+16k-debug
  # -f kernel-16k-debug-modules-core.list 16k-debug-modules-core
  install -m755 -d ${pkgdir}/lib/modules
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64+16k-debug
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/kernel
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/build
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/source
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/updates
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/weak-updates
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/systemtap
  _install fakeinstall/usr/share/doc/kernel-keys/6.15.10-402.asahi.aarch64+16k-debug
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/vdso
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/modules.block
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/modules.drm
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/modules.modesetting
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/modules.networking
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/modules.order
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k-debug/modules.alias
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k-debug/modules.alias.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k-debug/modules.builtin.alias.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k-debug/modules.builtin.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k-debug/modules.dep
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k-debug/modules.dep.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k-debug/modules.devname
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k-debug/modules.softdep
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k-debug/modules.symbols
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k-debug/modules.symbols.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k-debug/modules.weakdep
  # -f kernel-16k-debug-modules.list 16k-debug-modules
  # 16k-debug-devel
  %defverify(not mtime)
  _install fakeinstall/usr/src/kernels/6.15.10-402.asahi.aarch64+16k-debug
  # 16k-debug-devel-matched
  # -f kernel-16k-debug-modules-extra.list 16k-debug-modules-extra
  # -f kernel-16k-debug-modules-internal.list 16k-debug-modules-internal
  # -f debuginfo16k-debug.list 16k-debug-debuginfo
  # 16k-debug-uki-virt
  install -m755 -d ${pkgdir}/lib/modules
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64+16k-debug
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/System.map
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/symvers.xz
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/config
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/modules.builtin*
  %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k-debug/vmlinuz-virt.efi
  %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k-debug/.vmlinuz-virt.efi.hmac
  %ghost /boot/efi/EFI/Linux/*-6.15.10-402.asahi.aarch64+16k-debug.efi
  # 16k-debug-uki-virt-addons
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/vmlinuz-virt.efi.extra.d/ 
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k-debug/vmlinuz-virt.efi.extra.d/*.addon.efi
  # 16k-debug

  # -f kernel-16k-ldsoconf.list 16k-core

  install -Dpm0755 -t ${pkgdir}/usr/share/licenses/linux-asahi/ linux-6.15.10-402.asahi.aarch64/COPYING-6.15.10-402.asahi
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/vmlinuz
  %ghost /boot/vmlinuz-6.15.10-402.asahi.aarch64+16k
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/.vmlinuz.hmac 
  %ghost /boot/.vmlinuz-6.15.10-402.asahi.aarch64+16k.hmac 
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/dtb 
  %ghost /boot/dtb-6.15.10-402.asahi.aarch64+16k 
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/System.map
  %ghost /boot/System.map-6.15.10-402.asahi.aarch64+16k
  install -m755 -d ${pkgdir}/lib/modules
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64+16k
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/symvers.xz
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/config
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/modules.builtin*
  %ghost %attr(0644, root, root) /boot/symvers-6.15.10-402.asahi.aarch64+16k.xz
  %ghost %attr(0600, root, root) /boot/initramfs-6.15.10-402.asahi.aarch64+16k.img
  %ghost %attr(0644, root, root) /boot/config-6.15.10-402.asahi.aarch64+16k
  # -f kernel-16k-modules-core.list 16k-modules-core
  install -m755 -d ${pkgdir}/lib/modules
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64+16k
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64+16k/kernel
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/build
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/source
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/updates
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/weak-updates
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/systemtap
  _install fakeinstall/usr/share/doc/kernel-keys/6.15.10-402.asahi.aarch64+16k
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/vdso
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/modules.block
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/modules.drm
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/modules.modesetting
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/modules.networking
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/modules.order
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k/modules.alias
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k/modules.alias.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k/modules.builtin.alias.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k/modules.builtin.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k/modules.dep
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k/modules.dep.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k/modules.devname
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k/modules.softdep
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k/modules.symbols
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k/modules.symbols.bin
  %ghost %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k/modules.weakdep
  # -f kernel-16k-modules.list 16k-modules
  # 16k-devel
  %defverify(not mtime)
  _install fakeinstall/usr/src/kernels/6.15.10-402.asahi.aarch64+16k
  # 16k-devel-matched
  # -f kernel-16k-modules-extra.list 16k-modules-extra
  # -f kernel-16k-modules-internal.list 16k-modules-internal
  # -f debuginfo16k.list 16k-debuginfo
  # 16k-uki-virt
  install -m755 -d ${pkgdir}/lib/modules
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64+16k
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/System.map
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/symvers.xz
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/config
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/modules.builtin*
  %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k/vmlinuz-virt.efi
  %attr(0644, root, root) /lib/modules/6.15.10-402.asahi.aarch64+16k/.vmlinuz-virt.efi.hmac
  %ghost /boot/efi/EFI/Linux/*-6.15.10-402.asahi.aarch64+16k.efi
  # 16k-uki-virt-addons
  install -m755 -d ${pkgdir}/lib/modules/6.15.10-402.asahi.aarch64+16k/vmlinuz-virt.efi.extra.d/ 
  _install fakeinstall/lib/modules/6.15.10-402.asahi.aarch64+16k/vmlinuz-virt.efi.extra.d/*.addon.efi
  # 16k

  # modules-extra-matched
}
