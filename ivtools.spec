Summary:	IVTools - graphics editor
Summary(pl):	IVTools - program graficzny
Name:		ivtools
Version:	1.1.3
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/ivtools/%{name}-%{version}.tgz
# Source0-md5:	dc9353fb05e36dbd7483eaeabf99fc3d
Source1:	http://dl.sourceforge.net/ivtools/%{name}-doc-1.0.4.tgz
# Source1-md5:	162eff5538d03857be8ec2431b581974
Source2:	http://www.vectaport.com/pub/src/%{name}-0.7.10-html.tgz
# Source2-md5:	f73fcb6e15d98ae6a505517158eeb61a
Patch0:		%{name}-sprintf-fix.patch
URL:		http://www.ivtools.org/ivtools/index.html
BuildRequires:	XFree86-devel >= 3.3.5
BuildRequires:	bison >= 1.28
#BuildRequires:	clippoly-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IVTools is a suite of free X Window drawing editors for PostScript,
TeX, and web graphics production, as well as an embeddable extendable
vector graphic shell.

%description -l pl
IVTools jest prostym edytorem stworzonym do wspó³pracy z narzêdziami
takimi jak PostScript, TeX, oraz do tworzenia grafik udostêpnianych
poprzez WWW.

%package devel
Summary:	IVToosl development package
Summary(pl):	Narzêdzia programistyczne dla pakietu IVTools
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description devel
Development pacakage included all headers file.

%description devel -l pl
Pakiet programistyczny, zawiera pliki nag³ówkowe niezbêdne do
kompilacji przyk³adów, i w³asnych programów u¿ywaj±cych pakietu
IVTools.

%prep
%setup -q -n %{name}-1.1

%build
echo "This package requires clippoly library, but this is still under"
echo "development."
echo ""
echo "I can not copmile this libraries."
%configure2_13 \
	--enable-install-relative="yes"
%{__make} Makefile
%{__make} Makefiles
%{__make} depend
%{__make} \
	OPTIMIZE_CCFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions" \
	DEBUG_CCFLAGS="%{?debug:-g}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man{3,1}} \
	$RPM_BUILD_ROOT%{_includedir}/{Dispatch,IV-2_6,IV-3_1,IV-X11,IV-look} \
	$RPM_BUILD_ROOT%{_includedir}/{InterViews,OS,TIFF,Unidraw,ivstd} \
	$RPM_BUILD_ROOT%{_includedir}/{IV-2_6/InterViews,InterViews/Bitmaps} \
	$RPM_BUILD_ROOT%{_includedir}/Unidraw/{Commands,Components,Graphic,Tools}

%{__make} install \
	INSTPGMFLAGS=""

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_DIR/%{name}-1.1/

install bin/LINUX/* $RPM_BUILD_ROOT%{_bindir}
install lib/LINUX/*%{version}* $RPM_BUILD_ROOT%{_libdir}

install src/include/Dispatch/*.h $RPM_BUILD_ROOT%{_includedir}/Dispatch

install src/include/IV-2_6/*.h $RPM_BUILD_ROOT%{_includedir}/IV-2_6
install src/include/IV-2_6/InterViews/*.h \
	$RPM_BUILD_ROOT%{_includedir}/IV-2_6/InterViews

ln -sf ../InterViews $RPM_BUILD_ROOT%{_includedir}/IV-3_1/InterViews

install src/include/IV-X11/*.h $RPM_BUILD_ROOT%{_includedir}/IV-X11
install src/include/IV-look/*.h $RPM_BUILD_ROOT%{_includedir}/IV-look

install src/include/InterViews/*.h $RPM_BUILD_ROOT%{_includedir}/InterViews
install src/include/OS/*.h $RPM_BUILD_ROOT%{_includedir}/OS
install src/include/TIFF/*.h $RPM_BUILD_ROOT%{_includedir}/TIFF
install src/include/Unidraw/*.h $RPM_BUILD_ROOT%{_includedir}/Unidraw

install src/include/Unidraw/Commands/*.h \
	$RPM_BUILD_ROOT%{_includedir}/Unidraw/Commands
install src/include/Unidraw/Components/*.h \
	$RPM_BUILD_ROOT%{_includedir}/Unidraw/Components
install src/include/Unidraw/Graphic/*.h \
	$RPM_BUILD_ROOT%{_includedir}/Unidraw/Graphic
install src/include/Unidraw/Tools/*.h \
	$RPM_BUILD_ROOT%{_includedir}/Unidraw/Tools
install src/include/ivstd/*.h \
	$RPM_BUILD_ROOT%{_includedir}/ivstd

install src/include/InterViews/Bitmaps/*.bm \
	$RPM_BUILD_ROOT%{_includedir}/InterViews/Bitmaps

install man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
install man/man3/* $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES* COPYRIGHT MANIFEST* README README.ivmkcm
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*
%{_mandir}/man[13]/*

%files devel
%defattr(644,root,root,755)
%doc src/man/refman3.1/refman.PS
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
