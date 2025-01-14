#!/usr/bin/env bash

# FYI:
# This script requires the Arch Linux "rpm-tools" package.
#
# You can find rpm macros here (not sure if there are more somewhere else however):
# /usr/lib/rpm/macros
# /usr/lib/rpm/platform/*/macros
# ---
# Actually you can also run `rpmspec --showrc`

#TODO: set -o pipefail and/or similiar?

FEDORA_VERSION=41
SPEC_COPR_CGIT_URL=https://copr-dist-git.fedorainfracloud.org/cgit/@asahi/
SPEC_FEDORA_SRC_URL=https://src.fedoraproject.org/

echo ""
echo "Fetching files for Fedora Asahi Remix version $FEDORA_VERSION"
echo ""
echo "!!!"
echo "YOU NEED TO ADJUST THE \$FEDORA_VERSION VARIABLE IN THIS SCRIPT WHEN ASAHI REMIX SWITCHES TO A NEW FEDORA RELEASE!"
echo "!!!"
echo ""
echo "Starting in 3 seconds..."
sleep 3
echo ""

SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

declare -A PACKAGES=(
    #---
    #[<asahi-alarm-package>]="<[copr|fsrc]+spec-git-repo>,<file.spec>[|aarch64,x86_64,i386,...]}"
    #---
    #["alsa-ucm-conf-asahi"]=""
    #["asahi-alarm-keyring"]="<has no upstream repo>"
    #["asahi-audio"]=""
    #["asahi-bless"]=""
    #["asahi-calamares-configs"]=""
    #["asahi-configs"]=""
    #["asahi-desktop-meta"]=""
    #["asahi-fwextract"]=""
    #["asahi-meta"]=""
    #["asahi-scripts"]=""
    #["bankstown"]=""
    #["calamares"]=""
    ["FEX-Emu"]="fsrc+rpms/fex-emu,fex-emu.spec|aarch64"
    #["libkrun"]=""
    #["libkrunfw"]=""
    #["linux-asahi"]=""
    #["lsp-plugins"]=""
    #["lzfse"]=""
    #["m1n1"]=""
    ["mesa-asahi"]="copr+mesa/mesa.git,mesa.spec|aarch64,x86_64,i386"
    ["muvm"]="fsrc+rpms/rust-muvm,rust-muvm.spec|aarch64"
    #["speakersafetyd"]=""
    #["steam"]=""
    #["tiny-dfr"]=""
    #["uboot-asahi"]=""
    #["virglrenderer-asahi"]=""
    #["vulkan-tools"]=""
    #["widevine"]=""
    #["xkeyboard-config-asahi"]=""
    ["fex-emu-rootfs-arch"]="fsrc+rpms/fex-emu-rootfs-fedora,fex-emu-rootfs-fedora.spec|aarch64"
)

echo "Working... Be patient, I also have to download stuff..."

for ASAHI_PACKAGE in "${!PACKAGES[@]}"; do

    TARGET_FOLDER=${SCRIPTPATH}/${ASAHI_PACKAGE}/fedora-specs

    # First we create the package folder and it's sub-folder if it does not exist.
    # This way we can also add new packages with this script.
    mkdir -p "${TARGET_FOLDER}"

    MAP_VALUE=${PACKAGES[$ASAHI_PACKAGE]}
    FEDORA_GIT_REPO=${MAP_VALUE%%,*}
    SPEC_FILE_FULL=${MAP_VALUE#*,}
    SPEC_FILE=${SPEC_FILE_FULL%%|*}
    SPEC_ARCHS_STR=${SPEC_FILE_FULL#*|}
    IFS=',' read -r -a SPEC_ARCHS <<< "$SPEC_ARCHS_STR"

    echo ""
    for SPEC_ARCH in "${SPEC_ARCHS[@]}"; do
        SPEC_FILE_BASE="${TARGET_FOLDER}/${SPEC_FILE%.*}-${SPEC_ARCH}"
        SPEC_FILE_DEST_TMPL="${SPEC_FILE_BASE}-0-original.${SPEC_FILE##*.}"
        SPEC_FILE_DEST_FEDORA="${SPEC_FILE_BASE}-1-fedora.${SPEC_FILE##*.}"
        SPEC_FILE_DEST_ALARM="${SPEC_FILE_BASE}-2-alarm.${SPEC_FILE##*.}"

        ARCH_LIB=lib
        if [ "$SPEC_ARCH" == "i386" ]; then
            ARCH_LIB=lib32
        fi
        ARCH_LIB_DIR="/usr/$ARCH_LIB"

        if [[ "$FEDORA_GIT_REPO" == copr+* ]]; then
           FINAL_SPEC_URL="${SPEC_COPR_CGIT_URL}${FEDORA_GIT_REPO:5}/plain/${SPEC_FILE}?h=f${FEDORA_VERSION}"
        elif [[ "$FEDORA_GIT_REPO" == fsrc+* ]]; then
           FINAL_SPEC_URL="${SPEC_FEDORA_SRC_URL}${FEDORA_GIT_REPO:5}/raw/f${FEDORA_VERSION}/f/${SPEC_FILE}"
        else
          echo "Error: Not a correct git repo: ${FEDORA_GIT_REPO}"
          exit 1
        fi

        echo "Processing ${FINAL_SPEC_URL} for ${SPEC_ARCH} (+ removing changelog)..."

        curl -s -o "${SPEC_FILE_DEST_TMPL}" "${FINAL_SPEC_URL}"

        cp "${SPEC_FILE_DEST_TMPL}" "${SPEC_FILE_DEST_TMPL}.tmp"

        # Assuming the changelog always is at the end of the file, we remove everything from the line "%[auto]changelog" until eof
        # IMHO we do not need the changelog in the rendered file again, it's also easier to later diff the -fedora.spec and -alarm.spec file
        sed -i '/^%autochangelog$/,$d' "${SPEC_FILE_DEST_TMPL}.tmp"
        sed -i '/^%changelog$/,$d' "${SPEC_FILE_DEST_TMPL}.tmp"

        # Assuming all our sources/attachments are in the base folder,
        # it does not make sense to render copy commands that try to copy from base to base folder
        sed -i -E 's/^cp (.*)%SOURCE(.+) \.$//g' "${SPEC_FILE_DEST_TMPL}.tmp"

        # We force with_asahi_minimal, no matter which architecture we are on. This also will set "with_asahi 1".
        # BTW: It seems Fedora devs build the asahi mesa packages with `-D"with_asahi_minimal 0" -D"with_asahi 1"`,
        #      which just adds more gallium and vulkan drivers. I could reproduce that 1:1. We do not need those driver however,
        #      so it's totally fine to just use `-D"with_asahi_minimal 1"`.
        # FYI: -D"with_<option> 1" could also be written as --with=<option> (not sure how to set a value other than 1 though)
        rpmspec --target=${SPEC_ARCH} \
          -D"with_asahi_minimal 1" -D"fedora ${FEDORA_VERSION}" -D"rhel 0" \
          -D"_topdir ${SCRIPTPATH}/${ASAHI_PACKAGE}/" -D"_sourcedir ${SCRIPTPATH}/${ASAHI_PACKAGE}/" \
          -D"_builddir ${SCRIPTPATH}/${ASAHI_PACKAGE}/pkg/" -D"_sbindir /usr/bin" -D"_libexecdir /usr/lib/${ASAHI_PACKAGE}" \
          -D"_lib ${ARCH_LIB}" -D"_libdir ${ARCH_LIB_DIR}" -D"_metainfodir /usr/share/metainfo" \
          -D"__patch patch"  -D"__chmod chmod" -D"__strip strip" -D"__rpmuncompress rpmuncompress" -D"__mkdir mkdir" -D"__install install" \
          -D"autorelease 1" -D"changelog changelog_unused" \
          --parse "${SPEC_FILE_DEST_TMPL}.tmp" > "${SPEC_FILE_DEST_FEDORA}"

        rm ${SPEC_FILE_DEST_TMPL}.tmp

        #######################
        # Start doing cleanup #
        #######################

        # Replace lines that contain only changelog_unused with an empty line
        sed -i "s/^changelog_unused$//g" "${SPEC_FILE_DEST_FEDORA}"

        # //usr -> /usr
        sed -i "s/\/\/usr/\/usr/g" "${SPEC_FILE_DEST_FEDORA}"
        # //etc -> /etc
        sed -i "s/\/\/etc/\/etc/g" "${SPEC_FILE_DEST_FEDORA}"
        # Unfortunately absolute paths are used, but we would have to adjust paths anyway. Make them relative.
        # (The pkg one I introduced is a bit of a special one)
        # ATTENTION: DO NOT CHANGE THE ORDER OF THE NEXT LINES!
        sed -i "s/${SCRIPTPATH//\//\\/}\/${ASAHI_PACKAGE//\//\\/}\/pkg\/.*\/BUILDROOT/fakeinstall/g" "${SPEC_FILE_DEST_FEDORA}"
        sed -i "s/${SCRIPTPATH//\//\\/}\/${ASAHI_PACKAGE//\//\\/}\/pkg\/.*\-build/.\//g" "${SPEC_FILE_DEST_FEDORA}"
        sed -i "s/${SCRIPTPATH//\//\\/}\/${ASAHI_PACKAGE//\//\\/}\///g" "${SPEC_FILE_DEST_FEDORA}"

        # Replace lines that only contain spaces (or any type of whitespace) with an empty line
        sed -i 's/^[[:space:]]*$//' "${SPEC_FILE_DEST_FEDORA}"
        # Finally suppress repeated empty lines (= the same as `cat -s `)
        sed -i '/^$/N;/^\n$/D' "${SPEC_FILE_DEST_FEDORA}"

        ################################################################################################
        # Now we convert the rendered Fedora spec file to Alarm's PKGBUILD format as good as we can ;) #
        ################################################################################################

        cp "${SPEC_FILE_DEST_FEDORA}" "${SPEC_FILE_DEST_ALARM}.tmp"

        # This is a little bit magic now, thanks to ai.
        # This rearranges the file so that %files sections come at the end (in their original order),
        # followed by %check sections (also in their original order), while leaving all other sections unchanged.
        awk '
            /^%files/ { in_files = 1; in_check = 0; files_block = files_block $0 ORS; next }
            /^%check/ { in_files = 0; in_check = 1; check_block = check_block $0 ORS; next }
            in_files {
                if (/^%(files|prep|build|install|package)/) {
                    in_files = 0;
                } else {
                    files_block = files_block $0 ORS;
                    next;
                }
            }
            in_check {
                if (/^%(check|prep|build|install|package)/) {
                    in_check = 0;
                } else {
                    check_block = check_block $0 ORS;
                    next;
                }
            }
            { print $0 }
            END { printf "%s%s", files_block, check_block }
        ' "${SPEC_FILE_DEST_ALARM}.tmp" > "${SPEC_FILE_DEST_ALARM}"

        rm "${SPEC_FILE_DEST_ALARM}.tmp"

        # Replace line %meson_install and %meson_build with empty strings
        sed -i "s/^%meson_install$//g" "${SPEC_FILE_DEST_ALARM}"
        sed -i "s/^%meson_build$//g" "${SPEC_FILE_DEST_ALARM}"

        # Now we replace rpmuncompress with commands that fit better for a PKGBUILD
        # -x will become a tar -xf command
        sed -i "s/rpmuncompress -x/tar -xf/g" "${SPEC_FILE_DEST_ALARM}"
        # For now we assume that rpmuncompress not follows by " -" will just uncompress ascii files
        # We might need to enhance this hack later in case it will uncompress an archive in a spec file
        sed -i -E 's/rpmuncompress( [^-][^ ]*)/cat\1/g' "${SPEC_FILE_DEST_ALARM}"

        # We do not use a docs/ subfolder, so we do not need to cp file into it
        # This command only runs between the lines "%prep" and "%build", so only in the prepare section
        sed -i -E '/^%prep$/,/^%build$/ s/^cp (.+) docs\/$//g' "${SPEC_FILE_DEST_ALARM}"

        # From here on "0,/^%files/{//!b}; " in sed makes sure that we only modify lines that come after the first "%files..." line

        # "%dir " at the beginning of a line
        sed -i "0,/^%files/{//!b}; s/^%dir /install -m755 -d \${pkgdir}/g" "${SPEC_FILE_DEST_ALARM}"
        # "%doc docs/" at the beginning of a line
        sed -i "0,/^%files/{//!b}; s/^%doc docs\//install -Dpm0755 -t \${pkgdir}\/usr\/share\/doc\/${ASAHI_PACKAGE}\/ /g" "${SPEC_FILE_DEST_ALARM}"
        # "%doc " at the beginning of a line
        sed -i "0,/^%files/{//!b}; s/^%doc/install -Dpm0755 -t \${pkgdir}\/usr\/share\/doc\/${ASAHI_PACKAGE}\/ /g" "${SPEC_FILE_DEST_ALARM}"
        # "%license "at the beginning of a file
        sed -i "0,/^%files/{//!b}; s/^%license /install -Dpm0755 -t \${pkgdir}\/usr\/share\/licenses\/${ASAHI_PACKAGE}\/ /g" "${SPEC_FILE_DEST_ALARM}"
        # "/" at the beginning of a line - like /usr /etc, etc. will become "_install /..."
        sed -i '0,/^%files/{//!b}; s/^\//_install fakeinstall\//g' "${SPEC_FILE_DEST_ALARM}"

        ################################################################################################
        # Here you can implement package specific quirks                                               #
        ################################################################################################

        if [ "$ASAHI_PACKAGE" == "mesa-asahi" ]; then
          if [ "$SPEC_ARCH" != "aarch64" ]; then
            # /usr/lib[32] -> /usr/$LIBDIR
            # ATTENTION: DO NOT CHANGE THE ORDER OF THE NEXT LINES!
            sed -i "0,/^%install$/{//!b}; s/\/usr\/lib32/\/usr\/\$LIBDIR/g" "${SPEC_FILE_DEST_ALARM}"
            sed -i "0,/^%install$/{//!b}; s/\/usr\/lib/\/usr\/\$LIBDIR/g" "${SPEC_FILE_DEST_ALARM}"
          fi
        fi
        #if [ "$ASAHI_PACKAGE" == "<some-other-asahi-package-name>" ]; then
        #fi

        ################################################################################################
        # ATTENTION: This commands have to come last!                                                  #
        ################################################################################################

        # "%files " at the beginning of a line become a comment
        # From now on you can not have sed commands anymore that rely on "%files"
        sed -i "s/^%files /# /g" "${SPEC_FILE_DEST_ALARM}"
        sed -i "s/^%files$/# A spec %files section (it could be that part of the next lines duplicate part of the package() function)/g" "${SPEC_FILE_DEST_ALARM}"

        # Indent all non-empty lines with two spaces, for easier copy/pasting to PKGBULD ;)
        sed -i '/^[[:space:]]*[^[:space:]]/s/^/  /' "${SPEC_FILE_DEST_ALARM}"

        # Replace spec files' %prep, %build, %install and %check with PKGBUILD's prepare(), build(), package() and check() functions
        sed -i "s/^  %prep$/prepare\(\) {/g" "${SPEC_FILE_DEST_ALARM}"
        sed -i "s/^  %build$/}\n\nbuild() {/g" "${SPEC_FILE_DEST_ALARM}"
        sed -i "s/^  %install$/}\n\npackage() {/g" "${SPEC_FILE_DEST_ALARM}"
        sed -i "s/^  %check$/}\n\ncheck() {/g" "${SPEC_FILE_DEST_ALARM}"
        # Remove all empty lines at end of the file
        sed -i ':a;/^\s*$/{$d;N;};/\S/!ba' "${SPEC_FILE_DEST_ALARM}"
        # Add closing curly bracket at the end of the file to close the last function
        echo "}" >> "${SPEC_FILE_DEST_ALARM}"

        # Replace lines that only contain spaces (or any type of whitespace) with an empty line
        sed -i 's/^[[:space:]]*$//' "${SPEC_FILE_DEST_ALARM}"
        # Finally suppress repeated empty lines (= the same as `cat -s `)
        sed -i '/^$/N;/^\n$/D' "${SPEC_FILE_DEST_ALARM}"
    done
done

echo ""
echo "Done!"
echo ""
echo "To see what changed just run something like:"
echo "    git status"
echo "    git diff"
echo "    git difftool"
echo ""
