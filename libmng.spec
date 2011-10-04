Name: libmng
Version: 1.0.10
Release: 7
URL: http://www.libmng.com/
Summary: Library for Multiple-image Network Graphics support
# This is a common zlib variant.
License: zlib
Source: http://dl.sf.net/libmng/%{name}-%{version}.tar.gz
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: zlib-devel
BuildRequires: libjpeg-devel
BuildRequires: lcms-devel
BuildRequires: libtool

%package devel
Summary: Development files for the Multiple-image Network Graphics library
Group: Development/Libraries
Requires: %{name} = %{version}
Requires: zlib-devel
Requires: libjpeg-devel

%description
LibMNG is a library for accessing graphics in MNG (Multi-image Network
Graphics) and JNG (JPEG Network Graphics) formats.  MNG graphics are
basically animated PNGs.  JNG graphics are basically JPEG streams
integrated into a PNG chunk.

%description devel
LibMNG is a library for accessing MNG and JNG format graphics.  The
libmng-devel package contains files needed for developing or compiling
applications which use MNG graphics.

%prep
%setup -q

%build
cat unmaintained/autogen.sh | tr -d \\r > autogen.sh
chmod 755 autogen.sh
[ ! -x ./configure ] && ./autogen.sh --help # generate, but don't run
%configure --enable-shared --disable-static --with-zlib --with-jpeg \
	--with-gnu-ld --with-lcms
make %{?_smp_mflags}

%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,0755)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,0755)
%{_libdir}/*.so
%{_includedir}/*
%doc %{_mandir}/man3/*
%doc %{_mandir}/man5/*

