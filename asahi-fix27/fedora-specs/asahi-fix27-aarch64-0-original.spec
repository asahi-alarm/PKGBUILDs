Name:           asahi-fix27
Version:        0.1.0
Release:        %autorelease
Summary:        Fix macOS 27 bootability flag from linux side

# The Cargo metadata has no license field, which is relatively harmless for a
# non-crate project, but we have filed
#   Add `package.license` to `Cargo.toml`
#   https://github.com/AsahiLinux/asahi-fix27/pull/2
# to suggest adding one. The LICENSE file has standard GPLv2 text. There is no
# copyright notice as recommended in
# https://www.gnu.org/licenses/gpl-howto.html, but src/main.rs has:
#   // SPDX-License-Identifier: GPL-2.0-only
# and since this is the only nontrivial file in the project, it’s clear that
# this (and not GPL-2.0-or-later) is the intended overall license.
SourceLicense:  GPL-2.0-only
# Rust dependency licenses, from %%{cargo_licens_summary}:
#
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
License:        %{shrink:
    GPL-2.0-only AND
    MIT AND
    (Apache-2.0 OR MIT)
}
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/AsahiLinux/asahi-fix27
Source0:        %{url}/archive/%{version}/asahi-fix27-%{version}.tar.gz
# Add a simple hand-written man page
# https://github.com/AsahiLinux/asahi-fix27/pull/1
Source1:        asahi-fix27.1

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cargo-rpm-macros

%description
%{summary}.


%prep
%autosetup -p1
%cargo_prep


%generate_buildrequires
%cargo_generate_buildrequires -t


%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies


%install
install -D --preserve-timestamps --mode=0755 \
    --target='%{buildroot}%{_bindir}' target/rpm/asahi-fix27
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_mandir}/man1' '%{SOURCE1}'


%check
%cargo_test


%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/asahi-fix27
%{_mandir}/man1/asahi-fix27.1*


%changelog
%autochangelog
