# AsahiLinux-PKGBUILD

This repository holds PKGBUILD files for the AsahiLinux Arch Linux Arm
distribution. This will hold packages which are required to run Arch
Linux Arm on Apple Silicon based computers, starting with patched Linux
Kernel builds with hardware support.

## Hints

### Inspect how Fedora Asahi Remix builds their packages

To do this we can inspect their spec files:

```sh
# rpm-tools are required
sudo pacman -S rpm-tools

# For example, to get the Asahi Fedora 41 spec (you should of course use the latest Fedora Asahi one)
curl -O https://copr-dist-git.fedorainfracloud.org/cgit/@asahi/mesa/mesa.git/plain/mesa.spec?h=f41

# Usually you want the spec file for aarch64
rpmspec --target=aarch64 -D'autorelease 1' -D'changelog changelog' --parse mesa.spec | cat -s > mesa.spec.aarch64
# For the mesa x86_64 overlay you should also run:
rpmspec --target=x86_64 -D'autorelease 1' -D'changelog changelog' --parse mesa.spec | cat -s > mesa.spec.x86_64
# Same for mesa i386 overlay
rpmspec --target=i386 -D'autorelease 1' -D'changelog changelog' --parse mesa.spec | cat -s  > mesa.spec.i386
```

As you can see, you can override placeholders in the spec files via the `-D` flag.
Usually following placeholders are interesting (extracted from the mesa spec):

```
_arch
_isa
_datadir
_includedir
_libdir
_sysconfdir
```

Most of them should be set by correctly by `--target` anyway, but we may want to override specific ones if needed.

I recommend to `grep` a spec file to see if you could override others (here only looking for ones that start with underscore `%{_`):

```
grep '\%{_' file.spec
```

To make things easy we set up a `update-spec-files.sh` script in this repo which fetches and renders spec files of Fedora packages and saves them in a `fedora-specs` folder of a package in this repo.
