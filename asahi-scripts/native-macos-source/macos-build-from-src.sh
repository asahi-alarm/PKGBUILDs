#!/bin/bash
#
# This script will attempt a full build from source
# NOTE: It clones git repos within the asahi-alarm repo
#       The git diff in this dir will not look right
#
set -e

if [ "$(uname)" != "Darwin" ]; then
  echo "Your system is not: Darwin"
  echo "               got: $(uname)"
  exit 1
fi

export HOMEBREW_NO_AUTO_UPDATE=1
P="llvm lld rust rustup make libelf gnu-sed bindgen"
GOT=$(brew ls --versions $P)
MISSING=""
for a in $P; do
  if ! grep -q "^$a"<<<"$GOT"; then
    MISSING="$MISSING $a"
  fi
done
if [ -n "$MISSING" ]; then
  echo "* brew install $MISSING"
  brew install $MISSING
  rustup component add rust-src
  rustup target add aarch64-unknown-none-softfloat
fi

if [ ! -d m1n1 ]; then
  echo "* git clone --recursive --depth=1 https://github.com/AsahiLinux/m1n1"
  git clone --recursive --depth=1 https://github.com/AsahiLinux/m1n1
fi

J=12
echo "* cd m1n1; make BUILDSTD=1 -j$J"
(
  cd m1n1
  make BUILDSTD=1 -j$J
)

if [ ! -x m1n1/build/m1n1.macho ]; then
  ls -l m1n1/build/m1n1.macho
  exit 1
fi
echo "* -rwx m1n1/build/m1n1.macho"

if [ ! -d linux ]; then
  echo "* git clone --recursive --depth=1 https://github.com/AsahiLinux/linux -b asahi-wip linux"
  git clone --recursive --depth=1 https://github.com/AsahiLinux/linux -b asahi-wip linux


  cd linux # inline patches to fix the build even for case-insensitive fs

  git rm -f include/uapi/linux/netfilter/xt_CONNMARK.h \
                    include/uapi/linux/netfilter/xt_DSCP.h \ include/uapi/linux/netfilter/xt_MARK.h \ 
                    include/uapi/linux/netfilter/xt_RATEEST.h \ include/uapi/linux/netfilter/xt_TCPMSS.h \ 
                    include/uapi/linux/netfilter_ipv4/ipt_ECN.h \ include/uapi/linux/netfilter_ipv4/ipt_TTL.h \ 
                    include/uapi/linux/netfilter_ipv6/ip6t_HL.h

  git checkout HEAD include/uapi/linux/netfilter/xt_connmark.h \
                    include/uapi/linux/netfilter/xt_dscp.h \ include/uapi/linux/netfilter/xt_mark.h \ 
                    include/uapi/linux/netfilter/xt_rateest.h \ include/uapi/linux/netfilter/xt_tcpmss.h \ 
                    include/uapi/linux/netfilter_ipv4/ipt_ecn.h \ include/uapi/linux/netfilter_ipv4/ipt_ttl.h \ 
                    include/uapi/linux/netfilter_ipv6/ip6t_hl.h

  patch -p1 <<EOF
This adds xt_DSCP.h *and* include/uapi/linux/netfilter_ipv4/ipt_ECN.h to xt_dspc.h
index 7594e4df8..3c9acee15 100644
--- a/include/uapi/linux/netfilter/xt_dscp.h
+++ b/include/uapi/linux/netfilter/xt_dscp.h
@@ -29,4 +29,31 @@ struct xt_tos_match_info {
 	__u8 invert;
 };
 
+struct xt_DSCP_info {
+       __u8 dscp;
+};
+
+struct xt_tos_target_info {
+       __u8 tos_value;
+       __u8 tos_mask;
+};
+
+#define IPT_ECN_IP_MASK	(~XT_DSCP_MASK)
+
+#define IPT_ECN_OP_SET_IP	0x01	/* set ECN bits of IPv4 header */
+#define IPT_ECN_OP_SET_ECE	0x10	/* set ECE bit of TCP header */
+#define IPT_ECN_OP_SET_CWR	0x20	/* set CWR bit of TCP header */
+
+#define IPT_ECN_OP_MASK		0xce
+
+struct ipt_ECN_info {
+	__u8 operation;	/* bitset of operations */
+	__u8 ip_ect;	/* ECT codepoint of IPv4 header, pre-shifted */
+	union {
+		struct {
+			__u8 ece:1, cwr:1; /* TCP ECT bits */
+		} tcp;
+	} proto;
+};
+
 #endif /* _XT_DSCP_H */
This adds xt_RATEEST.h to xt_rateest.h
index 52a37bdc1..26a6e2cf6 100644
--- a/include/uapi/linux/netfilter/xt_rateest.h
+++ b/include/uapi/linux/netfilter/xt_rateest.h
@@ -36,4 +36,12 @@ struct xt_rateest_match_info {
 	struct xt_rateest	*est2 __attribute__((aligned(8)));
 };
 
+struct xt_rateest_target_info {
+       char                    name[IFNAMSIZ];
+       __s8                    interval;
+       __u8            ewma_log;
+       /* Used internally by the kernel */
+       struct xt_rateest       *est __attribute__((aligned(8)));
+};
+
 #endif /* _XT_RATEEST_MATCH_H */
xt_TCPMSS.h does not strictly include xt_tcpmss.h, but add the types there as an ugly hack
index 2268f58b4..ebc445301 100644
--- a/include/uapi/linux/netfilter/xt_tcpmss.h
+++ b/include/uapi/linux/netfilter/xt_tcpmss.h
@@ -9,4 +9,10 @@ struct xt_tcpmss_match_info {
     __u8 invert;
 };
 
+struct xt_tcpmss_info {
+       __u16 mss;
+};
+
+#define XT_TCPMSS_CLAMP_PMTU 0xffff
+
 #endif /*_XT_TCPMSS_MATCH_H*/
Rename XT_TARGET_foo files (add "t_") so they are not the same as XT_MATCH_foo
diff --git a/net/netfilter/Makefile b/net/netfilter/Makefile
index 6bfc250e4..680e8f4a3 100644
--- a/net/netfilter/Makefile
+++ b/net/netfilter/Makefile
@@ -167,20 +167,20 @@ obj-$(CONFIG_NETFILTER_XT_TARGET_CHECKSUM) += xt_CHECKSUM.o
 obj-$(CONFIG_NETFILTER_XT_TARGET_CLASSIFY) += xt_CLASSIFY.o
 obj-$(CONFIG_NETFILTER_XT_TARGET_CONNSECMARK) += xt_CONNSECMARK.o
 obj-$(CONFIG_NETFILTER_XT_TARGET_CT) += xt_CT.o
-obj-$(CONFIG_NETFILTER_XT_TARGET_DSCP) += xt_DSCP.o
-obj-$(CONFIG_NETFILTER_XT_TARGET_HL) += xt_HL.o
+obj-$(CONFIG_NETFILTER_XT_TARGET_DSCP) += xt_t_dscp.o
+obj-$(CONFIG_NETFILTER_XT_TARGET_HL) += xt_t_hl.o
 obj-$(CONFIG_NETFILTER_XT_TARGET_HMARK) += xt_HMARK.o
 obj-$(CONFIG_NETFILTER_XT_TARGET_LED) += xt_LED.o
 obj-$(CONFIG_NETFILTER_XT_TARGET_LOG) += xt_LOG.o
 obj-$(CONFIG_NETFILTER_XT_TARGET_NETMAP) += xt_NETMAP.o
 obj-$(CONFIG_NETFILTER_XT_TARGET_NFLOG) += xt_NFLOG.o
 obj-$(CONFIG_NETFILTER_XT_TARGET_NFQUEUE) += xt_NFQUEUE.o
-obj-$(CONFIG_NETFILTER_XT_TARGET_RATEEST) += xt_RATEEST.o
+obj-$(CONFIG_NETFILTER_XT_TARGET_RATEEST) += xt_t_rateest.o
 obj-$(CONFIG_NETFILTER_XT_TARGET_REDIRECT) += xt_REDIRECT.o
 obj-$(CONFIG_NETFILTER_XT_TARGET_MASQUERADE) += xt_MASQUERADE.o
 obj-$(CONFIG_NETFILTER_XT_TARGET_SECMARK) += xt_SECMARK.o
 obj-$(CONFIG_NETFILTER_XT_TARGET_TPROXY) += xt_TPROXY.o
-obj-$(CONFIG_NETFILTER_XT_TARGET_TCPMSS) += xt_TCPMSS.o
+obj-$(CONFIG_NETFILTER_XT_TARGET_TCPMSS) += xt_t_tcpmss.o
 obj-$(CONFIG_NETFILTER_XT_TARGET_TCPOPTSTRIP) += xt_TCPOPTSTRIP.o
 obj-$(CONFIG_NETFILTER_XT_TARGET_TEE) += xt_TEE.o
 obj-$(CONFIG_NETFILTER_XT_TARGET_TRACE) += xt_TRACE.o
This adds ipt_TTL.h to ipt_ttl.h
index ad0226a86..2c07957c0 100644
--- a/include/uapi/linux/netfilter_ipv4/ipt_ttl.h
+++ b/include/uapi/linux/netfilter_ipv4/ipt_ttl.h
@@ -20,5 +20,17 @@ struct ipt_ttl_info {
 	__u8	ttl;
 };
 
+enum {
+	IPT_TTL_SET = 0,
+	IPT_TTL_INC,
+	IPT_TTL_DEC
+};
+
+#define IPT_TTL_MAXMODE	IPT_TTL_DEC
+
+struct ipt_TTL_info {
+	__u8	mode;
+	__u8	ttl;
+};
 
 #endif
This adds ip6t_HL.h to ip6t_hl.h
index 6b62f9418..00ab5c812 100644
--- a/include/uapi/linux/netfilter_ipv6/ip6t_hl.h
+++ b/include/uapi/linux/netfilter_ipv6/ip6t_hl.h
@@ -21,5 +21,18 @@ struct ip6t_hl_info {
 	__u8	hop_limit;
 };
 
+enum {
+	IP6T_HL_SET = 0,
+	IP6T_HL_INC,
+	IP6T_HL_DEC
+};
+
+#define IP6T_HL_MAXMODE	IP6T_HL_DEC
+
+struct ip6t_HL_info {
+	__u8	mode;
+	__u8	hop_limit;
+};
+
 
 #endif
Fixes for brew install libelf, see https://seiya.me/blog/building-linux-on-macos-natively
new file mode 100644
index 000000000..c8a9ab33a
--- /dev/null
+++ b/scripts/macos-include/elf.h
@@ -0,0 +1,26 @@
+// scripts/macos-include/elf.h
+#pragma once
+#include <libelf/gelf.h>
+ 
+#define STT_SPARC_REGISTER 3
+#define R_386_32 1
+#define R_386_PC32 2
+#define R_MIPS_HI16 5
+#define R_MIPS_LO16 6
+#define R_MIPS_26 4
+#define R_MIPS_32 2
+#define R_ARM_ABS32 2
+#define R_ARM_REL32 3
+#define R_ARM_PC24 1
+#define R_ARM_CALL 28
+#define R_ARM_JUMP24 29
+#define R_ARM_THM_JUMP24 30
+#define R_ARM_THM_PC22 10
+#define R_ARM_MOVW_ABS_NC 43
+#define R_ARM_MOVT_ABS 44
+#define R_ARM_THM_MOVW_ABS_NC 47
+#define R_ARM_THM_MOVT_ABS 48
+#define R_ARM_THM_JUMP19 51
+#define R_AARCH64_ABS64 257
+#define R_AARCH64_PREL64 260
+#define EM_AARCH64 183
diff --git a/scripts/macos-include/byteswap.h b/scripts/macos-include/byteswap.h
new file mode 100644
index 000000000..fd97ed5e1
--- /dev/null
+++ b/scripts/macos-include/byteswap.h
@@ -0,0 +1,4 @@
+#pragma once
+#define bswap_16 __builtin_bswap16
+#define bswap_32 __builtin_bswap32
+#define bswap_64 __builtin_bswap64
diff --git a/scripts/macos-include/elf.h b/scripts/macos-include/elf.h
diff --git a/scripts/mod/file2alias.c b/scripts/mod/file2alias.c
index 4e99393a3..98aee9a4d 100644
--- a/scripts/mod/file2alias.c
+++ b/scripts/mod/file2alias.c
@@ -16,7 +16,10 @@
 #include "list.h"
 #include "xalloc.h"
 
+#define _UUID_T
+#define uuid_t int
 #include "modpost.h"
+#undef uuid_t
 #include "devicetable-offsets.h"
 
 /* We use the ELF typedefs for kernel_ulong_t but bite the bullet and
index b7296edc6..2108485d2 100644
--- a/usr/gen_init_cpio.c
+++ b/usr/gen_init_cpio.c
@@ -355,6 +355,41 @@ static int cpio_mkfile_csum(int fd, unsigned long size, uint32_t *csum)
 	return 0;
 }
 
+#if defined(__APPLE__)
+static int macos_copy_file_range(int fd_in, int fd_out, size_t size)
+{
+	/* This is not a copy_file_range implementation, more like a */
+	/* very basic copy */
+	if (lseek(fd_in, 0, SEEK_SET) < 0) {
+		fprintf(stderr, "macos_copy: seek(0) failed: %d", errno);
+		return -1;
+	}
+
+	size_t ofs = 0;
+	while (size) {
+		unsigned char filebuf[65536];
+		ssize_t this_read;
+		size_t this_size = MIN(size, sizeof(filebuf));
+
+		this_read = read(fd_in, filebuf, this_size);
+		if (this_read <= 0 || this_read > this_size) {
+			fprintf(stderr, "macos_copy: read at %zu: %d", ofs, errno);
+			return -1;
+		}
+
+		if (write(fd_out, filebuf, this_size) < this_read) {
+			fprintf(stderr, "macos_copy: write at %zu: %d", ofs, errno);
+			return -1;
+		}
+
+		size -= this_read;
+		ofs += this_read;
+	}
+	exit(1);
+	return 0;
+}
+#endif
+
 static int cpio_mkfile(const char *name, const char *location,
 			unsigned int mode, uid_t uid, gid_t gid,
 			unsigned int nlinks)
@@ -457,7 +492,12 @@ static int cpio_mkfile(const char *name, const char *location,
 			goto error;
 
 		if (size) {
-			this_read = copy_file_range(file, NULL, outfd, NULL, size, 0);
+			this_read = 
+#if defined(__APPLE__)
+				macos_copy_file_range(file, outfd, size);
+#else
+				copy_file_range(file, NULL, outfd, NULL, size, 0);
+#endif
 			if (this_read > 0) {
 				if (this_read > size)
 					goto error;
@@ -674,7 +714,11 @@ int main (int argc, char *argv[])
 			break;
 		case 'o':
 			outfd = open(optarg,
-				     O_WRONLY | O_CREAT | O_LARGEFILE | O_TRUNC,
+				     O_WRONLY | O_CREAT |
+#ifdef O_LARGEFILE
+                                     O_LARGEFILE |
+#endif
+                                     O_TRUNC,
 				     0600);
 			if (outfd < 0) {
 				fprintf(stderr, "failed to open %s\n", optarg);
EOF
  git add include/uapi/linux/netfilter/{xt_connmark.h,xt_dscp.h,xt_mark.h,xt_rateest.h,xt_tcpmss.h}
  git add include/uapi/linux/netfilter_ipv6/{ipt_ttl.h,ip6t_hl.h} scripts

  git checkout HEAD net/netfilter/xt_DSCP.c
  git mv net/netfilter/{xt_DSCP.c,xt_t_dscp.c}
  git checkout HEAD net/netfilter/{xt_HL.c,xt_dscp.c}
  git mv net/netfilter/{xt_HL.c,xt_t_hl.c}
  git checkout HEAD net/netfilter/{xt_RATEEST.c,xt_hl.c}
  git mv net/netfilter/{xt_RATEEST.c,xt_t_rateest.c}
  git checkout HEAD net/netfilter/{xt_TCPMSS.c,xt_rateest.c}
  git mv net/netfilter/{xt_TCPMSS.c,xt_t_tcpmss.c}
  git checkout HEAD net/netfilter/xt_tcpmss.c

  # the diff is "L"/"l" in poonceLock
  git rm -f tools/memory-model/litmus-tests/Z6.0+pooncelock+poonceLock+pombonce.litmus
  git rm tools/memory-model/litmus-tests/Z6.0+pooncelock+pooncelock+pombonce.litmus

  git commit -m "Case insens fix"
fi

if [ ! -d asahi-alarm ]; then
  git clone --depth=1 https://github.com/asahi-alarm/PKGBUILDs -b main asahi-alarm
fi

cp ../../linux-asahi/config linux/.config

(
  cd linux
  export PATH="$(brew --prefix gnu-sed)/libexec/gnubin:$(brew --prefix llvm)/bin:$(brew --prefix lld)/bin:$PATH"
  gmake LLVM=1 \
     HOSTCFLAGS="-Iscripts/macos-include -I $(brew --prefix libelf)/include" \
     -j$J olddefconfig

  if false; then
    gmake LLVM=1 \
       HOSTCFLAGS="-Iscripts/macos-include -I $(brew --prefix libelf)/include" \
       -j$J Image
  fi
)
