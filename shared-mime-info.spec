#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : shared-mime-info
Version  : 1.10
Release  : 18
URL      : http://freedesktop.org/~hadess/shared-mime-info-1.10.tar.xz
Source0  : http://freedesktop.org/~hadess/shared-mime-info-1.10.tar.xz
Source1  : shared-mime-info.tmpfiles
Source2  : update-mime-database.service
Summary  : Freedesktop.org Shared MIME Info
Group    : Development/Tools
License  : GPL-2.0
Requires: shared-mime-info-bin = %{version}-%{release}
Requires: shared-mime-info-config = %{version}-%{release}
Requires: shared-mime-info-data = %{version}-%{release}
Requires: shared-mime-info-license = %{version}-%{release}
Requires: shared-mime-info-locales = %{version}-%{release}
Requires: shared-mime-info-man = %{version}-%{release}
Requires: shared-mime-info-services = %{version}-%{release}
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libxml-2.0)

%description
This package contains:
- The freedesktop.org shared MIME database spec.
- The merged GNOME and KDE databases, in the new format.
- The update-mime-database command, used to install new MIME data.

%package bin
Summary: bin components for the shared-mime-info package.
Group: Binaries
Requires: shared-mime-info-data = %{version}-%{release}
Requires: shared-mime-info-config = %{version}-%{release}
Requires: shared-mime-info-license = %{version}-%{release}
Requires: shared-mime-info-services = %{version}-%{release}

%description bin
bin components for the shared-mime-info package.


%package config
Summary: config components for the shared-mime-info package.
Group: Default

%description config
config components for the shared-mime-info package.


%package data
Summary: data components for the shared-mime-info package.
Group: Data

%description data
data components for the shared-mime-info package.


%package dev
Summary: dev components for the shared-mime-info package.
Group: Development
Requires: shared-mime-info-bin = %{version}-%{release}
Requires: shared-mime-info-data = %{version}-%{release}
Provides: shared-mime-info-devel = %{version}-%{release}
Requires: shared-mime-info = %{version}-%{release}

%description dev
dev components for the shared-mime-info package.


%package license
Summary: license components for the shared-mime-info package.
Group: Default

%description license
license components for the shared-mime-info package.


%package locales
Summary: locales components for the shared-mime-info package.
Group: Default

%description locales
locales components for the shared-mime-info package.


%package man
Summary: man components for the shared-mime-info package.
Group: Default

%description man
man components for the shared-mime-info package.


%package services
Summary: services components for the shared-mime-info package.
Group: Systemd services

%description services
services components for the shared-mime-info package.


%prep
%setup -q -n shared-mime-info-1.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557099425
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --disable-update-mimedb
make

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 check

%install
export SOURCE_DATE_EPOCH=1557099425
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/shared-mime-info
cp COPYING %{buildroot}/usr/share/package-licenses/shared-mime-info/COPYING
%make_install
%find_lang shared-mime-info
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/update-mime-database.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/shared-mime-info.conf
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/
ln -s ../update-mime-database.service %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/update-mime-database.service
mv %{buildroot}/usr/share/mime/packages %{buildroot}/usr/share/mime-packages
rm -rf %{buildroot}/usr/share/mime
ln -sf ../../var/cache/mime %{buildroot}/usr/share/mime
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/update-mime-database

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/shared-mime-info.conf

%files data
%defattr(-,root,root,-)
/usr/share/mime
/usr/share/mime-packages/freedesktop.org.xml

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/shared-mime-info.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/shared-mime-info/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/update-mime-database.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/update-mime-database.service
/usr/lib/systemd/system/update-triggers.target.wants/update-mime-database.service

%files locales -f shared-mime-info.lang
%defattr(-,root,root,-)

