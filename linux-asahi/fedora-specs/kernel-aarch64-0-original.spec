# All Global changes to build and install go here.
# Per the below section about __spec_install_pre, any rpm
# environment changes that affect %%install need to go
# here before the %%install macro is pre-built.

# Disable frame pointers
%undefine _include_frame_pointers

# Disable LTO in userspace packages.
%global _lto_cflags %{nil}

# Option to enable compiling with clang instead of gcc.
%bcond_with toolchain_clang

%if %{with toolchain_clang}
%global toolchain clang
%endif

# Compile the kernel with LTO (only supported when building with clang).
%bcond_with clang_lto

%if %{with clang_lto} && %{without toolchain_clang}
{error:clang_lto requires --with toolchain_clang}
%endif

# RPM macros strip everything in BUILDROOT, either with __strip
# or find-debuginfo.sh. Make use of __spec_install_post override
# and save/restore binaries we want to package as unstripped.
%define buildroot_unstripped %{_builddir}/root_unstripped
%define buildroot_save_unstripped() \
(cd %{buildroot}; cp -rav --parents -t %{buildroot_unstripped}/ %1 || true) \
%{nil}
%define __restore_unstripped_root_post \
    echo "Restoring unstripped artefacts %{buildroot_unstripped} -> %{buildroot}" \
    cp -rav %{buildroot_unstripped}/. %{buildroot}/ \
%{nil}

# The kernel's %%install section is special
# Normally the %%install section starts by cleaning up the BUILD_ROOT
# like so:
#
# %%__spec_install_pre %%{___build_pre}\
#     [ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "${RPM_BUILD_ROOT}"\
#     mkdir -p `dirname "$RPM_BUILD_ROOT"`\
#     mkdir "$RPM_BUILD_ROOT"\
# %%{nil}
#
# But because of kernel variants, the %%build section, specifically
# BuildKernel(), moves each variant to its final destination as the
# variant is built.  This violates the expectation of the %%install
# section.  As a result we snapshot the current env variables and
# purposely leave out the removal section.  All global wide changes
# should be added above this line otherwise the %%install section
# will not see them.
%global __spec_install_pre %{___build_pre}

# Replace '-' with '_' where needed so that variants can use '-' in
# their name.
%define uname_suffix() %{lua:
	local flavour = rpm.expand('%{?1:+%{1}}')
	flavour = flavour:gsub('-', '_')
	if flavour ~= '' then
		print(flavour)
	end
}

# This returns the main kernel tied to a debug variant. For example,
# kernel-debug is the debug version of kernel, so we return an empty
# string. However, kernel-64k-debug is the debug version of kernel-64k,
# in this case we need to return "64k", and so on. This is used in
# macros below where we need this for some uname based requires.
%define uname_variant() %{lua:
	local flavour = rpm.expand('%{?1:%{1}}')
	_, _, main, sub = flavour:find("(%w+)-(.*)")
	if main then
		print("+" .. main)
	end
}


# At the time of this writing (2019-03), RHEL8 packages use w2.xzdio
# compression for rpms (xz, level 2).
# Kernel has several large (hundreds of mbytes) rpms, they take ~5 mins
# to compress by single-threaded xz. Switch to threaded compression,
# and from level 2 to 3 to keep compressed sizes close to "w2" results.
#
# NB: if default compression in /usr/lib/rpm/redhat/macros ever changes,
# this one might need tweaking (e.g. if default changes to w3.xzdio,
# change below to w4T.xzdio):
#
# This is disabled on i686 as it triggers oom errors

%ifnarch i686
%define _binary_payload w3T.xzdio
%endif

Summary: The Linux kernel
%if 0%{?fedora}
%define secure_boot_arch x86_64
%else
%define secure_boot_arch x86_64 aarch64 s390x ppc64le
%endif

# Signing for secure boot authentication
%ifarch %{secure_boot_arch}
%global signkernel 1
%else
%global signkernel 0
%endif

# Sign modules on all arches
%global signmodules 1

# Compress modules only for architectures that build modules
%ifarch noarch
%global zipmodules 0
%else
%global zipmodules 1
%endif

# Default compression algorithm
%global compression xz
%global compression_flags --compress --check=crc32 --lzma2=dict=1MiB
%global compext xz

%if 0%{?fedora}
%define primary_target fedora
%else
%define primary_target rhel
%endif

#
# genspec.sh variables
#

# kernel package name
%global package_name kernel
%global gemini 0
# Include Fedora files
%global include_fedora 1
# Include RHEL files
%global include_rhel 1
# Include RT files
%global include_rt 1
# Include Automotive files
%global include_automotive 1
# Provide Patchlist.changelog file
%global patchlist_changelog 1
# Set released_kernel to 1 when the upstream source tarball contains a
#  kernel release. (This includes prepatch or "rc" releases.)
# Set released_kernel to 0 when the upstream source tarball contains an
#  unreleased kernel development snapshot.
%global released_kernel 1
# Set debugbuildsenabled to 1 to build separate base and debug kernels
#  (on supported architectures). The kernel-debug-* subpackages will
#  contain the debug kernel.
# Set debugbuildsenabled to 0 to not build a separate debug kernel, but
#  to build the base kernel using the debug configuration. (Specifying
#  the --with-release option overrides this setting.)
%define debugbuildsenabled 1
# define buildid .local
%define specrpmversion 6.15.10
%define specversion 6.15.10
%define patchversion 6.15
%define pkgrelease 402.asahi
%define kversion 6
%define tarfile_release 6.15.10
# This is needed to do merge window version magic
%define patchlevel 15
# This allows pkg_release to have configurable %%{?dist} tag
%define specrelease 402.asahi%{?buildid}%{?dist}
# This defines the kabi tarball version
%define kabiversion 6.15.10

# If this variable is set to 1, a bpf selftests build failure will cause a
# fatal kernel package build error
%define selftests_must_build 0

#
# End of genspec.sh variables
#

%define pkg_release %{specrelease}

# libexec dir is not used by the linker, so the shared object there
# should not be exported to RPM provides
%global __provides_exclude_from ^%{_libexecdir}/kselftests

# The following build options are (mostly) enabled by default, but may become
# enabled/disabled by later architecture-specific checks.
# Where disabled by default, they can be enabled by using --with <opt> in the
# rpmbuild command, or by forcing these values to 1.
# Where enabled by default, they can be disabled by using --without <opt> in
# the rpmbuild command, or by forcing these values to 0.
#
# standard kernel
%define with_up        %{?_without_up:        0} %{?!_without_up:        1}
# build the base variants
%define with_base      %{?_without_base:      0} %{?!_without_base:      1}
# build also debug variants
%define with_debug     %{?_without_debug:     0} %{?!_without_debug:     1}
# kernel-zfcpdump (s390 specific kernel for zfcpdump)
%define with_zfcpdump  %{?_without_zfcpdump:  0} %{?!_without_zfcpdump:  1}
# kernel-16k (aarch64 kernel with 16K page_size)
%define with_arm64_16k %{?_with_arm64_16k:    1} %{?!_with_arm64_16k:    0}
# kernel-64k (aarch64 kernel with 64K page_size)
%define with_arm64_64k %{?_without_arm64_64k: 0} %{?!_without_arm64_64k: 1}
# kernel-rt (x86_64 and aarch64 only PREEMPT_RT enabled kernel)
%define with_realtime  %{?_without_realtime:  0} %{?!_without_realtime:  1}
# kernel-rt-64k (aarch64 RT kernel with 64K page_size)
%define with_realtime_arm64_64k %{?_without_realtime_arm64_64k: 0} %{?!_without_realtime_arm64_64k: 1}
# kernel-automotive (x86_64 and aarch64 with PREEMPT_RT enabled - currently off by default)
%define with_automotive %{?_with_automotive:  1} %{?!_with_automotive:   0}

# Supported variants
#            with_base with_debug    with_gcov
# up         X         X             X
# zfcpdump   X                       X
# arm64_16k  X         X             X
# arm64_64k  X         X             X
# realtime   X         X             X
# automotive X         X             X

# kernel-doc
%define with_doc       %{?_without_doc:       0} %{?!_without_doc:       1}
# kernel-headers
%define with_headers   %{?_without_headers:   0} %{?!_without_headers:   1}
%define with_cross_headers   %{?_without_cross_headers:   0} %{?!_without_cross_headers:   1}
# perf
%define with_perf      %{?_without_perf:      0} %{?!_without_perf:      1}
# libperf
%define with_libperf   %{?_without_libperf:   0} %{?!_without_libperf:   1}
# tools
%define with_tools     %{?_without_tools:     0} %{?!_without_tools:     1}
# ynl
%define with_ynl      %{?_without_ynl:      0} %{?!_without_ynl:      1}
# kernel-debuginfo
%define with_debuginfo %{?_without_debuginfo: 0} %{?!_without_debuginfo: 1}
# kernel-abi-stablelists
%define with_kernel_abi_stablelists %{?_without_kernel_abi_stablelists: 0} %{?!_without_kernel_abi_stablelists: 1}
# internal samples and selftests
%define with_selftests %{?_without_selftests: 0} %{?!_without_selftests: 1}
#
# Additional options for user-friendly one-off kernel building:
#
# Only build the base kernel (--with baseonly):
%define with_baseonly  %{?_with_baseonly:     1} %{?!_with_baseonly:     0}
# Only build the debug variants (--with dbgonly):
%define with_dbgonly   %{?_with_dbgonly:      1} %{?!_with_dbgonly:      0}
# Only build the realtime kernel (--with rtonly):
%define with_rtonly    %{?_with_rtonly:       1} %{?!_with_rtonly:       0}
# Only build the automotive kernel (--with automotiveonly):%
%define with_automotiveonly %{?_with_automotiveonly:       1} %{?!_with_automotiveonly:       0}
# Only build the tools package
%define with_toolsonly %{?_with_toolsonly:    1} %{?!_with_toolsonly:    0}
# Control whether we perform a compat. check against published ABI.
%define with_kabichk   %{?_without_kabichk:   0} %{?!_without_kabichk:   1}
# Temporarily disable kabi checks until RC.
%define with_kabichk 0
# Control whether we perform a compat. check against DUP ABI.
%define with_kabidupchk %{?_with_kabidupchk:  1} %{?!_with_kabidupchk:   0}
#
# Control whether to run an extensive DWARF based kABI check.
# Note that this option needs to have baseline setup in SOURCE300.
%define with_kabidwchk %{?_without_kabidwchk: 0} %{?!_without_kabidwchk: 1}
%define with_kabidw_base %{?_with_kabidw_base: 1} %{?!_with_kabidw_base: 0}
#
# Control whether to install the vdso directories.
%define with_vdso_install %{?_without_vdso_install: 0} %{?!_without_vdso_install: 1}
#
# should we do C=1 builds with sparse
%define with_sparse    %{?_with_sparse:       1} %{?!_with_sparse:       0}
#
# Cross compile requested?
%define with_cross    %{?_with_cross:         1} %{?!_with_cross:        0}
#
# build a release kernel on rawhide
%define with_release   %{?_with_release:      1} %{?!_with_release:      0}

# verbose build, i.e. no silent rules and V=1
%define with_verbose %{?_with_verbose:        1} %{?!_with_verbose:      0}

#
# check for mismatched config options
%define with_configchecks %{?_without_configchecks:        0} %{?!_without_configchecks:        1}

#
# gcov support
%define with_gcov %{?_with_gcov:1}%{?!_with_gcov:0}

# Want to build a vanilla kernel build without any non-upstream patches?
%define with_vanilla %{?_with_vanilla: 1} %{?!_with_vanilla: 0}

%ifarch x86_64 aarch64 riscv64
%define with_efiuki %{?_without_efiuki: 0} %{?!_without_efiuki: 1}
%else
%define with_efiuki 0
%endif

%if 0%{?fedora}
# Kernel headers are being split out into a separate package
%define with_headers 1
%define with_cross_headers 0
# no stablelist
%define with_kernel_abi_stablelists 0
%define with_arm64_16k 1
%define with_arm64_64k 0
%define with_realtime 0
%define with_realtime_arm64_64k 0
%define with_automotive 0
# for debugging issues with build process
%define with_verbose 1
%endif

%if %{with_verbose}
%define make_opts V=1
%else
%define make_opts -s
%endif

%if 0%{?fedora} >= 41 || 0%{?rhel} >= 9
%global perf_libbpf_dynamic LIBBPF_DYNAMIC=1
%endif

%if %{with toolchain_clang}
%ifarch s390x ppc64le
%global llvm_ias 0
%else
%global llvm_ias 1
%endif
%global clang_make_opts HOSTCC=clang CC=clang LLVM_IAS=%{llvm_ias}
%if %{with clang_lto}
# LLVM=1 enables use of all LLVM tools.
%global clang_make_opts %{clang_make_opts} LLVM=1
%endif
%global make_opts %{make_opts} %{clang_make_opts}
%endif

# turn off debug kernel and kabichk for gcov builds
%if %{with_gcov}
%define with_debug 0
%define with_kabichk 0
%define with_kabidupchk 0
%define with_kabidwchk 0
%define with_kabidw_base 0
%define with_kernel_abi_stablelists 0
%endif

# turn off kABI DWARF-based check if we're generating the base dataset
%if %{with_kabidw_base}
%define with_kabidwchk 0
%endif

%define make_target bzImage
%define image_install_path boot

%define KVERREL %{specversion}-%{release}.%{_target_cpu}
%define KVERREL_RE %(echo %KVERREL | sed 's/+/[+]/g')
%define hdrarch %_target_cpu
%define asmarch %_target_cpu

%if 0%{!?nopatches:1}
%define nopatches 0
%endif

%if %{with_vanilla}
%define nopatches 1
%endif

%if %{with_release}
%define debugbuildsenabled 1
%endif

%if !%{with_debuginfo}
%define _enable_debug_packages 0
%endif
%define debuginfodir /usr/lib/debug
# Needed because we override almost everything involving build-ids
# and debuginfo generation. Currently we rely on the old alldebug setting.
%global _build_id_links alldebug

# if requested, only build base kernel
%if %{with_baseonly}
%define with_debug 0
%define with_realtime 0
%define with_vdso_install 0
%define with_perf 0
%define with_libperf 0
%define with_tools 0
%define with_kernel_abi_stablelists 0
%define with_selftests 0
%endif

# if requested, only build debug kernel
%if %{with_dbgonly}
%define with_base 0
%define with_vdso_install 0
%define with_perf 0
%define with_libperf 0
%define with_tools 0
%define with_kernel_abi_stablelists 0
%define with_selftests 0
%endif

# if requested, only build realtime kernel
%if %{with_rtonly}
%define with_realtime 1
%define with_realtime_arm64_64k 1
%define with_automotive 0
%define with_up 0
%define with_debug 0
%define with_debuginfo 0
%define with_vdso_install 0
%define with_perf 0
%define with_libperf 0
%define with_tools 0
%define with_kernel_abi_stablelists 0
%define with_selftests 0
%define with_headers 0
%define with_efiuki 0
%define with_zfcpdump 0
%define with_arm64_16k 0
%define with_arm64_64k 0
%endif

# if requested, only build automotive kernel
%if %{with_automotiveonly}
%define with_automotive 1
%define with_realtime 0
%define with_up 0
%define with_debug 0
%define with_debuginfo 0
%define with_vdso_install 0
%define with_selftests 1
%endif

# if requested, only build tools
%if %{with_toolsonly}
%define with_tools 1
%define with_up 0
%define with_base 0
%define with_debug 0
%define with_realtime 0
%define with_realtime_arm64_64k 0
%define with_arm64_16k 0
%define with_arm64_64k 0
%define with_automotive 0
%define with_cross_headers 0
%define with_doc 0
%define with_selftests 0
%define with_headers 0
%define with_efiuki 0
%define with_zfcpdump 0
%define with_vdso_install 0
%define with_kabichk 0
%define with_kabidwchk 0
%define with_kabidw_base 0
%define with_kernel_abi_stablelists 0
%define with_selftests 0
%define with_vdso_install 0
%define with_configchecks 0
%endif

# RT and Automotive kernels are only built on x86_64 and aarch64
%ifnarch x86_64 aarch64
%define with_realtime 0
%define with_automotive 0
%endif

%if %{with_automotive}
# overrides compression algorithms for automotive
%global compression zstd
%global compression_flags --rm
%global compext zst

# automotive does not support the following variants
%define with_realtime 0
%define with_realtime_arm64_64k 0
%define with_arm64_16k 0
%define with_arm64_64k 0
%define with_efiuki 0
%define with_doc 0
%define with_headers 0
%define with_cross_headers 0
%define with_perf 0
%define with_libperf 0
%define with_tools 0
%define with_kabichk 0
%define with_kernel_abi_stablelists 0
%define with_kabidw_base 0
%endif


%if %{zipmodules}
%global zipsed -e 's/\.ko$/\.ko.%compext/'
# for parallel xz processes, replace with 1 to go back to single process
%endif

# turn off kABI DUP check and DWARF-based check if kABI check is disabled
%if !%{with_kabichk}
%define with_kabidupchk 0
%define with_kabidwchk 0
%endif

%if %{with_vdso_install}
%define use_vdso 1
%endif

%ifnarch noarch
%define with_kernel_abi_stablelists 0
%endif

# Overrides for generic default options

# only package docs noarch
%ifnarch noarch
%define with_doc 0
%define doc_build_fail true
%endif

%if 0%{?fedora}
# don't do debug builds on anything but aarch64 and x86_64
%ifnarch aarch64 x86_64
%define with_debug 0
%endif
%endif

%define all_configs %{name}-%{specrpmversion}-*.config

# don't build noarch kernels or headers (duh)
%ifarch noarch
%define with_up 0
%define with_realtime 0
%define with_automotive 0
%define with_headers 0
%define with_cross_headers 0
%define with_tools 0
%define with_perf 0
%define with_libperf 0
%define with_selftests 0
%define with_debug 0
%endif

# sparse blows up on ppc
%ifnarch ppc64le
%define with_sparse 0
%endif

# zfcpdump mechanism is s390 only
%ifnarch s390x
%define with_zfcpdump 0
%endif

# 16k and 64k variants only for aarch64
%ifnarch aarch64
%define with_arm64_16k 0
%define with_arm64_64k 0
%define with_realtime_arm64_64k 0
%endif

%if 0%{?fedora}
# This is not for Fedora
%define with_zfcpdump 0
%endif

# Per-arch tweaks

%ifarch i686
%define asmarch x86
%define hdrarch i386
%define kernel_image arch/x86/boot/bzImage
%endif

%ifarch x86_64
%define asmarch x86
%define kernel_image arch/x86/boot/bzImage
%endif

%ifarch ppc64le
%define asmarch powerpc
%define hdrarch powerpc
%define make_target vmlinux
%define kernel_image vmlinux
%define kernel_image_elf 1
%define use_vdso 0
%endif

%ifarch s390x
%define asmarch s390
%define hdrarch s390
%define kernel_image arch/s390/boot/bzImage
%define vmlinux_decompressor arch/s390/boot/vmlinux
%endif

%ifarch aarch64
%define asmarch arm64
%define hdrarch arm64
%define make_target vmlinuz.efi
%define kernel_image arch/arm64/boot/vmlinuz.efi
%endif

%ifarch riscv64
%define asmarch riscv
%define hdrarch riscv
%define make_target vmlinuz.efi
%define kernel_image arch/riscv/boot/vmlinuz.efi
%endif

# Should make listnewconfig fail if there's config options
# printed out?
%if %{nopatches}
%define with_configchecks 0
%endif

# To temporarily exclude an architecture from being built, add it to
# %%nobuildarches. Do _NOT_ use the ExclusiveArch: line, because if we
# don't build kernel-headers then the new build system will no longer let
# us use the previous build of that package -- it'll just be completely AWOL.
# Which is a BadThing(tm).

# We only build kernel-headers on the following...
%if 0%{?fedora}
%define nobuildarches i386
%else
%define nobuildarches i386 i686
%endif

%ifarch %nobuildarches
# disable BuildKernel commands
%define with_up 0
%define with_debug 0
%define with_zfcpdump 0
%define with_arm64_16k 0
%define with_arm64_64k 0
%define with_realtime 0
%define with_realtime_arm64_64k 0
%define with_automotive 0

%define with_debuginfo 0
%define with_perf 0
%define with_libperf 0
%define with_tools 0
%define with_selftests 0
%define _enable_debug_packages 0
%endif

# Architectures we build tools/cpupower on
%if 0%{?fedora}
%define cpupowerarchs %{ix86} x86_64 ppc64le aarch64 riscv64
%else
%define cpupowerarchs i686 x86_64 ppc64le aarch64 riscv64
%endif

# Architectures we build kernel livepatching selftests on
%define klptestarches x86_64 ppc64le s390x

%if 0%{?use_vdso}
%define _use_vdso 1
%else
%define _use_vdso 0
%endif

# If build of debug packages is disabled, we need to know if we want to create
# meta debug packages or not, after we define with_debug for all specific cases
# above. So this must be at the end here, after all cases of with_debug or not.
%define with_debug_meta 0
%if !%{debugbuildsenabled}
%if %{with_debug}
%define with_debug_meta 1
%endif
%define with_debug 0
%endif

# short-hand for "are we building base/non-debug variants of ...?"
%if %{with_up} && %{with_base}
%define with_up_base 1
%else
%define with_up_base 0
%endif
%if %{with_realtime} && %{with_base}
%define with_realtime_base 1
%else
%define with_realtime_base 0
%endif
%if %{with_automotive} && %{with_base}
%define with_automotive_base 1
%else
%define with_automotive_base 0
%endif
%if %{with_arm64_16k} && %{with_base}
%define with_arm64_16k_base 1
%else
%define with_arm64_16k_base 0
%endif
%if %{with_arm64_64k} && %{with_base}
%define with_arm64_64k_base 1
%else
%define with_arm64_64k_base 0
%endif
%if %{with_realtime_arm64_64k} && %{with_base}
%define with_realtime_arm64_64k_base 1
%else
%define with_realtime_arm64_64k_base 0
%endif

#
# Packages that need to be installed before the kernel is, because the %%post
# scripts use them.
#
%define kernel_prereq  coreutils, systemd >= 203-2, /usr/bin/kernel-install
%define initrd_prereq  dracut >= 027


Name: %{package_name}
License: ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-2-Clause) AND ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-3-Clause) AND ((GPL-2.0-only WITH Linux-syscall-note) OR CDDL-1.0) AND ((GPL-2.0-only WITH Linux-syscall-note) OR Linux-OpenIB) AND ((GPL-2.0-only WITH Linux-syscall-note) OR MIT) AND ((GPL-2.0-or-later WITH Linux-syscall-note) OR BSD-3-Clause) AND ((GPL-2.0-or-later WITH Linux-syscall-note) OR MIT) AND 0BSD AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0) AND BSD-3-Clause AND BSD-3-Clause-Clear AND CC0-1.0 AND GFDL-1.1-no-invariants-or-later AND GPL-1.0-or-later AND (GPL-1.0-or-later OR BSD-3-Clause) AND (GPL-1.0-or-later WITH Linux-syscall-note) AND GPL-2.0-only AND (GPL-2.0-only OR Apache-2.0) AND (GPL-2.0-only OR BSD-2-Clause) AND (GPL-2.0-only OR BSD-3-Clause) AND (GPL-2.0-only OR CDDL-1.0) AND (GPL-2.0-only OR GFDL-1.1-no-invariants-or-later) AND (GPL-2.0-only OR GFDL-1.2-no-invariants-only) AND (GPL-2.0-only OR GFDL-1.2-no-invariants-or-later) AND (GPL-2.0-only WITH Linux-syscall-note) AND GPL-2.0-or-later AND (GPL-2.0-or-later OR BSD-2-Clause) AND (GPL-2.0-or-later OR BSD-3-Clause) AND (GPL-2.0-or-later OR CC-BY-4.0) AND (GPL-2.0-or-later WITH GCC-exception-2.0) AND (GPL-2.0-or-later WITH Linux-syscall-note) AND ISC AND LGPL-2.0-or-later AND (LGPL-2.0-or-later OR BSD-2-Clause) AND (LGPL-2.0-or-later WITH Linux-syscall-note) AND LGPL-2.1-only AND (LGPL-2.1-only OR BSD-2-Clause) AND (LGPL-2.1-only WITH Linux-syscall-note) AND LGPL-2.1-or-later AND (LGPL-2.1-or-later WITH Linux-syscall-note) AND (Linux-OpenIB OR GPL-2.0-only) AND (Linux-OpenIB OR GPL-2.0-only OR BSD-2-Clause) AND Linux-man-pages-copyleft AND MIT AND (MIT OR Apache-2.0) AND (MIT OR GPL-2.0-only) AND (MIT OR GPL-2.0-or-later) AND (MIT OR LGPL-2.1-only) AND (MPL-1.1 OR GPL-2.0-only) AND (X11 OR GPL-2.0-only) AND (X11 OR GPL-2.0-or-later) AND Zlib AND (copyleft-next-0.3.1 OR GPL-2.0-or-later)
URL: https://www.kernel.org/
Version: %{specrpmversion}
Release: %{pkg_release}
# DO NOT CHANGE THE 'ExclusiveArch' LINE TO TEMPORARILY EXCLUDE AN ARCHITECTURE BUILD.
# SET %%nobuildarches (ABOVE) INSTEAD
%if 0%{?fedora}
ExclusiveArch: noarch x86_64 s390x aarch64 ppc64le riscv64
%else
ExclusiveArch: noarch i386 i686 x86_64 s390x aarch64 ppc64le
%endif
ExclusiveOS: Linux
%ifnarch %{nobuildarches}
Requires: kernel-core-uname-r = %{KVERREL}
Requires: kernel-modules-uname-r = %{KVERREL}
Requires: kernel-modules-core-uname-r = %{KVERREL}
Requires: ((kernel-modules-extra-uname-r = %{KVERREL}) if kernel-modules-extra-matched)
Provides: installonlypkg(kernel)
%endif


#
# List the packages used during the kernel build
#
BuildRequires: kmod, bash, coreutils, tar, git-core, which
BuildRequires: bzip2, xz, findutils, m4, perl-interpreter, perl-Carp, perl-devel, perl-generators, make, diffutils, gawk, %compression
# Kernel EFI/Compression set by CONFIG_KERNEL_ZSTD
%ifarch x86_64 aarch64 riscv64
BuildRequires: zstd
%endif
BuildRequires: gcc, binutils, redhat-rpm-config, hmaccalc, bison, flex, gcc-c++
BuildRequires: rust, rust-src, bindgen, rustfmt, clippy
BuildRequires: net-tools, hostname, bc, elfutils-devel
BuildRequires: dwarves
BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: python3-pyyaml
BuildRequires: kernel-rpm-macros
# glibc-static is required for a consistent build environment (specifically
# CONFIG_CC_CAN_LINK_STATIC=y).
BuildRequires: glibc-static
%if %{with_headers} || %{with_cross_headers}
BuildRequires: rsync
%endif
%if %{with_doc}
BuildRequires: xmlto, asciidoc, python3-sphinx, python3-sphinx_rtd_theme
%endif
%if %{with_sparse}
BuildRequires: sparse
%endif
%if %{with_perf}
BuildRequires: zlib-devel binutils-devel newt-devel perl(ExtUtils::Embed) bison flex xz-devel
BuildRequires: audit-libs-devel python3-setuptools
BuildRequires: java-devel
BuildRequires: libbpf-devel >= 0.6.0-1
BuildRequires: libbabeltrace-devel
BuildRequires: libtraceevent-devel
%ifnarch s390x
BuildRequires: numactl-devel
%endif
%ifarch aarch64
BuildRequires: opencsd-devel >= 1.0.0
%endif
%endif
%if %{with_tools}
BuildRequires: python3-docutils
BuildRequires: gettext ncurses-devel
BuildRequires: libcap-devel libcap-ng-devel
# The following are rtla requirements
BuildRequires: python3-docutils
BuildRequires: libtraceevent-devel
BuildRequires: libtracefs-devel
BuildRequires: libbpf-devel
BuildRequires: bpftool
BuildRequires: clang

%ifnarch s390x
BuildRequires: pciutils-devel
%endif
%ifarch i686 x86_64
BuildRequires: libnl3-devel
%endif
%endif

%if %{with_tools} && %{with_ynl}
BuildRequires: python3-pyyaml python3-jsonschema python3-pip python3-setuptools >= 61
BuildRequires: (python3-wheel if python3-setuptools < 70)
%endif

%if %{with_tools} || %{signmodules} || %{signkernel}
BuildRequires: openssl-devel
%endif
%if %{with_selftests}
BuildRequires: clang llvm-devel fuse-devel zlib-devel binutils-devel python3-docutils python3-jsonschema
%ifarch x86_64 riscv64
BuildRequires: lld
%endif
BuildRequires: libcap-devel libcap-ng-devel rsync libmnl-devel
BuildRequires: numactl-devel
%endif
BuildConflicts: rhbuildsys(DiskFree) < 500Mb
%if %{with_debuginfo}
BuildRequires: rpm-build, elfutils
BuildConflicts: rpm < 4.13.0.1-19
BuildConflicts: dwarves < 1.13
# Most of these should be enabled after more investigation
%undefine _include_minidebuginfo
%undefine _find_debuginfo_dwz_opts
%undefine _unique_build_ids
%undefine _unique_debug_names
%undefine _unique_debug_srcs
%undefine _debugsource_packages
%undefine _debuginfo_subpackages

# Remove -q option below to provide 'extracting debug info' messages
%global _find_debuginfo_opts -r -q

%global _missing_build_ids_terminate_build 1
%global _no_recompute_build_ids 1
%endif
%if %{with_kabidwchk} || %{with_kabidw_base}
BuildRequires: kabi-dw
%endif

%if %{signkernel}%{signmodules}
BuildRequires: openssl
%if %{signkernel}
# ELN uses Fedora signing process, so exclude
%if 0%{?rhel}%{?centos} && !0%{?eln}
BuildRequires: system-sb-certs
%endif
%ifarch x86_64 aarch64 riscv64
BuildRequires: nss-tools
BuildRequires: pesign >= 0.10-4
%endif
%endif
%endif

%if %{with_cross}
BuildRequires: binutils-%{_build_arch}-linux-gnu, gcc-%{_build_arch}-linux-gnu
%define cross_opts CROSS_COMPILE=%{_build_arch}-linux-gnu-
%define __strip %{_build_arch}-linux-gnu-strip

%if 0%{?fedora} && 0%{?fedora} <= 41
# Work around find-debuginfo for cross builds.
# find-debuginfo doesn't support any of CROSS options (RHEL-21797),
# and since debugedit > 5.0-16.el10, or since commit
#   dfe1f7ff30f4 ("find-debuginfo.sh: Exit with real exit status in parallel jobs")
# it now aborts on failure and build fails.
# debugedit-5.1-5 in F42 added support to override tools with target versions.
%undefine _include_gdb_index
%endif
%endif

# These below are required to build man pages
%if %{with_perf}
BuildRequires: xmlto
%endif
%if %{with_perf} || %{with_tools}
BuildRequires: asciidoc
%endif

%if %{with toolchain_clang}
BuildRequires: clang
%endif

%if %{with clang_lto}
BuildRequires: llvm
BuildRequires: lld
%endif

%if %{with_efiuki}
BuildRequires: dracut
# For dracut UEFI uki binaries
BuildRequires: binutils
# For the initrd
BuildRequires: lvm2
BuildRequires: systemd-boot-unsigned
# For systemd-stub and systemd-pcrphase
BuildRequires: systemd-udev >= 252-1
# For UKI kernel cmdline addons
BuildRequires: systemd-ukify
# For TPM operations in UKI initramfs
BuildRequires: tpm2-tools
# For UKI sb cert
%if 0%{?rhel}%{?centos} && !0%{?eln}
%if 0%{?centos}
BuildRequires: centos-sb-certs >= 9.0-23
%else
BuildRequires: redhat-sb-certs >= 9.4-0.1
%endif
%endif
%endif

# Because this is the kernel, it's hard to get a single upstream URL
# to represent the base without needing to do a bunch of patching. This
# tarball is generated from a src-git tree. If you want to see the
# exact git commit you can run
#
# xzcat -qq ${TARBALL} | git get-tar-commit-id
Source0: linux-%{tarfile_release}.tar.xz

Source1: Makefile.rhelver
Source2: kernel.changelog

Source10: redhatsecurebootca5.cer
Source13: redhatsecureboot501.cer

%if %{signkernel}
# Name of the packaged file containing signing key
%ifarch ppc64le
%define signing_key_filename kernel-signing-ppc.cer
%endif
%ifarch s390x
%define signing_key_filename kernel-signing-s390.cer
%endif

# Fedora/ELN pesign macro expects to see these cert file names, see:
# https://github.com/rhboot/pesign/blob/main/src/pesign-rpmbuild-helper.in#L216
%if 0%{?fedora}%{?eln}
%define pesign_name_0 redhatsecureboot501
%define secureboot_ca_0 %{SOURCE10}
%define secureboot_key_0 %{SOURCE13}
%endif

# RHEL/centos certs come from system-sb-certs
%if 0%{?rhel} && !0%{?eln}
%define secureboot_ca_0 %{_datadir}/pki/sb-certs/secureboot-ca-%{_arch}.cer
%define secureboot_key_0 %{_datadir}/pki/sb-certs/secureboot-kernel-%{_arch}.cer

%if 0%{?centos}
%define pesign_name_0 centossecureboot201
%else
%ifarch x86_64 aarch64
%define pesign_name_0 redhatsecureboot501
%endif
%ifarch s390x
%define pesign_name_0 redhatsecureboot302
%endif
%ifarch ppc64le
%define pesign_name_0 redhatsecureboot701
%endif
%endif
# rhel && !eln
%endif

# signkernel
%endif

Source20: mod-denylist.sh
Source21: mod-sign.sh
Source22: filtermods.py

%define modsign_cmd %{SOURCE21}

%if 0%{?include_rhel}
Source23: x509.genkey.rhel

Source24: %{name}-aarch64-rhel.config
Source25: %{name}-aarch64-debug-rhel.config

Source27: %{name}-ppc64le-rhel.config
Source28: %{name}-ppc64le-debug-rhel.config
Source29: %{name}-s390x-rhel.config
Source30: %{name}-s390x-debug-rhel.config
Source31: %{name}-s390x-zfcpdump-rhel.config
Source32: %{name}-x86_64-rhel.config
Source33: %{name}-x86_64-debug-rhel.config

Source34: def_variants.yaml.rhel

Source41: x509.genkey.centos
# ARM64 64K page-size kernel config
Source42: %{name}-aarch64-64k-rhel.config
Source43: %{name}-aarch64-64k-debug-rhel.config

%endif

%if 0%{?include_fedora}
Source50: x509.genkey.fedora

Source52: %{name}-aarch64-fedora.config
Source53: %{name}-aarch64-debug-fedora.config
Source54: %{name}-aarch64-16k-fedora.config
Source55: %{name}-aarch64-16k-debug-fedora.config
Source56: %{name}-ppc64le-fedora.config
Source57: %{name}-ppc64le-debug-fedora.config
Source58: %{name}-s390x-fedora.config
Source59: %{name}-s390x-debug-fedora.config
Source60: %{name}-x86_64-fedora.config
Source61: %{name}-x86_64-debug-fedora.config
Source700: %{name}-riscv64-fedora.config
Source701: %{name}-riscv64-debug-fedora.config

Source62: def_variants.yaml.fedora
%endif

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

%if 0%{?fedora}%{?eln}
%define ima_ca_cert %{SOURCE106}
%endif

%if 0%{?rhel} && !0%{?eln}
%define ima_ca_cert %{SOURCE103}
# rhel && !eln
%endif

%if 0%{?centos}
%define ima_signing_cert %{SOURCE105}
%else
%define ima_signing_cert %{SOURCE104}
%endif

%define ima_cert_name ima.cer

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

Source300: kernel-abi-stablelists-%{kabiversion}.tar.xz
Source301: kernel-kabi-dw-%{kabiversion}.tar.xz

%if 0%{include_rt}
%if 0%{include_rhel}
Source474: %{name}-aarch64-rt-rhel.config
Source475: %{name}-aarch64-rt-debug-rhel.config
Source476: %{name}-aarch64-rt-64k-rhel.config
Source477: %{name}-aarch64-rt-64k-debug-rhel.config
Source478: %{name}-x86_64-rt-rhel.config
Source479: %{name}-x86_64-rt-debug-rhel.config
%endif
%if 0%{include_fedora}
Source480: %{name}-aarch64-rt-fedora.config
Source481: %{name}-aarch64-rt-debug-fedora.config
Source482: %{name}-aarch64-rt-64k-fedora.config
Source483: %{name}-aarch64-rt-64k-debug-fedora.config
Source484: %{name}-x86_64-rt-fedora.config
Source485: %{name}-x86_64-rt-debug-fedora.config
Source486: %{name}-riscv64-rt-fedora.config
Source487: %{name}-riscv64-rt-debug-fedora.config
%endif
%endif

%if %{include_automotive}
# automotive config files
Source488: %{name}-aarch64-automotive-rhel.config
Source489: %{name}-aarch64-automotive-debug-rhel.config
Source490: %{name}-x86_64-automotive-rhel.config
Source491: %{name}-x86_64-automotive-debug-rhel.config
%endif


# Sources for kernel-tools
Source2002: kvm_stat.logrotate

# Some people enjoy building customized kernels from the dist-git in Fedora and
# use this to override configuration options. One day they may all use the
# source tree, but in the mean time we carry this to support the legacy workflow
Source3000: merge.py
Source3001: kernel-local
%if %{patchlist_changelog}
Source3002: Patchlist.changelog
%endif

Source4000: README.rst
Source4001: rpminspect.yaml
Source4002: gating.yaml

## Patches needed for building this package

%if !%{nopatches}

Patch1: patch-%{patchversion}-redhat.patch
%endif

# empty final patch to facilitate testing of kernel patches
Patch999999: linux-kernel-test.patch

# END OF PATCH DEFINITIONS

%description
The kernel meta package

#
# This macro does requires, provides, conflicts, obsoletes for a kernel package.
#	%%kernel_reqprovconf [-o] <subpackage>
# It uses any kernel_<subpackage>_conflicts and kernel_<subpackage>_obsoletes
# macros defined above.
#
%define kernel_reqprovconf(o) \
%if %{-o:0}%{!-o:1}\
Provides: kernel = %{specversion}-%{pkg_release}\
%endif\
Provides: kernel-%{_target_cpu} = %{specrpmversion}-%{pkg_release}%{uname_suffix %{?1:+%{1}}}\
Provides: kernel-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
Requires: kernel%{?1:-%{1}}-modules-core-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
Requires(pre): %{kernel_prereq}\
Requires(pre): %{initrd_prereq}\
Requires(pre): ((linux-firmware >= 20150904-56.git6ebf5d57) if linux-firmware)\
Recommends: linux-firmware\
Requires(preun): systemd >= 200\
Conflicts: xfsprogs < 4.3.0-1\
Conflicts: xorg-x11-drv-vmmouse < 13.0.99\
%{expand:%%{?kernel%{?1:_%{1}}_conflicts:Conflicts: %%{kernel%{?1:_%{1}}_conflicts}}}\
%{expand:%%{?kernel%{?1:_%{1}}_obsoletes:Obsoletes: %%{kernel%{?1:_%{1}}_obsoletes}}}\
%{expand:%%{?kernel%{?1:_%{1}}_provides:Provides: %%{kernel%{?1:_%{1}}_provides}}}\
# We can't let RPM do the dependencies automatic because it'll then pick up\
# a correct but undesirable perl dependency from the module headers which\
# isn't required for the kernel proper to function\
AutoReq: no\
AutoProv: yes\
%{nil}


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
%if 0%{?gemini}
Provides: kernel-headers = %{specversion}-%{release}
Obsoletes: kernel-headers < %{specversion}
%endif
%description headers
Kernel-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
glibc package.

%package cross-headers
Summary: Header files for the Linux kernel for use by cross-glibc
%if 0%{?gemini}
Provides: kernel-cross-headers = %{specversion}-%{release}
Obsoletes: kernel-cross-headers < %{specversion}
%endif
%description cross-headers
Kernel-cross-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
cross-glibc package.

%package debuginfo-common-%{_target_cpu}
Summary: Kernel source files used by %{name}-debuginfo packages
Provides: installonlypkg(kernel)
%description debuginfo-common-%{_target_cpu}
This package is required by %{name}-debuginfo subpackages.
It provides the kernel source files common to all builds.

%if %{with_perf}
%package -n perf
%if 0%{gemini}
Epoch: %{gemini}
%endif
Summary: Performance monitoring for the Linux kernel
Requires: bzip2
%description -n perf
This package contains the perf tool, which enables performance monitoring
of the Linux kernel.

%package -n perf-debuginfo
%if 0%{gemini}
Epoch: %{gemini}
%endif
Summary: Debug information for package perf
Requires: %{name}-debuginfo-common-%{_target_cpu} = %{specrpmversion}-%{release}
AutoReqProv: no
%description -n perf-debuginfo
This package provides debug information for the perf package.

# Note that this pattern only works right to match the .build-id
# symlinks because of the trailing nonmatching alternation and
# the leading .*, because of find-debuginfo.sh's buggy handling
# of matching the pattern against the symlinks file.
%{expand:%%global _find_debuginfo_opts %{?_find_debuginfo_opts} -p '.*%%{_bindir}/perf(\.debug)?|.*%%{_libexecdir}/perf-core/.*|.*%%{_libdir}/libperf-jvmti.so(\.debug)?|XXX' -o perf-debuginfo.list}

%package -n python3-perf
%if 0%{gemini}
Epoch: %{gemini}
%endif
Summary: Python bindings for apps which will manipulate perf events
%description -n python3-perf
The python3-perf package contains a module that permits applications
written in the Python programming language to use the interface
to manipulate perf events.

%package -n python3-perf-debuginfo
%if 0%{gemini}
Epoch: %{gemini}
%endif
Summary: Debug information for package perf python bindings
Requires: %{name}-debuginfo-common-%{_target_cpu} = %{specrpmversion}-%{release}
AutoReqProv: no
%description -n python3-perf-debuginfo
This package provides debug information for the perf python bindings.

# the python_sitearch macro should already be defined from above
%{expand:%%global _find_debuginfo_opts %{?_find_debuginfo_opts} -p '.*%%{python3_sitearch}/perf.*so(\.debug)?|XXX' -o python3-perf-debuginfo.list}

# with_perf
%endif

%if %{with_libperf}
%package -n libperf
Summary: The perf library from kernel source
%description -n libperf
This package contains the kernel source perf library.

%package -n libperf-devel
Summary: Developement files for the perf library from kernel source
Requires: libperf = %{version}-%{release}
%description -n libperf-devel
This package includes libraries and header files needed for development
of applications which use perf library from kernel source.

%package -n libperf-debuginfo
Summary: Debug information for package libperf
Group: Development/Debug
Requires: %{name}-debuginfo-common-%{_target_cpu} = %{version}-%{release}
AutoReqProv: no
%description -n libperf-debuginfo
This package provides debug information for the libperf package.

# Note that this pattern only works right to match the .build-id
# symlinks because of the trailing nonmatching alternation and
# the leading .*, because of find-debuginfo.sh's buggy handling
# of matching the pattern against the symlinks file.
%{expand:%%global _find_debuginfo_opts %{?_find_debuginfo_opts} -p '.*%%{_libdir}/libperf.so.*(\.debug)?|XXX' -o libperf-debuginfo.list}
# with_libperf
%endif

%if %{with_tools}
%package -n %{package_name}-tools
Summary: Assortment of tools for the Linux kernel
%ifarch %{cpupowerarchs}
Provides:  cpupowerutils = 1:009-0.6.p1
Obsoletes: cpupowerutils < 1:009-0.6.p1
Provides:  cpufreq-utils = 1:009-0.6.p1
Provides:  cpufrequtils = 1:009-0.6.p1
Obsoletes: cpufreq-utils < 1:009-0.6.p1
Obsoletes: cpufrequtils < 1:009-0.6.p1
Obsoletes: cpuspeed < 1:1.5-16
Requires: %{package_name}-tools-libs = %{specrpmversion}-%{release}
%endif
%define __requires_exclude ^%{_bindir}/python
%description -n %{package_name}-tools
This package contains the tools/ directory from the kernel source
and the supporting documentation.

%package -n %{package_name}-tools-libs
Summary: Libraries for the kernels-tools
%description -n %{package_name}-tools-libs
This package contains the libraries built from the tools/ directory
from the kernel source.

%package -n %{package_name}-tools-libs-devel
Summary: Assortment of tools for the Linux kernel
Requires: %{package_name}-tools = %{version}-%{release}
%ifarch %{cpupowerarchs}
Provides:  cpupowerutils-devel = 1:009-0.6.p1
Obsoletes: cpupowerutils-devel < 1:009-0.6.p1
%endif
Requires: %{package_name}-tools-libs = %{version}-%{release}
Provides: %{package_name}-tools-devel
%description -n %{package_name}-tools-libs-devel
This package contains the development files for the tools/ directory from
the kernel source.

%package -n %{package_name}-tools-debuginfo
Summary: Debug information for package %{package_name}-tools
Requires: %{name}-debuginfo-common-%{_target_cpu} = %{version}-%{release}
AutoReqProv: no
%description -n %{package_name}-tools-debuginfo
This package provides debug information for package %{package_name}-tools.

# Note that this pattern only works right to match the .build-id
# symlinks because of the trailing nonmatching alternation and
# the leading .*, because of find-debuginfo.sh's buggy handling
# of matching the pattern against the symlinks file.
%{expand:%%global _find_debuginfo_opts %{?_find_debuginfo_opts} -p '.*%%{_bindir}/bootconfig(\.debug)?|.*%%{_bindir}/centrino-decode(\.debug)?|.*%%{_bindir}/powernow-k8-decode(\.debug)?|.*%%{_bindir}/cpupower(\.debug)?|.*%%{_libdir}/libcpupower.*|.*%%{_bindir}/turbostat(\.debug)?|.*%%{_bindir}/x86_energy_perf_policy(\.debug)?|.*%%{_bindir}/tmon(\.debug)?|.*%%{_bindir}/lsgpio(\.debug)?|.*%%{_bindir}/gpio-hammer(\.debug)?|.*%%{_bindir}/gpio-event-mon(\.debug)?|.*%%{_bindir}/gpio-watch(\.debug)?|.*%%{_bindir}/iio_event_monitor(\.debug)?|.*%%{_bindir}/iio_generic_buffer(\.debug)?|.*%%{_bindir}/lsiio(\.debug)?|.*%%{_bindir}/intel-speed-select(\.debug)?|.*%%{_bindir}/page_owner_sort(\.debug)?|.*%%{_bindir}/slabinfo(\.debug)?|.*%%{_sbindir}/intel_sdsi(\.debug)?|XXX' -o %{package_name}-tools-debuginfo.list}

%package -n rtla
%if 0%{gemini}
Epoch: %{gemini}
%endif
Summary: Real-Time Linux Analysis tools
Requires: libtraceevent
Requires: libtracefs
Requires: libbpf
%ifarch %{cpupowerarchs}
Requires: %{package_name}-tools-libs = %{version}-%{release}
%endif
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

# with_tools
%endif

%if %{with_selftests}

%package selftests-internal
Summary: Kernel samples and selftests
Requires: binutils, bpftool, fuse-libs, iproute-tc, iputils, keyutils, nmap-ncat, python3
%description selftests-internal
Kernel sample programs and selftests.

# Note that this pattern only works right to match the .build-id
# symlinks because of the trailing nonmatching alternation and
# the leading .*, because of find-debuginfo.sh's buggy handling
# of matching the pattern against the symlinks file.
%{expand:%%global _find_debuginfo_opts %{?_find_debuginfo_opts} -p '.*%%{_libexecdir}/(ksamples|kselftests)/.*|XXX' -o selftests-debuginfo.list}

%define __requires_exclude ^liburandom_read.so.*$

# with_selftests
%endif

%define kernel_gcov_package() \
%package %{?1:%{1}-}gcov\
Summary: gcov graph and source files for coverage data collection.\
%description %{?1:%{1}-}gcov\
%{?1:%{1}-}gcov includes the gcov graph and source files for gcov coverage collection.\
%{nil}

%package -n %{package_name}-abi-stablelists
Summary: The Red Hat Enterprise Linux kernel ABI symbol stablelists
AutoReqProv: no
%description -n %{package_name}-abi-stablelists
The kABI package contains information pertaining to the Red Hat Enterprise
Linux kernel ABI, including lists of kernel symbols that are needed by
external Linux kernel modules, and a yum plugin to aid enforcement.

%if %{with_kabidw_base}
%package kernel-kabidw-base-internal
Summary: The baseline dataset for kABI verification using DWARF data
Group: System Environment/Kernel
AutoReqProv: no
%description kernel-kabidw-base-internal
The package contains data describing the current ABI of the Red Hat Enterprise
Linux kernel, suitable for the kabi-dw tool.
%endif

#
# This macro creates a kernel-<subpackage>-debuginfo package.
#	%%kernel_debuginfo_package <subpackage>
#
# Explanation of the find_debuginfo_opts: We build multiple kernels (debug,
# rt, 64k etc.) so the regex filters those kernels appropriately. We also
# have to package several binaries as part of kernel-devel but getting
# unique build-ids is tricky for these userspace binaries. We don't really
# care about debugging those so we just filter those out and remove it.
%define kernel_debuginfo_package() \
%package %{?1:%{1}-}debuginfo\
Summary: Debug information for package %{name}%{?1:-%{1}}\
Requires: %{name}-debuginfo-common-%{_target_cpu} = %{specrpmversion}-%{release}\
Provides: %{name}%{?1:-%{1}}-debuginfo-%{_target_cpu} = %{specrpmversion}-%{release}\
Provides: installonlypkg(kernel)\
AutoReqProv: no\
%description %{?1:%{1}-}debuginfo\
This package provides debug information for package %{name}%{?1:-%{1}}.\
This is required to use SystemTap with %{name}%{?1:-%{1}}-%{KVERREL}.\
%{expand:%%global _find_debuginfo_opts %{?_find_debuginfo_opts} --keep-section '.BTF' -p '.*\/usr\/src\/kernels/.*|XXX' -o ignored-debuginfo.list -p '/.*/%%{KVERREL_RE}%{?1:[+]%{1}}/.*|/.*%%{KVERREL_RE}%{?1:\+%{1}}(\.debug)?' -o debuginfo%{?1}.list}\
%{nil}

#
# This macro creates a kernel-<subpackage>-devel package.
#	%%kernel_devel_package [-m] <subpackage> <pretty-name>
#
%define kernel_devel_package(m) \
%package %{?1:%{1}-}devel\
Summary: Development package for building kernel modules to match the %{?2:%{2} }kernel\
Provides: kernel%{?1:-%{1}}-devel-%{_target_cpu} = %{specrpmversion}-%{release}\
Provides: kernel-devel-%{_target_cpu} = %{specrpmversion}-%{release}%{uname_suffix %{?1:+%{1}}}\
Provides: kernel-devel-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
Provides: installonlypkg(kernel)\
AutoReqProv: no\
Requires(pre): findutils\
Requires: findutils\
Requires: perl-interpreter\
Requires: openssl-devel\
Requires: elfutils-libelf-devel\
Requires: bison\
Requires: flex\
Requires: make\
Requires: gcc\
%if %{-m:1}%{!-m:0}\
Requires: kernel-devel-uname-r = %{KVERREL}%{uname_variant %{?1:%{1}}}\
%endif\
%description %{?1:%{1}-}devel\
This package provides kernel headers and makefiles sufficient to build modules\
against the %{?2:%{2} }kernel package.\
%{nil}

#
# This macro creates an empty kernel-<subpackage>-devel-matched package that
# requires both the core and devel packages locked on the same version.
#	%%kernel_devel_matched_package [-m] <subpackage> <pretty-name>
#
%define kernel_devel_matched_package(m) \
%package %{?1:%{1}-}devel-matched\
Summary: Meta package to install matching core and devel packages for a given %{?2:%{2} }kernel\
Requires: %{package_name}%{?1:-%{1}}-devel = %{specrpmversion}-%{release}\
Requires: %{package_name}%{?1:-%{1}}-core = %{specrpmversion}-%{release}\
%description %{?1:%{1}-}devel-matched\
This meta package is used to install matching core and devel packages for a given %{?2:%{2} }kernel.\
%{nil}

%define kernel_modules_extra_matched_package(m) \
%package modules-extra-matched\
Summary: Meta package which requires modules-extra to be installed for all kernels.\
%description modules-extra-matched\
This meta package provides a single reference that other packages can Require to have modules-extra installed for all kernels.\
%{nil}

#
# This macro creates a kernel-<subpackage>-modules-internal package.
#	%%kernel_modules_internal_package <subpackage> <pretty-name>
#
%define kernel_modules_internal_package() \
%package %{?1:%{1}-}modules-internal\
Summary: Extra kernel modules to match the %{?2:%{2} }kernel\
Group: System Environment/Kernel\
Provides: kernel%{?1:-%{1}}-modules-internal-%{_target_cpu} = %{specrpmversion}-%{release}\
Provides: kernel%{?1:-%{1}}-modules-internal-%{_target_cpu} = %{specrpmversion}-%{release}%{uname_suffix %{?1:+%{1}}}\
Provides: kernel%{?1:-%{1}}-modules-internal = %{specrpmversion}-%{release}%{uname_suffix %{?1:+%{1}}}\
Provides: installonlypkg(kernel-module)\
Provides: kernel%{?1:-%{1}}-modules-internal-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
Requires: kernel-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
Requires: kernel%{?1:-%{1}}-modules-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
Requires: kernel%{?1:-%{1}}-modules-core-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
AutoReq: no\
AutoProv: yes\
%description %{?1:%{1}-}modules-internal\
This package provides kernel modules for the %{?2:%{2} }kernel package for Red Hat internal usage.\
%{nil}

#
# This macro creates a kernel-<subpackage>-modules-extra package.
#	%%kernel_modules_extra_package [-m] <subpackage> <pretty-name>
#
%define kernel_modules_extra_package(m) \
%package %{?1:%{1}-}modules-extra\
Summary: Extra kernel modules to match the %{?2:%{2} }kernel\
Provides: kernel%{?1:-%{1}}-modules-extra-%{_target_cpu} = %{specrpmversion}-%{release}\
Provides: kernel%{?1:-%{1}}-modules-extra-%{_target_cpu} = %{specrpmversion}-%{release}%{uname_suffix %{?1:+%{1}}}\
Provides: kernel%{?1:-%{1}}-modules-extra = %{specrpmversion}-%{release}%{uname_suffix %{?1:+%{1}}}\
Provides: installonlypkg(kernel-module)\
Provides: kernel%{?1:-%{1}}-modules-extra-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
Requires: kernel-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
Requires: kernel%{?1:-%{1}}-modules-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
Requires: kernel%{?1:-%{1}}-modules-core-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
%if %{-m:1}%{!-m:0}\
Requires: kernel-modules-extra-uname-r = %{KVERREL}%{uname_variant %{?1:+%{1}}}\
%endif\
AutoReq: no\
AutoProv: yes\
%description %{?1:%{1}-}modules-extra\
This package provides less commonly used kernel modules for the %{?2:%{2} }kernel package.\
%{nil}

#
# This macro creates a kernel-<subpackage>-modules package.
#	%%kernel_modules_package [-m] <subpackage> <pretty-name>
#
%define kernel_modules_package(m) \
%package %{?1:%{1}-}modules\
Summary: kernel modules to match the %{?2:%{2}-}core kernel\
Provides: kernel%{?1:-%{1}}-modules-%{_target_cpu} = %{specrpmversion}-%{release}\
Provides: kernel-modules-%{_target_cpu} = %{specrpmversion}-%{release}%{uname_suffix %{?1:+%{1}}}\
Provides: kernel-modules = %{specrpmversion}-%{release}%{uname_suffix %{?1:+%{1}}}\
Provides: installonlypkg(kernel-module)\
Provides: kernel%{?1:-%{1}}-modules-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
Requires: kernel-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
Requires: kernel%{?1:-%{1}}-modules-core-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
%if %{-m:1}%{!-m:0}\
Requires: kernel-modules-uname-r = %{KVERREL}%{uname_variant %{?1:+%{1}}}\
%endif\
AutoReq: no\
AutoProv: yes\
%description %{?1:%{1}-}modules\
This package provides commonly used kernel modules for the %{?2:%{2}-}core kernel package.\
%{nil}

#
# This macro creates a kernel-<subpackage>-modules-core package.
#	%%kernel_modules_core_package [-m] <subpackage> <pretty-name>
#
%define kernel_modules_core_package(m) \
%package %{?1:%{1}-}modules-core\
Summary: Core kernel modules to match the %{?2:%{2}-}core kernel\
Provides: kernel%{?1:-%{1}}-modules-core-%{_target_cpu} = %{specrpmversion}-%{release}\
Provides: kernel-modules-core-%{_target_cpu} = %{specrpmversion}-%{release}%{uname_suffix %{?1:+%{1}}}\
Provides: kernel-modules-core = %{specrpmversion}-%{release}%{uname_suffix %{?1:+%{1}}}\
Provides: installonlypkg(kernel-module)\
Provides: kernel%{?1:-%{1}}-modules-core-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
Requires: kernel-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
%if %{-m:1}%{!-m:0}\
Requires: kernel-modules-core-uname-r = %{KVERREL}%{uname_variant %{?1:+%{1}}}\
%endif\
AutoReq: no\
AutoProv: yes\
%description %{?1:%{1}-}modules-core\
This package provides essential kernel modules for the %{?2:%{2}-}core kernel package.\
%{nil}

#
# this macro creates a kernel-<subpackage> meta package.
#	%%kernel_meta_package <subpackage>
#
%define kernel_meta_package() \
%package %{1}\
summary: kernel meta-package for the %{1} kernel\
Requires: kernel-%{1}-core-uname-r = %{KVERREL}%{uname_suffix %{1}}\
Requires: kernel-%{1}-modules-uname-r = %{KVERREL}%{uname_suffix %{1}}\
Requires: kernel-%{1}-modules-core-uname-r = %{KVERREL}%{uname_suffix %{1}}\
Requires: ((kernel-%{1}-modules-extra-uname-r = %{KVERREL}%{uname_suffix %{1}}) if kernel-modules-extra-matched)\
%if "%{1}" == "rt" || "%{1}" == "rt-debug" || "%{1}" == "rt-64k" || "%{1}" == "rt-64k-debug"\
Requires: realtime-setup\
%endif\
Provides: installonlypkg(kernel)\
%description %{1}\
The meta-package for the %{1} kernel\
%{nil}

#
# This macro creates a kernel-<subpackage> and its -devel and -debuginfo too.
#	%%define variant_summary The Linux kernel compiled for <configuration>
#	%%kernel_variant_package [-n <pretty-name>] [-m] [-o] <subpackage>
#
%define kernel_variant_package(n:mo) \
%package %{?1:%{1}-}core\
Summary: %{variant_summary}\
Provides: kernel-%{?1:%{1}-}core-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
Provides: installonlypkg(kernel)\
%if %{-m:1}%{!-m:0}\
Requires: kernel-core-uname-r = %{KVERREL}%{uname_variant %{?1:+%{1}}}\
Requires: kernel-%{?1:%{1}-}-modules-core-uname-r = %{KVERREL}%{uname_variant %{?1:+%{1}}}\
%endif\
%{expand:%%kernel_reqprovconf %{?1:%{1}} %{-o:%{-o}}}\
%if %{?1:1} %{!?1:0} \
%{expand:%%kernel_meta_package %{?1:%{1}}}\
%endif\
%{expand:%%kernel_devel_package %{?1:%{1}} %{!?{-n}:%{1}}%{?{-n}:%{-n*}} %{-m:%{-m}}}\
%{expand:%%kernel_devel_matched_package %{?1:%{1}} %{!?{-n}:%{1}}%{?{-n}:%{-n*}} %{-m:%{-m}}}\
%{expand:%%kernel_modules_package %{?1:%{1}} %{!?{-n}:%{1}}%{?{-n}:%{-n*}} %{-m:%{-m}}}\
%{expand:%%kernel_modules_core_package %{?1:%{1}} %{!?{-n}:%{1}}%{?{-n}:%{-n*}} %{-m:%{-m}}}\
%{expand:%%kernel_modules_extra_package %{?1:%{1}} %{!?{-n}:%{1}}%{?{-n}:%{-n*}} %{-m:%{-m}}}\
%if %{-m:0}%{!-m:1}\
%{expand:%%kernel_modules_internal_package %{?1:%{1}} %{!?{-n}:%{1}}%{?{-n}:%{-n*}}}\
%if 0%{!?fedora:1}\
%{expand:%%kernel_modules_partner_package %{?1:%{1}} %{!?{-n}:%{1}}%{?{-n}:%{-n*}}}\
%endif\
%{expand:%%kernel_debuginfo_package %{?1:%{1}}}\
%endif\
%if %{with_efiuki} && ("%{1}" != "rt" && "%{1}" != "rt-debug" && "%{1}" != "rt-64k" && "%{1}" != "rt-64k-debug")\
%package %{?1:%{1}-}uki-virt\
Summary: %{variant_summary} unified kernel image for virtual machines\
Provides: installonlypkg(kernel)\
Provides: kernel-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
Requires: kernel%{?1:-%{1}}-modules-core-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
Requires(pre): %{kernel_prereq}\
Requires(pre): systemd >= 254-1\
Recommends: uki-direct\
%package %{?1:%{1}-}uki-virt-addons\
Summary: %{variant_summary} unified kernel image addons for virtual machines\
Provides: installonlypkg(kernel)\
Requires: kernel%{?1:-%{1}}-uki-virt = %{specrpmversion}-%{release}\
Requires(pre): systemd >= 254-1\
%endif\
%if %{with_gcov}\
%{expand:%%kernel_gcov_package %{?1:%{1}}}\
%endif\
%{nil}

#
# This macro creates a kernel-<subpackage>-modules-partner package.
#	%%kernel_modules_partner_package <subpackage> <pretty-name>
#
%define kernel_modules_partner_package() \
%package %{?1:%{1}-}modules-partner\
Summary: Extra kernel modules to match the %{?2:%{2} }kernel\
Group: System Environment/Kernel\
Provides: kernel%{?1:-%{1}}-modules-partner-%{_target_cpu} = %{specrpmversion}-%{release}\
Provides: kernel%{?1:-%{1}}-modules-partner-%{_target_cpu} = %{specrpmversion}-%{release}%{uname_suffix %{?1:+%{1}}}\
Provides: kernel%{?1:-%{1}}-modules-partner = %{specrpmversion}-%{release}%{uname_suffix %{?1:+%{1}}}\
Provides: installonlypkg(kernel-module)\
Provides: kernel%{?1:-%{1}}-modules-partner-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
Requires: kernel-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
Requires: kernel%{?1:-%{1}}-modules-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
Requires: kernel%{?1:-%{1}}-modules-core-uname-r = %{KVERREL}%{uname_suffix %{?1:+%{1}}}\
AutoReq: no\
AutoProv: yes\
%description %{?1:%{1}-}modules-partner\
This package provides kernel modules for the %{?2:%{2} }kernel package for Red Hat partners usage.\
%{nil}

# Now, each variant package.
%if %{with_zfcpdump}
%define variant_summary The Linux kernel compiled for zfcpdump usage
%kernel_variant_package -o zfcpdump
%description zfcpdump-core
The kernel package contains the Linux kernel (vmlinuz) for use by the
zfcpdump infrastructure.
# with_zfcpdump
%endif

%if %{with_arm64_16k_base}
%define variant_summary The Linux kernel compiled for 16k pagesize usage
%kernel_variant_package 16k
%description 16k-core
The kernel package contains a variant of the ARM64 Linux kernel using
a 16K page size.
%endif

%if %{with_arm64_16k} && %{with_debug}
%define variant_summary The Linux kernel compiled with extra debugging enabled
%if !%{debugbuildsenabled}
%kernel_variant_package -m 16k-debug
%else
%kernel_variant_package 16k-debug
%endif
%description 16k-debug-core
The debug kernel package contains a variant of the ARM64 Linux kernel using
a 16K page size.
This variant of the kernel has numerous debugging options enabled.
It should only be installed when trying to gather additional information
on kernel bugs, as some of these options impact performance noticably.
%endif

%if %{with_arm64_64k_base}
%define variant_summary The Linux kernel compiled for 64k pagesize usage
%kernel_variant_package 64k
%description 64k-core
The kernel package contains a variant of the ARM64 Linux kernel using
a 64K page size.
%endif

%if %{with_arm64_64k} && %{with_debug}
%define variant_summary The Linux kernel compiled with extra debugging enabled
%if !%{debugbuildsenabled}
%kernel_variant_package -m 64k-debug
%else
%kernel_variant_package 64k-debug
%endif
%description 64k-debug-core
The debug kernel package contains a variant of the ARM64 Linux kernel using
a 64K page size.
This variant of the kernel has numerous debugging options enabled.
It should only be installed when trying to gather additional information
on kernel bugs, as some of these options impact performance noticably.
%endif

%if %{with_debug} && %{with_realtime}
%define variant_summary The Linux PREEMPT_RT kernel compiled with extra debugging enabled
%kernel_variant_package rt-debug
%description rt-debug-core
The kernel package contains the Linux kernel (vmlinuz), the core of any
Linux operating system.  The kernel handles the basic functions
of the operating system:  memory allocation, process allocation, device
input and output, etc.

This variant of the kernel has numerous debugging options enabled.
It should only be installed when trying to gather additional information
on kernel bugs, as some of these options impact performance noticably.
%endif

%if %{with_realtime_base}
%define variant_summary The Linux kernel compiled with PREEMPT_RT enabled
%kernel_variant_package rt
%description rt-core
This package includes a version of the Linux kernel compiled with the
PREEMPT_RT real-time preemption support
%endif

%if %{with_realtime_arm64_64k_base}
%define variant_summary The Linux PREEMPT_RT kernel compiled for 64k pagesize usage
%kernel_variant_package rt-64k
%description rt-64k-core
The kernel package contains a variant of the ARM64 Linux PREEMPT_RT kernel using
a 64K page size.
%endif

%if %{with_realtime_arm64_64k} && %{with_debug}
%define variant_summary The Linux PREEMPT_RT kernel compiled with extra debugging enabled
%if !%{debugbuildsenabled}
%kernel_variant_package -m rt-64k-debug
%else
%kernel_variant_package rt-64k-debug
%endif
%description rt-64k-debug-core
The debug kernel package contains a variant of the ARM64 Linux PREEMPT_RT kernel using
a 64K page size.
This variant of the kernel has numerous debugging options enabled.
It should only be installed when trying to gather additional information
on kernel bugs, as some of these options impact performance noticably.
%endif

%if %{with_debug} && %{with_automotive}
%define variant_summary The Linux Automotive kernel compiled with extra debugging enabled
%kernel_variant_package automotive-debug
%description automotive-debug-core
The kernel package contains the Linux kernel (vmlinuz), the core of any
Linux operating system.  The kernel handles the basic functions
of the operating system:  memory allocation, process allocation, device
input and output, etc.

This variant of the kernel has numerous debugging options enabled.
It should only be installed when trying to gather additional information
on kernel bugs, as some of these options impact performance noticably.
%endif

%if %{with_automotive_base}
%define variant_summary The Linux kernel compiled with PREEMPT_RT enabled
%kernel_variant_package automotive
%description automotive-core
This package includes a version of the Linux kernel compiled with the
PREEMPT_RT real-time preemption support, targeted for Automotive platforms
%endif

%if %{with_up} && %{with_debug}
%if !%{debugbuildsenabled}
%kernel_variant_package -m debug
%else
%kernel_variant_package debug
%endif
%description debug-core
The kernel package contains the Linux kernel (vmlinuz), the core of any
Linux operating system.  The kernel handles the basic functions
of the operating system:  memory allocation, process allocation, device
input and output, etc.

This variant of the kernel has numerous debugging options enabled.
It should only be installed when trying to gather additional information
on kernel bugs, as some of these options impact performance noticably.
%endif

%if %{with_up_base}
# And finally the main -core package

%define variant_summary The Linux kernel
%kernel_variant_package
%description core
The kernel package contains the Linux kernel (vmlinuz), the core of any
Linux operating system.  The kernel handles the basic functions
of the operating system: memory allocation, process allocation, device
input and output, etc.
%endif

%if %{with_up} && %{with_debug} && %{with_efiuki}
%description debug-uki-virt
Prebuilt debug unified kernel image for virtual machines.

%description debug-uki-virt-addons
Prebuilt debug unified kernel image addons for virtual machines.
%endif

%if %{with_up_base} && %{with_efiuki}
%description uki-virt
Prebuilt default unified kernel image for virtual machines.

%description uki-virt-addons
Prebuilt default unified kernel image addons for virtual machines.
%endif

%if %{with_arm64_16k} && %{with_debug} && %{with_efiuki}
%description 16k-debug-uki-virt
Prebuilt 16k debug unified kernel image for virtual machines.

%description 16k-debug-uki-virt-addons
Prebuilt 16k debug unified kernel image addons for virtual machines.
%endif

%if %{with_arm64_16k_base} && %{with_efiuki}
%description 16k-uki-virt
Prebuilt 16k unified kernel image for virtual machines.

%description 16k-uki-virt-addons
Prebuilt 16k unified kernel image addons for virtual machines.
%endif

%if %{with_arm64_64k} && %{with_debug} && %{with_efiuki}
%description 64k-debug-uki-virt
Prebuilt 64k debug unified kernel image for virtual machines.

%description 64k-debug-uki-virt-addons
Prebuilt 64k debug unified kernel image addons for virtual machines.
%endif

%if %{with_arm64_64k_base} && %{with_efiuki}
%description 64k-uki-virt
Prebuilt 64k unified kernel image for virtual machines.

%description 64k-uki-virt-addons
Prebuilt 64k unified kernel image addons for virtual machines.
%endif

%kernel_modules_extra_matched_package

%define log_msg() \
	{ set +x; } 2>/dev/null \
	_log_msglineno=$(grep -n %{*} %{_specdir}/${RPM_PACKAGE_NAME}.spec | grep log_msg | cut -d":" -f1) \
	echo "kernel.spec:${_log_msglineno}: %{*}" \
	set -x

%prep
%{log_msg "Start of prep stage"}

%{log_msg "Sanity checks"}

# do a few sanity-checks for --with *only builds
%if %{with_baseonly}
%if !%{with_up}
%{log_msg "Cannot build --with baseonly, up build is disabled"}
exit 1
%endif
%endif

# more sanity checking; do it quietly
if [ "%{patches}" != "%%{patches}" ] ; then
  for patch in %{patches} ; do
    if [ ! -f $patch ] ; then
	%{log_msg "ERROR: Patch  ${patch##/*/}  listed in specfile but is missing"}
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
  if ! grep -E "^Patch[0-9]+: $patch\$" %{_specdir}/${RPM_PACKAGE_NAME}.spec ; then
    if [ "${patch:0:8}" != "patch-%{kversion}." ] ; then
	%{log_msg "ERROR: Patch  $patch  not listed as a source patch in specfile"}
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
  %{log_msg "ApplyOptionalPatch: $1"}
  if [ ! -f $RPM_SOURCE_DIR/$patch ]; then
    exit 1
  fi
  local C=$(wc -l $RPM_SOURCE_DIR/$patch | awk '{print $1}')
  if [ "$C" -gt 9 ]; then
    ApplyPatch $patch ${1+"$@"}
  fi
}

%{log_msg "Untar kernel tarball"}
%setup -q -n kernel-%{tarfile_release} -c
mv linux-%{tarfile_release} linux-%{KVERREL}

cd linux-%{KVERREL}
cp -a %{SOURCE1} .

%{log_msg "Start of patch applications"}
%if !%{nopatches}

ApplyOptionalPatch patch-%{patchversion}-redhat.patch
%endif

ApplyOptionalPatch linux-kernel-test.patch

%{log_msg "End of patch applications"}
# END OF PATCH APPLICATIONS

# Any further pre-build tree manipulations happen here.
%{log_msg "Pre-build tree manipulations"}
chmod +x scripts/checkpatch.pl
mv COPYING COPYING-%{specrpmversion}-%{release}

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
%{log_msg "Fixing Python shebangs..."}
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
%ifnarch %nobuildarches

if [ -L configs ]; then
	rm -f configs
fi
mkdir configs
cd configs

%{log_msg "Copy additional source files into buildroot"}
# Drop some necessary files from the source dir into the buildroot
cp $RPM_SOURCE_DIR/%{name}-*.config .
cp %{SOURCE80} .
# merge.py
cp %{SOURCE3000} .
# kernel-local - rename and copy for partial snippet config process
cp %{SOURCE3001} partial-kernel-local-snip.config
cp %{SOURCE3001} partial-kernel-local-debug-snip.config
FLAVOR=%{primary_target} SPECPACKAGE_NAME=%{name} SPECVERSION=%{specversion} SPECRPMVERSION=%{specrpmversion} ./generate_all_configs.sh %{debugbuildsenabled}

# Collect custom defined config options
%{log_msg "Collect custom defined config options"}
PARTIAL_CONFIGS=""
%if %{with_gcov}
PARTIAL_CONFIGS="$PARTIAL_CONFIGS %{SOURCE70} %{SOURCE71}"
%endif
%if %{with toolchain_clang}
PARTIAL_CONFIGS="$PARTIAL_CONFIGS %{SOURCE72} %{SOURCE73}"
%endif
%if %{with clang_lto}
PARTIAL_CONFIGS="$PARTIAL_CONFIGS %{SOURCE74} %{SOURCE75} %{SOURCE76} %{SOURCE77}"
%endif
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
%{log_msg "Merge in any user-provided local config option changes"}
%ifnarch %nobuildarches
for i in %{all_configs}
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
%endif

%if %{signkernel}%{signmodules}

# Add DUP and kpatch certificates to system trusted keys for RHEL
%if 0%{?rhel}
%{log_msg "Add DUP and kpatch certificates to system trusted keys for RHEL"}
openssl x509 -inform der -in %{SOURCE100} -out rheldup3.pem
openssl x509 -inform der -in %{SOURCE101} -out rhelkpatch1.pem
openssl x509 -inform der -in %{SOURCE102} -out nvidiagpuoot001.pem
cat rheldup3.pem rhelkpatch1.pem nvidiagpuoot001.pem > ../certs/rhel.pem
%if %{signkernel}
%ifarch s390x ppc64le
openssl x509 -inform der -in %{secureboot_ca_0} -out secureboot.pem
cat secureboot.pem >> ../certs/rhel.pem
%endif
%endif

# rhel
%endif

openssl x509 -inform der -in %{ima_ca_cert} -out imaca.pem
cat imaca.pem >> ../certs/rhel.pem

for i in *.config; do
  sed -i 's@CONFIG_SYSTEM_TRUSTED_KEYS=""@CONFIG_SYSTEM_TRUSTED_KEYS="certs/rhel.pem"@' $i
done
%endif

%{log_msg "Set process_configs.sh $OPTS"}
cp %{SOURCE81} .
OPTS=""
%if %{with_configchecks}
	OPTS="$OPTS -w -n -c"
%endif
%if %{with clang_lto}
for opt in %{clang_make_opts}; do
  OPTS="$OPTS -m $opt"
done
%endif
%{log_msg "Generate redhat configs"}
RHJOBS=$RPM_BUILD_NCPUS SPECPACKAGE_NAME=%{name} ./process_configs.sh $OPTS %{specrpmversion}

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

%{log_msg "Set scripts/SOURCES targets"}
update_target=%{primary_target}
if [ "%{primary_target}" == "rhel" ]; then
: # no-op to avoid empty if-fi error
%if 0%{?centos}
  update_scripts $update_target
  %{log_msg "Updating scripts/sources to centos version"}
  update_target=centos
%endif
fi
update_scripts $update_target

%endif

%{log_msg "End of kernel config"}
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
%build
%{log_msg "Start of build stage"}

%{log_msg "General arch build configuration"}
rm -rf %{buildroot_unstripped} || true
mkdir -p %{buildroot_unstripped}

%if %{with_sparse}
%define sparse_mflags	C=1
%endif

cp_vmlinux()
{
  eu-strip --remove-comment -o "$2" "$1"
}

# Note we need to disable these flags for cross builds because the flags
# from redhat-rpm-config assume that host == target so target arch
# flags cause issues with the host compiler.
%if !%{with_cross}
%define build_hostcflags  %{?build_cflags}
%define build_hostldflags %{?build_ldflags}
%endif

%define make %{__make} %{?cross_opts} %{?make_opts} HOSTCFLAGS="%{?build_hostcflags}" HOSTLDFLAGS="%{?build_hostldflags}"

InitBuildVars() {
    %{log_msg "InitBuildVars for $1"}

    %{log_msg "InitBuildVars: Initialize build variables"}
    # Initialize the kernel .config file and create some variables that are
    # needed for the actual build process.

    Variant=$1

    # Pick the right kernel config file
    Config=%{name}-%{specrpmversion}-%{_target_cpu}${Variant:+-${Variant}}.config
    DevelDir=/usr/src/kernels/%{KVERREL}${Variant:++${Variant}}

    KernelVer=%{specversion}-%{release}.%{_target_cpu}${Variant:++${Variant}}

    %{log_msg "InitBuildVars: Update Makefile"}
    # make sure EXTRAVERSION says what we want it to say
    # Trim the release if this is a CI build, since KERNELVERSION is limited to 64 characters
    ShortRel=$(perl -e "print \"%{release}\" =~ s/\.pr\.[0-9A-Fa-f]{32}//r")
    perl -p -i -e "s/^EXTRAVERSION.*/EXTRAVERSION = -${ShortRel}.%{_target_cpu}${Variant:++${Variant}}/" Makefile

    # if pre-rc1 devel kernel, must fix up PATCHLEVEL for our versioning scheme
    # if we are post rc1 this should match anyway so this won't matter
    perl -p -i -e 's/^PATCHLEVEL.*/PATCHLEVEL = %{patchlevel}/' Makefile

    %{log_msg "InitBuildVars: Copy files"}
    %{make} %{?_smp_mflags} mrproper
    cp configs/$Config .config

    %if %{signkernel}%{signmodules}
    cp configs/x509.genkey certs/.
    %endif

%if %{with_debuginfo} == 0
    sed -i 's/^\(CONFIG_DEBUG_INFO.*\)=y/# \1 is not set/' .config
%endif

    Arch=`head -1 .config | cut -b 3-`
    %{log_msg "InitBuildVars: USING ARCH=$Arch"}

    KCFLAGS="%{?kcflags}"
}

#Build bootstrap bpftool
BuildBpftool(){
    export BPFBOOTSTRAP_CFLAGS=$(echo "%{__global_compiler_flags}" | sed -r "s/\-specs=[^\ ]+\/redhat-annobin-cc1//")
    export BPFBOOTSTRAP_LDFLAGS=$(echo "%{__global_ldflags}" | sed -r "s/\-specs=[^\ ]+\/redhat-annobin-cc1//")
    CFLAGS="" LDFLAGS="" make EXTRA_CFLAGS="${BPFBOOTSTRAP_CFLAGS}" EXTRA_CXXFLAGS="${BPFBOOTSTRAP_CFLAGS}" EXTRA_LDFLAGS="${BPFBOOTSTRAP_LDFLAGS}" %{?make_opts} %{?clang_make_opts} V=1 -C tools/bpf/bpftool bootstrap
}

BuildKernel() {
    %{log_msg "BuildKernel for $4"}
    MakeTarget=$1
    KernelImage=$2
    DoVDSO=$3
    Variant=$4
    InstallName=${5:-vmlinuz}

    %{log_msg "Setup variables"}
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

%if %{with_gcov}
    %{log_msg "Setup build directories"}
    # Make build directory unique for each variant, so that gcno symlinks
    # are also unique for each variant.
    if [ -n "$Variant" ]; then
        ln -s $(pwd) ../linux-%{KVERREL}-${Variant}
    fi
    %{log_msg "GCOV - continuing build in: $(pwd)"}
    pushd ../linux-%{KVERREL}${Variant:+-${Variant}}
    pwd > ../kernel${Variant:+-${Variant}}-gcov.list
%endif

    %{log_msg "Calling InitBuildVars for $Variant"}
    InitBuildVars $Variant

    %{log_msg "BUILDING A KERNEL FOR ${Variant} %{_target_cpu}..."}

    %{make} ARCH=$Arch olddefconfig >/dev/null

    %{log_msg "Setup build-ids"}
    # This ensures build-ids are unique to allow parallel debuginfo
    perl -p -i -e "s/^CONFIG_BUILD_SALT.*/CONFIG_BUILD_SALT=\"%{KVERREL}\"/" .config
    %{make} ARCH=$Arch KCFLAGS="$KCFLAGS" WITH_GCOV="%{?with_gcov}" %{?_smp_mflags} $MakeTarget %{?sparse_mflags} %{?kernel_mflags}
    if [ $DoModules -eq 1 ]; then
	%{make} ARCH=$Arch KCFLAGS="$KCFLAGS" WITH_GCOV="%{?with_gcov}" %{?_smp_mflags} modules %{?sparse_mflags} || exit 1
    fi

    %{log_msg "Setup RPM_BUILD_ROOT directories"}
    mkdir -p $RPM_BUILD_ROOT/%{image_install_path}
    mkdir -p $RPM_BUILD_ROOT/lib/modules/$KernelVer
    mkdir -p $RPM_BUILD_ROOT/lib/modules/$KernelVer/systemtap
%if %{with_debuginfo}
    mkdir -p $RPM_BUILD_ROOT%{debuginfodir}/%{image_install_path}
%endif

%ifarch aarch64 riscv64
    %{log_msg "Build dtb kernel"}
    %{make} ARCH=$Arch dtbs INSTALL_DTBS_PATH=$RPM_BUILD_ROOT/%{image_install_path}/dtb-$KernelVer
    %{make} ARCH=$Arch dtbs_install INSTALL_DTBS_PATH=$RPM_BUILD_ROOT/%{image_install_path}/dtb-$KernelVer
    cp -r $RPM_BUILD_ROOT/%{image_install_path}/dtb-$KernelVer $RPM_BUILD_ROOT/lib/modules/$KernelVer/dtb
    find arch/$Arch/boot/dts -name '*.dtb' -type f -delete
%endif

    %{log_msg "Cleanup temp btf files"}
    # Remove large intermediate files we no longer need to save space
    # (-f required for zfcpdump builds that do not enable BTF)
    rm -f vmlinux.o .tmp_vmlinux.btf

    %{log_msg "Install files to RPM_BUILD_ROOT"}

    # Comment out specific config settings that may use resources not available
    # to the end user so that the packaged config file can be easily reused with
    # upstream make targets
    %if %{signkernel}%{signmodules}
      sed -i -e '/^CONFIG_SYSTEM_TRUSTED_KEYS/{
        i\# The kernel was built with
        s/^/# /
        a\# We are resetting this value to facilitate local builds
        a\CONFIG_SYSTEM_TRUSTED_KEYS=""
        }' .config
    %endif

    # Start installing the results
    install -m 644 .config $RPM_BUILD_ROOT/boot/config-$KernelVer
    install -m 644 .config $RPM_BUILD_ROOT/lib/modules/$KernelVer/config
    install -m 644 System.map $RPM_BUILD_ROOT/boot/System.map-$KernelVer
    install -m 644 System.map $RPM_BUILD_ROOT/lib/modules/$KernelVer/System.map

    %{log_msg "Reserving 40MB in boot for initramfs"}
    # We estimate the size of the initramfs because rpm needs to take this size
    # into consideration when performing disk space calculations. (See bz #530778)
    dd if=/dev/zero of=$RPM_BUILD_ROOT/boot/initramfs-$KernelVer.img bs=1M count=40

    if [ -f arch/$Arch/boot/zImage.stub ]; then
      %{log_msg "Copy zImage.stub to RPM_BUILD_ROOT"}
      cp arch/$Arch/boot/zImage.stub $RPM_BUILD_ROOT/%{image_install_path}/zImage.stub-$KernelVer || :
      cp arch/$Arch/boot/zImage.stub $RPM_BUILD_ROOT/lib/modules/$KernelVer/zImage.stub-$KernelVer || :
    fi

    %if %{signkernel}
    %{log_msg "Copy kernel for signing"}
    if [ "$KernelImage" = vmlinux ]; then
        # We can't strip and sign $KernelImage in place, because
        # we need to preserve original vmlinux for debuginfo.
        # Use a copy for signing.
        $CopyKernel $KernelImage $KernelImage.tosign
        KernelImage=$KernelImage.tosign
        CopyKernel=cp
    fi

    SignImage=$KernelImage

    %ifarch x86_64 aarch64
    %{log_msg "Sign kernel image"}
    %pesign -s -i $SignImage -o vmlinuz.signed -a %{secureboot_ca_0} -c %{secureboot_key_0} -n %{pesign_name_0}
    %endif
    %ifarch s390x ppc64le
    if [ -x /usr/bin/rpm-sign ]; then
	rpm-sign --key "%{pesign_name_0}" --lkmsign $SignImage --output vmlinuz.signed
    elif [ "$DoModules" == "1" -a "%{signmodules}" == "1" ]; then
	chmod +x scripts/sign-file
	./scripts/sign-file -p sha256 certs/signing_key.pem certs/signing_key.x509 $SignImage vmlinuz.signed
    else
	mv $SignImage vmlinuz.signed
    fi
    %endif

    if [ ! -s vmlinuz.signed ]; then
	%{log_msg "pesigning failed"}
        exit 1
    fi
    mv vmlinuz.signed $SignImage
    # signkernel
    %endif

    %{log_msg "copy signed kernel"}
    $CopyKernel $KernelImage \
                $RPM_BUILD_ROOT/%{image_install_path}/$InstallName-$KernelVer
    chmod 755 $RPM_BUILD_ROOT/%{image_install_path}/$InstallName-$KernelVer
    cp $RPM_BUILD_ROOT/%{image_install_path}/$InstallName-$KernelVer $RPM_BUILD_ROOT/lib/modules/$KernelVer/$InstallName

    # hmac sign the kernel for FIPS
    %{log_msg "hmac sign the kernel for FIPS"}
    %{log_msg "Creating hmac file: $RPM_BUILD_ROOT/%{image_install_path}/.vmlinuz-$KernelVer.hmac"}
    ls -l $RPM_BUILD_ROOT/%{image_install_path}/$InstallName-$KernelVer
    (cd $RPM_BUILD_ROOT/%{image_install_path} && sha512hmac $InstallName-$KernelVer) > $RPM_BUILD_ROOT/%{image_install_path}/.vmlinuz-$KernelVer.hmac;
    cp $RPM_BUILD_ROOT/%{image_install_path}/.vmlinuz-$KernelVer.hmac $RPM_BUILD_ROOT/lib/modules/$KernelVer/.vmlinuz.hmac

    if [ $DoModules -eq 1 ]; then
	%{log_msg "Install modules in RPM_BUILD_ROOT"}
	# Override $(mod-fw) because we don't want it to install any firmware
	# we'll get it from the linux-firmware package and we don't want conflicts
	%{make} %{?_smp_mflags} ARCH=$Arch INSTALL_MOD_PATH=$RPM_BUILD_ROOT %{?_smp_mflags} modules_install KERNELRELEASE=$KernelVer mod-fw=
    fi

%if %{with_gcov}
    %{log_msg "install gcov-needed files to $BUILDROOT/$BUILD/"}
    # install gcov-needed files to $BUILDROOT/$BUILD/...:
    #   gcov_info->filename is absolute path
    #   gcno references to sources can use absolute paths (e.g. in out-of-tree builds)
    #   sysfs symlink targets (set up at compile time) use absolute paths to BUILD dir
    find . \( -name '*.gcno' -o -name '*.[chS]' \) -exec install -D '{}' "$RPM_BUILD_ROOT/$(pwd)/{}" \;
%endif

    %{log_msg "Add VDSO files"}
    # add an a noop %%defattr statement 'cause rpm doesn't like empty file list files
    echo '%%defattr(-,-,-)' > ../kernel${Variant:+-${Variant}}-ldsoconf.list
    if [ $DoVDSO -ne 0 ]; then
        %{make} ARCH=$Arch INSTALL_MOD_PATH=$RPM_BUILD_ROOT vdso_install KERNELRELEASE=$KernelVer
        if [ -s ldconfig-kernel.conf ]; then
             install -D -m 444 ldconfig-kernel.conf \
                $RPM_BUILD_ROOT/etc/ld.so.conf.d/kernel-$KernelVer.conf
	     echo /etc/ld.so.conf.d/kernel-$KernelVer.conf >> ../kernel${Variant:+-${Variant}}-ldsoconf.list
        fi

        rm -rf $RPM_BUILD_ROOT/lib/modules/$KernelVer/vdso/.build-id
    fi

    %{log_msg "Save headers/makefiles, etc. for kernel-headers"}
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
    %{log_msg "GENERATING kernel ABI metadata"}
    %compression --stdout %compression_flags < Module.symvers > $RPM_BUILD_ROOT/boot/symvers-$KernelVer.%compext
    cp $RPM_BUILD_ROOT/boot/symvers-$KernelVer.%compext $RPM_BUILD_ROOT/lib/modules/$KernelVer/symvers.%compext

%if %{with_kabichk}
    %{log_msg "kABI checking is enabled in kernel SPEC file."}
    chmod 0755 $RPM_SOURCE_DIR/check-kabi
    if [ -e $RPM_SOURCE_DIR/Module.kabi_%{_target_cpu}$Variant ]; then
        cp $RPM_SOURCE_DIR/Module.kabi_%{_target_cpu}$Variant $RPM_BUILD_ROOT/Module.kabi
        $RPM_SOURCE_DIR/check-kabi -k $RPM_BUILD_ROOT/Module.kabi -s Module.symvers || exit 1
        # for now, don't keep it around.
        rm $RPM_BUILD_ROOT/Module.kabi
    else
	%{log_msg "NOTE: Cannot find reference Module.kabi file."}
    fi
%endif

%if %{with_kabidupchk}
    %{log_msg "kABI DUP checking is enabled in kernel SPEC file."}
    if [ -e $RPM_SOURCE_DIR/Module.kabi_dup_%{_target_cpu}$Variant ]; then
        cp $RPM_SOURCE_DIR/Module.kabi_dup_%{_target_cpu}$Variant $RPM_BUILD_ROOT/Module.kabi
        $RPM_SOURCE_DIR/check-kabi -k $RPM_BUILD_ROOT/Module.kabi -s Module.symvers || exit 1
        # for now, don't keep it around.
        rm $RPM_BUILD_ROOT/Module.kabi
    else
	%{log_msg "NOTE: Cannot find DUP reference Module.kabi file."}
    fi
%endif

%if %{with_kabidw_base}
    # Don't build kabi base for debug kernels
    if [ "$Variant" != "zfcpdump" -a "$Variant" != "debug" ]; then
        mkdir -p $RPM_BUILD_ROOT/kabi-dwarf
        tar -xvf %{SOURCE301} -C $RPM_BUILD_ROOT/kabi-dwarf

        mkdir -p $RPM_BUILD_ROOT/kabi-dwarf/stablelists
        tar -xvf %{SOURCE300} -C $RPM_BUILD_ROOT/kabi-dwarf/stablelists

	%{log_msg "GENERATING DWARF-based kABI baseline dataset"}
        chmod 0755 $RPM_BUILD_ROOT/kabi-dwarf/run_kabi-dw.sh
        $RPM_BUILD_ROOT/kabi-dwarf/run_kabi-dw.sh generate \
            "$RPM_BUILD_ROOT/kabi-dwarf/stablelists/kabi-current/kabi_stablelist_%{_target_cpu}" \
            "$(pwd)" \
            "$RPM_BUILD_ROOT/kabidw-base/%{_target_cpu}${Variant:+.${Variant}}" || :

        rm -rf $RPM_BUILD_ROOT/kabi-dwarf
    fi
%endif

%if %{with_kabidwchk}
    if [ "$Variant" != "zfcpdump" ]; then
        mkdir -p $RPM_BUILD_ROOT/kabi-dwarf
        tar -xvf %{SOURCE301} -C $RPM_BUILD_ROOT/kabi-dwarf
        if [ -d "$RPM_BUILD_ROOT/kabi-dwarf/base/%{_target_cpu}${Variant:+.${Variant}}" ]; then
            mkdir -p $RPM_BUILD_ROOT/kabi-dwarf/stablelists
            tar -xvf %{SOURCE300} -C $RPM_BUILD_ROOT/kabi-dwarf/stablelists

	    %{log_msg "GENERATING DWARF-based kABI dataset"}
            chmod 0755 $RPM_BUILD_ROOT/kabi-dwarf/run_kabi-dw.sh
            $RPM_BUILD_ROOT/kabi-dwarf/run_kabi-dw.sh generate \
                "$RPM_BUILD_ROOT/kabi-dwarf/stablelists/kabi-current/kabi_stablelist_%{_target_cpu}" \
                "$(pwd)" \
                "$RPM_BUILD_ROOT/kabi-dwarf/base/%{_target_cpu}${Variant:+.${Variant}}.tmp" || :

	    %{log_msg "kABI DWARF-based comparison report"}
            $RPM_BUILD_ROOT/kabi-dwarf/run_kabi-dw.sh compare \
                "$RPM_BUILD_ROOT/kabi-dwarf/base/%{_target_cpu}${Variant:+.${Variant}}" \
                "$RPM_BUILD_ROOT/kabi-dwarf/base/%{_target_cpu}${Variant:+.${Variant}}.tmp" || :
	    %{log_msg "End of kABI DWARF-based comparison report"}
        else
	    %{log_msg "Baseline dataset for kABI DWARF-BASED comparison report not found"}
        fi

        rm -rf $RPM_BUILD_ROOT/kabi-dwarf
    fi
%endif

   %{log_msg "Cleanup Makefiles/Kconfig files"}
    # then drop all but the needed Makefiles/Kconfig files
    rm -rf $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/scripts
    rm -rf $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/include
    cp .config $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
    cp -a scripts $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
    rm -rf $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/scripts/tracing
    rm -f $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/scripts/spdxcheck.py

%ifarch s390x
    # CONFIG_EXPOLINE_EXTERN=y produces arch/s390/lib/expoline/expoline.o
    # which is needed during external module build.
    %{log_msg "Copy expoline.o"}
    if [ -f arch/s390/lib/expoline/expoline.o ]; then
      cp -a --parents arch/s390/lib/expoline/expoline.o $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
    fi
%endif

    %{log_msg "Copy additional files for make targets"}
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
      cp -a arch/$Arch/scripts $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/arch/%{_arch} || :
    fi
    if [ -f arch/$Arch/*lds ]; then
      cp -a arch/$Arch/*lds $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/arch/%{_arch}/ || :
    fi
    if [ -f arch/%{asmarch}/kernel/module.lds ]; then
      cp -a --parents arch/%{asmarch}/kernel/module.lds $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
    fi
    find $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/scripts \( -iname "*.o" -o -iname "*.cmd" \) -exec rm -f {} +
%ifarch ppc64le
    cp -a --parents arch/powerpc/lib/crtsavres.[So] $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
%endif
    if [ -d arch/%{asmarch}/include ]; then
      cp -a --parents arch/%{asmarch}/include $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
    fi
    if [ -d tools/arch/%{asmarch}/include ]; then
      cp -a --parents tools/arch/%{asmarch}/include $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
    fi
%ifarch aarch64
    # arch/arm64/include/asm/xen references arch/arm
    cp -a --parents arch/arm/include/asm/xen $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
    # arch/arm64/include/asm/opcodes.h references arch/arm
    cp -a --parents arch/arm/include/asm/opcodes.h $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
%endif
    cp -a include $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/include
    # Cross-reference from include/perf/events/sof.h
    cp -a sound/soc/sof/sof-audio.h $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/sound/soc/sof
%ifarch i686 x86_64
    # files for 'make prepare' to succeed with kernel-devel
    cp -a --parents arch/x86/entry/syscalls/syscall_32.tbl $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
    cp -a --parents arch/x86/entry/syscalls/syscall_64.tbl $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
    cp -a --parents arch/x86/tools/relocs_32.c $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
    cp -a --parents arch/x86/tools/relocs_64.c $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
    cp -a --parents arch/x86/tools/relocs.c $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
    cp -a --parents arch/x86/tools/relocs_common.c $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
    cp -a --parents arch/x86/tools/relocs.h $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
    cp -a --parents arch/x86/purgatory/purgatory.c $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
    cp -a --parents arch/x86/purgatory/stack.S $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
    cp -a --parents arch/x86/purgatory/setup-x86_64.S $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
    cp -a --parents arch/x86/purgatory/entry64.S $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
    cp -a --parents arch/x86/boot/string.h $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
    cp -a --parents arch/x86/boot/string.c $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
    cp -a --parents arch/x86/boot/ctype.h $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/

    cp -a --parents scripts/syscalltbl.sh $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/
    cp -a --parents scripts/syscallhdr.sh $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/

    cp -a --parents tools/arch/x86/include/asm $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
    cp -a --parents tools/arch/x86/include/uapi/asm $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
    cp -a --parents tools/objtool/arch/x86/lib $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
    cp -a --parents tools/arch/x86/lib/ $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
    cp -a --parents tools/arch/x86/tools/gen-insn-attr-x86.awk $RPM_BUILD_ROOT/lib/modules/$KernelVer/build
    cp -a --parents tools/objtool/arch/x86/ $RPM_BUILD_ROOT/lib/modules/$KernelVer/build

%endif
    %{log_msg "Clean up intermediate tools files"}
    # Clean up intermediate tools files
    find $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/tools \( -iname "*.o" -o -iname "*.cmd" \) -exec rm -f {} +

    # Make sure the Makefile, version.h, and auto.conf have a matching
    # timestamp so that external modules can be built
    touch -r $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/Makefile \
        $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/include/generated/uapi/linux/version.h \
        $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/include/config/auto.conf

%if %{with_debuginfo}
    eu-readelf -n vmlinux | grep "Build ID" | awk '{print $NF}' > vmlinux.id
    cp vmlinux.id $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/vmlinux.id

    %{log_msg "Copy additional files for kernel-debuginfo rpm"}
    #
    # save the vmlinux file for kernel debugging into the kernel-debuginfo rpm
    # (use mv + symlink instead of cp to reduce disk space requirements)
    #
    mkdir -p $RPM_BUILD_ROOT%{debuginfodir}/lib/modules/$KernelVer
    mv vmlinux $RPM_BUILD_ROOT%{debuginfodir}/lib/modules/$KernelVer
    ln -s $RPM_BUILD_ROOT%{debuginfodir}/lib/modules/$KernelVer/vmlinux vmlinux
    if [ -n "%{?vmlinux_decompressor}" ]; then
	    eu-readelf -n  %{vmlinux_decompressor} | grep "Build ID" | awk '{print $NF}' > vmlinux.decompressor.id
	    # Without build-id the build will fail. But for s390 the build-id
	    # wasn't added before 5.11. In case it is missing prefer not
	    # packaging the debuginfo over a build failure.
	    if [ -s vmlinux.decompressor.id ]; then
		    cp vmlinux.decompressor.id $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/vmlinux.decompressor.id
		    cp %{vmlinux_decompressor} $RPM_BUILD_ROOT%{debuginfodir}/lib/modules/$KernelVer/vmlinux.decompressor
	    fi
    fi

    # build and copy the vmlinux-gdb plugin files into kernel-debuginfo
    %{make} ARCH=$Arch %{?_smp_mflags} scripts_gdb
    cp -a --parents scripts/gdb/{,linux/}*.py $RPM_BUILD_ROOT%{debuginfodir}/lib/modules/$KernelVer
    # this should be a relative symlink (Kbuild creates an absolute one)
    ln -s scripts/gdb/vmlinux-gdb.py $RPM_BUILD_ROOT%{debuginfodir}/lib/modules/$KernelVer/vmlinux-gdb.py
    %py_byte_compile %{python3} $RPM_BUILD_ROOT%{debuginfodir}/lib/modules/$KernelVer/scripts/gdb
%endif

    %{log_msg "Create modnames"}
    find $RPM_BUILD_ROOT/lib/modules/$KernelVer -name "*.ko" -type f >modnames

    # mark modules executable so that strip-to-file can strip them
    xargs --no-run-if-empty chmod u+x < modnames

    # Generate a list of modules for block and networking.
    %{log_msg "Generate a list of modules for block and networking"}
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

    %{log_msg "detect missing or incorrect license tags"}
    # detect missing or incorrect license tags
    ( find $RPM_BUILD_ROOT/lib/modules/$KernelVer -name '*.ko' | xargs /sbin/modinfo -l | \
        grep -E -v 'GPL( v2)?$|Dual BSD/GPL$|Dual MPL/GPL$|GPL and additional rights$' ) && exit 1


    if [ $DoModules -eq 0 ]; then
        %{log_msg "Create empty files for RPM packaging"}
        # Ensure important files/directories exist to let the packaging succeed
        echo '%%defattr(-,-,-)' > ../kernel${Variant:+-${Variant}}-modules-core.list
        echo '%%defattr(-,-,-)' > ../kernel${Variant:+-${Variant}}-modules.list
        echo '%%defattr(-,-,-)' > ../kernel${Variant:+-${Variant}}-modules-extra.list
        echo '%%defattr(-,-,-)' > ../kernel${Variant:+-${Variant}}-modules-internal.list
        echo '%%defattr(-,-,-)' > ../kernel${Variant:+-${Variant}}-modules-partner.list
        mkdir -p $RPM_BUILD_ROOT/lib/modules/$KernelVer/kernel
        # Add files usually created by make modules, needed to prevent errors
        # thrown by depmod during package installation
        touch $RPM_BUILD_ROOT/lib/modules/$KernelVer/modules.order
        touch $RPM_BUILD_ROOT/lib/modules/$KernelVer/modules.builtin
    fi

    # Copy the System.map file for depmod to use
    cp System.map $RPM_BUILD_ROOT/.

    if [[ "$Variant" == "rt" || "$Variant" == "rt-debug" || "$Variant" == "rt-64k" || "$Variant" == "rt-64k-debug" || "$Variant" == "automotive" || "$Variant" == "automotive-debug" ]]; then
	%{log_msg "Skipping efiuki build"}
    else
%if %{with_efiuki}
        %{log_msg "Setup the EFI UKI kernel"}

        # RHEL/CentOS specific .SBAT entries
%if 0%{?centos}
        SBATsuffix="centos"
%else
%if 0%{?fedora}
        SBATsuffix="fedora"
%else
        SBATsuffix="rhel"
%endif
%endif
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

    	dracut --conf=%{SOURCE86} \
           --confdir=$(mktemp -d) \
           --verbose \
           --kver "$KernelVer" \
           --kmoddir "$RPM_BUILD_ROOT/lib/modules/$KernelVer/" \
           --logfile=$(mktemp) \
           --uefi \
%if 0%{?rhel} && !0%{?eln}
           --sbat "$SBAT" \
%endif
           --kernel-image $(realpath $KernelImage) \
           --kernel-cmdline 'console=tty0 console=ttyS0' \
	   $KernelUnifiedImage

  KernelAddonsDirOut="$KernelUnifiedImage.extra.d"
  mkdir -p $KernelAddonsDirOut
  python3 %{SOURCE151} %{SOURCE152} $KernelAddonsDirOut virt %{primary_target} %{_target_cpu} "$ADDONS_SBAT"

%if %{signkernel}
	%{log_msg "Sign the EFI UKI kernel"}
%if 0%{?fedora}%{?eln}
        %pesign -s -i $KernelUnifiedImage -o $KernelUnifiedImage.signed -a %{secureboot_ca_0} -c %{secureboot_key_0} -n %{pesign_name_0}
%else
%if 0%{?centos}
        UKI_secureboot_name=centossecureboot204
%else
        UKI_secureboot_name=redhatsecureboot504
%endif
        UKI_secureboot_cert=%{_datadir}/pki/sb-certs/secureboot-uki-virt-%{_arch}.cer

        %pesign -s -i $KernelUnifiedImage -o $KernelUnifiedImage.signed -a %{secureboot_ca_0} -c $UKI_secureboot_cert -n $UKI_secureboot_name
# 0%{?fedora}%{?eln}
%endif
        if [ ! -s $KernelUnifiedImage.signed ]; then
            echo "pesigning failed"
            exit 1
        fi
        mv $KernelUnifiedImage.signed $KernelUnifiedImage

      for addon in "$KernelAddonsDirOut"/*; do
        %pesign -s -i $addon -o $addon.signed -a %{secureboot_ca_0} -c %{secureboot_key_0} -n %{pesign_name_0}
        rm -f $addon
        mv $addon.signed $addon
      done

# signkernel
%endif

    # hmac sign the UKI for FIPS
    KernelUnifiedImageHMAC="$KernelUnifiedImageDir/.$InstallName-virt.efi.hmac"
    %{log_msg "hmac sign the UKI for FIPS"}
    %{log_msg "Creating hmac file: $KernelUnifiedImageHMAC"}
    (cd $KernelUnifiedImageDir && sha512hmac $InstallName-virt.efi) > $KernelUnifiedImageHMAC;

# with_efiuki
%endif
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
            %{SOURCE20} "$RPM_BUILD_ROOT" lib/modules/$KernelVer $absolute_file_list
	fi

%if %{zipmodules}
        # deny-mod script works with kmods as they are now (not compressed),
        # but if they will be we need to add compext to all
        sed -i %{?zipsed} $absolute_file_list
%endif
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

        %{log_msg "Create module list files for all kernel variants"}
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
        %{SOURCE22} -l "../filtermods-$KernelVer.log" sort -d $RPM_BUILD_ROOT/lib/modules/$KernelVer/modules.dep -c configs/def_variants.yaml $variants_param -o .. || ret=$?
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
%if 0%{!?fedora:1}
        create_module_file_list "partner" ../modules-partner.list ../kernel${Variant:+-${Variant}}-modules-partner.list 1 1
%endif
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
    %{log_msg "Cleanup build files"}
    rm -f $RPM_BUILD_ROOT/System.map
    %{log_msg "Remove depmod files"}
    remove_depmod_files

%if %{with_cross}
    make -C $RPM_BUILD_ROOT/lib/modules/$KernelVer/build M=scripts clean
    make -C $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/tools/bpf/resolve_btfids clean
    sed -i 's/REBUILD_SCRIPTS_FOR_CROSS:=0/REBUILD_SCRIPTS_FOR_CROSS:=1/' $RPM_BUILD_ROOT/lib/modules/$KernelVer/build/Makefile
%endif

    # Move the devel headers out of the root file system
    %{log_msg "Move the devel headers to RPM_BUILD_ROOT"}
    mkdir -p $RPM_BUILD_ROOT/usr/src/kernels
    mv $RPM_BUILD_ROOT/lib/modules/$KernelVer/build $RPM_BUILD_ROOT/$DevelDir

    # This is going to create a broken link during the build, but we don't use
    # it after this point.  We need the link to actually point to something
    # when kernel-devel is installed, and a relative link doesn't work across
    # the F17 UsrMove feature.
    ln -sf $DevelDir $RPM_BUILD_ROOT/lib/modules/$KernelVer/build

%if %{with_debuginfo}
    # Generate vmlinux.h and put it to kernel-devel path
    # zfcpdump build does not have btf anymore
    if [ "$Variant" != "zfcpdump" ]; then
	%{log_msg "Build the bootstrap bpftool to generate vmlinux.h"}
        # Build the bootstrap bpftool to generate vmlinux.h
        BuildBpftool
        tools/bpf/bpftool/bootstrap/bpftool btf dump file vmlinux format c > $RPM_BUILD_ROOT/$DevelDir/vmlinux.h
    fi
%endif

    %{log_msg "Cleanup kernel-devel and kernel-debuginfo files"}
    # prune junk from kernel-devel
    find $RPM_BUILD_ROOT/usr/src/kernels -name ".*.cmd" -delete
    # prune junk from kernel-debuginfo
    find $RPM_BUILD_ROOT/usr/src/kernels -name "*.mod.c" -delete

    # Red Hat UEFI Secure Boot CA cert, which can be used to authenticate the kernel
    %{log_msg "Install certs"}
    mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/kernel-keys/$KernelVer
%if %{signkernel}
    install -m 0644 %{secureboot_ca_0} $RPM_BUILD_ROOT%{_datadir}/doc/kernel-keys/$KernelVer/kernel-signing-ca.cer
    %ifarch s390x ppc64le
    if [ -x /usr/bin/rpm-sign ]; then
        install -m 0644 %{secureboot_key_0} $RPM_BUILD_ROOT%{_datadir}/doc/kernel-keys/$KernelVer/%{signing_key_filename}
    fi
    %endif
%endif

%if 0%{?rhel}
    # Red Hat IMA code-signing cert, which is used to authenticate package files
    install -m 0644 %{ima_signing_cert} $RPM_BUILD_ROOT%{_datadir}/doc/kernel-keys/$KernelVer/%{ima_cert_name}
%endif

%if %{signmodules}
    if [ $DoModules -eq 1 ]; then
        # Save the signing keys so we can sign the modules in __modsign_install_post
        cp certs/signing_key.pem certs/signing_key.pem.sign${Variant:++${Variant}}
        cp certs/signing_key.x509 certs/signing_key.x509.sign${Variant:++${Variant}}
        %ifarch s390x ppc64le
        if [ ! -x /usr/bin/rpm-sign ]; then
            install -m 0644 certs/signing_key.x509.sign${Variant:++${Variant}} $RPM_BUILD_ROOT%{_datadir}/doc/kernel-keys/$KernelVer/kernel-signing-ca.cer
            openssl x509 -in certs/signing_key.pem.sign${Variant:++${Variant}} -outform der -out $RPM_BUILD_ROOT%{_datadir}/doc/kernel-keys/$KernelVer/%{signing_key_filename}
            chmod 0644 $RPM_BUILD_ROOT%{_datadir}/doc/kernel-keys/$KernelVer/%{signing_key_filename}
        fi
        %endif
    fi
%endif

%if %{with_gcov}
    popd
%endif
}

###
# DO it...
###

# prepare directories
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/boot
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}

cd linux-%{KVERREL}

%if %{with_debug}
%if %{with_realtime}
BuildKernel %make_target %kernel_image %{_use_vdso} rt-debug
%endif

%if %{with_realtime_arm64_64k}
BuildKernel %make_target %kernel_image %{_use_vdso} rt-64k-debug
%endif

%if %{with_automotive}
BuildKernel %make_target %kernel_image %{_use_vdso} automotive-debug
%endif

%if %{with_arm64_16k}
BuildKernel %make_target %kernel_image %{_use_vdso} 16k-debug
%endif

%if %{with_arm64_64k}
BuildKernel %make_target %kernel_image %{_use_vdso} 64k-debug
%endif

%if %{with_up}
BuildKernel %make_target %kernel_image %{_use_vdso} debug
%endif
%endif

%if %{with_zfcpdump}
BuildKernel %make_target %kernel_image %{_use_vdso} zfcpdump
%endif

%if %{with_arm64_16k_base}
BuildKernel %make_target %kernel_image %{_use_vdso} 16k
%endif

%if %{with_arm64_64k_base}
BuildKernel %make_target %kernel_image %{_use_vdso} 64k
%endif

%if %{with_realtime_base}
BuildKernel %make_target %kernel_image %{_use_vdso} rt
%endif

%if %{with_realtime_arm64_64k_base}
BuildKernel %make_target %kernel_image %{_use_vdso} rt-64k
%endif

%if %{with_automotive_base}
BuildKernel %make_target %kernel_image %{_use_vdso} automotive
%endif

%if %{with_up_base}
BuildKernel %make_target %kernel_image %{_use_vdso}
%endif

%ifnarch noarch i686 %{nobuildarches}
%if !%{with_debug} && !%{with_zfcpdump} && !%{with_up} && !%{with_arm64_16k} && !%{with_arm64_64k} && !%{with_realtime} && !%{with_realtime_arm64_64k} && !%{with_automotive}
# If only building the user space tools, then initialize the build environment
# and some variables so that the various userspace tools can be built.
%{log_msg "Initialize userspace tools build environment"}
InitBuildVars
# Some tests build also modules, and need Module.symvers
if ! [[ -e Module.symvers ]] && [[ -f $DevelDir/Module.symvers ]]; then
    %{log_msg "Found Module.symvers in DevelDir, copying to ."}
    cp "$DevelDir/Module.symvers" .
fi
%endif
%endif

%ifarch aarch64
%global perf_build_extra_opts CORESIGHT=1
%endif
%global perf_make \
  %{__make} %{?make_opts} EXTRA_CFLAGS="${RPM_OPT_FLAGS}" EXTRA_CXXFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags} -Wl,-E" %{?cross_opts} -C tools/perf V=1 NO_PERF_READ_VDSO32=1 NO_PERF_READ_VDSOX32=1 WERROR=0 NO_LIBUNWIND=1 HAVE_CPLUS_DEMANGLE=1 NO_GTK2=1 NO_STRLCPY=1 NO_BIONIC=1 %{?perf_libbpf_dynamic} LIBTRACEEVENT_DYNAMIC=1 %{?perf_build_extra_opts} prefix=%{_prefix} PYTHON=%{__python3}
%if %{with_perf}
%{log_msg "Build perf"}
# perf
# make sure check-headers.sh is executable
chmod +x tools/perf/check-headers.sh
%{perf_make} DESTDIR=$RPM_BUILD_ROOT all
%endif

%if %{with_libperf}
%global libperf_make \
  %{__make} %{?make_opts} EXTRA_CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" %{?cross_opts} -C tools/lib/perf V=1
  %{log_msg "build libperf"}
%{libperf_make} DESTDIR=$RPM_BUILD_ROOT
%endif

%global tools_make \
  CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" EXTRA_CFLAGS="${RPM_OPT_FLAGS}" %{make} %{?make_opts}

%ifarch %{cpupowerarchs}
    # link against in-tree libcpupower for idle state support
    %global rtla_make %{tools_make} LDFLAGS="%{__global_ldflags} -L../../power/cpupower" INCLUDES="-I../../power/cpupower/lib"
%else
    %global rtla_make %{tools_make}
%endif

%if %{with_tools}

%if %{with_ynl}
pushd tools/net/ynl
export PIP_CONFIG_FILE=/tmp/pip.config
cat <<EOF > $PIP_CONFIG_FILE
[install]
no-index = true
no-build-isolation = false
EOF
%{tools_make} %{?_smp_mflags} DESTDIR=$RPM_BUILD_ROOT install
popd
%endif

%ifarch %{cpupowerarchs}
# cpupower
# make sure version-gen.sh is executable.
chmod +x tools/power/cpupower/utils/version-gen.sh
%{log_msg "build cpupower"}
%{tools_make} %{?_smp_mflags} -C tools/power/cpupower CPUFREQ_BENCH=false DEBUG=false
%ifarch x86_64
    pushd tools/power/cpupower/debug/x86_64
    %{log_msg "build centrino-decode powernow-k8-decode"}
    %{tools_make} %{?_smp_mflags} centrino-decode powernow-k8-decode
    popd
%endif
%ifarch x86_64
   pushd tools/power/x86/x86_energy_perf_policy/
   %{log_msg "build x86_energy_perf_policy"}
   %{tools_make}
   popd
   pushd tools/power/x86/turbostat
   %{log_msg "build turbostat"}
   %{tools_make}
   popd
   pushd tools/power/x86/intel-speed-select
   %{log_msg "build intel-speed-select"}
   %{tools_make}
   popd
   pushd tools/arch/x86/intel_sdsi
   %{log_msg "build intel_sdsi"}
   %{tools_make} CFLAGS="${RPM_OPT_FLAGS}"
   popd
%endif
%endif
pushd tools/thermal/tmon/
%{log_msg "build tmon"}
%{tools_make}
popd
pushd tools/bootconfig/
%{log_msg "build bootconfig"}
%{tools_make}
popd
pushd tools/iio/
%{log_msg "build iio"}
%{tools_make}
popd
pushd tools/gpio/
%{log_msg "build gpio"}
%{tools_make}
popd
# build VM tools
pushd tools/mm/
%{log_msg "build slabinfo page_owner_sort"}
%{tools_make} slabinfo page_owner_sort
popd
pushd tools/verification/rv/
%{log_msg "build rv"}
%{tools_make}
popd
pushd tools/tracing/rtla
%{log_msg "build rtla"}
%{rtla_make}
popd
%endif

#set RPM_VMLINUX_H
if [ -f $RPM_BUILD_ROOT/$DevelDir/vmlinux.h ]; then
  RPM_VMLINUX_H=$RPM_BUILD_ROOT/$DevelDir/vmlinux.h
elif [ -f $DevelDir/vmlinux.h ]; then
  RPM_VMLINUX_H=$DevelDir/vmlinux.h
fi
echo "${RPM_VMLINUX_H}" > ../vmlinux_h_path

%if %{with_selftests}
%{log_msg "start build selftests"}
# Unfortunately, samples/bpf/Makefile expects that the headers are installed
# in the source tree. We installed them previously to $RPM_BUILD_ROOT/usr
# but there's no way to tell the Makefile to take them from there.
%{log_msg "install headers for selftests"}
%{make} %{?_smp_mflags} headers_install

# If we re building only tools without kernel, we need to generate config
# headers and prepare tree for modules building. The modules_prepare target
# will cover both.
if [ ! -f include/generated/autoconf.h ]; then
   %{log_msg "modules_prepare for selftests"}
   %{make} %{?_smp_mflags} modules_prepare
fi

# Build BPFtool for samples/bpf
if [ ! -f tools/bpf/bpftool/bootstrap/bpftool ]; then
  BuildBpftool
fi

%{log_msg "build samples/bpf"}
%{make} %{?_smp_mflags} ARCH=$Arch BPFTOOL=$(pwd)/tools/bpf/bpftool/bootstrap/bpftool V=1 M=samples/bpf/ VMLINUX_H="${RPM_VMLINUX_H}" || true

pushd tools/testing/selftests
# We need to install here because we need to call make with ARCH set which
# doesn't seem possible to do in the install section.
%if %{selftests_must_build}
  force_targets="FORCE_TARGETS=1"
%else
  force_targets=""
%endif

%{log_msg "main selftests compile"}
%{make} %{?_smp_mflags} ARCH=$Arch V=1 TARGETS="bpf cgroup mm net net/forwarding net/mptcp net/netfilter net/packetdrill tc-testing memfd drivers/net/bonding iommu cachestat pid_namespace rlimits" SKIP_TARGETS="" $force_targets INSTALL_PATH=%{buildroot}%{_libexecdir}/kselftests VMLINUX_H="${RPM_VMLINUX_H}" install

%ifarch %{klptestarches}
	# kernel livepatching selftest test_modules will build against
	# /lib/modules/$(shell uname -r)/build tree unless KDIR is set
	export KDIR=$(realpath $(pwd)/../../..)
	%{make} %{?_smp_mflags} ARCH=$Arch V=1 TARGETS="livepatch" SKIP_TARGETS="" $force_targets INSTALL_PATH=%{buildroot}%{_libexecdir}/kselftests VMLINUX_H="${RPM_VMLINUX_H}" install || true
%endif

# 'make install' for bpf is broken and upstream refuses to fix it.
# Install the needed files manually.
%{log_msg "install selftests"}
for dir in bpf bpf/no_alu32 bpf/progs; do
	# In ARK, the rpm build continues even if some of the selftests
	# cannot be built. It's not always possible to build selftests,
	# as upstream sometimes dependens on too new llvm version or has
	# other issues. If something did not get built, just skip it.
	test -d $dir || continue
	mkdir -p %{buildroot}%{_libexecdir}/kselftests/$dir
	find $dir -maxdepth 1 -type f \( -executable -o -name '*.py' -o -name settings -o \
		-name 'btf_dump_test_case_*.c' -o -name '*.ko' -o \
		-name '*.o' -exec sh -c 'readelf -h "{}" | grep -q "^  Machine:.*BPF"' \; \) -print0 | \
	xargs -0 cp -t %{buildroot}%{_libexecdir}/kselftests/$dir || true
done
%buildroot_save_unstripped "usr/libexec/kselftests/bpf/test_progs"
%buildroot_save_unstripped "usr/libexec/kselftests/bpf/test_progs-no_alu32"
popd
%{log_msg "end build selftests"}
%endif

%if %{with_doc}
%{log_msg "start install docs"}
# Make the HTML pages.
%{log_msg "build html docs"}
%{__make} PYTHON=/usr/bin/python3 htmldocs || %{doc_build_fail}

# sometimes non-world-readable files sneak into the kernel source tree
chmod -R a=rX Documentation
find Documentation -type d | xargs chmod u+w
%{log_msg "end install docs"}
%endif

# Module signing (modsign)
#
# This must be run _after_ find-debuginfo.sh runs, otherwise that will strip
# the signature off of the modules.
#
# Don't sign modules for the zfcpdump variant as it is monolithic.

%define __modsign_install_post \
  if [ "%{signmodules}" -eq "1" ]; then \
    %{log_msg "Signing kernel modules ..."} \
    modules_dirs="$(shopt -s nullglob; echo $RPM_BUILD_ROOT/lib/modules/%{KVERREL}*)" \
    for modules_dir in $modules_dirs; do \
        variant_suffix="${modules_dir#$RPM_BUILD_ROOT/lib/modules/%{KVERREL}}" \
        [ "$variant_suffix" == "+zfcpdump" ] && continue \
	%{log_msg "Signing modules for %{KVERREL}${variant_suffix}"} \
        %{modsign_cmd} certs/signing_key.pem.sign${variant_suffix} certs/signing_key.x509.sign${variant_suffix} $modules_dir/ \
    done \
  fi \
  if [ "%{zipmodules}" -eq "1" ]; then \
    %{log_msg "Compressing kernel modules ..."} \
    find $RPM_BUILD_ROOT/lib/modules/ -type f -name '*.ko' | xargs -n 16 -P${RPM_BUILD_NCPUS} -r %compression %compression_flags; \
  fi \
%{nil}

###
### Special hacks for debuginfo subpackages.
###

# This macro is used by %%install, so we must redefine it before that.
%define debug_package %{nil}

%if %{with_debuginfo}

%ifnarch noarch %{nobuildarches}
%global __debug_package 1
%files -f debugfiles.list debuginfo-common-%{_target_cpu}
%endif

%endif

# We don't want to package debuginfo for self-tests and samples but
# we have to delete them to avoid an error messages about unpackaged
# files.
# Delete the debuginfo for kernel-devel files
%define __remove_unwanted_dbginfo_install_post \
  if [ "%{with_selftests}" -ne "0" ]; then \
    rm -rf $RPM_BUILD_ROOT/usr/lib/debug/usr/libexec/ksamples; \
    rm -rf $RPM_BUILD_ROOT/usr/lib/debug/usr/libexec/kselftests; \
  fi \
  rm -rf $RPM_BUILD_ROOT/usr/lib/debug/usr/src; \
%{nil}

# Make debugedit and gdb-add-index use target versions of tools
# when cross-compiling. This is supported since debugedit-5.1-5.fc42
# https://inbox.sourceware.org/debugedit/20250220153858.963312-1-mark@klomp.org/
%if %{with_cross}
%define __override_target_tools_for_debugedit \
	export OBJCOPY=%{_build_arch}-linux-gnu-objcopy \
	export NM=%{_build_arch}-linux-gnu-nm \
	export READELF=%{_build_arch}-linux-gnu-readelf \
%{nil}
%endif

#
# Disgusting hack alert! We need to ensure we sign modules *after* all
# invocations of strip occur, which is in __debug_install_post if
# find-debuginfo.sh runs, and __os_install_post if not.
#
%define __spec_install_post \
  %{?__override_target_tools_for_debugedit:%{__override_target_tools_for_debugedit}}\
  %{?__debug_package:%{__debug_install_post}}\
  %{__arch_install_post}\
  %{__os_install_post}\
  %{__remove_unwanted_dbginfo_install_post}\
  %{__restore_unstripped_root_post}\
  %{__modsign_install_post}

###
### install
###

%install

cd linux-%{KVERREL}

# re-define RPM_VMLINUX_H, because it doesn't carry over from %build
RPM_VMLINUX_H="$(cat ../vmlinux_h_path)"

%if %{with_doc}
docdir=$RPM_BUILD_ROOT%{_datadir}/doc/kernel-doc-%{specversion}-%{pkgrelease}

# copy the source over
mkdir -p $docdir
tar -h -f - --exclude=man --exclude='.*' -c Documentation | tar xf - -C $docdir
cat %{SOURCE2} | xz > $docdir/kernel.changelog.xz
chmod 0644 $docdir/kernel.changelog.xz

# with_doc
%endif

# We have to do the headers install before the tools install because the
# kernel headers_install will remove any header files in /usr/include that
# it doesn't install itself.

%if %{with_headers}
# Install kernel headers
%{__make} ARCH=%{hdrarch} INSTALL_HDR_PATH=$RPM_BUILD_ROOT/usr headers_install

find $RPM_BUILD_ROOT/usr/include \
     \( -name .install -o -name .check -o \
        -name ..install.cmd -o -name ..check.cmd \) -delete

%endif

%if %{with_cross_headers}
HDR_ARCH_LIST='arm64 powerpc s390 x86 riscv'
mkdir -p $RPM_BUILD_ROOT/usr/tmp-headers

for arch in $HDR_ARCH_LIST; do
	mkdir $RPM_BUILD_ROOT/usr/tmp-headers/arch-${arch}
	%{__make} ARCH=${arch} INSTALL_HDR_PATH=$RPM_BUILD_ROOT/usr/tmp-headers/arch-${arch} headers_install
done

find $RPM_BUILD_ROOT/usr/tmp-headers \
     \( -name .install -o -name .check -o \
        -name ..install.cmd -o -name ..check.cmd \) -delete

# Copy all the architectures we care about to their respective asm directories
for arch in $HDR_ARCH_LIST ; do
	mkdir -p $RPM_BUILD_ROOT/usr/${arch}-linux-gnu/include
	mv $RPM_BUILD_ROOT/usr/tmp-headers/arch-${arch}/include/* $RPM_BUILD_ROOT/usr/${arch}-linux-gnu/include/
done

rm -rf $RPM_BUILD_ROOT/usr/tmp-headers
%endif

%if %{with_kernel_abi_stablelists}
# kabi directory
INSTALL_KABI_PATH=$RPM_BUILD_ROOT/lib/modules/
mkdir -p $INSTALL_KABI_PATH

# install kabi releases directories
tar -xvf %{SOURCE300} -C $INSTALL_KABI_PATH
# with_kernel_abi_stablelists
%endif

%if %{with_perf}
# perf tool binary and supporting scripts/binaries
%{perf_make} DESTDIR=$RPM_BUILD_ROOT lib=%{_lib} install-bin
# remove the 'trace' symlink.
rm -f %{buildroot}%{_bindir}/trace

# For both of the below, yes, this should be using a macro but right now
# it's hard coded and we don't actually want it anyway right now.
# Whoever wants examples can fix it up!

# remove examples
rm -rf %{buildroot}/usr/lib/perf/examples
rm -rf %{buildroot}/usr/lib/perf/include

# python-perf extension
%{perf_make} DESTDIR=$RPM_BUILD_ROOT install-python_ext

# perf man pages (note: implicit rpm magic compresses them later)
mkdir -p %{buildroot}/%{_mandir}/man1
%{perf_make} DESTDIR=$RPM_BUILD_ROOT install-man

# remove any tracevent files, eg. its plugins still gets built and installed,
# even if we build against system's libtracevent during perf build (by setting
# LIBTRACEEVENT_DYNAMIC=1 above in perf_make macro). Those files should already
# ship with libtraceevent package.
rm -rf %{buildroot}%{_libdir}/traceevent
%endif

%if %{with_libperf}
%{libperf_make} DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{_libdir} install install_headers
# This is installed on some arches and we don't want to ship it
rm -rf %{buildroot}%{_libdir}/libperf.a
%endif

%if %{with_tools}
%ifarch %{cpupowerarchs}
%{make} -C tools/power/cpupower DESTDIR=$RPM_BUILD_ROOT libdir=%{_libdir} mandir=%{_mandir} CPUFREQ_BENCH=false install
%find_lang cpupower
mv cpupower.lang ../
%ifarch x86_64
    pushd tools/power/cpupower/debug/x86_64
    install -m755 centrino-decode %{buildroot}%{_bindir}/centrino-decode
    install -m755 powernow-k8-decode %{buildroot}%{_bindir}/powernow-k8-decode
    popd
%endif
chmod 0755 %{buildroot}%{_libdir}/libcpupower.so*
%endif
%ifarch x86_64
   mkdir -p %{buildroot}%{_mandir}/man8
   pushd tools/power/x86/x86_energy_perf_policy
   %{tools_make} DESTDIR=%{buildroot} install
   popd
   pushd tools/power/x86/turbostat
   %{tools_make} DESTDIR=%{buildroot} install
   popd
   pushd tools/power/x86/intel-speed-select
   %{tools_make} DESTDIR=%{buildroot} install
   popd
   pushd tools/arch/x86/intel_sdsi
   %{tools_make} CFLAGS="${RPM_OPT_FLAGS}" DESTDIR=%{buildroot} BINDIR=%{_sbindir} install
   popd
%endif
pushd tools/thermal/tmon
%{tools_make} INSTALL_ROOT=%{buildroot} install
popd
pushd tools/bootconfig
%{tools_make} DESTDIR=%{buildroot} install
popd
pushd tools/iio
%{tools_make} DESTDIR=%{buildroot} install
popd
pushd tools/gpio
%{tools_make} DESTDIR=%{buildroot} install
popd
install -m644 -D %{SOURCE2002} %{buildroot}%{_sysconfdir}/logrotate.d/kvm_stat
pushd tools/kvm/kvm_stat
%{__make} INSTALL_ROOT=%{buildroot} install-tools
%{__make} INSTALL_ROOT=%{buildroot} install-man
install -m644 -D kvm_stat.service %{buildroot}%{_unitdir}/kvm_stat.service
popd
# install VM tools
pushd tools/mm/
install -m755 slabinfo %{buildroot}%{_bindir}/slabinfo
install -m755 page_owner_sort %{buildroot}%{_bindir}/page_owner_sort
popd
pushd tools/verification/rv/
%{tools_make} DESTDIR=%{buildroot} install
popd
pushd tools/tracing/rtla/
%{tools_make} DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_bindir}/hwnoise
rm -f %{buildroot}%{_bindir}/osnoise
rm -f %{buildroot}%{_bindir}/timerlat
(cd %{buildroot}

        ln -sf rtla ./%{_bindir}/hwnoise
        ln -sf rtla ./%{_bindir}/osnoise
        ln -sf rtla ./%{_bindir}/timerlat
)
popd
%endif

%if %{with_selftests}
pushd samples
install -d %{buildroot}%{_libexecdir}/ksamples
# install bpf samples
pushd bpf
install -d %{buildroot}%{_libexecdir}/ksamples/bpf
find -type f -executable -exec install -m755 {} %{buildroot}%{_libexecdir}/ksamples/bpf \;
install -m755 *.sh %{buildroot}%{_libexecdir}/ksamples/bpf
# test_lwt_bpf.sh compiles test_lwt_bpf.c when run; this works only from the
# kernel tree. Just remove it.
rm %{buildroot}%{_libexecdir}/ksamples/bpf/test_lwt_bpf.sh
install -m644 *_kern.o %{buildroot}%{_libexecdir}/ksamples/bpf || true
install -m644 tcp_bpf.readme %{buildroot}%{_libexecdir}/ksamples/bpf
popd
# install pktgen samples
pushd pktgen
install -d %{buildroot}%{_libexecdir}/ksamples/pktgen
find . -type f -executable -exec install -m755 {} %{buildroot}%{_libexecdir}/ksamples/pktgen/{} \;
find . -type f ! -executable -exec install -m644 {} %{buildroot}%{_libexecdir}/ksamples/pktgen/{} \;
popd
popd
# install mm selftests
pushd tools/testing/selftests/mm
find -type d -exec install -d %{buildroot}%{_libexecdir}/kselftests/mm/{} \;
find -type f -executable -exec install -D -m755 {} %{buildroot}%{_libexecdir}/kselftests/mm/{} \;
find -type f ! -executable -exec install -D -m644 {} %{buildroot}%{_libexecdir}/kselftests/mm/{} \;
popd
# install cgroup selftests
pushd tools/testing/selftests/cgroup
find -type d -exec install -d %{buildroot}%{_libexecdir}/kselftests/cgroup/{} \;
find -type f -executable -exec install -D -m755 {} %{buildroot}%{_libexecdir}/kselftests/cgroup/{} \;
find -type f ! -executable -exec install -D -m644 {} %{buildroot}%{_libexecdir}/kselftests/cgroup/{} \;
popd
# install drivers/net/mlxsw selftests
pushd tools/testing/selftests/drivers/net/mlxsw
find -type d -exec install -d %{buildroot}%{_libexecdir}/kselftests/drivers/net/mlxsw/{} \;
find -type f -executable -exec install -D -m755 {} %{buildroot}%{_libexecdir}/kselftests/drivers/net/mlxsw/{} \;
find -type f ! -executable -exec install -D -m644 {} %{buildroot}%{_libexecdir}/kselftests/drivers/net/mlxsw/{} \;
popd
# install drivers/net/netdevsim selftests
pushd tools/testing/selftests/drivers/net/netdevsim
find -type d -exec install -d %{buildroot}%{_libexecdir}/kselftests/drivers/net/netdevsim/{} \;
find -type f -executable -exec install -D -m755 {} %{buildroot}%{_libexecdir}/kselftests/drivers/net/netdevsim/{} \;
find -type f ! -executable -exec install -D -m644 {} %{buildroot}%{_libexecdir}/kselftests/drivers/net/netdevsim/{} \;
popd
# install drivers/net/bonding selftests
pushd tools/testing/selftests/drivers/net/bonding
find -type d -exec install -d %{buildroot}%{_libexecdir}/kselftests/drivers/net/bonding/{} \;
find -type f -executable -exec install -D -m755 {} %{buildroot}%{_libexecdir}/kselftests/drivers/net/bonding/{} \;
find -type f ! -executable -exec install -D -m644 {} %{buildroot}%{_libexecdir}/kselftests/drivers/net/bonding/{} \;
popd
# install net/forwarding selftests
pushd tools/testing/selftests/net/forwarding
find -type d -exec install -d %{buildroot}%{_libexecdir}/kselftests/net/forwarding/{} \;
find -type f -executable -exec install -D -m755 {} %{buildroot}%{_libexecdir}/kselftests/net/forwarding/{} \;
find -type f ! -executable -exec install -D -m644 {} %{buildroot}%{_libexecdir}/kselftests/net/forwarding/{} \;
popd
# install net/mptcp selftests
pushd tools/testing/selftests/net/mptcp
find -type d -exec install -d %{buildroot}%{_libexecdir}/kselftests/net/mptcp/{} \;
find -type f -executable -exec install -D -m755 {} %{buildroot}%{_libexecdir}/kselftests/net/mptcp/{} \;
find -type f ! -executable -exec install -D -m644 {} %{buildroot}%{_libexecdir}/kselftests/net/mptcp/{} \;
popd
# install tc-testing selftests
pushd tools/testing/selftests/tc-testing
find -type d -exec install -d %{buildroot}%{_libexecdir}/kselftests/tc-testing/{} \;
find -type f -executable -exec install -D -m755 {} %{buildroot}%{_libexecdir}/kselftests/tc-testing/{} \;
find -type f ! -executable -exec install -D -m644 {} %{buildroot}%{_libexecdir}/kselftests/tc-testing/{} \;
popd
# install livepatch selftests
pushd tools/testing/selftests/livepatch
find -type d -exec install -d %{buildroot}%{_libexecdir}/kselftests/livepatch/{} \;
find -type f -executable -exec install -D -m755 {} %{buildroot}%{_libexecdir}/kselftests/livepatch/{} \;
find -type f ! -executable -exec install -D -m644 {} %{buildroot}%{_libexecdir}/kselftests/livepatch/{} \;
popd
# install net/netfilter selftests
pushd tools/testing/selftests/net/netfilter
find -type d -exec install -d %{buildroot}%{_libexecdir}/kselftests/net/netfilter/{} \;
find -type f -executable -exec install -D -m755 {} %{buildroot}%{_libexecdir}/kselftests/net/netfilter/{} \;
find -type f ! -executable -exec install -D -m644 {} %{buildroot}%{_libexecdir}/kselftests/net/netfilter/{} \;
popd
# install net/packetdrill selftests
pushd tools/testing/selftests/net/packetdrill
find -type d -exec install -d %{buildroot}%{_libexecdir}/kselftests/net/packetdrill/{} \;
find -type f -executable -exec install -D -m755 {} %{buildroot}%{_libexecdir}/kselftests/net/packetdrill/{} \;
find -type f ! -executable -exec install -D -m644 {} %{buildroot}%{_libexecdir}/kselftests/net/packetdrill/{} \;
popd

# install memfd selftests
pushd tools/testing/selftests/memfd
find -type d -exec install -d %{buildroot}%{_libexecdir}/kselftests/memfd/{} \;
find -type f -executable -exec install -D -m755 {} %{buildroot}%{_libexecdir}/kselftests/memfd/{} \;
find -type f ! -executable -exec install -D -m644 {} %{buildroot}%{_libexecdir}/kselftests/memfd/{} \;
popd
# install iommu selftests
pushd tools/testing/selftests/iommu
find -type d -exec install -d %{buildroot}%{_libexecdir}/kselftests/iommu/{} \;
find -type f -executable -exec install -D -m755 {} %{buildroot}%{_libexecdir}/kselftests/iommu/{} \;
find -type f ! -executable -exec install -D -m644 {} %{buildroot}%{_libexecdir}/kselftests/iommu/{} \;
popd
# install rlimits selftests
pushd tools/testing/selftests/rlimits
find -type d -exec install -d %{buildroot}%{_libexecdir}/kselftests/rlimits/{} \;
find -type f -executable -exec install -D -m755 {} %{buildroot}%{_libexecdir}/kselftests/rlimits/{} \;
find -type f ! -executable -exec install -D -m644 {} %{buildroot}%{_libexecdir}/kselftests/rlimits/{} \;
popd
# install pid_namespace selftests
pushd tools/testing/selftests/pid_namespace
find -type d -exec install -d %{buildroot}%{_libexecdir}/kselftests/pid_namespace/{} \;
find -type f -executable -exec install -D -m755 {} %{buildroot}%{_libexecdir}/kselftests/pid_namespace/{} \;
find -type f ! -executable -exec install -D -m644 {} %{buildroot}%{_libexecdir}/kselftests/pid_namespace/{} \;
popd
%endif

###
### clean
###

###
### scripts
###

%if %{with_tools}
%post -n %{package_name}-tools-libs
/sbin/ldconfig

%postun -n %{package_name}-tools-libs
/sbin/ldconfig
%endif

#
# This macro defines a %%post script for a kernel*-devel package.
#	%%kernel_devel_post [<subpackage>]
# Note we don't run hardlink if ostree is in use, as ostree is
# a far more sophisticated hardlink implementation.
# https://github.com/projectatomic/rpm-ostree/commit/58a79056a889be8814aa51f507b2c7a4dccee526
#
# The deletion of *.hardlink-temporary files is a temporary workaround
# for this bug in the hardlink binary (fixed in util-linux 2.38):
# https://github.com/util-linux/util-linux/issues/1602
#
%define kernel_devel_post() \
%{expand:%%post %{?1:%{1}-}devel}\
if [ -f /etc/sysconfig/kernel ]\
then\
    . /etc/sysconfig/kernel || exit $?\
fi\
if [ "$HARDLINK" != "no" -a -x /usr/bin/hardlink -a ! -e /run/ostree-booted ] \
then\
    (cd /usr/src/kernels/%{KVERREL}%{?1:+%{1}} &&\
     /usr/bin/find . -type f | while read f; do\
       hardlink -c /usr/src/kernels/*%{?dist}.*/$f $f > /dev/null\
     done;\
     /usr/bin/find /usr/src/kernels -type f -name '*.hardlink-temporary' -delete\
    )\
fi\
%if %{with_cross}\
    echo "Building scripts and resolve_btfids"\
    env --unset=ARCH make -C /usr/src/kernels/%{KVERREL}%{?1:+%{1}} prepare_after_cross\
%endif\
%{nil}

#
# This macro defines a %%post script for a kernel*-modules-extra package.
# It also defines a %%postun script that does the same thing.
#	%%kernel_modules_extra_post [<subpackage>]
#
%define kernel_modules_extra_post() \
%{expand:%%post %{?1:%{1}-}modules-extra}\
/sbin/depmod -a %{KVERREL}%{?1:+%{1}}\
%{nil}\
%{expand:%%postun %{?1:%{1}-}modules-extra}\
/sbin/depmod -a %{KVERREL}%{?1:+%{1}}\
%{nil}

#
# This macro defines a %%post script for a kernel*-modules-internal package.
# It also defines a %%postun script that does the same thing.
#	%%kernel_modules_internal_post [<subpackage>]
#
%define kernel_modules_internal_post() \
%{expand:%%post %{?1:%{1}-}modules-internal}\
/sbin/depmod -a %{KVERREL}%{?1:+%{1}}\
%{nil}\
%{expand:%%postun %{?1:%{1}-}modules-internal}\
/sbin/depmod -a %{KVERREL}%{?1:+%{1}}\
%{nil}

#
# This macro defines a %%post script for a kernel*-modules-partner package.
# It also defines a %%postun script that does the same thing.
#	%%kernel_modules_partner_post [<subpackage>]
#
%define kernel_modules_partner_post() \
%{expand:%%post %{?1:%{1}-}modules-partner}\
/sbin/depmod -a %{KVERREL}%{?1:+%{1}}\
%{nil}\
%{expand:%%postun %{?1:%{1}-}modules-partner}\
/sbin/depmod -a %{KVERREL}%{?1:+%{1}}\
%{nil}

#
# This macro defines a %%post script for a kernel*-modules package.
# It also defines a %%postun script that does the same thing.
#	%%kernel_modules_post [<subpackage>]
#
%define kernel_modules_post() \
%{expand:%%post %{?1:%{1}-}modules}\
/sbin/depmod -a %{KVERREL}%{?1:+%{1}}\
if [ ! -f %{_localstatedir}/lib/rpm-state/%{name}/installing_core_%{KVERREL}%{?1:+%{1}} ]; then\
	mkdir -p %{_localstatedir}/lib/rpm-state/%{name}\
	touch %{_localstatedir}/lib/rpm-state/%{name}/need_to_run_dracut_%{KVERREL}%{?1:+%{1}}\
fi\
%{nil}\
%{expand:%%postun %{?1:%{1}-}modules}\
/sbin/depmod -a %{KVERREL}%{?1:+%{1}}\
%{nil}\
%{expand:%%posttrans %{?1:%{1}-}modules}\
if [ -f %{_localstatedir}/lib/rpm-state/%{name}/need_to_run_dracut_%{KVERREL}%{?1:+%{1}} ]; then\
	rm -f %{_localstatedir}/lib/rpm-state/%{name}/need_to_run_dracut_%{KVERREL}%{?1:+%{1}}\
	echo "Running: dracut -f --kver %{KVERREL}%{?1:+%{1}}"\
	dracut -f --kver "%{KVERREL}%{?1:+%{1}}" || exit $?\
fi\
%{nil}

#
# This macro defines a %%post script for a kernel*-modules-core package.
#	%%kernel_modules_core_post [<subpackage>]
#
%define kernel_modules_core_post() \
%{expand:%%posttrans %{?1:%{1}-}modules-core}\
/sbin/depmod -a %{KVERREL}%{?1:+%{1}}\
%{nil}

# This macro defines a %%posttrans script for a kernel package.
#	%%kernel_variant_posttrans [-v <subpackage>] [-u uki-suffix]
# More text can follow to go at the end of this variant's %%post.
#
%define kernel_variant_posttrans(v:u:) \
%{expand:%%posttrans %{?-v:%{-v*}-}%{!?-u*:core}%{?-u*:uki-%{-u*}}}\
%if 0%{!?fedora:1}\
%if !%{with_automotive}\
if [ -x %{_sbindir}/weak-modules ]\
then\
    %{_sbindir}/weak-modules --add-kernel %{KVERREL}%{?-v:+%{-v*}} || exit $?\
fi\
%endif\
%endif\
rm -f %{_localstatedir}/lib/rpm-state/%{name}/installing_core_%{KVERREL}%{?-v:+%{-v*}}\
/bin/kernel-install add %{KVERREL}%{?-v:+%{-v*}} /lib/modules/%{KVERREL}%{?-v:+%{-v*}}/vmlinuz%{?-u:-%{-u*}.efi} || exit $?\
if [[ ! -e "/boot/symvers-%{KVERREL}%{?-v:+%{-v*}}.%compext" ]]; then\
    cp "/lib/modules/%{KVERREL}%{?-v:+%{-v*}}/symvers.%compext" "/boot/symvers-%{KVERREL}%{?-v:+%{-v*}}.%compext"\
    if command -v restorecon &>/dev/null; then\
        restorecon "/boot/symvers-%{KVERREL}%{?-v:+%{-v*}}.%compext"\
    fi\
fi\
%{nil}

#
# This macro defines a %%post script for a kernel package and its devel package.
#	%%kernel_variant_post [-v <subpackage>] [-r <replace>]
# More text can follow to go at the end of this variant's %%post.
#
%define kernel_variant_post(v:r:) \
%{expand:%%kernel_devel_post %{?-v*}}\
%{expand:%%kernel_modules_post %{?-v*}}\
%{expand:%%kernel_modules_core_post %{?-v*}}\
%{expand:%%kernel_modules_extra_post %{?-v*}}\
%{expand:%%kernel_modules_internal_post %{?-v*}}\
%if 0%{!?fedora:1}\
%{expand:%%kernel_modules_partner_post %{?-v*}}\
%endif\
%{expand:%%kernel_variant_posttrans %{?-v*:-v %{-v*}}}\
%{expand:%%post %{?-v*:%{-v*}-}core}\
%{-r:\
if [ `uname -i` == "x86_64" -o `uname -i` == "i386" ] &&\
   [ -f /etc/sysconfig/kernel ]; then\
  /bin/sed -r -i -e 's/^DEFAULTKERNEL=%{-r*}$/DEFAULTKERNEL=kernel%{?-v:-%{-v*}}/' /etc/sysconfig/kernel || exit $?\
fi}\
mkdir -p %{_localstatedir}/lib/rpm-state/%{name}\
touch %{_localstatedir}/lib/rpm-state/%{name}/installing_core_%{KVERREL}%{?-v:+%{-v*}}\
%{nil}

#
# This macro defines a %%preun script for a kernel package.
#	%%kernel_variant_preun [-v <subpackage>] -u [uki-suffix]
#
%define kernel_variant_preun(v:u:) \
%{expand:%%preun %{?-v:%{-v*}-}%{!?-u*:core}%{?-u*:uki-%{-u*}}}\
/bin/kernel-install remove %{KVERREL}%{?-v:+%{-v*}} || exit $?\
%if !%{with_automotive}\
if [ -x %{_sbindir}/weak-modules ]\
then\
    %{_sbindir}/weak-modules --remove-kernel %{KVERREL}%{?-v:+%{-v*}} || exit $?\
fi\
%endif\
%{nil}

%if %{with_up_base} && %{with_efiuki}
%kernel_variant_posttrans -u virt
%kernel_variant_preun -u virt
%endif

%if %{with_up_base}
%kernel_variant_preun
%kernel_variant_post
%endif

%if %{with_zfcpdump}
%kernel_variant_preun -v zfcpdump
%kernel_variant_post -v zfcpdump
%endif

%if %{with_up} && %{with_debug} && %{with_efiuki}
%kernel_variant_posttrans -v debug -u virt
%kernel_variant_preun -v debug -u virt
%endif

%if %{with_up} && %{with_debug}
%kernel_variant_preun -v debug
%kernel_variant_post -v debug
%endif

%if %{with_arm64_16k_base}
%kernel_variant_preun -v 16k
%kernel_variant_post -v 16k
%endif

%if %{with_debug} && %{with_arm64_16k}
%kernel_variant_preun -v 16k-debug
%kernel_variant_post -v 16k-debug
%endif

%if %{with_arm64_16k} && %{with_debug} && %{with_efiuki}
%kernel_variant_posttrans -v 16k-debug -u virt
%kernel_variant_preun -v 16k-debug -u virt
%endif

%if %{with_arm64_16k_base} && %{with_efiuki}
%kernel_variant_posttrans -v 16k -u virt
%kernel_variant_preun -v 16k -u virt
%endif

%if %{with_arm64_64k_base}
%kernel_variant_preun -v 64k
%kernel_variant_post -v 64k
%endif

%if %{with_debug} && %{with_arm64_64k}
%kernel_variant_preun -v 64k-debug
%kernel_variant_post -v 64k-debug
%endif

%if %{with_arm64_64k} && %{with_debug} && %{with_efiuki}
%kernel_variant_posttrans -v 64k-debug -u virt
%kernel_variant_preun -v 64k-debug -u virt
%endif

%if %{with_arm64_64k_base} && %{with_efiuki}
%kernel_variant_posttrans -v 64k -u virt
%kernel_variant_preun -v 64k -u virt
%endif

%if %{with_realtime_base}
%kernel_variant_preun -v rt
%kernel_variant_post -v rt -r kernel
%endif

%if %{with_automotive_base}
%kernel_variant_preun -v automotive
%kernel_variant_post -v automotive -r kernel
%endif

%if %{with_realtime} && %{with_debug}
%kernel_variant_preun -v rt-debug
%kernel_variant_post -v rt-debug
%endif

%if %{with_realtime_arm64_64k_base}
%kernel_variant_preun -v rt-64k
%kernel_variant_post -v rt-64k
%kernel_kvm_post rt-64k
%endif

%if %{with_debug} && %{with_realtime_arm64_64k}
%kernel_variant_preun -v rt-64k-debug
%kernel_variant_post -v rt-64k-debug
%kernel_kvm_post rt-64k-debug
%endif

%if %{with_automotive} && %{with_debug}
%kernel_variant_preun -v automotive-debug
%kernel_variant_post -v automotive-debug
%endif

###
### file lists
###

%if %{with_headers}
%files headers
/usr/include/*
%exclude %{_includedir}/cpufreq.h
%exclude %{_includedir}/ynl
%endif

%if %{with_cross_headers}
%files cross-headers
/usr/*-linux-gnu/include/*
%endif

%if %{with_kernel_abi_stablelists}
%files -n %{package_name}-abi-stablelists
/lib/modules/kabi-*
%endif

%if %{with_kabidw_base}
%ifarch x86_64 s390x ppc64 ppc64le aarch64 riscv64
%files kernel-kabidw-base-internal
%defattr(-,root,root)
/kabidw-base/%{_target_cpu}/*
%endif
%endif

# only some architecture builds need kernel-doc
%if %{with_doc}
%files doc
%defattr(-,root,root)
%{_datadir}/doc/kernel-doc-%{specversion}-%{pkgrelease}/Documentation/*
%dir %{_datadir}/doc/kernel-doc-%{specversion}-%{pkgrelease}/Documentation
%dir %{_datadir}/doc/kernel-doc-%{specversion}-%{pkgrelease}
%{_datadir}/doc/kernel-doc-%{specversion}-%{pkgrelease}/kernel.changelog.xz
%endif

%if %{with_perf}
%files -n perf
%{_bindir}/perf
%{_libdir}/libperf-jvmti.so
%dir %{_libexecdir}/perf-core
%{_libexecdir}/perf-core/*
%{_mandir}/man[1-8]/perf*
%{_sysconfdir}/bash_completion.d/perf
%doc linux-%{KVERREL}/tools/perf/Documentation/examples.txt
%{_docdir}/perf-tip/tips.txt
%{_includedir}/perf/perf_dlfilter.h

%files -n python3-perf
%{python3_sitearch}/*

%if %{with_debuginfo}
%files -f perf-debuginfo.list -n perf-debuginfo

%files -f python3-perf-debuginfo.list -n python3-perf-debuginfo
%endif
# with_perf
%endif

%if %{with_libperf}
%files -n libperf
%{_libdir}/libperf.so.0
%{_libdir}/libperf.so.0.0.1

%files -n libperf-devel
%{_libdir}/libperf.so
%{_libdir}/pkgconfig/libperf.pc
%{_includedir}/internal/*.h
%{_includedir}/perf/bpf_perf.h
%{_includedir}/perf/core.h
%{_includedir}/perf/cpumap.h
%{_includedir}/perf/event.h
%{_includedir}/perf/evlist.h
%{_includedir}/perf/evsel.h
%{_includedir}/perf/mmap.h
%{_includedir}/perf/threadmap.h
%{_mandir}/man3/libperf.3.gz
%{_mandir}/man7/libperf-counting.7.gz
%{_mandir}/man7/libperf-sampling.7.gz
%{_docdir}/libperf/examples/sampling.c
%{_docdir}/libperf/examples/counting.c
%{_docdir}/libperf/html/libperf.html
%{_docdir}/libperf/html/libperf-counting.html
%{_docdir}/libperf/html/libperf-sampling.html

%if %{with_debuginfo}
%files -f libperf-debuginfo.list -n libperf-debuginfo
%endif

# with_libperf
%endif


%if %{with_tools}
%ifnarch %{cpupowerarchs}
%files -n %{package_name}-tools
%else
%files -n %{package_name}-tools -f cpupower.lang
%{_bindir}/cpupower
%{_datadir}/bash-completion/completions/cpupower
%ifarch x86_64
%{_bindir}/centrino-decode
%{_bindir}/powernow-k8-decode
%endif
%{_mandir}/man[1-8]/cpupower*
%ifarch x86_64
%{_bindir}/x86_energy_perf_policy
%{_mandir}/man8/x86_energy_perf_policy*
%{_bindir}/turbostat
%{_mandir}/man8/turbostat*
%{_bindir}/intel-speed-select
%{_sbindir}/intel_sdsi
%endif
# cpupowerarchs
%endif
%{_bindir}/tmon
%{_bindir}/bootconfig
%{_bindir}/iio_event_monitor
%{_bindir}/iio_generic_buffer
%{_bindir}/lsiio
%{_bindir}/lsgpio
%{_bindir}/gpio-hammer
%{_bindir}/gpio-event-mon
%{_bindir}/gpio-watch
%{_mandir}/man1/kvm_stat*
%{_bindir}/kvm_stat
%{_unitdir}/kvm_stat.service
%config(noreplace) %{_sysconfdir}/logrotate.d/kvm_stat
%{_bindir}/page_owner_sort
%{_bindir}/slabinfo
%if %{with_ynl}
%{_bindir}/ynl*
%{_docdir}/ynl
%{_datadir}/ynl
%{python3_sitelib}/pyynl*
%endif

%if %{with_debuginfo}
%files -f %{package_name}-tools-debuginfo.list -n %{package_name}-tools-debuginfo
%endif

%files -n %{package_name}-tools-libs
%ifarch %{cpupowerarchs}
%{_libdir}/libcpupower.so.1
%{_libdir}/libcpupower.so.1.0.1
%endif

%files -n %{package_name}-tools-libs-devel
%ifarch %{cpupowerarchs}
%{_libdir}/libcpupower.so
%{_includedir}/cpufreq.h
%{_includedir}/cpuidle.h
%{_includedir}/powercap.h
%endif
%if %{with_ynl}
%{_libdir}/libynl*
%{_includedir}/ynl
%endif

%files -n rtla
%{_bindir}/rtla
%{_bindir}/hwnoise
%{_bindir}/osnoise
%{_bindir}/timerlat
%{_mandir}/man1/rtla-hwnoise.1.gz
%{_mandir}/man1/rtla-osnoise-hist.1.gz
%{_mandir}/man1/rtla-osnoise-top.1.gz
%{_mandir}/man1/rtla-osnoise.1.gz
%{_mandir}/man1/rtla-timerlat-hist.1.gz
%{_mandir}/man1/rtla-timerlat-top.1.gz
%{_mandir}/man1/rtla-timerlat.1.gz
%{_mandir}/man1/rtla.1.gz

%files -n rv
%{_bindir}/rv
%{_mandir}/man1/rv-list.1.gz
%{_mandir}/man1/rv-mon-wip.1.gz
%{_mandir}/man1/rv-mon-wwnr.1.gz
%{_mandir}/man1/rv-mon.1.gz
%{_mandir}/man1/rv-mon-sched.1.gz
%{_mandir}/man1/rv.1.gz

# with_tools
%endif

%if %{with_selftests}
%files selftests-internal
%{_libexecdir}/ksamples
%{_libexecdir}/kselftests
%endif

# empty meta-package
%if %{with_up_base}
%ifnarch %nobuildarches noarch
%files
%endif
%endif

# This is %%{image_install_path} on an arch where that includes ELF files,
# or empty otherwise.
%define elf_image_install_path %{?kernel_image_elf:%{image_install_path}}

#
# This macro defines the %%files sections for a kernel package
# and its devel and debuginfo packages.
#	%%kernel_variant_files [-k vmlinux] <use_vdso> <condition> <subpackage>
#
%define kernel_variant_files(k:) \
%if %{2}\
%{expand:%%files %{?1:-f kernel-%{?3:%{3}-}ldsoconf.list} %{?3:%{3}-}core}\
%{!?_licensedir:%global license %%doc}\
%%license linux-%{KVERREL}/COPYING-%{version}-%{release}\
/lib/modules/%{KVERREL}%{?3:+%{3}}/%{?-k:%{-k*}}%{!?-k:vmlinuz}\
%ghost /%{image_install_path}/%{?-k:%{-k*}}%{!?-k:vmlinuz}-%{KVERREL}%{?3:+%{3}}\
/lib/modules/%{KVERREL}%{?3:+%{3}}/.vmlinuz.hmac \
%ghost /%{image_install_path}/.vmlinuz-%{KVERREL}%{?3:+%{3}}.hmac \
%ifarch aarch64 riscv64\
/lib/modules/%{KVERREL}%{?3:+%{3}}/dtb \
%ghost /%{image_install_path}/dtb-%{KVERREL}%{?3:+%{3}} \
%endif\
/lib/modules/%{KVERREL}%{?3:+%{3}}/System.map\
%ghost /boot/System.map-%{KVERREL}%{?3:+%{3}}\
%dir /lib/modules\
%dir /lib/modules/%{KVERREL}%{?3:+%{3}}\
/lib/modules/%{KVERREL}%{?3:+%{3}}/symvers.%compext\
/lib/modules/%{KVERREL}%{?3:+%{3}}/config\
/lib/modules/%{KVERREL}%{?3:+%{3}}/modules.builtin*\
%ghost %attr(0644, root, root) /boot/symvers-%{KVERREL}%{?3:+%{3}}.%compext\
%ghost %attr(0600, root, root) /boot/initramfs-%{KVERREL}%{?3:+%{3}}.img\
%ghost %attr(0644, root, root) /boot/config-%{KVERREL}%{?3:+%{3}}\
%{expand:%%files -f kernel-%{?3:%{3}-}modules-core.list %{?3:%{3}-}modules-core}\
%dir /lib/modules\
%dir /lib/modules/%{KVERREL}%{?3:+%{3}}\
%dir /lib/modules/%{KVERREL}%{?3:+%{3}}/kernel\
/lib/modules/%{KVERREL}%{?3:+%{3}}/build\
/lib/modules/%{KVERREL}%{?3:+%{3}}/source\
/lib/modules/%{KVERREL}%{?3:+%{3}}/updates\
/lib/modules/%{KVERREL}%{?3:+%{3}}/weak-updates\
/lib/modules/%{KVERREL}%{?3:+%{3}}/systemtap\
%{_datadir}/doc/kernel-keys/%{KVERREL}%{?3:+%{3}}\
%if %{1}\
/lib/modules/%{KVERREL}%{?3:+%{3}}/vdso\
%endif\
/lib/modules/%{KVERREL}%{?3:+%{3}}/modules.block\
/lib/modules/%{KVERREL}%{?3:+%{3}}/modules.drm\
/lib/modules/%{KVERREL}%{?3:+%{3}}/modules.modesetting\
/lib/modules/%{KVERREL}%{?3:+%{3}}/modules.networking\
/lib/modules/%{KVERREL}%{?3:+%{3}}/modules.order\
%ghost %attr(0644, root, root) /lib/modules/%{KVERREL}%{?3:+%{3}}/modules.alias\
%ghost %attr(0644, root, root) /lib/modules/%{KVERREL}%{?3:+%{3}}/modules.alias.bin\
%ghost %attr(0644, root, root) /lib/modules/%{KVERREL}%{?3:+%{3}}/modules.builtin.alias.bin\
%ghost %attr(0644, root, root) /lib/modules/%{KVERREL}%{?3:+%{3}}/modules.builtin.bin\
%ghost %attr(0644, root, root) /lib/modules/%{KVERREL}%{?3:+%{3}}/modules.dep\
%ghost %attr(0644, root, root) /lib/modules/%{KVERREL}%{?3:+%{3}}/modules.dep.bin\
%ghost %attr(0644, root, root) /lib/modules/%{KVERREL}%{?3:+%{3}}/modules.devname\
%ghost %attr(0644, root, root) /lib/modules/%{KVERREL}%{?3:+%{3}}/modules.softdep\
%ghost %attr(0644, root, root) /lib/modules/%{KVERREL}%{?3:+%{3}}/modules.symbols\
%ghost %attr(0644, root, root) /lib/modules/%{KVERREL}%{?3:+%{3}}/modules.symbols.bin\
%ghost %attr(0644, root, root) /lib/modules/%{KVERREL}%{?3:+%{3}}/modules.weakdep\
%{expand:%%files -f kernel-%{?3:%{3}-}modules.list %{?3:%{3}-}modules}\
%{expand:%%files %{?3:%{3}-}devel}\
%defverify(not mtime)\
/usr/src/kernels/%{KVERREL}%{?3:+%{3}}\
%{expand:%%files %{?3:%{3}-}devel-matched}\
%{expand:%%files -f kernel-%{?3:%{3}-}modules-extra.list %{?3:%{3}-}modules-extra}\
%{expand:%%files -f kernel-%{?3:%{3}-}modules-internal.list %{?3:%{3}-}modules-internal}\
%if 0%{!?fedora:1}\
%{expand:%%files -f kernel-%{?3:%{3}-}modules-partner.list %{?3:%{3}-}modules-partner}\
%endif\
%if %{with_debuginfo}\
%ifnarch noarch\
%{expand:%%files -f debuginfo%{?3}.list %{?3:%{3}-}debuginfo}\
%endif\
%endif\
%if %{with_efiuki} && "%{3}" != "rt" && "%{3}" != "rt-debug" && "%{3}" != "rt-64k" && "%{3}" != "rt-64k-debug"\
%{expand:%%files %{?3:%{3}-}uki-virt}\
%dir /lib/modules\
%dir /lib/modules/%{KVERREL}%{?3:+%{3}}\
/lib/modules/%{KVERREL}%{?3:+%{3}}/System.map\
/lib/modules/%{KVERREL}%{?3:+%{3}}/symvers.%compext\
/lib/modules/%{KVERREL}%{?3:+%{3}}/config\
/lib/modules/%{KVERREL}%{?3:+%{3}}/modules.builtin*\
%attr(0644, root, root) /lib/modules/%{KVERREL}%{?3:+%{3}}/%{?-k:%{-k*}}%{!?-k:vmlinuz}-virt.efi\
%attr(0644, root, root) /lib/modules/%{KVERREL}%{?3:+%{3}}/.%{?-k:%{-k*}}%{!?-k:vmlinuz}-virt.efi.hmac\
%ghost /%{image_install_path}/efi/EFI/Linux/%{?-k:%{-k*}}%{!?-k:*}-%{KVERREL}%{?3:+%{3}}.efi\
%{expand:%%files %{?3:%{3}-}uki-virt-addons}\
%dir /lib/modules/%{KVERREL}%{?3:+%{3}}/%{?-k:%{-k*}}%{!?-k:vmlinuz}-virt.efi.extra.d/ \
/lib/modules/%{KVERREL}%{?3:+%{3}}/%{?-k:%{-k*}}%{!?-k:vmlinuz}-virt.efi.extra.d/*.addon.efi\
%endif\
%if %{?3:1} %{!?3:0}\
%{expand:%%files %{3}}\
%endif\
%if %{with_gcov}\
%ifnarch %nobuildarches noarch\
%{expand:%%files -f kernel-%{?3:%{3}-}gcov.list %{?3:%{3}-}gcov}\
%endif\
%endif\
%endif\
%{nil}

%kernel_variant_files %{_use_vdso} %{with_up_base}
%if %{with_up}
%kernel_variant_files %{_use_vdso} %{with_debug} debug
%endif
%if %{with_arm64_16k}
%kernel_variant_files %{_use_vdso} %{with_debug} 16k-debug
%endif
%if %{with_arm64_64k}
%kernel_variant_files %{_use_vdso} %{with_debug} 64k-debug
%endif
%kernel_variant_files %{_use_vdso} %{with_realtime_base} rt
%if %{with_realtime}
%kernel_variant_files %{_use_vdso} %{with_debug} rt-debug
%endif
%kernel_variant_files %{_use_vdso} %{with_automotive_base} automotive
%if %{with_automotive}
%kernel_variant_files %{_use_vdso} %{with_debug} automotive-debug
%endif
%if %{with_debug_meta}
%files debug
%files debug-core
%files debug-devel
%files debug-devel-matched
%files debug-modules
%files debug-modules-core
%files debug-modules-extra
%if %{with_arm64_16k}
%files 16k-debug
%files 16k-debug-core
%files 16k-debug-devel
%files 16k-debug-devel-matched
%files 16k-debug-modules
%files 16k-debug-modules-extra
%endif
%if %{with_arm64_64k}
%files 64k-debug
%files 64k-debug-core
%files 64k-debug-devel
%files 64k-debug-devel-matched
%files 64k-debug-modules
%files 64k-debug-modules-extra
%endif
%endif
%kernel_variant_files %{_use_vdso} %{with_zfcpdump} zfcpdump
%kernel_variant_files %{_use_vdso} %{with_arm64_16k_base} 16k
%kernel_variant_files %{_use_vdso} %{with_arm64_64k_base} 64k
%kernel_variant_files %{_use_vdso} %{with_realtime_arm64_64k_base} rt-64k
%if %{with_realtime_arm64_64k}
%kernel_variant_files %{_use_vdso} %{with_debug} rt-64k-debug
%endif

%files modules-extra-matched

# plz don't put in a version string unless you're going to tag
# and build.
#
#
%changelog
* Sun Aug 24 2025 Neal Gompa <neal@gompa.dev> [6.15.10-402.asahi]
- DO NOT SUBMIT: usb: dwc3: Add "apple,t8103-dwc3" compatible (Janne Grunau)

* Mon Aug 18 2025 Neal Gompa <neal@gompa.dev> [6.15.10-401.asahi]
- rust: kernel: of: Fix !CONFIG_OF build (Janne Grunau)

* Sun Aug 17 2025 Neal Gompa <neal@gompa.dev> [6.15.10-400.asahi]
- redhat/configs: Disable Nova GPU driver (Neal Gompa)
- redhat: Conditionally disable libbpf_dynamic on <F41 and <EL9 (Neal Gompa)
- redhat/configs: Disable the Apple touchbar panel driver at the common level (Neal Gompa)
- redhat/configs: Disable CS42L84 at common level (Neal Gompa)
- redhat: Enable kernel-16k flavor for Fedora (Neal Gompa)
- redhat: Tweak spec to do a verbose build (Neal Gompa)
- redhat/configs: aarch64: Enable Apple Secure Enclave Processor driver (Neal Gompa)
- redhat/configs: aarch64: Enable Apple Always-On Processor support (Neal Gompa)
- redhat/configs: aarch64: Enable Mac SMC sensors driver (Neal Gompa)
- redhat/configs: aarch64: Enable DMA SIO and DCP Audio drivers (Neal Gompa)
- redhat/fedora_files/def_variants.yaml.fedora: Add apple and asahi drm drivers (Neal Gompa)
- redhat/configs: aarch64: Enable Apple Image Signal Processor driver (Neal Gompa)
- redhat/configs: aarch64: Enable Apple touchbar display drivers (Neal Gompa)
- redhat/configs: aarch64: Change CONFIG_APPLE_MAILBOX to =y (Neal Gompa)
- redhat/configs: aarch64: Change CONFIG_APPLE_RTKIT from =m to =y (Eric Curtin)
- redhat/configs: aarch64: Enable Asahi DRM driver (Neal Gompa)
- redhat: Enable kernel-headers build (Neal Gompa)
- redhat/configs: aarch64: Enable ARM64_MEMORY_MODEL_CONTROL (Neal Gompa)
- redhat/configs: s390x: Drop CONFIG_BACKLIGHT_CLASS_DEVICE=m for Fedora (Neal Gompa)
- redhat/configs: aarch64: asahi: Turn on downstream Apple Silicon configs (Neal Gompa)
- rust: iio: common: aop: Add TODO fn/struct docs (Janne Grunau)
- soc: apple: Add SEP driver. (Sasha Finkelstein)
- rust: soc: apple: Add Apple mailbox abstractions (Sasha Finkelstein)
- iio: common: Add AOP sensor drivers (Sasha Finkelstein)
- ASoC: apple: aop: Add module parameter to check mics without beamforming (Janne Grunau)
- ASoC: apple: Add aop_audio driver (Sasha Finkelstein)
- soc: apple: Add support for the AOP co-processor (Sasha Finkelstein)
- rust: alloc: kvec: WIP(?): Add swap_remove() for AOP series (Sasha Finkelstein)
- rust: device: WIP(?): Add get_drvdata for AOP series (Sasha Finkelstein)
- rust: bindings: WIP(?): Add IIO bits for AOP series (Sasha Finkelstein)
- rust: bindings: WIP(?): Add sound bits for AOP series (Sasha Finkelstein)
- rust: soc: apple: rtkit: Add apple_rtkit_has_endpoint (Sasha Finkelstein)
- rust: bindgen: Make snd_dec_flac opaque (Janne Grunau)
- rust: device: HACK? make parent() public (Janne Grunau)
- rust: device: WIP(?): Make as_raw() public for AOP series (Sasha Finkelstein)
- rust: property: HACK? make as_raw() public (Sasha Finkelstein)
- fixup! media: apple: Add Apple ISP driver (Janne Grunau)
- media: apple: isp: Support system sleep (Eileen Yoon)
- media: apple: isp: Use a mutex instead of a spinlock for channels (Hector Martin)
- media: apple: isp: implement ENUM_FRAMEINTERVALS trivially (Hector Martin)
- media: apple: isp: Enable IMX364 sensor (Hector Martin)
- media: apple: isp: Show camera presets even for unsupported sensors (Hector Martin)
- media: apple: isp: Parse firmware version from device tree (Janne Grunau)
- media: apple: isp: Use a more user-friendly device name (Hector Martin)
- media: apple: isp: Option to use CMD_STOP (ifdeffed out) (Asahi Lina)
- media: apple: isp: Only reset coproc when necessary, fix minor race (Asahi Lina)
- media: apple: isp: VMap only what is necessary, remove redundant logging state bit (Asahi Lina)
- media: apple: isp: Add a missing read barrier (possibly?) (Asahi Lina)
- media: apple: isp: Clear IRQs when resetting coproc (Asahi Lina)
- media: apple: isp: Rework meta surface handling & buffer return (Asahi Lina)
- media: apple: isp: Use cached IOMMU mappings (Asahi Lina)
- media: apple: isp: Zero out pages allocated to ISP (Asahi Lina)
- media: apple: isp: Make sub-pmdomain handling explicit (Asahi Lina)
- media: apple: isp: Minor changes to cam flow (Asahi Lina)
- media: apple: isp: Add flicker_sensor_set cmd (Asahi Lina)
- media: apple: isp: t8112 fixes... (Asahi Lina)
- media: apple: isp: Limit maximal number of buffers (Janne Grunau)
- media: apple: isp: t8112 HW config (Janne Grunau)
- media: apple: isp: Use a second region for MBOX_IRQ_{DOORBELL,ACK} (Janne Grunau)
- media: apple: isp: Make channel sends not interruptible (Asahi Lina)
- media: apple: isp: Maybe fix some DMA ordering issues (Asahi Lina)
- media: apple: isp: Add STOP and POWER_DOWN commands (Asahi Lina)
- media: apple: isp: Implement posted commands (Asahi Lina)
- media: apple: isp: Propagate EINTR from firmware loads (Asahi Lina)
- media: apple: isp: Remove ioread/iowrite and stop doing raw address translation (Asahi Lina)
- media: apple: isp: Switch to threaded IRQs (Asahi Lina)
- media: apple: isp: Always enable singleplane API, make multiple a module param (Asahi Lina)
- media: apple: isp: Working t602x and multiple formats and more fixes (Asahi Lina)
- media: apple: isp: t602x hw config (Asahi Lina)
- media: apple: isp: Support >32bit VAs for t602x (Asahi Lina)
- media: apple: isp: fix copyright (Eileen Yoon)
- media: apple: isp: alloc static surfaces only once (Eileen Yoon)
- media: apple: isp: misc isp-fw.c improvements (Eileen Yoon)
- media: apple: isp: rm old isp_resv struct (Eileen Yoon)
- media: apple: isp: rm unused bootargs members (Eileen Yoon)
- media: apple: isp: s/asc/coproc/ (Eileen Yoon)
- media: apple: isp: wmb() before GPIO write (Eileen Yoon)
- media: apple: isp: Don't use define for bootargs size (Eileen Yoon)
- media: apple: isp: Better document info struct fields (Eileen Yoon)
- media: apple: isp: Set platform_id in bootargs (Eileen Yoon)
- media: apple: WIP: t6000 hax (Hector Martin)
- media: apple: isp: Do not defer on failure to initialize DART (Hector Martin)
- media: apple: isp: Drop the DART mirroring stuff (Hector Martin)
- media: apple: isp: Split gpio/mbox MMIO range (Eileen Yoon)
- media: apple: isp: Enable t6000 (Hector Martin)
- media: apple: isp: Fixup shared region arg (Hector Martin)
- media: apple: isp: Use preallocated heap (Hector Martin)
- media: apple: isp: IMX558 initial support (Eileen Yoon)
- media: apple: Add Apple ISP driver (Eileen Yoon)
- arm64: cpufeature: Unify SCOPE_LOCAL_CPU early & late behavior (Asahi Lina)
- KVM: arm64: Expose TSO capability to guests and context switch (Asahi Lina)
- arm64: Implement Apple IMPDEF TSO memory model control (Hector Martin)
- arm64: Introduce scaffolding to add ACTLR_EL1 to thread state (Hector Martin)
- arm64: Implement PR_{GET,SET}_MEM_MODEL for always-TSO CPUs (Hector Martin)
- prctl: Introduce PR_{SET,GET}_MEM_MODEL (Hector Martin)
- drm/asahi: Hook up crashdump to devcoredump (Asahi Lina)
- rust: devcoredump: Add devcoredump abstraction (Asahi Lina)
- rust: uapi: Add ELF headers (Asahi Lina)
- drm/asahi: gpu: Hook up crashdump generation (Asahi Lina)
- drm/asahi: mmu: Wire up kernel AS dumper (Asahi Lina)
- drm/asahi: crashdump: Add crash dumper module (Asahi Lina)
- drm/asahi: pgtable: Add helpers for decoding PTE perms (Asahi Lina)
- drm/asahi: pgtable: Add dumper (Asahi Lina)
- drm/asahi: Implement ASAHI_BIND_SINGLE_PAGE (mmu/pgtbl) (Asahi Lina)
- drm/asahi: RiiR page tables (Asahi Lina)
- rust: page: Add physical address conversion functions (Asahi Lina)
- rust: addr: Add a module to declare core address types (Asahi Lina)
- rust: page: Make with_page_mapped() and with_pointer_into_page() public (Asahi Lina)
- samples: rust: Fix for Owned page (Janne Grunau)
- rust: page: Convert to Ownable (Asahi Lina)
- drm/asahi: Adapt to v6.15 + v6.16-rc1 rust / driver-core(rust) (Janne Grunau)
- drm/asahi: port to new UAPI (Janne Grunau)
- drm/asahi: Implement ASAHI_BIND_SINGLE_PAGE (uapi) (Asahi Lina)
- drm/asahi: mmu: Add some barriers (Asahi Lina)
- drm/asahi: debug: Add PgTable debug category (Asahi Lina)
- drm/asahi: mmu: UAT change for rust page table rewrite (Asahi Lina)
- drm/asahi: mmu: Change step_remap() to new api (Asahi Lina)
- drm/asahi: mmu: Fix deadlock on remap ops (Asahi Lina)
- drm/asahi: workqueue: Defer freeing the last completed work item (Asahi Lina)
- drm/asahi: mmu: Fix 2x step_remap case (Asahi Lina)
- drm/asahi: file: Reject gem_bind past the end of the object (Asahi Lina)
- drm/asahi: mmu: Change step_remap() to new api (Asahi Lina)
- drm/asahi: Add the USER_TIMESTAMPS feature (Asahi Lina)
- drm/asahi: Set a bit for internal non-render barriers on G14X (Asahi Lina)
- drm/asahi: file: Add user_timestamp_frequency_hz to params (Asahi Lina)
- drm/asahi: queue/render,compute: Plumb through timestamps extension (Asahi Lina)
- drm/asahi: fw, queue: Plumb through UserTimestamps -> TimestampPointers (Asahi Lina)
- drm/asahi: queue: Plumb through objects XArray and add timestamp getter (Asahi Lina)
- drm/asahi: fw, queue: Add UserTimestamp object to job structs (Asahi Lina)
- drm/asahi: file: Implement ASAHI_GEM_BIND_OBJECT (Asahi Lina)
- drm/asahi: gpu: Implement mapping timestamp buffers (Asahi Lina)
- drm/asahi: workqueue: Restrict command objects to only job commands (Asahi Lina)
- drm/asahi: Document timestamp ops better, refactor fields (Asahi Lina)
- drm/asahi: gpu: Add a max object count garbage limit (Asahi Lina)
- drm/asahi: alloc: Be more verbose about failures (Asahi Lina)
- drm/asahi: gpu: Collect garbage for private/gpuro together (Asahi Lina)
- drm/asahi: gpu: Force Box move with manual Box<T>::into_inner() (Janne Grunau)
- drm/asahi: Implement ASAHI_GET_TIME (Asahi Lina)
- drm/asahi: Implement missing ASAHI_BIND_OP_UNBIND (Asahi Lina)
- drm/asahi: Align kernel range to buffer::PAGE_SIZE (Asahi Lina)
- drm/asahi: HACK: Disable compute preemption for now (Asahi Lina)
- drm/asahi: Add robust_isolation kernel parameter (Asahi Lina)
- drm/asahi: Clean up jobs in a workqueue (Asahi Lina)
- drm/asahi: workqueue: Fix "Cannot submit, but queue is empty?" bug (Asahi Lina)
- drm/asahi: event: Initialize stamps to different values (Asahi Lina)
- drm/asahi: Handle channel errors (Asahi Lina)
- drm/asahi: gpu: Show unknown field in timeouts (Asahi Lina)
- drm/asahi: Fix event tracking when JobSubmission is dropped (Asahi Lina)
- drm/asahi: Fix u32 mult overflow on large tilebufs/TPCs (Asahi Lina)
- drm/asahi: Signal soft fault support to userspace (Asahi Lina)
- drm/asahi: file: Update to newer VM_BIND API (Asahi Lina)
- drm/asahi: queue: Split into Queue and QueueInner (Asahi Lina)
- drm/asahi: Implement GEM objects sharing a single DMA resv (Asahi Lina)
- drm/asahi: mmu: Fix lockdep issues with GpuVm (Asahi Lina)
- drm/asahi: Convert more ranges to Range<> (Asahi Lina)
- drm/asahi: Move the unknown dummy page to the top of the address space (Asahi Lina)
- drm/asahi: mmu: Convert to using Range (Asahi Lina)
- drm/asahi: util: Add RangeExt helpers for Range<T> (Asahi Lina)
- drm/asahi: Refactor address types (Asahi Lina)
- drm/asahi: Convert to GPUVM and implement more VM_BIND ops (Asahi Lina)
- drm/asahi: Don't lock up when unmapping PTEs fails (Asahi Lina)
- drm/asahi: alloc: Do not allocate memory to free memory (Asahi Lina)
- drm/asahi: Identify and implement helper config register (Asahi Lina)
- drm/asahi: Identify and allocate clustered layering metadata buf (Asahi Lina)
- drm/asahi: Add verbose UAPI error reporting (Asahi Lina)
- drm/asahi: render: Identify and set Z/S strides for layered rendering (Asahi Lina)
- drm/asahi: fw,queue: Implement helper programs (Asahi Lina)
- drm/asahi: compute/render: Implement bindless samplers (Asahi Lina)
- drm/asahi: buffer,render: Identify and provide layer meta buf (Asahi Lina)
- drm/asahi: alloc: Support tagging array allocs (Asahi Lina)
- drm/asahi: Add the Asahi driver for Apple AGX GPUs (Asahi Lina)
- rust: bindings: Bind the Asahi DRM UAPI (Asahi Lina)
- rust: macros: Add versions macro (Asahi Lina)
- rust: drm/gpuvm: Add GpuVaFlags support (Asahi Lina)
- rust: drm: Add GPUVM Manager abstraction (Asahi Lina)
- drm/gpuvm: Plumb through flags into drm_gpuva_init (Asahi Lina)
- drm/gpuva: Add DRM_GPUVA_SINGLE_PAGE flag and logic (Asahi Lina)
- drm/gpuvm: Plumb through flags into drm_gpuva_op_map (Asahi Lina)
- drm/gpuvm: Add a flags argument to drm_gpuvm_sm_map[_*] (Asahi Lina)
- drm/gpuvm: Add drm_gpuvm_bo_unmap() (Asahi Lina)
- rust: drm: sched: Add GPU scheduler abstraction (Asahi Lina)
- drm/scheduler: Fix UAF in drm_sched_fence_get_timeline_name (Asahi Lina)
- rust: drm: syncobj: Add DRM Sync Object abstraction (Asahi Lina)
- rust: drm: mm: Add DRM MM Range Allocator abstraction (Asahi Lina)
- rust: scatterlist: Make SGTable::raw_iter public (Janne Grunau)
- rust: drm: gem: shmem: Implemente Send + Sync for Object<T> (Janne Grunau)
- rust: drm: gem: Remove impossible trait bound impl_as_opaque!() (Janne Grunau)
- rust: drm: gem: shmem: Switch to Opaque<drm_gem_shmem_object> (Janne Grunau)
- rust: drm: gem: Add BaseObject::prime_export() (Lyude Paul)
- rust: drm: gem: Add export() callback (Lyude Paul)
- rust: Add dma_buf stub bindings (Lyude Paul)
- rust: drm: gem: Introduce OwnedSGTable (Lyude Paul)
- rust: drm: gem: shmem: Add share_dma_resv to ObjectConfig (Asahi Lina)
- rust: drm: gem: shmem: Add DRM shmem helper abstraction (Asahi Lina)
- rust: drm: gem: Add OpaqueObject (Lyude Paul)
- rust: gem: Introduce BaseDriverObject::Args (Lyude Paul)
- drm/gem/shmem: Extract drm_gem_shmem_release() from drm_gem_shmem_free() (Lyude Paul)
- drm/gem/shmem: Extract drm_gem_shmem_init() from drm_gem_shmem_create() (Lyude Paul)
- rust: drm: gem: Add raw_dma_resv() function (Lyude Paul)
- rust: drm: file: Add as_raw() (Janne Grunau)
- samples: rust: add sample code for scatterlist bindings (Abdiel Janulgue)
- rust: add initial scatterlist bindings (Abdiel Janulgue)
- rust: drm: gem: Support driver-private GEM object types (Lyude Paul)
- rust: drm: gem: Drop Object::SIZE (Lyude Paul)
- rust: drm: gem: Add DriverFile type alias (Lyude Paul)
- rust: drm: gem: Simplify use of generics (Lyude Paul)
- HACK: rust: drm: Support unsafe Device::new() without data (Janne Grunau)
- rust: drm: Move FEATURES back to drivers (Janne Grunau)
- rust: drm: driver: Add feature flags used by asahi (Janne Grunau)
- rust: helpers: Add bindings/wrappers for dma_resv_lock (Asahi Lina)
- drm/shmem-helper: Add lockdep asserts to vmap/vunmap (Asahi Lina)
- rust: dma_fence: Add DMA Fence abstraction (Asahi Lina)
- drm/sched: Avoid memory leaks with cancel_job() callback (Philipp Stanner)
- rust: drm: Drop the use of Opaque for ioctl arguments (Beata Michalska)
- drm: Add UAPI for the Asahi driver (Alyssa Rosenzweig)
- drm: apple: Support sync objects (Janne Grunau)
- fixup! gpu: drm: apple: Add DCP audio driver (Janne Grunau)
- drm: dcp: Adjust .mode_valid signature (Janne Grunau)
- drm: apple: Use piodma default iommu domain (Janne Grunau)
- fixup! drm/apple: Get rid of the piodma dummy driver (Janne Grunau)
- fixup! WIP: drm/apple: Add DCP display driver (Janne Grunau)
- drm/apple: fix audioless build (Alyssa Rosenzweig)
- drm: apple: dptx: Issue HPD event early on gpio/type-c disconnect (Janne Grunau)
- drm: apple: dptx: Configure number of lanes for dptx-phy (Janne Grunau)
- drm: apple: HDMI: Check HPD state before enabling the IRQ (Janne Grunau)
- drm: apple: dptx: Rework/document get_max_lane_count() (Janne Grunau)
- drm: apple: iomfb: Adapt `IOMFB_METHOD` for gcc 15 (Janne Grunau)
- drm: apple: audio: Rework audio service handling (Janne Grunau)
- drm: apple: afk: Allow replies after service 'teardown' (Janne Grunau)
- drm: apple: dptx: Tidy up lane count handling (Janne Grunau)
- drm: apple: dptx: Silence DPTX_APCALL_{GET,SET}_DOWN_SPREAD (Janne Grunau)
- drm: apple: Handle dcps with "phys" property as dcpext (Janne Grunau)
- drm: apple: Support up to 3 DCP instances. (Janne Grunau)
- drm: apple: Revert "Use delayed work for debounced oob HPD" (Janne Grunau)
- drm: apple: Use delayed work for debounced oob HPD (Janne Grunau)
- drm: apple: iomfb: Clear non-visible planes (Janne Grunau)
- drm: apple: Use dest rct in offscreen test (Janne Grunau)
- drm: apple: refactor apple_plane_atomic_check (Janne Grunau)
- drm: apple: make plane zpos immutable (James Calligeros)
- drm: apple: warn about broken sw cursor fallback (James Calligeros)
- drm: apple: use correct min/max plane scaling factors (James Calligeros)
- drm: apple: add support for overlay planes (James Calligeros)
- drm: apple: reject plane commit if it will crash DCP (James Calligeros)
- drm: apple: constrain swaps to maximum blendable surfaces (James Calligeros)
- drm: apple: respect drm_plane_state zpos (James Calligeros)
- drm: apple: Add .get_scanout_buffer for drm_panic support (Janne Grunau)
- drm: apple: Add CRTC CRC support (Janne Grunau)
- drm: apple: audio: Implement runtime PM support (Janne Grunau)
- drm: apple: Enable EDID support by default (Janne Grunau)
- ALSA: Introduce 'snd_interval_rate_bits' (Martin Povišer)
- drm: apple: iomfb: Provide the EDID as connector property (Janne Grunau)
- drm: apple: Add dcpav-service-ep (Janne Grunau)
- drm: apple: afk: Optionally match against EPICName (Janne Grunau)
- Revert "drm: apple: HACK: Do not delete piodma platform device" (Janne Grunau)
- drm: apple: iomfb: Align buffer size on unmap/free as well (Janne Grunau)
- drm/apple: Fix missing mode init (feel free to squash) (Asahi Lina)
- drm: apple: dptxport: get_max_lane_count: Retrieve lane count from phy (Janne Grunau)
- drm: apple: dptx: Fix get_drive_settings retcode (Janne Grunau)
- drm: apple: Add oob hotplug event (Sven Peter)
- drm/apple: audio: Fix hotplug notifications (Asahi Lina)
- drm/apple: audio: Defer DMA channel acquisition to device open (Asahi Lina)
- drm/apple: audio: Create a device link to the DMA device (Asahi Lina)
- drm/apple: Explicitly stop AFK endpoints on shutdown (Asahi Lina)
- drm: apple: Override drm_vblank's page flip event handling [HACK] (Janne Grunau)
- drm: apple: disable HDMI audio by default (Janne Grunau)
- drm: apple: av: Warn only once about failed calls (Janne Grunau)
- drm: apple: Reduce log spam about busy command channel (Janne Grunau)
- drm: apple: Fix broken MemDescRelay::release_descriptor callback number (Janne Grunau)
- drm: apple: Switch back to drm_atomic_helper_commit_tail_rpm() (Janne Grunau)
- drm: apple: backlight: release lock in error path (Caspar Schutijser)
- drm/apple: fix double words in comments (Jonathan Gray)
- drm: apple: audio: Avoid probe errors (Janne Grunau)
- drm: apple: audio: Make the DP/HDMI audio driver a full driver (Janne Grunau)
- drm: apple: audio: move the audio driver into the DCP module (Janne Grunau)
- drm: apple: av: Use a workqueue (Janne Grunau)
- drm: apple: audio: init AV endpoint later (Janne Grunau)
- drm: apple: dptx: Remove DPTX disconnect/connect on init (Janne Grunau)
- gpu: drm: apple: Add DCP audio driver (Martin Povišer)
- drm: apple: av: Do not open AV service from afk receive handler (Janne Grunau)
- drm: apple: av: Support macOS 12.3 and 13.5 firmware APIs (Janne Grunau)
- gpu: drm: apple: Set up client of AV endpoint (Martin Povišer)
- gpu: drm: apple: Expose injecting of EPIC calls via debugfs (Martin Povišer)
- drm: apple: iomfb: export property dicts in connector debugfs (Janne Grunau)
- drm: apple: Add Kconfig option for audio (Janne Grunau)
- drm: apple: dptx: Debounce HPD by simple msleep() (Janne Grunau)
- drm: apple: Fix/remove log messages (Janne Grunau)
- drm: apple: backlight: force backlight update after resume (Mark Kettenis)
- drm/apple: spelling fixes (Jonathan Gray)
- drm/apple: Add missing RTKit Kconfig dependency (Alyssa Ross)
- drm: apple: mark local functions static (Arnd Bergmann)
- drm: apple: epic: systemep: Parse "mNits" log events (Janne Grunau)
- drm: apple: epic: Pass full notfiy/report payload to handler (Janne Grunau)
- drm: apple: parser: constify parser data (Janne Grunau)
- drm: apple: iomfb: Always parse DisplayAttributes (Janne Grunau)
- drm: apple: Prefer RGB SDR modes (Janne Grunau)
- drm: apple: dptx: Wait for link config on connect (Janne Grunau)
- drm: apple: Be less noisy about teardown notifies without service (Janne Grunau)
- drm: apple: dcp: Fix resume with DPTX based display outputs (Janne Grunau)
- drm: apple: Adjust startup sequence and timing for dptx (Janne Grunau)
- drm: apple: iomfb: Extend hotplug/mode parsing logging (Janne Grunau)
- drm : apple: iomfb: Handle OOB ASYNC/CB context (Janne Grunau)
- drm: apple: iomfb: Use drm_kms_helper_connector_hotplug_event (Janne Grunau)
- drm: apple: Fix DPTX hotplug handling (Janne Grunau)
- drm: apple: Move modeset into drm_crtc's atomic_enable (Janne Grunau)
- drm: apple: dptx: Log connect/disconnect calls (Janne Grunau)
- drm: apple: Extract modeset crtc's atomic_flush() (Janne Grunau)
- drm: apple: iomfb: Improve hotplug related logging (Janne Grunau)
- drm: apple: HPD: Only act on connect IRQs (Janne Grunau)
- drm: apple: dptx: Wait for completion of dptx_connect. (Janne Grunau)
- drm: apple: Disconnect dptx When the CRTC is powered down (Janne Grunau)
- drm: apple: dptx: Implement APCALL_DEACTIVATE and reset the phy (Janne Grunau)
- Revert "drm: apple: iomfb: Do not match/create PMU service for dcpext" (Janne Grunau)
- drm: apple: Keep information at which swap_id fb are still referenced (Janne Grunau)
- drm: apple: Implement D592 callback (Janne Grunau)
- drm: apple: afk: Update read pointer before processing message (Janne Grunau)
- drm: apple: HACK: Do not delete piodma platform device (Janne Grunau)
- drm: apple: dptxep: Implement drive settings stuff (Hector Martin)
- drm: apple: dptxep: Fix reply size check (Hector Martin)
- drm: apple: Fix missing unlock path in dcp_dptx_connect (Hector Martin)
- drm: apple: afk: Clear commands before sending them (Hector Martin)
- drm: apple: dptx: Adapt dptxport_connect() to observed behavior (Janne Grunau)
- drm: apple: dptx: Add DPTX_APCALL_ACTIVATE (Janne Grunau)
- drm: apple: dptx: Add set_active_lanes APCALL (Janne Grunau)
- drm: apple: dptx: port interface to macOS 13.5 firmware (Janne Grunau)
- drm: apple: dptx: Port APCALL to macOS 13.3 firmware (Janne Grunau)
- drm: apple: afk: Adapt to macOS 13.3 firmware (Janne Grunau)
- drm: apple: iomfb: Do not match/create PMU service for dcpext (Janne Grunau)
- drm: apple: Move offsets for rt_bandwidth callback to DT (Janne Grunau)
- drm: apple: Add DPTX support (Sven Peter)
- drm: apple: afk: Use linear array of services (Janne Grunau)
- drm: apple: DCP AFK/EPIC support (Sven Peter)
- gpu: drm: apple: Add sound mode parsing (Martin Povišer)
- gpu: drm: apple: Add 'parse_blob' (Martin Povišer)
- gpu: drm: apple: Add utility functions for matching on dict keys (Martin Povišer)
- mux: apple dp crossbar: Support t602x DP cross bar variant (Janne Grunau)
- mux: apple dp crossbar: Read UNK_TUNABLE before and after writing it (Janne Grunau)
- mux: apple dp crossbar: FIFO_RD_UNK_EN seems to use 2 bits per dispext* (Janne Grunau)
- mux: apple dp crossbar: Support t8112 varient (Janne Grunau)
- mux: apple DP xbar: Add Apple silicon DisplayPort crossbar (Sven Peter)
- drm: apple: Remove explicit asc-dram-mask handling (Janne Grunau)
- drm: apple: iomfb: Increase modeset tiemout to 8.5 seconds (Janne Grunau)
- drm: apple: iomfb: implement abort_swaps_dcp (Janne Grunau)
- drm: apple: dcp: Remove cargo-culted devm_of_platform_populate (Janne Grunau)
- drm: apple: dcp: Port over to DEFINE_SIMPLE_DEV_PM_OPS (Janne Grunau)
- drm: apple: Update supported firmware versions to 12.3 and 13.5 (Janne Grunau)
- drm: apple: Add D129 allocate_bandwidth iomfb callback (Janne Grunau)
- drm: apple: Align PIODMA buffers to SZ_16K (Janne Grunau)
- drm/apple: Use iommu domain for piodma maps (Janne Grunau)
- drm/apple: Get rid of the piodma dummy driver (Janne Grunau)
- drm: apple: backlight: avoid updating the brightness with a commit (Janne Grunau)
- drm: apple: iomfb: limit backlight updates to integrated panels (Janne Grunau)
- drm: apple: Only match backlight service on DCP with panel (Janne Grunau)
- drm: apple: iomfb: Increase modeset timeout to 2.5 seconds (Janne Grunau)
- drm/apple: Mark DCP as being in the wakeup path (Hector Martin)
- drm/apple: Remove simpledrm framebuffer before DRM device alloc (Janne Grunau)
- WIP: drm/apple: Port to incompatible V13.3 firmware interface (Janne Grunau)
- dcp: Warn if DMA mapping fails (Hector Martin)
- dcp: T602X bwreq support (Hector Martin)
- dcp: 42-bit DMA masks (Hector Martin)
- dcp: Add get_tiling_state (Hector Martin)
- dcp: Allow unused trampolines (Hector Martin)
- drm/apple: Drop unsupported DRM_FORMAT_ARGB2101010 (Janne Grunau)
- drm/apple: Support color transformation matrices (Janne Grunau)
- drm/apple: ignore surf[3] in clear swap calls (Janne Grunau)
- drm/apple: Add support for the macOS 13.2 DCP firmware (Janne Grunau)
- drm/apple: Add callbacks triggered by last_client_close_dcp() (Janne Grunau)
- drm/apple: purge unused dcp_update_notify_clients_dcp (Janne Grunau)
- drm/apple: Align buffers to 16K page size (Asahi Lina)
- drm/apple: Move panel options to its own sub-struct (Janne Grunau)
- drm/apple: Use backlight_get_brightness() (Janne Grunau)
- drm/apple: Set backlight level indirectly if no mode is set (Janne Grunau)
- drm/apple: Fix bad error return (Asahi Lina)
- drm/apple: Fix parse_string() memory leaks (Asahi Lina)
- drm/apple: simplify IOMFB_THUNK_INOUT (Janne Grunau)
- gpu: drm: apple: Wait for iomfb initialization (Janne Grunau)
- gpu: drm: apple: Use components to avoid deferred probing (Janne Grunau)
- drm/apple: Allocate drm objects according to drm's expectations (Janne Grunau)
- drm/apple: Use drm_module_platform_driver (Janne Grunau)
- gpu: drm: apple: Use aperture_remove_conflicting_devices (Janne Grunau)
- drm/apple: Update swap handling (Janne Grunau)
- gpu: drm: apple: Clear all surfaces on startup (Janne Grunau)
- drm/apple: Enable 10-bit mode & set colorspace to native (Hector Martin)
- Revert "gpu: drm: apple: reenable support for {A,X}RGB2101010" (Janne Grunau)
- gpu: drm: apple: Add show_notch module parameter (Janne Grunau)
- gpu: drm: apple: reenable support for {A,X}RGB2101010 (Janne Grunau)
- gpu: drm: apple: Add IOMobileFramebufferAP::get_color_remap_mode (Janne Grunau)
- gpu: drm: apple: Prefer SDR color modes (Janne Grunau)
- gpu: drm: apple: Add tracing for color and timing modes (Janne Grunau)
- gpu: drm: apple: Skip parsing elements of virtual timing modes (Janne Grunau)
- gpu: drm: apple: Parse color modes completely (Janne Grunau)
- drm/apple: Disable fake vblank IRQ machinery (Asahi Lina)
- drm/apple: Check if DCP firmware is supported (Janne Grunau)
- drm/apple: Report "PMUS.Temperature" only for mini-LED backlights (Janne Grunau)
- drm/apple: Schedule backlight update on enable_backlight_message_ap_gated (Janne Grunau)
- drm/asahi: Fix backlight restores on non-microLED devices (Asahi Lina)
- drm/apple: Remove obsolete ignore_swap_complete (Asahi Lina)
- drm/apple: Wait for power on request to complete synchronously (Asahi Lina)
- drm/apple: Read display dimensions from devicetree (Janne Grunau)
- drm/apple: Implement drm_crtc_helper_funcs.mode_fixup (Janne Grunau)
- drm/apple: Add trace point for display brightness (Janne Grunau)
- drm/apple: register backlight device after IOMFB start (Janne Grunau)
- gpu: drm: apple: Avoid drm_fb_dma_get_gem_addr (Janne Grunau)
- drm/apple: Fix suspend/resume handling (Hector Martin)
- HACK: gpu: drm: apple: j314/j316: Ignore 120 Hz mode for integrated display (Janne Grunau)
- gpu: drm: apple: Brightness control via atomic commits (Janne Grunau)
- gpu: drm: apple: "match" PMU/backlight services on init (Janne Grunau)
- gpu: drm: apple: iomfb: Unify call and callback channels (Janne Grunau)
- gpu: drm: apple: iomfb: Use FIELD_{GET,PREP} (Janne Grunau)
- gpu: drm: apple: Prevent NULL pointer in dcp_hotplug (Janne Grunau)
- gpu: drm: apple: Set maximal framebuffer size correctly (Janne Grunau)
- gpu: drm: apple: Fix shutdown of partially probed dcp (Janne Grunau)
- gpu: drm: apple: Provide notch-less modes (Janne Grunau)
- gpu: drm: apple: Support opaque pixel formats (Janne Grunau)
- gpu: drm: apple: Remove other framebuffers before DRM setup (Janne Grunau)
- gpu: drm: apple: Specify correct number of DCP*s for drm_vblank_init (Janne Grunau)
- gpu: drm: apple: Fix DCP initialisation (Janne Grunau)
- gpu: drm: apple: Fix DCP run time PM (Janne Grunau)
- gpu: drm: apple: Add dcp_crtc_atomic_check (Janne Grunau)
- gpu: drm: apple: Send an disconnected hotplug event on ASC crash (Janne Grunau)
- gpu: drm: apple: Convert 2 non-assert WARN()s to dev_err() (Janne Grunau)
- gpu: drm: apple: Reject modes without valid color mode (Janne Grunau)
- gpu: drm: apple: Add apple_drm_gem_dumb_create() (Janne Grunau)
- gpu: drm: apple: Add support for DRM_FORMAT_XRGB2101010 (Janne Grunau)
- gpu: drm: apple: Unbreak multiple DCP plane <-> crtc matching (Janne Grunau)
- gpu: drm: apple: Start using tracepoints (Janne Grunau)
- drm: apple: Replace atomic refcount with kref (Janne Grunau)
- drm: apple: Fix connector state on devices with integrated display (Janne Grunau)
- gpu: drm: apple: Use connector types from devicetree (Janne Grunau)
- WIP: add header test target copied from i915 (Janne Grunau)
- drm/apple: Split dcpep/iomfb out of dcp.c (Janne Grunau)
- drm/apple: make note about drm.mode_config.max_width/height (Janne Grunau)
- drm/apple: Mark the connecter on init only with modes as connected (Janne Grunau)
- drm/apple: Allow modesets even when disconnected (Janne Grunau)
- drm/apple: Fix kzalloc in dcp_flush() (Asahi Lina)
- drm/apple: laod piodma dev via explicit phandle (Janne Grunau)
- WIP: drm/apple: Change the way to clear unused surfaces (Janne Grunau)
- drm/apple: Support memory unmapping/freeing (Janne Grunau)
- drm/apple: clear callback's output data (Janne Grunau)
- drm/apple: implement read_edt_data (Janne Grunau)
- drm/apple: Add less tons of questionable debug prints (Janne Grunau)
- drm/apple: Add somewhat useful debug prints (Janne Grunau)
- drm/apple: toggle power only when active state changes (Janne Grunau)
- drm/apple: Add t600x support (Janne Grunau)
- drm/apple: Clear used callback/cookie on dcp_ack (Janne Grunau)
- drm/apple: Add DCP interface definitions used on t600x (Janne Grunau)
- drm/apple: Log callbacks with their tag as debug output (Janne Grunau)
- drm/apple: Switch to nonblocking commit handling (Janne Grunau)
- drm/apple: dcp: fix TRAMPOLINE_IN macro (Janne Grunau)
- drm/apple: Implement suspend/resume for DCP (Alyssa Rosenzweig)
- drm/apple: Use "apple,asc-dram-mask" for rtkit iovas (Janne Grunau)
- drm/apple: Reference only swapped out framebuffers (Janne Grunau)
- drm/apple: Add nop sr_set_uint_prop callback for t600x-dcp (Janne Grunau)
- drm/apple: Fix rt_bandwidth for t600x (Janne Grunau)
- drm/apple: Use a device tree defined clock for dcpep_cb_get_frequency (Janne Grunau)
- HACK: drm/apple: avoid DCP swaps without attached surfaces (Janne Grunau)
- drm/apple: Start coprocessor on probe (Janne Grunau)
- drm: apple: Relicense DCP driver as dual MIT / GPL v2.0 (Janne Grunau)
- WIP: drm/apple: Add DCP display driver (Alyssa Rosenzweig)
- rust: helpers: Add dma_mapping_error() helper (Sasha Finkelstein)
- rust: io: Add helper for memcpy_toio (Sasha Finkelstein)
- Rust: io: Add memcpy_fromio wrapper (Asahi Lina)
- rust: Add Ownable/Owned types (Asahi Lina)
- rust: of: Discourage us of "of" properties (Janne Grunau)
- rust: of: Add reserved_mem_region_to_resource_byname() (Janne Grunau)
- rust: io: resource: Add owned Resource initialiser (Janne Grunau)
- rust: of: Add OF node abstraction (Asahi Lina)
- of: reserved_mem: Add functions to parse "memory-region" (Rob Herring (Arm))
- rust: soc: apple: rtkit: Add Apple RTKit abstraction (Asahi Lina)
- rust: xarray: Add xarray::remove() convenience function (Janne Grunau)
- rust: kernel: xarray: Implement XArray::find() (Asahi Lina)
- rust: xarray: add `insert` and `reserve` (Tamir Duberstein)
- rust: xarray: implement Default for AllocKind (Tamir Duberstein)
- rust: xarray: use the prelude (Tamir Duberstein)
- rust: time: Add wrapper for fsleep() function (FUJITA Tomonori)
- rust: time: Avoid 64-bit integer division on 32-bit architectures (FUJITA Tomonori)
- rust: kernel: init: Support type paths in try_init!() and try_pin_init!() (Asahi Lina)
- rust: pin-init: Support type paths in pin_init!() and friends (Asahi Lina)
- rust: kernel: lock: Add Lock::pin_init() (Asahi Lina)
- rust: alloc: Flags: Switch to declare_flags_type!() macro. (Asahi Lina)
- rust: types: Add declare_flags_type() (Asahi Lina)
- rust: alloc: vec: Import .drain() / Drain from rust library (Janne Grunau)
- rust: alloc: vec: Add dropped `set_len()` for ::drain() (Janne Grunau)
- rust: alloc: vec: Add TryFrom trait (Janne Grunau)
- rust: alloc: kbox: Add AsRef implementation to Box (Sasha Finkelstein)
- rust: allocator: Disable clippy::undocumented_unsafe_blocks lint (Asahi Lina)
- rust: kernel: platform: Add ::while_bound_with() (Janne Grunau)
- rust: device: Allow access to bound device (Janne Grunau)
- rust: device: Add support for locking the device (Janne Grunau)
- rust: error: Add ENOSYS from uapi/asm-generic/errno.h (Janne Grunau)
- rust: error: Add ECANCELED from uapi/asm-generic/errno.h (Janne Grunau)
- rust: error: Add ENODATA from uapi/asm-generic/errno.h (Janne Grunau)
- rust: error: Add ETIMEDOUT from uapi/asm-generic/errno.h (Janne Grunau)
- rust: init: Add default() utility function (Asahi Lina)
- rust: derive `Zeroable` for all structs & unions generated by bindgen where possible (Benno Lossin)
- rust: add `pin-init` as a dependency to `bindings` and `uapi` (Benno Lossin)
- rust: device: property: Fix use for Sealed trait (Janne Grunau)
- samples: rust: platform: Add property read examples (Remo Senekowitsch)
- rust: device: Add property_get_reference_args (Remo Senekowitsch)
- rust: device: Add child accessor and iterator (Remo Senekowitsch)
- rust: device: Implement accessors for firmware properties (Remo Senekowitsch)
- rust: device: Introduce PropertyGuard (Remo Senekowitsch)
- rust: device: Enable printing fwnode name and path (Remo Senekowitsch)
- rust: device: Move property_present() to FwNode (Remo Senekowitsch)
- rust: device: Create FwNode abstraction for accessing device properties (Remo Senekowitsch)
- rust: dma: add dma addressing capabilities (Danilo Krummrich)
- rust: dma: add as_slice/write functions for CoherentAllocation (Abdiel Janulgue)
- rust: dma: convert the read/write macros to return Result (Abdiel Janulgue)
- rust: dma: clarify wording and be consistent in `coherent` nomenclature (Abdiel Janulgue)
- modules: add rust modules files to MAINTAINERS (Andreas Hindborg)
- rust: samples: add a module parameter to the rust_minimal sample (Andreas Hindborg)
- rust: module: update the module macro with module parameter support (Andreas Hindborg)
- rust: module: use a reference in macros::module::module (Andreas Hindborg)
- rust: introduce module_param module (Andreas Hindborg)
- rust: str: add radix prefixed integer parsing functions (Andreas Hindborg)
- rust: macros: enable use of hyphens in module names (Anisse Astier)
- rust: io: mem: Add Mem abstraction (Asahi Lina)
- rust: platform: allow ioremap of platform resources (Daniel Almeida)
- rust: platform: add resource accessors (Daniel Almeida)
- rust: io: mem: add a generic iomem abstraction (Daniel Almeida)
- rust: io: add resource abstraction (Daniel Almeida)
- rust: fix rust <> nova merge conflicts for v6.16-rc1 (Janne Grunau)
- gpu: drm: nova: select AUXILIARY_BUS instead of depending on it (Alexandre Courbot)
- gpu: nova-core: select AUXILIARY_BUS instead of depending on it (Alexandre Courbot)
- samples: rust: select AUXILIARY_BUS instead of depending on it (Alexandre Courbot)
- rust: drm: gem: Implement AlwaysRefCounted for all gem objects automatically (Lyude Paul)
- rust: drm: gem: s/into_gem_obj()/as_raw()/ (Lyude Paul)
- rust: drm: gem: Refactor IntoGEMObject::from_gem_obj() to as_ref() (Lyude Paul)
- rust: drm: gem: Use NonNull for Object::dev (Lyude Paul)
- gpu: nova-core: move Firmware to firmware module (Alexandre Courbot)
- gpu: nova-core: fix layout of NV_PMC_BOOT_0 (Alexandre Courbot)
- gpu: nova-core: define registers layout using helper macro (Alexandre Courbot)
- gpu: nova-core: take bound device in Gpu::new (Alexandre Courbot)
- gpu: nova-core: add missing GA100 definition (Alexandre Courbot)
- gpu: nova-core: derive useful traits for Chipset (Alexandre Courbot)
- drm: nova-drm: add initial driver skeleton (Danilo Krummrich)
- gpu: nova-core: register auxiliary device for nova-drm (Danilo Krummrich)
- rust: devres: fix doctest build under `!CONFIG_PCI` (Miguel Ojeda)
- samples: rust: pci: take advantage of Devres::access() (Danilo Krummrich)
- rust: devres: implement Devres::access() (Danilo Krummrich)
- rust: revocable: implement Revocable::access() (Danilo Krummrich)
- rust: device: conditionally expect `dead_code` for `parent()` (Miguel Ojeda)
- MAINTAINERS: add DRM Rust source files to DRM DRIVERS (Danilo Krummrich)
- rust: drm: gem: Add GEM object abstraction (Asahi Lina)
- rust: drm: file: Add File abstraction (Asahi Lina)
- rust: drm: add DRM driver registration (Asahi Lina)
- rust: drm: add device abstraction (Asahi Lina)
- rust: drm: add driver abstractions (Asahi Lina)
- rust: drm: ioctl: Add DRM ioctl abstraction (Asahi Lina)
- drm: drv: implement __drm_dev_alloc() (Danilo Krummrich)
- samples: rust: convert PCI rust sample driver to use try_access_with() (Alexandre Courbot)
- rust/revocable: add try_access_with() convenience method (Alexandre Courbot)
- samples: rust: add Rust auxiliary driver sample (Danilo Krummrich)
- rust: auxiliary: add auxiliary registration (Danilo Krummrich)
- rust: auxiliary: add auxiliary device / driver abstractions (Danilo Krummrich)
- rust: device: implement Device::parent() (Danilo Krummrich)
- rust: types: add `Opaque::zeroed` (Danilo Krummrich)
- rust: platform: impl TryFrom<&Device> for &platform::Device (Danilo Krummrich)
- rust: pci: impl TryFrom<&Device> for &pci::Device (Danilo Krummrich)
- rust: dma: require a bound device (Danilo Krummrich)
- rust: devres: require a bound device (Danilo Krummrich)
- rust: pci: move iomap_region() to impl Device<Bound> (Danilo Krummrich)
- rust: device: implement Bound device context (Danilo Krummrich)
- rust: pci: preserve device context in AsRef (Danilo Krummrich)
- rust: platform: preserve device context in AsRef (Danilo Krummrich)
- rust: device: implement device context for Device (Danilo Krummrich)
- rust: device: implement impl_device_context_into_aref! (Danilo Krummrich)
- rust: device: implement impl_device_context_deref! (Danilo Krummrich)
- gpu: nova-core: remove completed Vec extentions from task list (Andrew Ballance)
- rust: list: Fix typo `much` in arc.rs (Sylvan Smit)
- rust: check type of `$ptr` in `container_of!` (Tamir Duberstein)
- rust: workqueue: remove HasWork::OFFSET (Tamir Duberstein)
- rust: retain pointer mut-ness in `container_of!` (Tamir Duberstein)
- Documentation: rust: testing: add docs on the new KUnit `#[test]` tests (Miguel Ojeda)
- Documentation: rust: rename `#[test]`s to "`rusttest` host tests" (Miguel Ojeda)
- rust: str: take advantage of the `-> Result` support in KUnit `#[test]`'s (Miguel Ojeda)
- rust: str: simplify KUnit tests `format!` macro (Miguel Ojeda)
- rust: str: convert `rusttest` tests into KUnit (Miguel Ojeda)
- rust: add `kunit_tests` to the prelude (Miguel Ojeda)
- rust: kunit: support checked `-> Result`s in KUnit `#[test]`s (Miguel Ojeda)
- rust: kunit: support KUnit-mapped `assert!` macros in `#[test]`s (Miguel Ojeda)
- rust: make section names plural (Patrick Miller)
- rust: dma: add missing Markdown code span (Miguel Ojeda)
- rust: task: add missing Markdown code spans and intra-doc links (Miguel Ojeda)
- rust: alloc: add missing Markdown code span (Miguel Ojeda)
- rust: alloc: add missing Markdown code spans (Miguel Ojeda)
- rust: platform: fix docs related to missing Markdown code spans (Miguel Ojeda)
- rust: add C FFI types to the prelude (Miguel Ojeda)
- docs: rust: quick-start: update Ubuntu instructions (Igor Korotin)
- rust: use absolute paths in macros referencing core and kernel (Igor Korotin)
- rust: workaround `bindgen` issue with forward references to `enum` types (Miguel Ojeda)
- rust: list: Add examples for linked list (I Hsin Cheng)
- rust: list: Use "List::is_empty()" to perform checking when possible (I Hsin Cheng)
- rust: remove unneeded Rust 1.87.0 `allow(clippy::ptr_eq)` (Miguel Ojeda)
- rust: str: fix typo in comment (Jihed Chaibi)
- MAINTAINERS: mailmap: update Benno Lossin's email address (Benno Lossin)
- rust: alloc: add Vec::insert_within_capacity (Alice Ryhl)
- rust: alloc: add Vec::remove (Alice Ryhl)
- rust: alloc: add Vec::retain (Alice Ryhl)
- rust: alloc: add Vec::drain_all (Alice Ryhl)
- rust: alloc: add Vec::push_within_capacity (Alice Ryhl)
- rust: alloc: add Vec::pop (Alice Ryhl)
- rust: alloc: add Vec::clear (Alice Ryhl)
- rust: alloc: replace `Vec::set_len` with `inc_len` (Tamir Duberstein)
- rust: alloc: refactor `Vec::truncate` using `dec_len` (Tamir Duberstein)
- rust: alloc: add `Vec::dec_len` (Tamir Duberstein)
- rust: alloc: add Vec::len() <= Vec::capacity invariant (Tamir Duberstein)
- rust: alloc: allow coercion from `Box<T>` to `Box<dyn U>` if T implements U (Alexandre Courbot)
- rust: alloc: use `spare_capacity_mut` to reduce unsafe (Tamir Duberstein)
- rust: alloc: add Vec::resize method (Andrew Ballance)
- rust: alloc: add Vec::truncate method (Andrew Ballance)
- rust: pin-init: improve documentation for `Zeroable` derive macros (Benno Lossin)
- rust: pin-init: fix typos (Benno Lossin)
- rust: pin-init: add `MaybeZeroable` derive macro (Benno Lossin)
- rust: pin-init: allow `Zeroable` derive macro to also be applied to unions (Benno Lossin)
- rust: pin-init: allow `pub` fields in `derive(Zeroable)` (Benno Lossin)
- rust: pin-init: Update the structural pinning link in readme. (Christian Schrefl)
- rust: pin-init: Update Changelog and Readme (Christian Schrefl)
- rust: pin-init: Implement `Wrapper` for `UnsafePinned` behind feature flag. (Christian Schrefl)
- rust: pin-init: Add the `Wrapper` trait. (Christian Schrefl)
- rust: pin-init: add `cast_[pin_]init` functions to change the initialized type (Benno Lossin)
- rust: pin-init: examples: use `allow` instead of `expect` (Benno Lossin)
- rust: pin-init: examples: conditionally enable `feature(lint_reasons)` (Benno Lossin)
- rust: pin-init: internal: skip rustfmt formatting of kernel-only module (Benno Lossin)
- rust: pin-init: synchronize README.md (Benno Lossin)
- MAINTAINERS: add entry for Rust XArray API (Tamir Duberstein)
- rust: xarray: Add an abstraction for XArray (Tamir Duberstein)
- rust: types: add `ForeignOwnable::PointedTo` (Tamir Duberstein)
- MAINTAINERS: rust: Add a new section for all of the time stuff (FUJITA Tomonori)
- rust: time: Introduce Instant type (FUJITA Tomonori)
- rust: time: Introduce Delta type (FUJITA Tomonori)
- rust: time: Add PartialEq/Eq/PartialOrd/Ord trait to Ktime (FUJITA Tomonori)
- rust: hrtimer: Add Ktime temporarily (FUJITA Tomonori)
- rust: replace rustdoc references to alloc::format (Andrew Ballance)
- rust: convert raw URLs to Markdown autolinks in comments (Xizhe Yin)
- rust: clarify the language unstable features in use (Miguel Ojeda)
- rust: uaccess: take advantage of the prelude and `Result`'s defaults (Miguel Ojeda)
- rust: static_assert: add optional message (Altan Ozlu)
- docs: rust: explain that `///` vs. `//` applies to private items too (Miguel Ojeda)
- rust: page: optimize rust symbol generation for Page (Kunwu Chan)
- dmaengine: apple-sio: Implement runtime PM (Janne Grunau)
- dmaengine: apple-sio: Fix chan freeing in error path (Asahi Lina)
- dmaengine: apple-sio: Add Apple SIO driver (Martin Povišer)
- dt-bindings: dma: apple,sio: Add schema (Martin Povišer)
- phy: apple: atc: Ensure DP mode is used for DP-only ATC phys (Janne Grunau)
- phy: apple: atc: Add missing mutex_unlock in error case (Janne Grunau)
- phy: apple: dptx: Add debug prints for unexpected values (Janne Grunau)
- phy: apple: atc: support mode switches in atcphy_dpphy_set_mode() (Janne Grunau)
- HACK: phy: apple: atc: Ignore fake submodes (Janne Grunau)
- phy: apple: atc: Support 'set_lanes' in DP mode (Janne Grunau)
- phy: apple: atc: Support DisplayPort only operation (Janne Grunau)
- phy: apple: atc: Reorder ACIOPHY_CROSSBAR and ACIOPHY_MISC ops (Janne Grunau)
- phy: apple: atc: Split atcphy_dp_configure_lane() (Janne Grunau)
- phy: apple: Add DP TX phy driver (Janne Grunau)
- usb: typec: tipd: Clear interrupts first (Sven Peter)
- WIP: phy: apple: Add Apple Type-C PHY (Sven Peter)
- xhci-pci: asmedia: Add a firmware loader for ASM2214a chips (Hector Martin)
- PCI: apple: Avoid PERST# deassertion through gpiod initialization (Janne Grunau)
- PCI: apple: Log the time it takes for links to come up (Hector Martin)
- PCI: apple: Reorder & improve link-up logic (Hector Martin)
- PCI: apple: Make link up timeout configurable, default to 500ms (Hector Martin)
- PCI: apple: Skip controller port setup for online links (Janne Grunau)
- PCI: apple: Add support for optional PWREN GPIO (Hector Martin)
- PCI: apple: Probe all GPIOs for availability first (Hector Martin)
- dt-bindings: pci: apple,pcie: Add subnode binding, pwren-gpios property (Hector Martin)
- PCI: apple: Add T602x PCIe support (Hector Martin)
- PCI: apple: Abstract register offsets via a SoC-specific structure (Hector Martin)
- PCI: apple: Drop poll for CORE_RC_PHYIF_STAT_REFCLK (Hector Martin)
- PCI: apple: Move port PHY registers to their own reg items (Hector Martin)
- PCI: apple: Move away from INTMSK{SET,CLR} for INTx and private interrupts (Marc Zyngier)
- PCI: apple: Dynamically allocate RID-to_SID bitmap (Marc Zyngier)
- PCI: apple: Move over to standalone probing (Marc Zyngier)
- PCI: ecam: Allow cfg->priv to be pre-populated from the root port device (Marc Zyngier)
- PCI: host-generic: Extract an ecam bridge creation helper from pci_host_common_probe() (Marc Zyngier)
- dt-bindings: pci: apple,pcie: Add t6020 compatible string (Alyssa Rosenzweig)
- nvmem: Add apple-spmi-nvmem driver (Hector Martin)
- spmi: add a spmi driver for Apple SoC (Jean-Francois Bortolotti)
- macsmc: power: ac: Report only supported properties (Janne Grunau)
- macsmc: rtkit: Return -EIO instead of negated SMC results (Janne Grunau)
- hwmon: macsmc: wire up manual fan control support (James Calligeros)
- platform/apple: smc: Add apple_smc_write_f32_scaled (Janne Grunau)
- power: supply: macsmc_power: Report not charging for CHLS thresholds (Janne Grunau)
- power: supply: macsmc_power: Remove CSIL (Hector Martin)
- power: supply: macsmc_power: Add CHLS charge thresholds (Hector Martin)
- hwmon: macsmc: Avoid global writable hwmon_chip_info (Janne Grunau)
- hwmon: add macsmc-hwmon driver (James Calligeros)
- platform/apple: smc: Add apple_smc_read_ioft_scaled (Janne Grunau)
- power: supply: macsmc_power: Add more properties (Hector Martin)
- power: supply: macsmc_power: Report available charge_behaviours (Thomas Weißschuh)
- power: supply: macsmc_power: Add CHWA charge thresholds (Hector Martin)
- power: supply: macsmc_power: Log power data on button presses (Hector Martin)
- macsmc: Fix race between backend and core on notifications (Hector Martin)
- power: supply: macsmc_power: Add a debug mode to print power usage (Hector Martin)
- platform/apple: smc: Add apple_smc_read_f32_scaled (Hector Martin)
- power: supply: macsmc_power: Add critical level shutdown & misc events (Hector Martin)
- Input: macsmc-hid: Support the power button on desktops (Hector Martin)
- gpio: macsmc: Add IRQ support (Hector Martin)
- Input: macsmc-hid: Support button/lid wakeups (Hector Martin)
- Input: macsmc-hid: New driver to handle the Apple Mac SMC buttons/lid (Hector Martin)
- rtc: Add new rtc-macsmc driver for Apple Silicon Macs (Hector Martin)
- power: reset: macsmc-reboot: Add driver for rebooting via Apple SMC (Hector Martin)
- power: supply: macsmc_power: Add AC power supply (Hector Martin)
- power: supply: macsmc_power: Turn off OBC flags if macOS left them on (Hector Martin)
- power: supply: macsmc_power: Use BUIC instead of BRSC for charge (Hector Martin)
- power: supply: macsmc_power: Add more props, rework others (Hector Martin)
- power: supply: macsmc_power: Add present prop (Hector Martin)
- power: supply: macsmc_power: Add cycle count and health props (Hector Martin)
- power: supply: macsmc_power: Driver for Apple SMC power/battery stats (Hector Martin)
- gpio: Add new gpio-macsmc driver for Apple Macs (Hector Martin)
- platform/apple: Add new Apple Mac SMC driver (Hector Martin)
- lib/vsprintf: Add support for generic FOURCCs by extending %%p4cc (Hector Martin)
- DO NOT MERGE: HID: apple: Add fnmode which ignores function keys (Janne Grunau)
- HID: transport: spi: apple: Use distinctive names input devices (Janne Grunau)
- HID: transport: spi: apple: Increase receive buffer size (Janne Grunau)
- HID: magicmouse: Query device dimensions via HID report (Hector Martin)
- HID: transport: spi: Implement GET FEATURE (Hector Martin)
- HID: magicmouse: Handle touch controller resets on SPI devices (Hector Martin)
- HID: Bump maximum report size to 16384 (Hector Martin)
- HID: transport: spi: Add suspend support (Janne Grunau)
- HID: magicmouse: Add .reset_resume for SPI trackpads (Janne Grunau)
- HID: transport: spi: Check status message after transmits (Janne Grunau)
- soc: apple: Add RTKit helper driver (Hector Martin)
- hid: Add Apple DockChannel HID transport driver (Hector Martin)
- soc: apple: Add DockChannel driver (Hector Martin)
- hid: magicmouse: Add MTP multi-touch device support (Hector Martin)
- hid: apple: Bind to HOST devices for MTP (Hector Martin)
- HID: core: Handle HOST bus type when announcing devices (Hector Martin)
- HID: add HOST vendor/device IDs for Apple MTP devices (Hector Martin)
- WIP: HID: transport: spi: add Apple SPI transport (Janne Grunau)
- HID: magicmouse: add support for Macbook trackpads (Janne Grunau)
- HID: magicmouse: use ops function pointers for input functionality (Janne Grunau)
- HID: magicmouse: use struct input_mt_pos for X/Y (Janne Grunau)
- HID: magicmouse: use a define of the max number of touch contacts (Janne Grunau)
- HID: apple: add Fn key mapping for Macbook Pro with touchbar (Janne Grunau)
- HID: apple: add Fn key mapping for Apple silicon MacBooks (Janne Grunau)
- HID: apple: add support for internal keyboards (Janne Grunau)
- HID: add device IDs for Apple SPI HID devices (Janne Grunau)
- fixup! wifi: brcmfmac: Add support for firmware signatures (Janne Grunau)
- [brcmfmac] Disable partial SAE offload (Daniel Berlin)
- [brcmfmac] Clean up and common interface creation handling (Daniel Berlin)
- [brcmfmac] Support bandwidth caps for all bands (Daniel Berlin)
- [brcmfmac] Add support for more rate info in station dumps (Daniel Berlin)
- [brcmfmac] Set chanspec during join. (Daniel Berlin)
- [brcmfmac] Add support for more auth suites in roaming offload (Daniel Berlin)
- [brcmfmac] Let feature attachment fail, and fail if we can't handle the interface versions we find. (Daniel Berlin)
- [brcmfmac] Support new join parameter structure versions (Hector Martin)
- [brcmfmac] Structurize scan parameter handling (Daniel Berlin)
- [brcmfmac] Structurize PNF scan and add support for latest version (Daniel Berlin)
- fixup! define missing event message extension (Daniel Berlin)
- fixup! fix FWIL definition to use SSID length constant (Daniel Berlin)
- [brcmfmac] Fix regulatory domain handling to reset bands properly (Daniel Berlin)
- [brcmfmac] Add support for 6G bands and HE (Daniel Berlin)
- [brcmfmac] Support high power/low power/etc scan flags (Daniel Berlin)
- [brcmfmac] Support GCMP cipher suite, used by WPA3. (Daniel Berlin)
- [brcmfmac] Compute number of available antennas and set it in wiphy structure. (Daniel Berlin)
- [brcmfmac] Dynamically configure VHT settings to match firmware (Daniel Berlin)
- [brcmfmac] Add support for encoding/decoding 6g chanspecs (Daniel Berlin)
- [brcmfmac] Finish firmware mem map, fix heap start calculation bug. (Daniel Berlin)
- brcmfmac: Fix AP mode (Patrick Blass)
- wifi: brcmfmac: Add BCM4388 support (Hector Martin)
- wifi: brcmfmac: Extend brcmf_wsec_pmk_le (Hector Martin)
- wifi: brcmfmac: Support bss_info up to v112 (Hector Martin)
- wifi: brcmfmac: Implement event_msgs_ext (Hector Martin)
- wifi: brcmfmac: Add support for SCAN_V3 (Hector Martin)
- wifi: brcmfmac: Mask all IRQs before starting firmware (Hector Martin)
- wifi: brcmfmac: Do not set reset vector when signatures are in use (Hector Martin)
- wifi: brcmfmac: pcie: Initialize IRQs before firmware boot (Hector Martin)
- wifi: brcmfmac: pcie: Access pcie core registers via dedicated window (Hector Martin)
- wifi: brcmfmac: Handle watchdog properly in newer cores (Hector Martin)
- wifi: brcmfmac: chip: ca7: Only disable D11 cores; handle an arbitrary number (Hector Martin)
- wifi: brcmfmac: Increase bandlist size (Hector Martin)
- wifi: brcmfmac: msgbuf: Increase RX ring sizes to 2048 (Hector Martin)
- wifi: brcmfmac: Add support for firmware signatures (Hector Martin)
- wifi: brcmfmac: Add support for SYSMEM corerev >= 12 & fix < 12 (Hector Martin)
- wifi: brcmfmac: Do not service msgbuf IRQs until ready in MSI mode (Hector Martin)
- wifi: brcmfmac: Shut up p2p unknown frame error (Hector Martin)
- wifi: brcmfmac: Support exchanging power mailbox messages via commonring (Hector Martin)
- wifi: brcmfmac: Implement the H2D/D2H mailbox data commonring messages (Hector Martin)
- wifi: brcmfmac: Add a new bus op for D2H mailbox message handling (Hector Martin)
- wifi: brcmfmac: Add newer msgbuf packet types up to 0x2e (Hector Martin)
- wifi: brcmfmac: Support v6+ flags and set host_cap properly (Hector Martin)
- wifi: brcmfmac: Fix logic for deciding which doorbell registers to use (Hector Martin)
- wifi: brcmfmac: Handle PCIe MSI properly (Hector Martin)
- wifi: brcmfmac: Add missing shared area defines to pcie.c (Hector Martin)
- fixup! ASoC: macaudio: Sense improvements (Janne Grunau)
- fixup! ASoC: macaudio: Sense improvements (Janne Grunau)
- fixup! ASoC: macaudio: Sense improvements (Janne Grunau)
- fixup! ASoC: apple: Add macaudio machine driver (Janne Grunau)
- soc: apple: rtkit: Add tracekit endpoint. (Sasha Finkelstein)
- soc: apple: rtkit: Add apple_rtkit_has_endpoint() (Sasha Finkelstein)
- DO NOT MERGE: dmaengine: apple-admac: Add temporary aop-admac compatible (Sasha Finkelstein)
- READ COMMIT MESSAGE! macaudio: Enable second round of models (Hector Martin)
- READ COMMIT MESSAGE! macaudio: Enable first round of models (Hector Martin)
- ALSA: Support nonatomic dmaengine PCMs (Martin Povišer)
- HACK: ALSA: Export 'snd_pcm_known_rates' (Martin Povišer)
- fixup! dmaengine: apple-admac: Add Apple ADMAC driver (Martin Povišer)
- macaudio: Fix missing kconfig requirement (Sasha Finkelstein)
- ASoC: apple: mca: More delay (Hector Martin)
- ASoC: apple: mca: Add more delay after configuring clock (Hector Martin)
- macaudio: Disable j313 and j274 (Hector Martin)
- ASoC: apple: mca: Add delay after configuring clock (Hector Martin)
- macaudio: Avoid matches against cs42l84's constrols (Janne Grunau)
- macaudio: Fix CHECK return condition checking (Hector Martin)
- macaudio: Sync all gains with macOS (Hector Martin)
- macaudio: Turn please_blow_up_my_speakers into an int (Hector Martin)
- macaudio: Change device ID form Jxxx to AppleJxxx (Hector Martin)
- macaudio: Set the card name explicitly (Hector Martin)
- macaudio: Officially enable j313 speakers (Hector Martin)
- macaudio: Skip speaker sense PCM if no sense or no speakers (Hector Martin)
- macaudio: Remove -3dB safety pad from j313 (Hector Martin)
- ASoC: tas2770: Add zero-fill and pull-down controls (Hector Martin)
- ASoC: tas2770: Add SDZ regulator (Hector Martin)
- macaudio: Rework platform config & add all remaining platforms (Hector Martin)
- ALSA: dmaengine: Always terminate DMA when a PCM is closed (Hector Martin)
- ASoC: apple: mca: Increase reset timeout (Hector Martin)
- macaudio: Use an explicit mutex for the speaker volume lock (Hector Martin)
- ASoC: tas2764: Add SDZ regulator (Hector Martin)
- macaudio: Disable debug (Hector Martin)
- macaudio: Use the same volume limit for all amps (Hector Martin)
- macaudio: Initialize speaker lock properly (Hector Martin)
- macaudio: Enable VSENSE switches (Hector Martin)
- macaudio: Allow DT enabled speakers and gate them off in the driver (Hector Martin)
- ASoC: apple: mca: Do not mark clocks in use for non-providers (Hector Martin)
- macaudio: Add a getter for the interlock (Hector Martin)
- alsa: pcm: Remove the qos request only if active (Hector Martin)
- macaudio: speaker volume safety interlocks (Hector Martin)
- ASoC: ops: Export snd_soc_control_matches() (Hector Martin)
- ASoC: macaudio: Sense improvements (Hector Martin)
- ASoC: macaudio: Fix PD link double-frees? (Hector Martin)
- ASoC: macaudio: Do not disable ISENSE/VSENSE switches on j314 (Martin Povišer)
- ASoC: macaudio: Add 'Speakers Up Indicator' control (Martin Povišer)
- ASoC: macaudio: Remove stale 'speaker_nchans' fields (Martin Povišer)
- ASoC: tas2764: Crop SDOUT zero-out mask based on BCLK ratio (Martin Povišer)
- ASoC: tas2764: Configure zeroing of SDOUT slots (Martin Povišer)
- ASoC: apple: mca: Support capture on multiples BEs (Martin Povišer)
- ASoC: macaudio: Tune constraining of FEs, add BCLK (Martin Povišer)
- NOT UPSTREAMABLE: ASoC: tas2764: Redo I/V sense logic (Martin Povišer)
- ASoC: macaudio: Do not constrain sense PCM (Martin Povišer)
- ASoC: macaudio: Tweak "no audio route" message (Martin Povišer)
- ASoC: macaudio: Start speaker sense capture support (Martin Povišer)
- ASoC: apple: mca: Fix SYNCGEN enable on FE clock consumers (Martin Povišer)
- ASoC: apple: mca: Support FEs being clock consumers (Martin Povišer)
- ASoC: apple: mca: Factor out mca_be_get_fe (Martin Povišer)
- ASoC: apple: mca: Separate data & clock port setup (Martin Povišer)
- ASoC: macaudio: Tune DT parsing error messages (Martin Povišer)
- ASoC: macaudio: Condition selecting NCO driver on COMMON_CLK (Martin Povišer)
- ALSA: control: Add kcontrol callbacks for lock/unlock (Hector Martin)
- ASoC: macaudio: alias j415 kcontrols to j314 (James Calligeros)
- ASoC: apple: mca: Move clock shutdown to be shutdown (Hector Martin)
- ASoC: cs42l42: Set a faster digital ramp-up rate (Hector Martin)
- ASoC: macaudio: constrain frontend channel counts (James Calligeros)
- ASoC: macaudio: Add initial j313 fixup_controls (Martin Povišer)
- ASoC: macaudio: Improve message on opening of unrouted PCM devices (Martin Povišer)
- ASoC: macaudio: Alias f413 fixups to j314 (Hector Martin)
- ASoC: macaudio: Gate off experimental platforms (Hector Martin)
- ASoC: macaudio: s/void_warranty/please_blow_up_my_speakers/ (Hector Martin)
- ASoC: macaudio: s/Freq/Frequency/ in TAS2764 control (Martin Povišer)
- ASoC: macaudio: Drop the 'inverse jack' speaker stuff (Martin Povišer)
- ASoC: macaudio: Rename ALSA driver to simple 'macaudio' (Martin Povišer)
- ASoC: macaudio: Add j493 fixup_controls (Martin Povišer)
- ASoC: macaudio: Add j375 fixup_controls (Martin Povišer)
- ASoC: dapm: Export new 'graph.dot' file in debugfs (Martin Povišer)
- ASoC: macaudio: Fix headset routes (Martin Povišer)
- ASoC: cs42l42: Do not advertise sample bit symmetry (Martin Povišer)
- ASoC: cs42l42: Fix typo (Martin Povišer)
- ASoC: apple: Add macaudio machine driver (Martin Povišer)
- dt-bindings: sound: Add Apple Macs sound peripherals (Martin Povišer)
- ASoC: card: Let 'fixup_controls' return errors (Martin Povišer)
- ASoC: ops: Introduce 'soc_set_enum_kctl' (Martin Povišer)
- ASoC: ops: Introduce 'snd_soc_deactivate_kctl' (Martin Povišer)
- ASoC: ops: Accept patterns in snd_soc_limit_volume (Martin Povišer)
- ASoC: ops: Move guts out of snd_soc_limit_volume (Martin Povišer)
- ASoC: tas2764: expose die temp to hwmon (James Calligeros)
- ASoC: tas2770: expose die temp to hwmon (James Calligeros)
- ASoC: tas2764: Apply Apple quirks (Martin Povišer)
- ASoC: tas2764: Raise regmap range maximum (Martin Povišer)
- ASoC: tas2770: Support setting the PDM TX slot (Hector Martin)
- apple-nvme: defer cache flushes by a specified amount (Jens Axboe)
- MAINTAINERS: Add Apple dwc3 bindings to ARM/APPLE (Hector Martin)
- usb: dwc3: core: Allow phy suspend during init for role_switch_reset_quirk (Janne Grunau)
- usb: dwc3: apple: Do not use host-vbus-glitches workaround (Janne Grunau)
- usb: dwc3: Add support for Apple DWC3 (Sven Peter)
- dt-bindings: usb: Add Apple dwc3 bindings (Sven Peter)
- mmc: pci: gl9755: Quirk UHS-2 for Apple GL9755 (Janne Grunau)
- mmc: sdhci-uhs2: Add quirk for devices with broken UHS-2 (Janne Grunau)
- mmc: core: Skip SD UHS-II enumeration on missing UHS2 cap (Janne Grunau)
- of: Workaround missing '#{address,size}-cells' properties [drop v6.13 + 2] (Janne Grunau)
- Increase MAX_LOCKDEP_CHAIN_HLOCKS (Asahi Lina)
- arm64: Increase kernel stack size to 32K (Asahi Lina)
- drm/simpledrm: Set DMA and coherency mask (Janne Grunau)
- soc: apple: apple-pmgr-pwrstate: Mark on-at-boot PDs as wakeup (Hector Martin)
- tty: serial: samsung_tty: Mark as wakeup_path on no_console_suspend (Hector Martin)
- soc: apple: apple-pmgr-pwrstate: Mark on-at-boot PDs as DEFER_OFF (Hector Martin)
- PM: domains: Add a flag to defer power-off until all consumers probe (Hector Martin)
- driver core: fw_devlink: Add fw_devlink_count_absent_consumers() (Hector Martin)
- i2c: pasemi: Log bus reset causes (Hector Martin)
- usb: typec: tipd: Be more verbose about errors (Hector Martin)
- i2c: pasemi: Improve timeout handling and error recovery (Hector Martin)
- firmware_loader: Add /lib/firmware/vendor path (Hector Martin)
- PCI: apple: Add depends on PAGE_SIZE_16KB (Janne Grunau)
- mmc: sdhci-pci: Support setting CD debounce delay (Hector Martin)
- mmc: sdhci-pci: Support external CD GPIO on all OF systems (Hector Martin)
- of: Demote "Bad cell count" to debug message (Hector Martin)
- tty: serial: samsung_tty: Support runtime PM (Hector Martin)
- iommu: apple-dart: Revert separate iommu_ops for locked/bypass DARTs (Janne Grunau)
- iommu: apple-dart: Disallow identity domains for locked DARTs (Janne Grunau)
- iommu: apple-dart: Support combinations of locked and unlocked DARTs (Janne Grunau)
- fixup! iommu/dart: Support locked DARTs (Janne Grunau)
- fixup! iommu/dart: Track if the DART is locked (Janne Grunau)
- iommu/dart: Support locked DARTs (Alyssa Rosenzweig)
- iommu/dart: Add iommu_ops for locked DARTs (Janne Grunau)
- iommu/dart: Track if the DART is locked (Alyssa Rosenzweig)
- iommu/dart: Use virtual memory ttbr entries in apple_dart_cfg (Janne Grunau)
- iommu/dart: Use separate iommu_ops for DARTs w/o bypass (Janne Grunau)
- iommu: Handle translated device firmware mappings (Janne Grunau)
- iommu: Rename iommu_create_device_direct_mappings() (Janne Grunau)
- iommu: Parse translated reserved regions (Janne Grunau)
- iommu: Add IOMMU_RESV_TRANSLATED for non 1:1 mapped reserved regions (Janne Grunau)
- iommu/of: Free fwspec on probe deferrel (Janne Grunau)
- iommu: apple-dart: Check for fwspec in the device probe path (Hector Martin)
- iommu: apple-dart: Support specifying the DMA aperture in the DT (Hector Martin)
- iommu: apple-dart: Add 4-level page table support (Hector Martin)
- iommu: apple-dart: Make the hw register fields u32s (Hector Martin)
- iommu: apple-dart: Clear stream error indicator bits for T8110 DARTs (Hector Martin)
- iommu: io-pgtable: Add 4-level page table support (Hector Martin)
- iommu: apple-dart: Enable runtime PM (Hector Martin)
- iommu: apple-dart: Link to consumers with blanket RPM_ACTIVE (Martin Povišer)
- iommu: apple-dart: Power on device when handling IRQs (Asahi Lina)
- irqchip/apple-aic: Add support for AICv3 (Janne Grunau)
- soc: apple: rtkit: Pass 0 as size for a NULL crashlog buffer (Janne Grunau)
- soc: apple: rtkit: Use scope-based cleanup in apple_rtkit_crashlog_rx() (Janne Grunau)
- cpuidle: apple: Do not load on unsupported Apple platforms (Janne Grunau)
- cpuidle: apple: Add Apple SoC cpuidle driver (Hector Martin)
- soc: apple: pmgr: Add externally-clocked property (Hector Martin)
- soc: apple: pmgr: Add force-disable/force-reset (Asahi Lina)
- dt-bindings: power: apple,pmgr-pwrstate: Add force-{disable,reset} (Asahi Lina)
- soc: apple: Add driver for Apple PMGR misc controls (Hector Martin)
- soc: apple: rtkit: Add devm_apple_rtkit_free() (Janne Grunau)
- HID: lenovo: Remove CONFIG_ACPI dependency (Janne Grunau)
- ACPI: platform_profile: Add support for non-ACPI platforms (Armin Wolf)
- watchdog: apple: set max_hw_heartbeat_ms instead of max_timeout (Florian Klink)
- DO NOT SUBMIT: arm64: dts: apple: t8103-j457: Add unused PCIe port01 (Janne Grunau)
- arm64: dts: apple: t600x-j375: Move gpu properties to individual devices (Janne Grunau)
- arm64: dts: apple: Move PCIe-GE nodes intro their own file (Janne Grunau)
- arm64: dts: apple: t6022-j180d: Delete non pcie-ge nodes (Janne Grunau)
- arm64: dts: apple: touchbar: Mark ps_dispdfr_be as always-on (Janne Grunau)
- arm64: dts: apple: t6022-j180d: Enable second HDMI port (Janne Grunau)
- arm64: dts: apple: t6022-j180d: Add node for built-in PCIe devices (Janne Grunau)
- arm64: dts: apple: t6022-j180d: Probe all PCIe devices (Janne Grunau)
- arm64: dts: apple: t8103-j45x: Mark missing beamforming (Janne Grunau)
- arm64: dts: apple: t8112-j493: Enable AOP (Janne Grunau)
- arm64: dts: apple: t8112-j415: Enable AOP (Janne Grunau)
- arm64: dts: apple: t8112-j413: Enable AOP (Janne Grunau)
- arm64: dts: apple: t8103-j45x: Enable AOP (Janne Grunau)
- arm64: dts: apple: t8103-j313: Enable AOP (Janne Grunau)
- arm64: dts: apple: t8103-j293: Enable AOP (Janne Grunau)
- arm64: dts: apple: t600x-j314-j316: Enable AOP (Janne Grunau)
- arm64: dts: apple: Remove no-map from remaining agx regions (Asahi Lina)
- arm64: dts: apple: Remove no-map from pagetables region (Asahi Lina)
- arm64: dts: apple: Add AOP audio identifiers (Sasha Finkelstein)
- arm64: dts: apple: Add SEP device tree nodes (Sasha Finkelstein)
- arm64: dts: apple: Add AOP and subdevices (Sasha Finkelstein)
- arm64: dts: apple: j474s: correct case of Mac mini (Jonathan Gray)
- arm64: dts: apple: t602x-j4xx: Add SMC hwmon sensors (Janne Grunau)
- arm64: dts: apple: t600x-j3xx: Add SMC hwmon sensors (Janne Grunau)
- arm64: dts: apple: t8112: Add SMC hwmon sensors (Janne Grunau)
- arm64: dts: apple: t8103: Add SMC hwmon sensors (Janne Grunau)
- arm64: dts: apple: add common hwmon keys and fans (James Calligeros)
- arm64: apple: t8112-j473: Enable sio explicitly (Janne Grunau)
- arm64: apple: t8103-j274: Enable sio explicitly (Janne Grunau)
- arm64: apple: t60x0/t60x1: Enable sio explicitly (Janne Grunau)
- arm64: apple: t60xx: Enable DP/HMI audio nodes on all devices (Janne Grunau)
- arm64: apple: t602x: Add sio and dpaudio device nodes (Janne Grunau)
- arm64: apple: t600x: Add sio and dpaudio device nodes (Janne Grunau)
- arm64: apple: t600x: Move dart_sio* to dieX (Janne Grunau)
- arm64: apple: t8112: Add SIO, DPA nodes; hook up to DCP (Janne Grunau)
- arm64: apple: t8103: Add SIO, DPA nodes; hook up to DCP (Martin Povišer)
- arm64: apple: t602x: pmgr: SIO: Add audio, spi and uart power-domains (Janne Grunau)
- arm64: apple: t600x: pmgr: SIO: Add audio, spi and uart power-domains (Janne Grunau)
- arm64: apple: t8112-pmgr: SIO: Add audio, spi and uart power-domains (Janne Grunau)
- arm64: apple: t8103-pmgr: SIO: Add audio, spi and uart power-domains (Martin Povišer)
- arm64: dts: apple: t8112-j473: Use dcpext for HDMI out (Janne Grunau)
- arm64: dts: apple: j474s/j475c: Use dcpext0 for HDMI out (Janne Grunau)
- arm64: dts: apple: Fill device node for dp2hdmi on Macbook Pros (Janne Grunau)
- arm64: dts: apple: t6022-{j180,j475}: Enable dcpext0/dptx-phy/dp2hdmi (Janne Grunau)
- arm64: dts: apple: t6020-j474,t6021-j475: Enable dcp/dptx-phy/dp2hdmi (Janne Grunau)
- arm64: dts: apple: t8112-j473: Enable dcp/dptx-phy/dp2hdmi (Janne Grunau)
- arm64: dts: apple: t602x: Add device nodes for atc DP crossbar (Janne Grunau)
- arm64: dts: apple: t600x: Add device nodes for atc DP crossbar (Janne Grunau)
- arm64: dts: apple: t602x: Add lpdptx-phy node (Janne Grunau)
- arm64: dts: apple: t8112: Add dptx-phy node (Janne Grunau)
- arm64: dts: apple: t602x: Add t6020 dispext device nodes (Janne Grunau)
- arm64: dts: apple: t600x: Add t6000 dispext device nodes (Janne Grunau)
- arm64: dts: apple: t8112: Add dcpext/dispext0 nodes (Janne Grunau)
- arm64: dts: apple: t8103: Add dcpext/dispext0 nodes (Janne Grunau)
- arm64: dts: apple: t602x: Add "apple,min-state" to ps_dispextN_cpu0 (Janne Grunau)
- arm64: dts: apple: t600x: Add "apple,min-state" to ps_dispextN_cpu0 (Janne Grunau)
- arm64: dts: apple: t8112: Switch to apple,dma-range (Janne Grunau)
- arm64: dts: apple: t8103: Switch to apple,dma-range (Janne Grunau)
- arm64: dts: apple: t600x: Switch to apple,dma-range (Janne Grunau)
- arm64: dts: apple: Disable ps_isp_sys unless it is used (Janne Grunau)
- arm64: dts: apple: add opp-microwatt to t8103/t600x (James Calligeros)
- arm64: dts: apple: j313: Model SDZ GPIO as a regulator (Hector Martin)
- arm64: dts: apple: j293: Model SDZ GPIO as a regulator (Hector Martin)
- arm64: dts: apple: describe shared SDZ GPIO for tas2764 (James Calligeros)
- arm64: dts: apple: j493: Enable speakers (Hector Martin)
- arm64: dts: apple: j313: Enable speakers (Hector Martin)
- arm64: dts: apple: j293: Enable speakers (Hector Martin)
- arm64: dts: apple: j375 & friends: Enable speakers (Hector Martin)
- arm64: dts: apple: t600x-j314-j316: Set sound compatibles per device (Hector Martin)
- arm64: dts: apple: j413: Model SDZ GPIO as a regulator (Hector Martin)
- arm64: dts: apple: j493: Add missing speaker amp IRQs (Hector Martin)
- arm64: dts: apple: j415: Add missing speaker amp IRQs (Hector Martin)
- arm64: dts: apple: j413: Add missing speaker amp IRQs (Hector Martin)
- arm64: dts: apple: j313: Add missing speaker amp IRQs (Hector Martin)
- arm64: dts: apple: j293: Add missing speaker amp IRQs (Hector Martin)
- arm64: dts: apple: j375: Add missing speaker amp IRQs (Hector Martin)
- arm64: dts: apple: j415: Enable speakers (Hector Martin)
- arm64: dts: apple: j413: Enable speakers (Hector Martin)
- arm64: dts: apple: j314/j316: Enable speakers (Hector Martin)
- arm64: dts: apple: t8103-j313: Add I/VMON slots to amps (Hector Martin)
- arm64: dts: apple: t8103-j293: Add I/VMON slots to amps (Hector Martin)
- arm64: dts: apple: t8112-j493: Add I/VMON slots to amps (Hector Martin)
- arm64: dts: apple: t8112-j473: Add I/VMON slots to amp (Hector Martin)
- arm64: dts: apple: t8112-j415: Add I/VMON slots to amps (Hector Martin)
- arm64: dts: apple: t8112-j413: Add I/VMON slots to amps (Hector Martin)
- arm64: dts: apple: t600x-j180d: Add I/VMON slots to amps (Hector Martin)
- arm64: dts: apple: t600x-j375: Add I/VMON slots to amp (Hector Martin)
- arm64: dts: apple: t8112: Mark MCA power states as externally-clocked (Hector Martin)
- arm64: dts: apple: t8103: Mark MCA power states as externally-clocked (Hector Martin)
- arm64: dts: apple: t602x: Mark MCA power states as externally-clocked (Hector Martin)
- arm64: dts: apple: t600x: Mark MCA power states as externally-clocked (Hector Martin)
- arm64: dts: apple: t600x-j314-j316: Zero out unused speaker sense slots (Martin Povišer)
- arm64: dts: apple: t600x-j314-j316: Add speaker I/V sense slots (Martin Povišer)
- arm64: dts: apple: t8103-j274: Add speaker I/V sense slots (Martin Povišer)
- arm64: dts: apple: imx558: Add downscaled resolution presets (Hector Martin)
- arm64: dts: apple: imx248: Add scaled and cropped presets (Janne Grunau)
- arm64: dts: ISP platform configs (Asahi Lina)
- arm64: dts: apple: t602x: Add ISP nodes (Asahi Lina)
- arm64: dts: apple: t8112: Add ISP nodes (Hector Martin)
- arm64: dts: apple: t6000: Add ISP nodes (Eileen Yoon)
- arm64: dts: apple: t8103: Add ISP nodes (Eileen Yoon)
- arm64: dts: apple: t8112: Add nvram alias (Hector Martin)
- arm64: dts: apple: t8103: Add nvram alias (Hector Martin)
- arm64: dts: apple: t6022-j180.dtsi: Add spi nor flash and nvram partition (Janne Grunau)
- arm64: dts: apple: t600x-j375.dtsi: Add spi nor flash and nvram partition (Janne Grunau)
- arm64: dts: apple: t8112: add opp-microwatt props to avalanche/blizzard (James Calligeros)
- arm64: dts: apple: t6020x: Mark dptx_phy_ps only on laptops always-on (Janne Grunau)
- arm64: dts: apple: t8112-j473: Add dptx-phy power-domain (Janne Grunau)
- arm64: dts: apple: t602x: Add initial Mac Studio (2023) device trees (Janne Grunau)
- arm64: dts: apple: t6020-j474s: Disable dcp until lpdpphy is supported (Janne Grunau)
- arm64: dts: apple: t6022: Disable dcp thouroughly (Janne Grunau)
- arm64: dts: apple: Share USB-C port node on t6022 devices (Janne Grunau)
- arm64: dts: apple: t8112-j473: Set GPU base pstate (Asahi Lina)
- arm64: dts: apple: Add devicetree for Macbook Air (15-inch, M2, 2023) (Janne Grunau)
- arm64: dts: apple: t8112: Add touchbar digitizer node (Janne Grunau)
- arm64: dts: apple: t6022: Add APCIE-GE nodes (Hector Martin)
- arm64: dts: apple: Add j180d (Mac Pro 2023) device tree (Hector Martin)
- arm64: dts: apple: Add initial t6022 support (Hector Martin)
- arm64: dts: apple: t600x-j375.dtsi: Add missing etherhet0 alias (Hector Martin)
- arm64: dts: apple: Add T602x GPU node (Asahi Lina)
- arm64: dts: apple: t8112: Enable turbo CPU p-states (Hector Martin)
- arm64: dts: apple: t8103: Enable turbo CPU p-states (Hector Martin)
- arm64: dts: apple: t600x: Enable turbo CPU p-states (Hector Martin)
- arm64: dts: apple: Make ps_msg always-on (Hector Martin)
- arm64: dts: apple: t600x: Remove obsolete comment in ans2 power domain (Hector Martin)
- arm64: dts: apple: Add pmgr-misc nodes to t60xx (Hector Martin)
- DO NOT SUBMIT: arm64: dts: apple: t6020-j474s: Add unused PCIe port01 (Janne Grunau)
- arm64: dts: apple: Add identity dma-ranges mapping (Hector Martin)
- arm64: dts: apple: Add MTP nodes to t6020x (Hector Martin)
- arm64: dts: apple: Add initial t602x device trees (Hector Martin)
- arm64: dts: apple: Fix t600x mca IRQs (Hector Martin)
- arm64: dts: apple: Add keyboard alias & layout props for t8112 laptops (Hector Martin)
- arm64: dts: apple: j314/j316: Disable ATC3_USB_AON power domain (Hector Martin)
- arm64: dts: apple: t8112: Add "ps_disp0_cpu0" as resets for dcp (Janne Grunau)
- arm64: dts: apple: t8103: Add "ps_disp0_cpu0" as resets for dcp (Janne Grunau)
- arm64: dts: apple: t600x: Add "ps_disp0_cpu0" as resets for dcp (Janne Grunau)
- arm64: dts: apple: t8103: Add missing ps_pmp dependency to ps_gfx (Janne Grunau)
- arm64: dts: apple: t8112: Add DCP power domain to missing devices (Hector Martin)
- arm64: dts: apple: t8103: Add DCP power domain to missing devices (Hector Martin)
- arm64: dts: apple: t600x: Add DCP power domain to missing devices (Hector Martin)
- arm64: dts: apple: Add GPU firmware versions to t8113/t600x (Asahi Lina)
- arm64: dts: apple: Add GPU nodes to T8112 (Asahi Lina)
- arm64: dts: apple: Add no-map to GPU reserved-memory nodes (Asahi Lina)
- arm64: dts: t8103: Add GPU leak coefficients (Asahi Lina)
- arm64: dts: Add t600x GPU nodes (Asahi Lina)
- arm64: dts: Add power data for t8103 (Asahi Lina)
- arm64: dts: Add GPU performance data to t8103.dts (Asahi Lina)
- arm64: dts: apple: t8103*: Add GPU nodes (Asahi Lina)
- scripts/dtc: Add support for floating-point literals (Asahi Lina)
- arm64: dts: apple: t8112: Add dcp/disp0 nodes (Janne Grunau)
- arm64: dts: apple: t8112: Add ATCPHY nodes (Janne Grunau)
- arm64: dts: apple: t8112: Add eFuses node (Janne Grunau)
- arch: arm64: apple: Add dcp panel node for t600x based laptops (Janne Grunau)
- arch: arm64: apple: Add dcp panel node for t8103 based laptops and imacs (Janne Grunau)
- arch: arm64: dts: apple: t600x: Add ATCPHY nodes (R)
- arch: arm64: dts: apple: t6000: Add eFuses node (R)
- arm64: dts: apple: t8103: Add ATCPHY node (Sven Peter)
- arm64: dts: apple: t8103: Add eFuses node (Sven Peter)
- arch: arm64: apple: t600x: Add connector type property for DCP* (Janne Grunau)
- arch: arm64: apple: t8103: Add connector type property for DCP* (Janne Grunau)
- arch: arm64: apple: t600x: Add display controller related device tree nodes (Janne Grunau)
- arch: arm64: apple: Add display controller related device tree nodes (Hector Martin)
- arch: arm64: apple: t600x: Mark USB and PCIe as "dma-coherent" (Janne Grunau)
- arch: arm64: apple: Add missing power state deps for display (Janne Grunau)
- arm64: dts: apple: t6001-j375c: Add USB3 hub GPIO initialization (Hector Martin)
- arm64: dts: apple: Drop 'integrated audio' from sound models (Martin Povišer)
- arm64: dts: apple: t600x-jxxx: Put in audio nodes (Martin Povišer)
- arm64: dts: apple: t8103*: Put in audio nodes (Martin Povišer)
- arm64: dts: apple: t600x: Add bluetooth device trees (Hector Martin)
- arm64: dts: apple: Add PCI power enable GPIOs (Hector Martin)
- arm64: dts: apple: Add WiFi module and antenna properties (Hector Martin)
- arm64: dts: apple: t600x: Add dwc3 nodes (Janne Grunau)
- arm64: dts: apple: j31[46]: Add keyboard nodes (Janne Grunau)
- arm64: dts: apple: Add PMU NVMEM and SMC RTC/reboot nodes (Hector Martin)
- arm64: dts: apple: Add SMC node to t600x devicetrees (Hector Martin)
- arm64: dts: apple: Keep PCIe power domain on (Hector Martin)
- arm64: dts: apple: Mark ATC USB AON domains as always-on (Hector Martin)
- arm64: dts: apple: Add PMU NVMEM and SMC RTC/reboot nodes (Hector Martin)
- arm64: dts: apple: Add SMC node to t8103/t6001 devicetrees (Hector Martin)
- arm64: dts: apple: Add PCI power enable GPIOs (Hector Martin)
- arm64: dts: apple: t8103: Add spi3 keyboard node (Janne Grunau)
- arm64: dts: apple: t8103: Add dwc3 nodes (Hector Martin)
- arm64: dts: apple: t8112: Add mtp device nodes for j413/j493 (Janne Grunau)
- arm64: dts: apple: t8112: Add dwc3 nodes (Janne Grunau)
- arm64: dts: apple: t8112*: Put in audio nodes (Martin Povišer)
- arm64: dts: apple: t8112: Add SMC node to devicetree (Hector Martin)
- arm64: dts: apple: t8112: Add wlan/bt PCIe device nodes (Janne Grunau)
- arm64: dts: apple: t8112: Remove always-on from the PMP node (Hector Martin)
- arm64: dts: apple: Add PMIC NVMEM (Hector Martin)
- arm64: dts: apple: Add SPMI controller nodes (Sasha Finkelstein)
- arm64: dts: apple: t8015: Add CPU caches (Nick Chan)
- arm64: dts: apple: t8012: Add CPU caches (Nick Chan)
- arm64: dts: apple: t8011: Add CPU caches (Nick Chan)
- arm64: dts: apple: t8010: Add CPU caches (Nick Chan)
- arm64: dts: apple: s8001: Add CPU caches (Nick Chan)
- arm64: dts: apple: s800-0-3: Add CPU caches (Nick Chan)
- arm64: dts: apple: t7001: Add CPU caches (Nick Chan)
- arm64: dts: apple: t7000: Add CPU caches (Nick Chan)
- arm64: dts: apple: s5l8960x: Add CPU caches (Nick Chan)

* Fri Aug 15 2025 Justin M. Forbes <jforbes@fedoraproject.org> [6.15.10-0]
- Enable CONFIG_VHOST_ENABLE_FORK_OWNER_CONTROL (Justin M. Forbes)
- Disable NOVA_CORE (Justin M. Forbes)
- Revert "crypto: sig - Disable signing" (Justin M. Forbes)
- btrfs: fix log tree replay failure due to file with 0 links and extents (Filipe Manana)
- Linux v6.15.10

* Fri Aug 01 2025 Augusto Caringi <acaringi@redhat.com> [6.15.9-0]
- Linux v6.15.9

* Thu Jul 24 2025 Augusto Caringi <acaringi@redhat.com> [6.15.8-0]
- Linux v6.15.8

* Thu Jul 17 2025 Augusto Caringi <acaringi@redhat.com> [6.15.7-0]
- Linux v6.15.7

* Thu Jul 10 2025 Augusto Caringi <acaringi@redhat.com> [6.15.6-0]
- Turn on MITIGATION_TSA for RHEL configs (Augusto Caringi)
- Turn on TSA Mitigation for Fedora (Justin M. Forbes)
- Linux v6.15.6

* Sun Jul 06 2025 Justin M. Forbes <jforbes@fedoraproject.org> [6.15.5-0]
- io_uring: gate REQ_F_ISREG on !S_ANON_INODE as well (Jens Axboe)
- Linux v6.15.5

* Fri Jun 27 2025 Justin M. Forbes <jforbes@fedoraproject.org> [6.15.4-0]
- redhat: Restore the status quo wrt memory onlining (Vitaly Kuznetsov) [2375049]
- Linux v6.15.4

* Thu Jun 19 2025 Justin M. Forbes <jforbes@fedoraproject.org> [6.15.3-0]
- ACPICA: Refuse to evaluate a method if arguments are missing (Rafael J. Wysocki)
- Linux v6.15.3

* Fri Jun 13 2025 Justin M. Forbes <jforbes@fedoraproject.org> [6.15.2-0]
- wifi: ath12k: support MLO as well if single_chip_mlo_support flag is set (Baochen Qiang)
- wifi: ath12k: use fw_features only when it is valid (Baochen Qiang)
- wifi: ath12k: introduce ath12k_fw_feature_supported() (Baochen Qiang)
- aarch64: Switch TI_SCI_CLK and TI_SCI_PM_DOMAINS symbols to built-in (Peter Robinson)
- redhat/configs: fedora: set some qcom clk, icc, and pinctrl drivers to built in (Brian Masney)

* Tue Jun 10 2025 Justin M. Forbes <jforbes@fedoraproject.org> [6.15.2-0]
- Revert "drm/amd/display: more liberal vmin/vmax update for freesync" (Justin M. Forbes)
- Linux v6.15.2

* Wed Jun 04 2025 Justin M. Forbes <jforbes@fedoraproject.org> [6.15.1-0]
- arm64: dts: rockchip: Drop assigned-clock* from cpu nodes on rk3588 (Diederik de Haas)
- arm64: dts: rockchip: Improve LED config for NanoPi R5S (Diederik de Haas)
- arm64: dts: rockchip: Move rk3568 PCIe3 MSI to use GIC ITS (Chukun Pan)
- arm64: dts: rockchip: Update eMMC for NanoPi R5 series (Peter Robinson)
- arm64: dts: rockchip: Add vcc-supply to SPI flash on rk3566-rock3c (Peter Robinson)
- arm64: dts: rockchip: Add vcc-supply to SPI flash on rk3566-quartz64-b (Diederik de Haas)
- arm64: dts: rockchip: Add phy-supply to gmac0 on NanoPi R5S (Diederik de Haas)
- arm64: dts: rockchip: Add vcc-supply to SPI flash on rk3588-rock-5b (Diederik de Haas)
- arm64: dts: rockchip: Add vcc-supply to SPI flash on rk3399-rockpro64 (Diederik de Haas)
- arm64: dts: rockchip: Add vcc-supply to SPI flash on rk3328-rock64 (Diederik de Haas)
- arm64: dts: rockchip: Move SHMEM memory to reserved memory on rk3588 (Chukun Pan)
- arm64: dts: rockchip: Add gmac phy reset GPIO to QNAP TS433 (Uwe Kleine-König)
- arm64: dts: rockchip: Correct gmac phy address on QNAP TS433 (Uwe Kleine-König)
- Reset build id for fedora-srpm script (Justin M. Forbes)
- redhat/configs: Add configs for new ov02c10 and ov02e10 drivers (Hans de Goede)
- media: i2c: Add Omnivision OV02C10 sensor driver (Heimir Thor Sverrisson)
- media: i2c: ov02e10: add OV02E10 image sensor driver (Jingjing Xiong)
- platform/x86: int3472: Debug log when remapping pins (Hans de Goede)
- platform/x86: int3472: Add handshake pin support (Hans de Goede)
- platform/x86: int3472: Prepare for registering more than 1 GPIO regulator (Hans de Goede)
- platform/x86: int3472: Avoid GPIO regulator spikes (Hans de Goede)
- platform/x86: int3472: Make regulator supply name configurable (Hans de Goede)
- platform/x86: int3472: Rework AVDD second sensor quirk handling (Hans de Goede)
- platform/x86: int3472: Drop unused gpio field from struct int3472_gpio_regulator (Hans de Goede)
- platform/x86: int3472: Stop setting a supply-name for GPIO regulators (Hans de Goede)
- platform/x86: int3472: Add skl_int3472_register_clock() helper (Hans de Goede)
- powerpc: Fix struct termio related ioctl macros (Madhavan Srinivasan)
- Initial setup for stable Fedora releases (Justin M. Forbes)
- Reset RHEL_RELEASE for the 6.16 cycle (Justin M. Forbes)
- fedora: add 'fedora' SBAT suffix for UKI addons (Li Tian)
- redhat: add downstream SBAT for UKI addons (Emanuele Giuseppe Esposito)
- uki_addons: provide custom SBAT as input parameter (Emanuele Giuseppe Esposito)
- uki_addons: remove completely sbat/sbat.conf (Emanuele Giuseppe Esposito)
- Linux v6.15.1

* Mon May 26 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-60]
- Consolidate configs to common for 6.15 (Justin M. Forbes)
- Linux v6.15.0

* Thu May 22 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc7.d608703fcdd9.59]
- Linux v6.15.0-0.rc7.d608703fcdd9

* Wed May 21 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc7.4a95bc121ccd.58]
- redhat/configs: automotive: enable MHI_BUS_EP (Eric Chanudet)
- Fix PHYSICAL_ALIGN for x86 Fedora (Justin M. Forbes)
- Switch ZSWAP_ZPOOL_DEFAULT to ZSMALLOC as ZBUD has been removed (Justin M. Forbes)
- redhat: configs: rhel: Enable CX231XX drivers (Kate Hsuan)
- configs: add redhat/configs/common/generic/CONFIG_OBJTOOL_WERROR (Ryan Sullivan) [RHEL-85301]
- redhat: make ENABLE_WERROR also enable OBJTOOL_WERROR (Ryan Sullivan) [RHEL-85301]
- redhat/configs: Enable CONFIG_X86_POSTED_MSI (Jerry Snitselaar)
- Linux v6.15.0-0.rc7.4a95bc121ccd

* Mon May 19 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc7.57]
- redhat/configs: remove CRC16 config files (Scott Weaver)
- Linux v6.15.0-0.rc7

* Sun May 18 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc6.5723cc3450bc.56]
- Revert CONFIG_GENKSYMS in pending for x86 (Justin M. Forbes)
- Linux v6.15.0-0.rc6.5723cc3450bc

* Sat May 17 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc6.172a9d94339c.55]
- Linux v6.15.0-0.rc6.172a9d94339c

* Fri May 16 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc6.fee3e843b309.54]
- Linux v6.15.0-0.rc6.fee3e843b309

* Thu May 15 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc6.088d13246a46.53]
- Flip GENKSYMS for RHEL (Justin M. Forbes)
- Linux v6.15.0-0.rc6.088d13246a46

* Thu May 15 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc6.9f35e33144ae.52]
- Move MITIGATION_ITS to the x86 directory (Justin M. Forbes)
- Set MITIGATION_ITS for Fedora (Justin M. Forbes)
- Fedora: arm: Updates for QCom devices (Souradeep Chowdhury)

* Wed May 14 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc6.9f35e33144ae.51]
- redhat/configs: Explicitly disable CONFIG_VIRTIO_MEM on powerpc in RHEL (Thomas Huth)
- redhat/configs: Consolidate the CONFIG_AP_DEBUG config switch (Thomas Huth)
- Linux v6.15.0-0.rc6.9f35e33144ae

* Tue May 13 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc6.e9565e23cd89.50]
- Set Fedora configs for 6.15 (Justin M. Forbes)
- Linux v6.15.0-0.rc6.e9565e23cd89

* Mon May 12 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc6.49]
- Shorten the uname for git snapshots (Justin M. Forbes)
- Linux v6.15.0-0.rc6

* Sun May 11 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc5.3ce9925823c7.48]
- Linux v6.15.0-0.rc5.3ce9925823c7

* Sat May 10 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc5.1a33418a69cc.47]
- nvme: explicitly enable the nvme keyring (Maurizio Lombardi)
- Linux v6.15.0-0.rc5.1a33418a69cc

* Fri May 09 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc5.9c69f8884904.46]
- Enable the gs_usb CAN bus driver in RHEL (Radu Rendec)
- Stop disabling some modules needed to run on Azure (Pierre-Yves Chibon)
- redhat/configs: enable ACPI_DEBUG on non-debug kernels (Mark Langsdorf)
- specfile:  add with_toolsonly variable to build only tools packages (Clark Williams)
- redhat/configs: Enable CONFIG_TYPEC_TBT_ALTMODE in RHEL (Desnes Nunes) [RHEL-78931]
- Linux v6.15.0-0.rc5.9c69f8884904

* Thu May 08 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc5.d76bb1ebb558.45]
- Linux v6.15.0-0.rc5.d76bb1ebb558

* Wed May 07 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc5.0d8d44db295c.44]
- Linux v6.15.0-0.rc5.0d8d44db295c

* Tue May 06 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc5.01f95500a162.43]
- Linux v6.15.0-0.rc5.01f95500a162

* Mon May 05 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc5.42]
- Linux v6.15.0-0.rc5

* Sun May 04 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc4.e8ab83e34bdc.41]
- Linux v6.15.0-0.rc4.e8ab83e34bdc

* Sat May 03 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc4.95d3481af6dc.40]
- Turn on ACPI_DEBUG for Fedora (Justin M. Forbes)
- redhat: fix kernel-rt-kvm package removal for Fedora (Thorsten Leemhuis)
- Linux v6.15.0-0.rc4.95d3481af6dc

* Fri May 02 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc4.ebd297a2affa.39]
- redhat/configs: aarch64: Enable Apple touchbar display driver for Fedora (Neal Gompa)
- Linux v6.15.0-0.rc4.ebd297a2affa

* Thu May 01 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc4.4f79eaa2ceac.38]
- redhat: remove kernel-rt-kvm package (Clark Williams)
- redhat: introduce modules-extra-matched meta package (Jan Stancek)
- Fix up some Netfilter configs for Fedora (Justin M. Forbes)
- Turn NF_CT_NETLINK_TIMEOUT for Fedora (Justin M. Forbes)
- Turn on NF_CONNTRACK_TIMEOUT for Fedora (Justin M. Forbes)
- Linux v6.15.0-0.rc4.4f79eaa2ceac

* Wed Apr 30 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc4.b6ea1680d0ac.37]
- redhat/configs: Adjust CONFIG_TUNE for s390x (Mete Durlu)
- Linux v6.15.0-0.rc4.b6ea1680d0ac

* Tue Apr 29 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc4.ca91b9500108.36]
- redhat/spec: fix selftests dependencies (Gregory Bell) [RHEL-88228]
- redhat: add namespace selftests to kernel-modules-internal package (Joel Savitz) [RHEL-88635]
- Turn off CONFIG_PCI_REALLOC_ENABLE_AUTO for Fedora (Justin M. Forbes)
- Linux v6.15.0-0.rc4.ca91b9500108

* Mon Apr 28 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc4.35]
- Linux v6.15.0-0.rc4

* Sun Apr 27 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc3.5bc1018675ec.34]
- Linux v6.15.0-0.rc3.5bc1018675ec

* Sat Apr 26 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc3.f1a3944c860b.33]
- Linux v6.15.0-0.rc3.f1a3944c860b

* Fri Apr 25 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc3.02ddfb981de8.32]
- gitlab-ci: enable pipelines for rt-64k (Clark Williams)
- rt-64k:  Enable building 64k page-size RT kernel (Clark Williams)
- Linux v6.15.0-0.rc3.02ddfb981de8

* Thu Apr 24 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc3.a79be02bba5c.31]
- redhat: drop Y issues from changelog (Jan Stancek)
- redhat/configs: Update the CONFIG_KERNEL_IMAGE_BASE kernel config option (Thomas Huth)
- redhat/configs: Remove the obsolete CONFIG_ZCRYPT_DEBUG switches (Thomas Huth)
- redhat/configs: Consolidate the CONFIG_AP switch (Thomas Huth)
- Linux v6.15.0-0.rc3.a79be02bba5c

* Wed Apr 23 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc3.bc3372351d0c.30]
- Linux v6.15.0-0.rc3.bc3372351d0c

* Tue Apr 22 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc3.a33b5a08cbbd.29]
- fedora: updates for 6.15 (Peter Robinson)
- redhat/configs: Disable CONFIG_COMPAT option on s390 (Mete Durlu) [RHEL-24047]
- Linux v6.15.0-0.rc3.a33b5a08cbbd

* Mon Apr 21 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc3.9d7a0577c9db.28]
- Linux v6.15.0-0.rc3.9d7a0577c9db

* Sun Apr 20 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc2.6fea5fabd332.27]
- Linux v6.15.0-0.rc2.6fea5fabd332

* Sat Apr 19 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc2.8560697b23dc.26]
- uki: Add weak dependency on 'uki-direct' (Vitaly Kuznetsov)
- redhat/kernel.spec: fix duplicate packaging of ynl headers (Jan Stancek)
- Enable FunctionFS on aarch64 + x86 (Sam Day)
- Linux v6.15.0-0.rc2.8560697b23dc

* Fri Apr 18 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc2.fc96b232f8e7.25]
- Turn on USB Gadget for Fedora x86 (Justin M. Forbes)
- Linux v6.15.0-0.rc2.fc96b232f8e7

* Thu Apr 17 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc2.cfb2e2c57aef.24]
- redhat: enable drm panic screen with a QR code (Scott Weaver)
- redhat: enable Rust code in ELN (Scott Weaver)
- redhat: strip leading '(' in dist-get-buildreqs (Jan Stancek)
- Linux v6.15.0-0.rc2.cfb2e2c57aef

* Wed Apr 16 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc2.1a1d569a75f3.23]
- Linux v6.15.0-0.rc2.1a1d569a75f3

* Tue Apr 15 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc2.834a4a689699.22]
- Linux v6.15.0-0.rc2.834a4a689699

* Mon Apr 14 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc2.21]
- Linux v6.15.0-0.rc2

* Sun Apr 13 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc1.7cdabafc0012.20]
- Linux v6.15.0-0.rc1.7cdabafc0012

* Sat Apr 12 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc1.3bde70a2c827.19]
- Linux v6.15.0-0.rc1.3bde70a2c827

* Fri Apr 11 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc1.900241a5cc15.18]
- Linux v6.15.0-0.rc1.900241a5cc15

* Thu Apr 10 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc1.3b07108ada81.17]
- Linux v6.15.0-0.rc1.3b07108ada81

* Wed Apr 09 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc1.a24588245776.16]
- Fix up CONFIG_CRC_ITU_T mismatch (Scott Weaver)
- Fix up CONFIG_CRC16 mismatch (Scott Weaver)
- Linux v6.15.0-0.rc1.a24588245776

* Wed Apr 09 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc1.15]
- redhat: remove kernel-ipaclones-internal package (Joe Lawrence)
- redhat/kernel.spec.template: add net packetdrill selftests (Hangbin Liu)
- redhat/kernel.spec.template: Build rtla with BPF sample collection (Tomas Glozar)

* Tue Apr 08 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc1.14]
- redhat/configs: automotive: Enable CONFIG_BOOTPARAM_HUNG_TASK_PANIC config (Dorinda Bassey)
- samples/bpf: fix build (Gregory Bell)
- redhat: create 'systemd-volatile-overlay' addon for UKI (Emanuele Giuseppe Esposito)

* Mon Apr 07 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc1.13]
- fedora: arm64: move some TI drivers to modular (Peter Robinson)
- fedora: minor cleanups for 6.14 (Peter Robinson)
- redhat/configs: enable CONFIG_I2C_MUX_PCA954x on x86 (Michal Schmidt)
- Linux v6.15.0-0.rc1

* Sun Apr 06 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc0.f4d2ef48250a.12]
- Linux v6.15.0-0.rc0.f4d2ef48250a

* Sat Apr 05 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc0.a8662bcd2ff1.11]
- Linux v6.15.0-0.rc0.a8662bcd2ff1

* Fri Apr 04 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc0.e48e99b6edf4.10]
- Linux v6.15.0-0.rc0.e48e99b6edf4

* Thu Apr 03 2025 Fedora Kernel Team <kernel-team@fedoraproject.org> [6.15.0-0.rc0.a2cc6ff5ec8f.9]
- redhat: bump RHEL_MAJOR (Jan Stancek)
- redhat/configs: enable CONFIG_AMD_3D_VCACHE for x86 on RHEL (David Arcari)
- Linux v6.15.0-0.rc0.a2cc6ff5ec8f


###
# The following Emacs magic makes C-c C-e use UTC dates.
# Local Variables:
# rpm-change-log-uses-utc: t
# End:
###
