#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : shared-mime-info
Version  : 1.8
Release  : 8
URL      : http://freedesktop.org/~hadess/shared-mime-info-1.8.tar.xz
Source0  : http://freedesktop.org/~hadess/shared-mime-info-1.8.tar.xz
Summary  : Freedesktop common MIME database
Group    : Development/Tools
License  : GPL-2.0
Requires: shared-mime-info-bin
Requires: shared-mime-info-locales
Requires: shared-mime-info-doc
Requires: shared-mime-info-data
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(libxml-2.0)

%description
This package contains:
- The freedesktop.org shared MIME database spec.
- The merged GNOME and KDE databases, in the new format.
- The update-mime-database command, used to install new MIME data.

%package bin
Summary: bin components for the shared-mime-info package.
Group: Binaries
Requires: shared-mime-info-data

%description bin
bin components for the shared-mime-info package.


%package data
Summary: data components for the shared-mime-info package.
Group: Data

%description data
data components for the shared-mime-info package.


%package dev
Summary: dev components for the shared-mime-info package.
Group: Development
Requires: shared-mime-info-bin
Requires: shared-mime-info-data
Provides: shared-mime-info-devel

%description dev
dev components for the shared-mime-info package.


%package doc
Summary: doc components for the shared-mime-info package.
Group: Documentation

%description doc
doc components for the shared-mime-info package.


%package locales
Summary: locales components for the shared-mime-info package.
Group: Default

%description locales
locales components for the shared-mime-info package.


%prep
%setup -q -n shared-mime-info-1.8

%build
export LANG=C
export SOURCE_DATE_EPOCH=1488387436
%configure --disable-static
make V=1

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 check

%install
export SOURCE_DATE_EPOCH=1488387436
rm -rf %{buildroot}
%make_install
%find_lang shared-mime-info

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/update-mime-database

%files data
%defattr(-,root,root,-)
/usr/share/mime/XMLnamespaces
/usr/share/mime/aliases
/usr/share/mime/application/andrew-inset.xml
/usr/share/mime/application/annodex.xml
/usr/share/mime/application/atom+xml.xml
/usr/share/mime/application/dicom.xml
/usr/share/mime/application/ecmascript.xml
/usr/share/mime/application/epub+zip.xml
/usr/share/mime/application/font-woff.xml
/usr/share/mime/application/geo+json.xml
/usr/share/mime/application/gml+xml.xml
/usr/share/mime/application/gnunet-directory.xml
/usr/share/mime/application/gpx+xml.xml
/usr/share/mime/application/gzip.xml
/usr/share/mime/application/illustrator.xml
/usr/share/mime/application/javascript.xml
/usr/share/mime/application/jrd+json.xml
/usr/share/mime/application/json-patch+json.xml
/usr/share/mime/application/json.xml
/usr/share/mime/application/ld+json.xml
/usr/share/mime/application/mac-binhex40.xml
/usr/share/mime/application/mathematica.xml
/usr/share/mime/application/mathml+xml.xml
/usr/share/mime/application/mbox.xml
/usr/share/mime/application/metalink+xml.xml
/usr/share/mime/application/metalink4+xml.xml
/usr/share/mime/application/msword-template.xml
/usr/share/mime/application/msword.xml
/usr/share/mime/application/mxf.xml
/usr/share/mime/application/octet-stream.xml
/usr/share/mime/application/oda.xml
/usr/share/mime/application/ogg.xml
/usr/share/mime/application/owl+xml.xml
/usr/share/mime/application/oxps.xml
/usr/share/mime/application/pdf.xml
/usr/share/mime/application/pgp-encrypted.xml
/usr/share/mime/application/pgp-keys.xml
/usr/share/mime/application/pgp-signature.xml
/usr/share/mime/application/pkcs10.xml
/usr/share/mime/application/pkcs12.xml
/usr/share/mime/application/pkcs7-mime.xml
/usr/share/mime/application/pkcs7-signature.xml
/usr/share/mime/application/pkcs8.xml
/usr/share/mime/application/pkix-cert.xml
/usr/share/mime/application/pkix-crl.xml
/usr/share/mime/application/pkix-pkipath.xml
/usr/share/mime/application/postscript.xml
/usr/share/mime/application/prs.plucker.xml
/usr/share/mime/application/ram.xml
/usr/share/mime/application/raml+yaml.xml
/usr/share/mime/application/rdf+xml.xml
/usr/share/mime/application/relax-ng-compact-syntax.xml
/usr/share/mime/application/rss+xml.xml
/usr/share/mime/application/rtf.xml
/usr/share/mime/application/sdp.xml
/usr/share/mime/application/sieve.xml
/usr/share/mime/application/smil+xml.xml
/usr/share/mime/application/sql.xml
/usr/share/mime/application/vnd.adobe.flash.movie.xml
/usr/share/mime/application/vnd.android.package-archive.xml
/usr/share/mime/application/vnd.apple.mpegurl.xml
/usr/share/mime/application/vnd.chess-pgn.xml
/usr/share/mime/application/vnd.coffeescript.xml
/usr/share/mime/application/vnd.comicbook+zip.xml
/usr/share/mime/application/vnd.corel-draw.xml
/usr/share/mime/application/vnd.debian.binary-package.xml
/usr/share/mime/application/vnd.emusic-emusic_package.xml
/usr/share/mime/application/vnd.flatpak.ref.xml
/usr/share/mime/application/vnd.flatpak.repo.xml
/usr/share/mime/application/vnd.flatpak.xml
/usr/share/mime/application/vnd.framemaker.xml
/usr/share/mime/application/vnd.google-earth.kml+xml.xml
/usr/share/mime/application/vnd.google-earth.kmz.xml
/usr/share/mime/application/vnd.hp-hpgl.xml
/usr/share/mime/application/vnd.hp-pcl.xml
/usr/share/mime/application/vnd.iccprofile.xml
/usr/share/mime/application/vnd.lotus-1-2-3.xml
/usr/share/mime/application/vnd.lotus-wordpro.xml
/usr/share/mime/application/vnd.mozilla.xul+xml.xml
/usr/share/mime/application/vnd.ms-access.xml
/usr/share/mime/application/vnd.ms-asf.xml
/usr/share/mime/application/vnd.ms-cab-compressed.xml
/usr/share/mime/application/vnd.ms-excel.addin.macroenabled.12.xml
/usr/share/mime/application/vnd.ms-excel.sheet.binary.macroenabled.12.xml
/usr/share/mime/application/vnd.ms-excel.sheet.macroenabled.12.xml
/usr/share/mime/application/vnd.ms-excel.template.macroenabled.12.xml
/usr/share/mime/application/vnd.ms-excel.xml
/usr/share/mime/application/vnd.ms-htmlhelp.xml
/usr/share/mime/application/vnd.ms-powerpoint.addin.macroenabled.12.xml
/usr/share/mime/application/vnd.ms-powerpoint.presentation.macroenabled.12.xml
/usr/share/mime/application/vnd.ms-powerpoint.slide.macroenabled.12.xml
/usr/share/mime/application/vnd.ms-powerpoint.slideshow.macroenabled.12.xml
/usr/share/mime/application/vnd.ms-powerpoint.template.macroenabled.12.xml
/usr/share/mime/application/vnd.ms-powerpoint.xml
/usr/share/mime/application/vnd.ms-publisher.xml
/usr/share/mime/application/vnd.ms-tnef.xml
/usr/share/mime/application/vnd.ms-visio.drawing.macroenabled.main+xml.xml
/usr/share/mime/application/vnd.ms-visio.drawing.main+xml.xml
/usr/share/mime/application/vnd.ms-visio.stencil.macroenabled.main+xml.xml
/usr/share/mime/application/vnd.ms-visio.stencil.main+xml.xml
/usr/share/mime/application/vnd.ms-visio.template.macroenabled.main+xml.xml
/usr/share/mime/application/vnd.ms-visio.template.main+xml.xml
/usr/share/mime/application/vnd.ms-word.document.macroenabled.12.xml
/usr/share/mime/application/vnd.ms-word.template.macroenabled.12.xml
/usr/share/mime/application/vnd.ms-works.xml
/usr/share/mime/application/vnd.ms-wpl.xml
/usr/share/mime/application/vnd.nintendo.snes.rom.xml
/usr/share/mime/application/vnd.oasis.opendocument.chart-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.chart.xml
/usr/share/mime/application/vnd.oasis.opendocument.database.xml
/usr/share/mime/application/vnd.oasis.opendocument.formula-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.formula.xml
/usr/share/mime/application/vnd.oasis.opendocument.graphics-flat-xml.xml
/usr/share/mime/application/vnd.oasis.opendocument.graphics-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.graphics.xml
/usr/share/mime/application/vnd.oasis.opendocument.image.xml
/usr/share/mime/application/vnd.oasis.opendocument.presentation-flat-xml.xml
/usr/share/mime/application/vnd.oasis.opendocument.presentation-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.presentation.xml
/usr/share/mime/application/vnd.oasis.opendocument.spreadsheet-flat-xml.xml
/usr/share/mime/application/vnd.oasis.opendocument.spreadsheet-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.spreadsheet.xml
/usr/share/mime/application/vnd.oasis.opendocument.text-flat-xml.xml
/usr/share/mime/application/vnd.oasis.opendocument.text-master.xml
/usr/share/mime/application/vnd.oasis.opendocument.text-template.xml
/usr/share/mime/application/vnd.oasis.opendocument.text-web.xml
/usr/share/mime/application/vnd.oasis.opendocument.text.xml
/usr/share/mime/application/vnd.openofficeorg.extension.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.presentationml.presentation.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.presentationml.slide.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.presentationml.slideshow.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.presentationml.template.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.spreadsheetml.template.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.wordprocessingml.document.xml
/usr/share/mime/application/vnd.openxmlformats-officedocument.wordprocessingml.template.xml
/usr/share/mime/application/vnd.palm.xml
/usr/share/mime/application/vnd.rar.xml
/usr/share/mime/application/vnd.rn-realmedia.xml
/usr/share/mime/application/vnd.snap.xml
/usr/share/mime/application/vnd.squashfs.xml
/usr/share/mime/application/vnd.stardivision.calc.xml
/usr/share/mime/application/vnd.stardivision.chart.xml
/usr/share/mime/application/vnd.stardivision.draw.xml
/usr/share/mime/application/vnd.stardivision.impress.xml
/usr/share/mime/application/vnd.stardivision.mail.xml
/usr/share/mime/application/vnd.stardivision.math.xml
/usr/share/mime/application/vnd.stardivision.writer.xml
/usr/share/mime/application/vnd.sun.xml.calc.template.xml
/usr/share/mime/application/vnd.sun.xml.calc.xml
/usr/share/mime/application/vnd.sun.xml.draw.template.xml
/usr/share/mime/application/vnd.sun.xml.draw.xml
/usr/share/mime/application/vnd.sun.xml.impress.template.xml
/usr/share/mime/application/vnd.sun.xml.impress.xml
/usr/share/mime/application/vnd.sun.xml.math.xml
/usr/share/mime/application/vnd.sun.xml.writer.global.xml
/usr/share/mime/application/vnd.sun.xml.writer.template.xml
/usr/share/mime/application/vnd.sun.xml.writer.xml
/usr/share/mime/application/vnd.symbian.install.xml
/usr/share/mime/application/vnd.tcpdump.pcap.xml
/usr/share/mime/application/vnd.visio.xml
/usr/share/mime/application/vnd.wordperfect.xml
/usr/share/mime/application/winhlp.xml
/usr/share/mime/application/x-7z-compressed.xml
/usr/share/mime/application/x-abiword.xml
/usr/share/mime/application/x-ace.xml
/usr/share/mime/application/x-alz.xml
/usr/share/mime/application/x-amiga-disk-format.xml
/usr/share/mime/application/x-amipro.xml
/usr/share/mime/application/x-aportisdoc.xml
/usr/share/mime/application/x-apple-diskimage.xml
/usr/share/mime/application/x-applix-spreadsheet.xml
/usr/share/mime/application/x-applix-word.xml
/usr/share/mime/application/x-arc.xml
/usr/share/mime/application/x-archive.xml
/usr/share/mime/application/x-arj.xml
/usr/share/mime/application/x-asp.xml
/usr/share/mime/application/x-atari-2600-rom.xml
/usr/share/mime/application/x-atari-7800-rom.xml
/usr/share/mime/application/x-awk.xml
/usr/share/mime/application/x-bcpio.xml
/usr/share/mime/application/x-bittorrent.xml
/usr/share/mime/application/x-blender.xml
/usr/share/mime/application/x-bsdiff.xml
/usr/share/mime/application/x-bzdvi.xml
/usr/share/mime/application/x-bzip-compressed-tar.xml
/usr/share/mime/application/x-bzip.xml
/usr/share/mime/application/x-bzpdf.xml
/usr/share/mime/application/x-bzpostscript.xml
/usr/share/mime/application/x-cb7.xml
/usr/share/mime/application/x-cbr.xml
/usr/share/mime/application/x-cbt.xml
/usr/share/mime/application/x-ccmx.xml
/usr/share/mime/application/x-cd-image.xml
/usr/share/mime/application/x-cdrdao-toc.xml
/usr/share/mime/application/x-cisco-vpn-settings.xml
/usr/share/mime/application/x-class-file.xml
/usr/share/mime/application/x-compress.xml
/usr/share/mime/application/x-compressed-tar.xml
/usr/share/mime/application/x-core.xml
/usr/share/mime/application/x-cpio-compressed.xml
/usr/share/mime/application/x-cpio.xml
/usr/share/mime/application/x-csh.xml
/usr/share/mime/application/x-cue.xml
/usr/share/mime/application/x-dar.xml
/usr/share/mime/application/x-dbf.xml
/usr/share/mime/application/x-dc-rom.xml
/usr/share/mime/application/x-designer.xml
/usr/share/mime/application/x-desktop.xml
/usr/share/mime/application/x-dia-diagram.xml
/usr/share/mime/application/x-dia-shape.xml
/usr/share/mime/application/x-docbook+xml.xml
/usr/share/mime/application/x-doom-wad.xml
/usr/share/mime/application/x-dvi.xml
/usr/share/mime/application/x-e-theme.xml
/usr/share/mime/application/x-egon.xml
/usr/share/mime/application/x-executable.xml
/usr/share/mime/application/x-fictionbook+xml.xml
/usr/share/mime/application/x-fluid.xml
/usr/share/mime/application/x-font-afm.xml
/usr/share/mime/application/x-font-bdf.xml
/usr/share/mime/application/x-font-dos.xml
/usr/share/mime/application/x-font-framemaker.xml
/usr/share/mime/application/x-font-libgrx.xml
/usr/share/mime/application/x-font-linux-psf.xml
/usr/share/mime/application/x-font-otf.xml
/usr/share/mime/application/x-font-pcf.xml
/usr/share/mime/application/x-font-speedo.xml
/usr/share/mime/application/x-font-sunos-news.xml
/usr/share/mime/application/x-font-tex-tfm.xml
/usr/share/mime/application/x-font-tex.xml
/usr/share/mime/application/x-font-ttf.xml
/usr/share/mime/application/x-font-ttx.xml
/usr/share/mime/application/x-font-type1.xml
/usr/share/mime/application/x-font-vfont.xml
/usr/share/mime/application/x-gameboy-color-rom.xml
/usr/share/mime/application/x-gameboy-rom.xml
/usr/share/mime/application/x-gamecube-rom.xml
/usr/share/mime/application/x-gamegear-rom.xml
/usr/share/mime/application/x-gba-rom.xml
/usr/share/mime/application/x-gdbm.xml
/usr/share/mime/application/x-gedcom.xml
/usr/share/mime/application/x-genesis-32x-rom.xml
/usr/share/mime/application/x-genesis-rom.xml
/usr/share/mime/application/x-gettext-translation.xml
/usr/share/mime/application/x-glade.xml
/usr/share/mime/application/x-gnucash.xml
/usr/share/mime/application/x-gnumeric.xml
/usr/share/mime/application/x-gnuplot.xml
/usr/share/mime/application/x-go-sgf.xml
/usr/share/mime/application/x-graphite.xml
/usr/share/mime/application/x-gtk-builder.xml
/usr/share/mime/application/x-gtktalog.xml
/usr/share/mime/application/x-gz-font-linux-psf.xml
/usr/share/mime/application/x-gzdvi.xml
/usr/share/mime/application/x-gzpdf.xml
/usr/share/mime/application/x-gzpostscript.xml
/usr/share/mime/application/x-hdf.xml
/usr/share/mime/application/x-hfe-floppy-image.xml
/usr/share/mime/application/x-hwp.xml
/usr/share/mime/application/x-hwt.xml
/usr/share/mime/application/x-ica.xml
/usr/share/mime/application/x-iff.xml
/usr/share/mime/application/x-ipod-firmware.xml
/usr/share/mime/application/x-ipynb+json.xml
/usr/share/mime/application/x-iso9660-appimage.xml
/usr/share/mime/application/x-it87.xml
/usr/share/mime/application/x-iwork-keynote-sffkey.xml
/usr/share/mime/application/x-java-archive.xml
/usr/share/mime/application/x-java-jce-keystore.xml
/usr/share/mime/application/x-java-jnlp-file.xml
/usr/share/mime/application/x-java-keystore.xml
/usr/share/mime/application/x-java-pack200.xml
/usr/share/mime/application/x-java.xml
/usr/share/mime/application/x-jbuilder-project.xml
/usr/share/mime/application/x-karbon.xml
/usr/share/mime/application/x-kchart.xml
/usr/share/mime/application/x-kexi-connectiondata.xml
/usr/share/mime/application/x-kexiproject-shortcut.xml
/usr/share/mime/application/x-kexiproject-sqlite2.xml
/usr/share/mime/application/x-kexiproject-sqlite3.xml
/usr/share/mime/application/x-kformula.xml
/usr/share/mime/application/x-killustrator.xml
/usr/share/mime/application/x-kivio.xml
/usr/share/mime/application/x-kontour.xml
/usr/share/mime/application/x-kpovmodeler.xml
/usr/share/mime/application/x-kpresenter.xml
/usr/share/mime/application/x-krita.xml
/usr/share/mime/application/x-kspread-crypt.xml
/usr/share/mime/application/x-kspread.xml
/usr/share/mime/application/x-ksysv-package.xml
/usr/share/mime/application/x-kugar.xml
/usr/share/mime/application/x-kword-crypt.xml
/usr/share/mime/application/x-kword.xml
/usr/share/mime/application/x-lha.xml
/usr/share/mime/application/x-lhz.xml
/usr/share/mime/application/x-lrzip-compressed-tar.xml
/usr/share/mime/application/x-lrzip.xml
/usr/share/mime/application/x-lyx.xml
/usr/share/mime/application/x-lz4-compressed-tar.xml
/usr/share/mime/application/x-lz4.xml
/usr/share/mime/application/x-lzip-compressed-tar.xml
/usr/share/mime/application/x-lzip.xml
/usr/share/mime/application/x-lzma-compressed-tar.xml
/usr/share/mime/application/x-lzma.xml
/usr/share/mime/application/x-lzop.xml
/usr/share/mime/application/x-lzpdf.xml
/usr/share/mime/application/x-m4.xml
/usr/share/mime/application/x-macbinary.xml
/usr/share/mime/application/x-magicpoint.xml
/usr/share/mime/application/x-markaby.xml
/usr/share/mime/application/x-matroska.xml
/usr/share/mime/application/x-mif.xml
/usr/share/mime/application/x-mimearchive.xml
/usr/share/mime/application/x-mobipocket-ebook.xml
/usr/share/mime/application/x-mozilla-bookmarks.xml
/usr/share/mime/application/x-ms-dos-executable.xml
/usr/share/mime/application/x-ms-wim.xml
/usr/share/mime/application/x-msi.xml
/usr/share/mime/application/x-mswinurl.xml
/usr/share/mime/application/x-mswrite.xml
/usr/share/mime/application/x-msx-rom.xml
/usr/share/mime/application/x-n64-rom.xml
/usr/share/mime/application/x-nautilus-link.xml
/usr/share/mime/application/x-navi-animation.xml
/usr/share/mime/application/x-neo-geo-pocket-rom.xml
/usr/share/mime/application/x-nes-rom.xml
/usr/share/mime/application/x-netcdf.xml
/usr/share/mime/application/x-netshow-channel.xml
/usr/share/mime/application/x-nintendo-ds-rom.xml
/usr/share/mime/application/x-nzb.xml
/usr/share/mime/application/x-object.xml
/usr/share/mime/application/x-ole-storage.xml
/usr/share/mime/application/x-oleo.xml
/usr/share/mime/application/x-pagemaker.xml
/usr/share/mime/application/x-pak.xml
/usr/share/mime/application/x-par2.xml
/usr/share/mime/application/x-partial-download.xml
/usr/share/mime/application/x-pc-engine-rom.xml
/usr/share/mime/application/x-pef-executable.xml
/usr/share/mime/application/x-perl.xml
/usr/share/mime/application/x-php.xml
/usr/share/mime/application/x-pkcs7-certificates.xml
/usr/share/mime/application/x-planperfect.xml
/usr/share/mime/application/x-pocket-word.xml
/usr/share/mime/application/x-profile.xml
/usr/share/mime/application/x-pw.xml
/usr/share/mime/application/x-python-bytecode.xml
/usr/share/mime/application/x-qpress.xml
/usr/share/mime/application/x-qtiplot.xml
/usr/share/mime/application/x-quattropro.xml
/usr/share/mime/application/x-quicktime-media-link.xml
/usr/share/mime/application/x-qw.xml
/usr/share/mime/application/x-raw-disk-image-xz-compressed.xml
/usr/share/mime/application/x-raw-disk-image.xml
/usr/share/mime/application/x-riff.xml
/usr/share/mime/application/x-rpm.xml
/usr/share/mime/application/x-ruby.xml
/usr/share/mime/application/x-sami.xml
/usr/share/mime/application/x-saturn-rom.xml
/usr/share/mime/application/x-sc.xml
/usr/share/mime/application/x-sega-cd-rom.xml
/usr/share/mime/application/x-sega-pico-rom.xml
/usr/share/mime/application/x-sg1000-rom.xml
/usr/share/mime/application/x-shar.xml
/usr/share/mime/application/x-shared-library-la.xml
/usr/share/mime/application/x-sharedlib.xml
/usr/share/mime/application/x-shellscript.xml
/usr/share/mime/application/x-shorten.xml
/usr/share/mime/application/x-siag.xml
/usr/share/mime/application/x-slp.xml
/usr/share/mime/application/x-smaf.xml
/usr/share/mime/application/x-sms-rom.xml
/usr/share/mime/application/x-source-rpm.xml
/usr/share/mime/application/x-spss-por.xml
/usr/share/mime/application/x-spss-sav.xml
/usr/share/mime/application/x-sqlite2.xml
/usr/share/mime/application/x-sqlite3.xml
/usr/share/mime/application/x-stuffit.xml
/usr/share/mime/application/x-subrip.xml
/usr/share/mime/application/x-sv4cpio.xml
/usr/share/mime/application/x-sv4crc.xml
/usr/share/mime/application/x-t602.xml
/usr/share/mime/application/x-tar.xml
/usr/share/mime/application/x-tarz.xml
/usr/share/mime/application/x-tex-gf.xml
/usr/share/mime/application/x-tex-pk.xml
/usr/share/mime/application/x-tgif.xml
/usr/share/mime/application/x-theme.xml
/usr/share/mime/application/x-thomson-cartridge-memo7.xml
/usr/share/mime/application/x-thomson-cassette.xml
/usr/share/mime/application/x-thomson-sap-image.xml
/usr/share/mime/application/x-toutdoux.xml
/usr/share/mime/application/x-trash.xml
/usr/share/mime/application/x-trig.xml
/usr/share/mime/application/x-troff-man-compressed.xml
/usr/share/mime/application/x-troff-man.xml
/usr/share/mime/application/x-tzo.xml
/usr/share/mime/application/x-ufraw.xml
/usr/share/mime/application/x-ustar.xml
/usr/share/mime/application/x-wais-source.xml
/usr/share/mime/application/x-wii-rom.xml
/usr/share/mime/application/x-wii-wad.xml
/usr/share/mime/application/x-windows-themepack.xml
/usr/share/mime/application/x-wpg.xml
/usr/share/mime/application/x-wwf.xml
/usr/share/mime/application/x-x509-ca-cert.xml
/usr/share/mime/application/x-xar.xml
/usr/share/mime/application/x-xbel.xml
/usr/share/mime/application/x-xliff.xml
/usr/share/mime/application/x-xpinstall.xml
/usr/share/mime/application/x-xz-compressed-tar.xml
/usr/share/mime/application/x-xz.xml
/usr/share/mime/application/x-xzpdf.xml
/usr/share/mime/application/x-yaml.xml
/usr/share/mime/application/x-zerosize.xml
/usr/share/mime/application/x-zip-compressed-fb2.xml
/usr/share/mime/application/x-zoo.xml
/usr/share/mime/application/xhtml+xml.xml
/usr/share/mime/application/xml-dtd.xml
/usr/share/mime/application/xml-external-parsed-entity.xml
/usr/share/mime/application/xml.xml
/usr/share/mime/application/xslt+xml.xml
/usr/share/mime/application/xspf+xml.xml
/usr/share/mime/application/zip.xml
/usr/share/mime/application/zlib.xml
/usr/share/mime/audio/aac.xml
/usr/share/mime/audio/ac3.xml
/usr/share/mime/audio/amr-wb.xml
/usr/share/mime/audio/amr.xml
/usr/share/mime/audio/annodex.xml
/usr/share/mime/audio/basic.xml
/usr/share/mime/audio/flac.xml
/usr/share/mime/audio/midi.xml
/usr/share/mime/audio/mp2.xml
/usr/share/mime/audio/mp4.xml
/usr/share/mime/audio/mpeg.xml
/usr/share/mime/audio/ogg.xml
/usr/share/mime/audio/prs.sid.xml
/usr/share/mime/audio/vnd.dts.hd.xml
/usr/share/mime/audio/vnd.dts.xml
/usr/share/mime/audio/vnd.rn-realaudio.xml
/usr/share/mime/audio/webm.xml
/usr/share/mime/audio/x-adpcm.xml
/usr/share/mime/audio/x-aifc.xml
/usr/share/mime/audio/x-aiff.xml
/usr/share/mime/audio/x-amzxml.xml
/usr/share/mime/audio/x-ape.xml
/usr/share/mime/audio/x-flac+ogg.xml
/usr/share/mime/audio/x-gsm.xml
/usr/share/mime/audio/x-iriver-pla.xml
/usr/share/mime/audio/x-it.xml
/usr/share/mime/audio/x-m4b.xml
/usr/share/mime/audio/x-matroska.xml
/usr/share/mime/audio/x-minipsf.xml
/usr/share/mime/audio/x-mo3.xml
/usr/share/mime/audio/x-mod.xml
/usr/share/mime/audio/x-mpegurl.xml
/usr/share/mime/audio/x-ms-asx.xml
/usr/share/mime/audio/x-ms-wma.xml
/usr/share/mime/audio/x-musepack.xml
/usr/share/mime/audio/x-opus+ogg.xml
/usr/share/mime/audio/x-psf.xml
/usr/share/mime/audio/x-psflib.xml
/usr/share/mime/audio/x-riff.xml
/usr/share/mime/audio/x-s3m.xml
/usr/share/mime/audio/x-scpls.xml
/usr/share/mime/audio/x-speex+ogg.xml
/usr/share/mime/audio/x-speex.xml
/usr/share/mime/audio/x-stm.xml
/usr/share/mime/audio/x-tta.xml
/usr/share/mime/audio/x-voc.xml
/usr/share/mime/audio/x-vorbis+ogg.xml
/usr/share/mime/audio/x-wav.xml
/usr/share/mime/audio/x-wavpack-correction.xml
/usr/share/mime/audio/x-wavpack.xml
/usr/share/mime/audio/x-xi.xml
/usr/share/mime/audio/x-xm.xml
/usr/share/mime/audio/x-xmf.xml
/usr/share/mime/generic-icons
/usr/share/mime/globs
/usr/share/mime/globs2
/usr/share/mime/icons
/usr/share/mime/image/bmp.xml
/usr/share/mime/image/cgm.xml
/usr/share/mime/image/dpx.xml
/usr/share/mime/image/emf.xml
/usr/share/mime/image/fax-g3.xml
/usr/share/mime/image/fits.xml
/usr/share/mime/image/g3fax.xml
/usr/share/mime/image/gif.xml
/usr/share/mime/image/ief.xml
/usr/share/mime/image/jp2.xml
/usr/share/mime/image/jpeg.xml
/usr/share/mime/image/openraster.xml
/usr/share/mime/image/png.xml
/usr/share/mime/image/rle.xml
/usr/share/mime/image/svg+xml-compressed.xml
/usr/share/mime/image/svg+xml.xml
/usr/share/mime/image/tiff.xml
/usr/share/mime/image/vnd.adobe.photoshop.xml
/usr/share/mime/image/vnd.djvu+multipage.xml
/usr/share/mime/image/vnd.djvu.xml
/usr/share/mime/image/vnd.dwg.xml
/usr/share/mime/image/vnd.dxf.xml
/usr/share/mime/image/vnd.microsoft.icon.xml
/usr/share/mime/image/vnd.ms-modi.xml
/usr/share/mime/image/vnd.rn-realpix.xml
/usr/share/mime/image/vnd.wap.wbmp.xml
/usr/share/mime/image/vnd.zbrush.pcx.xml
/usr/share/mime/image/webp.xml
/usr/share/mime/image/wmf.xml
/usr/share/mime/image/x-3ds.xml
/usr/share/mime/image/x-adobe-dng.xml
/usr/share/mime/image/x-applix-graphics.xml
/usr/share/mime/image/x-bzeps.xml
/usr/share/mime/image/x-canon-cr2.xml
/usr/share/mime/image/x-canon-crw.xml
/usr/share/mime/image/x-cmu-raster.xml
/usr/share/mime/image/x-compressed-xcf.xml
/usr/share/mime/image/x-dcraw.xml
/usr/share/mime/image/x-dds.xml
/usr/share/mime/image/x-dib.xml
/usr/share/mime/image/x-eps.xml
/usr/share/mime/image/x-exr.xml
/usr/share/mime/image/x-fpx.xml
/usr/share/mime/image/x-fuji-raf.xml
/usr/share/mime/image/x-gzeps.xml
/usr/share/mime/image/x-icns.xml
/usr/share/mime/image/x-ilbm.xml
/usr/share/mime/image/x-jng.xml
/usr/share/mime/image/x-kodak-dcr.xml
/usr/share/mime/image/x-kodak-k25.xml
/usr/share/mime/image/x-kodak-kdc.xml
/usr/share/mime/image/x-lwo.xml
/usr/share/mime/image/x-lws.xml
/usr/share/mime/image/x-macpaint.xml
/usr/share/mime/image/x-minolta-mrw.xml
/usr/share/mime/image/x-msod.xml
/usr/share/mime/image/x-niff.xml
/usr/share/mime/image/x-nikon-nef.xml
/usr/share/mime/image/x-olympus-orf.xml
/usr/share/mime/image/x-panasonic-raw.xml
/usr/share/mime/image/x-panasonic-raw2.xml
/usr/share/mime/image/x-pentax-pef.xml
/usr/share/mime/image/x-photo-cd.xml
/usr/share/mime/image/x-pict.xml
/usr/share/mime/image/x-portable-anymap.xml
/usr/share/mime/image/x-portable-bitmap.xml
/usr/share/mime/image/x-portable-graymap.xml
/usr/share/mime/image/x-portable-pixmap.xml
/usr/share/mime/image/x-quicktime.xml
/usr/share/mime/image/x-rgb.xml
/usr/share/mime/image/x-sgi.xml
/usr/share/mime/image/x-sigma-x3f.xml
/usr/share/mime/image/x-skencil.xml
/usr/share/mime/image/x-sony-arw.xml
/usr/share/mime/image/x-sony-sr2.xml
/usr/share/mime/image/x-sony-srf.xml
/usr/share/mime/image/x-sun-raster.xml
/usr/share/mime/image/x-tga.xml
/usr/share/mime/image/x-tiff-multipage.xml
/usr/share/mime/image/x-win-bitmap.xml
/usr/share/mime/image/x-xbitmap.xml
/usr/share/mime/image/x-xcf.xml
/usr/share/mime/image/x-xcursor.xml
/usr/share/mime/image/x-xfig.xml
/usr/share/mime/image/x-xpixmap.xml
/usr/share/mime/image/x-xwindowdump.xml
/usr/share/mime/inode/blockdevice.xml
/usr/share/mime/inode/chardevice.xml
/usr/share/mime/inode/directory.xml
/usr/share/mime/inode/fifo.xml
/usr/share/mime/inode/mount-point.xml
/usr/share/mime/inode/socket.xml
/usr/share/mime/inode/symlink.xml
/usr/share/mime/magic
/usr/share/mime/message/delivery-status.xml
/usr/share/mime/message/disposition-notification.xml
/usr/share/mime/message/external-body.xml
/usr/share/mime/message/news.xml
/usr/share/mime/message/partial.xml
/usr/share/mime/message/rfc822.xml
/usr/share/mime/message/x-gnu-rmail.xml
/usr/share/mime/mime.cache
/usr/share/mime/model/iges.xml
/usr/share/mime/model/vrml.xml
/usr/share/mime/multipart/alternative.xml
/usr/share/mime/multipart/appledouble.xml
/usr/share/mime/multipart/digest.xml
/usr/share/mime/multipart/encrypted.xml
/usr/share/mime/multipart/mixed.xml
/usr/share/mime/multipart/related.xml
/usr/share/mime/multipart/report.xml
/usr/share/mime/multipart/signed.xml
/usr/share/mime/multipart/x-mixed-replace.xml
/usr/share/mime/packages/freedesktop.org.xml
/usr/share/mime/subclasses
/usr/share/mime/text/cache-manifest.xml
/usr/share/mime/text/calendar.xml
/usr/share/mime/text/css.xml
/usr/share/mime/text/csv-schema.xml
/usr/share/mime/text/csv.xml
/usr/share/mime/text/enriched.xml
/usr/share/mime/text/html.xml
/usr/share/mime/text/htmlh.xml
/usr/share/mime/text/markdown.xml
/usr/share/mime/text/plain.xml
/usr/share/mime/text/rfc822-headers.xml
/usr/share/mime/text/richtext.xml
/usr/share/mime/text/rust.xml
/usr/share/mime/text/sgml.xml
/usr/share/mime/text/spreadsheet.xml
/usr/share/mime/text/tab-separated-values.xml
/usr/share/mime/text/troff.xml
/usr/share/mime/text/turtle.xml
/usr/share/mime/text/vcard.xml
/usr/share/mime/text/vnd.graphviz.xml
/usr/share/mime/text/vnd.rn-realtext.xml
/usr/share/mime/text/vnd.sun.j2me.app-descriptor.xml
/usr/share/mime/text/vnd.trolltech.linguist.xml
/usr/share/mime/text/vnd.wap.wml.xml
/usr/share/mime/text/vnd.wap.wmlscript.xml
/usr/share/mime/text/vtt.xml
/usr/share/mime/text/x-adasrc.xml
/usr/share/mime/text/x-authors.xml
/usr/share/mime/text/x-bibtex.xml
/usr/share/mime/text/x-c++hdr.xml
/usr/share/mime/text/x-c++src.xml
/usr/share/mime/text/x-changelog.xml
/usr/share/mime/text/x-chdr.xml
/usr/share/mime/text/x-cmake.xml
/usr/share/mime/text/x-cobol.xml
/usr/share/mime/text/x-copying.xml
/usr/share/mime/text/x-credits.xml
/usr/share/mime/text/x-csharp.xml
/usr/share/mime/text/x-csrc.xml
/usr/share/mime/text/x-dcl.xml
/usr/share/mime/text/x-dsl.xml
/usr/share/mime/text/x-dsrc.xml
/usr/share/mime/text/x-eiffel.xml
/usr/share/mime/text/x-emacs-lisp.xml
/usr/share/mime/text/x-erlang.xml
/usr/share/mime/text/x-fortran.xml
/usr/share/mime/text/x-genie.xml
/usr/share/mime/text/x-gettext-translation-template.xml
/usr/share/mime/text/x-gettext-translation.xml
/usr/share/mime/text/x-gherkin.xml
/usr/share/mime/text/x-go.xml
/usr/share/mime/text/x-google-video-pointer.xml
/usr/share/mime/text/x-haskell.xml
/usr/share/mime/text/x-idl.xml
/usr/share/mime/text/x-imelody.xml
/usr/share/mime/text/x-install.xml
/usr/share/mime/text/x-iptables.xml
/usr/share/mime/text/x-java.xml
/usr/share/mime/text/x-ldif.xml
/usr/share/mime/text/x-lilypond.xml
/usr/share/mime/text/x-literate-haskell.xml
/usr/share/mime/text/x-log.xml
/usr/share/mime/text/x-lua.xml
/usr/share/mime/text/x-makefile.xml
/usr/share/mime/text/x-matlab.xml
/usr/share/mime/text/x-meson.xml
/usr/share/mime/text/x-microdvd.xml
/usr/share/mime/text/x-moc.xml
/usr/share/mime/text/x-modelica.xml
/usr/share/mime/text/x-mof.xml
/usr/share/mime/text/x-mpsub.xml
/usr/share/mime/text/x-mrml.xml
/usr/share/mime/text/x-ms-regedit.xml
/usr/share/mime/text/x-mup.xml
/usr/share/mime/text/x-nfo.xml
/usr/share/mime/text/x-objcsrc.xml
/usr/share/mime/text/x-ocaml.xml
/usr/share/mime/text/x-ocl.xml
/usr/share/mime/text/x-ooc.xml
/usr/share/mime/text/x-opml+xml.xml
/usr/share/mime/text/x-pascal.xml
/usr/share/mime/text/x-patch.xml
/usr/share/mime/text/x-python.xml
/usr/share/mime/text/x-qml.xml
/usr/share/mime/text/x-readme.xml
/usr/share/mime/text/x-reject.xml
/usr/share/mime/text/x-rpm-spec.xml
/usr/share/mime/text/x-sass.xml
/usr/share/mime/text/x-scala.xml
/usr/share/mime/text/x-scheme.xml
/usr/share/mime/text/x-scons.xml
/usr/share/mime/text/x-scss.xml
/usr/share/mime/text/x-setext.xml
/usr/share/mime/text/x-ssa.xml
/usr/share/mime/text/x-subviewer.xml
/usr/share/mime/text/x-svhdr.xml
/usr/share/mime/text/x-svsrc.xml
/usr/share/mime/text/x-tcl.xml
/usr/share/mime/text/x-tex.xml
/usr/share/mime/text/x-texinfo.xml
/usr/share/mime/text/x-troff-me.xml
/usr/share/mime/text/x-troff-mm.xml
/usr/share/mime/text/x-troff-ms.xml
/usr/share/mime/text/x-twig.xml
/usr/share/mime/text/x-txt2tags.xml
/usr/share/mime/text/x-uil.xml
/usr/share/mime/text/x-uri.xml
/usr/share/mime/text/x-uuencode.xml
/usr/share/mime/text/x-vala.xml
/usr/share/mime/text/x-verilog.xml
/usr/share/mime/text/x-vhdl.xml
/usr/share/mime/text/x-xmi.xml
/usr/share/mime/text/x-xslfo.xml
/usr/share/mime/text/xmcd.xml
/usr/share/mime/treemagic
/usr/share/mime/types
/usr/share/mime/version
/usr/share/mime/video/3gpp.xml
/usr/share/mime/video/3gpp2.xml
/usr/share/mime/video/annodex.xml
/usr/share/mime/video/dv.xml
/usr/share/mime/video/isivideo.xml
/usr/share/mime/video/mp2t.xml
/usr/share/mime/video/mp4.xml
/usr/share/mime/video/mpeg.xml
/usr/share/mime/video/ogg.xml
/usr/share/mime/video/quicktime.xml
/usr/share/mime/video/vnd.mpegurl.xml
/usr/share/mime/video/vnd.rn-realvideo.xml
/usr/share/mime/video/vnd.vivo.xml
/usr/share/mime/video/wavelet.xml
/usr/share/mime/video/webm.xml
/usr/share/mime/video/x-anim.xml
/usr/share/mime/video/x-flic.xml
/usr/share/mime/video/x-flv.xml
/usr/share/mime/video/x-javafx.xml
/usr/share/mime/video/x-matroska-3d.xml
/usr/share/mime/video/x-matroska.xml
/usr/share/mime/video/x-mng.xml
/usr/share/mime/video/x-ms-wmv.xml
/usr/share/mime/video/x-msvideo.xml
/usr/share/mime/video/x-nsv.xml
/usr/share/mime/video/x-ogm+ogg.xml
/usr/share/mime/video/x-sgi-movie.xml
/usr/share/mime/video/x-theora+ogg.xml
/usr/share/mime/x-content/audio-cdda.xml
/usr/share/mime/x-content/audio-dvd.xml
/usr/share/mime/x-content/audio-player.xml
/usr/share/mime/x-content/blank-bd.xml
/usr/share/mime/x-content/blank-cd.xml
/usr/share/mime/x-content/blank-dvd.xml
/usr/share/mime/x-content/blank-hddvd.xml
/usr/share/mime/x-content/ebook-reader.xml
/usr/share/mime/x-content/image-dcf.xml
/usr/share/mime/x-content/image-picturecd.xml
/usr/share/mime/x-content/software.xml
/usr/share/mime/x-content/unix-software.xml
/usr/share/mime/x-content/video-bluray.xml
/usr/share/mime/x-content/video-dvd.xml
/usr/share/mime/x-content/video-hddvd.xml
/usr/share/mime/x-content/video-svcd.xml
/usr/share/mime/x-content/video-vcd.xml
/usr/share/mime/x-content/win32-software.xml
/usr/share/mime/x-epoc/x-sisx-app.xml

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/shared-mime-info.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files locales -f shared-mime-info.lang
%defattr(-,root,root,-)

