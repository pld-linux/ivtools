Summary:	IVTools - graphics editor
Summary(pl):	IVTools - program graficzny
Name:		ivtools
Version:	0.8.1
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source0:	http://www.vectaport.com/pub/src/%name-%version.tgz
Source1:	http://www.vectaport.com/pub/src/%name-doc-0.8.tgz
Source2:	http://www.vectaport.com/pub/src/%name-0.7.10-html.tgz
Patch0:		ivtools-sprintf-fix.patch
URL:		http://www.vectaport.com/ivtools/
BuildRequires:	XFree86-devel >= 3.3.5
BuildRequires:	bison >= 1.28
#BuildRequires:	clippoly-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6
%define _mandir	/usr/share/man

%description
IVTools is a suite of free X Windows drawing editors for PostScript, TeX,
and web graphics production, as well as an embeddable extendable vector
graphic shell.

%description -l pl
IVTools jest prostym edytorem stworzonym do wspó³pracy z narzêdziami
takimi jak PostScript, TeX, oraz do tworzenia grafik udostêpnianych 
poprzez WWW.

%package devel
Summary:	IVToosl development package
Summary(pl):	Narzêdzia programistyczne dla pakietu IVTools.
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika

%description devel
Development pacakage included all headers file.

%description -l pl devel
Pakiet programistyczny, zawiera pliki nag³ówkowe niezbêdne do kompilacji
przyk³adów, i w³asnych programów u¿ywaj±cych pakietu IVTools.

%prep
%setup -q -n %name-0.8

%build
echo "This package requires clippoly library, but this is still under"
echo "development."
echo ""
echo "I can not copmile this libraried."
./configure --prefix=%{_prefix} \
	--enable-install-relative="yes"
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS" Makefile
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS" Makefiles
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS" depend
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir},%{_mandir}/{man3,man1}}
%{__make} install 

install %{SOURCE1} $RPM_BUILD_DIR/%name-0.8/
install %{SOURCE2} $RPM_BUILD_DIR/%name-0.8/

install bin/LINUX/* $RPM_BUILD_ROOT%{_bindir}
install lib/LINUX/*%{version}* $RPM_BUILD_ROOT%{_libdir}

install -d $RPM_BUILD_ROOT%{_includedir}/{Dispatch,IV-2_6,IV-3_1,IV-X11,IV-look}
install -d $RPM_BUILD_ROOT%{_includedir}/{InterViews,OS,TIFF,Unidraw,ivstd}

install src/include/Dispatch/*.h $RPM_BUILD_ROOT%{_includedir}/Dispatch/

install src/include/IV-2_6/*.h $RPM_BUILD_ROOT%{_includedir}/IV-2_6/
install -d $RPM_BUILD_ROOT%{_includedir}/IV-2_6/InterViews
install src/include/IV-2_6/InterViews/*.h \
	$RPM_BUILD_ROOT%{_includedir}/IV-2_6/InterViews/
	
(cd $RPM_BUILD_ROOT%{_includedir}/IV-3_1;ln -s ../InterViews InterViews)

install src/include/IV-X11/*.h $RPM_BUILD_ROOT%{_includedir}/IV-X11/

install src/include/IV-look/*.h $RPM_BUILD_ROOT%{_includedir}/IV-look/

install src/include/InterViews/*.h $RPM_BUILD_ROOT%{_includedir}/InterViews/
install -d $RPM_BUILD_ROOT%{_includedir}/InterViews/Bitmaps
install src/include/InterViews/Bitmaps/*.bm \
	 $RPM_BUILD_ROOT%{_includedir}/InterViews/Bitmaps/
	 
install src/include/OS/*.h $RPM_BUILD_ROOT%{_includedir}/OS/

install src/include/TIFF/*.h $RPM_BUILD_ROOT%{_includedir}/TIFF/

install src/include/Unidraw/*.h $RPM_BUILD_ROOT%{_includedir}/Unidraw/

install -d $RPM_BUILD_ROOT%{_includedir}/Unidraw/Commands
install -d $RPM_BUILD_ROOT%{_includedir}/Unidraw/Components
install -d $RPM_BUILD_ROOT%{_includedir}/Unidraw/Graphic
install -d $RPM_BUILD_ROOT%{_includedir}/Unidraw/Tools

install src/include/Unidraw/Commands/*.h \
	$RPM_BUILD_ROOT%{_includedir}/Unidraw/Commands/
install src/include/Unidraw/Components/*.h \
	$RPM_BUILD_ROOT%{_includedir}/Unidraw/Components/
install src/include/Unidraw/Graphic/*.h \
	$RPM_BUILD_ROOT%{_includedir}/Unidraw/Graphic/
install src/include/Unidraw/Tools/*.h \
	$RPM_BUILD_ROOT%{_includedir}/Unidraw/Tools/

install src/include/ivstd/*.h $RPM_BUILD_ROOT%{_includedir}/ivstd/

install man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1/
install man/man3/* $RPM_BUILD_ROOT%{_mandir}/man3/

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/*
gzip -9nf src/man/refman3.1/refman.PS
gzip -9nf CHANGES* COPYRIGHT MANIFEST* README* VERSION

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES*.gz COPYRIGHT.gz MANIFEST*.gz README*.gz VERSION.gz
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_libdir}/*

%attr(644,root,root) %{_mandir}/man1/*.gz
%attr(644,root,root) %{_mandir}/man3/*.gz

%files devel
%doc src/man/refman3.1/refman.PS.gz
%defattr(644,root,root,755)
%{_includedir}/Dispatch
%{_includedir}/IV-2_6
%{_includedir}/IV-3_1
%{_includedir}/IV-X11
%{_includedir}/IV-look
%{_includedir}/InterViews
%{_includedir}/OS
%{_includedir}/TIFF
%{_includedir}/Unidraw
%{_includedir}/ivstd
