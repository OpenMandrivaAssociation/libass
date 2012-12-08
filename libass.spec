%define major	4
%define libname	%mklibname ass %{major}
%define devname	%mklibname ass -d

Summary:	Library for SSA/ASS subtitles rendering
Name:		libass
Version:	0.10.0
Release:	2
License:	GPLv2+
Group:		System/Libraries
URL:		http://code.google.com/p/libass/
Source:		http://libass.googlecode.com/files/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(enca)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fribidi)

%description
Libass is a portable library for SSA/ASS subtitles rendering.

%package -n %{libname}
Summary:	Shared library for SSA/ASS subtitles rendering
Group:		System/Libraries

%description -n %{libname}
Libass is a portable library for SSA/ASS subtitles rendering.

%package -n %{devname}
Summary:	Development files for libass development
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	ass-devel = %{version}-%{release}
Provides:	libass-devel = %{version}-%{release}

%description -n %{devname}
Libass is a portable library for SSA/ASS subtitles rendering.

This package contains the files for developing applications which
will use libass.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libass.so.%{major}*

%files -n %{devname}
%doc Changelog
%{_libdir}/libass.so
%{_includedir}/ass
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Wed Jan 11 2012 Götz Waschk <waschk@mandriva.org> 0.10.0-1mdv2012.0
+ Revision: 759772
- update build deps
- new version
- remove libtool archive

* Mon Jun 20 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.11-5
+ Revision: 686313
- avoid pulling 32 bit libraries on 64 bit arch

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.11-4
+ Revision: 660213
- mass rebuild

* Fri Nov 26 2010 Götz Waschk <waschk@mandriva.org> 0.9.11-3mdv2011.0
+ Revision: 601536
- rebuild

* Sat Aug 28 2010 Götz Waschk <waschk@mandriva.org> 0.9.11-2mdv2011.0
+ Revision: 573780
- update URL

* Thu Aug 12 2010 Anssi Hannula <anssi@mandriva.org> 0.9.11-1mdv2011.0
+ Revision: 569175
- new version

* Sat Jul 10 2010 Anssi Hannula <anssi@mandriva.org> 0.9.9-1mdv2011.0
+ Revision: 549973
- initial Mandriva release

