
%define name	libass
%define version	0.9.11

%define major	4
%define libname	%mklibname ass %major
%define devname	%mklibname ass -d

Summary:	Library for SSA/ASS subtitles rendering
Name:		%name
Version:	%version
Release:	%mkrel 5
License:	GPLv2+
Group:		System/Libraries
URL:		http://code.google.com/p/libass/
Source:		http://libass.googlecode.com/files/%name-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	enca-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype2-devel

%description
Libass is a portable library for SSA/ASS subtitles rendering.

%package -n %libname
Summary:	Shared library for SSA/ASS subtitles rendering
Group:		System/Libraries

%description -n %libname
Libass is a portable library for SSA/ASS subtitles rendering.

%package -n %devname
Summary:	Development files for libass development
Group:		Development/C
Requires:	%libname = %version
Provides:	ass-devel = %version-%release
Provides:	libass-devel = %version-%release

%description -n %devname
Libass is a portable library for SSA/ASS subtitles rendering.

This package contains the files for developing applications which
will use libass.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%if "%{_lib}" == "lib64"
perl -pi -e "s|-L/usr/lib\b|-L%{_libdir}|g" %{buildroot}%{_libdir}/*.la
%endif

%clean
rm -rf %{buildroot}

%files -n %libname
%{_libdir}/libass.so.%{major}*

%files -n %devname
%doc Changelog
%{_libdir}/libass.a
%{_libdir}/libass.la
%{_libdir}/libass.so
%{_includedir}/ass
%{_libdir}/pkgconfig/%{name}.pc

