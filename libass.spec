%define major 4
%define libname %mklibname ass %{major}
%define devname %mklibname ass -d

Summary:	Library for SSA/ASS subtitles rendering
Name:		libass
Version:	0.10.1
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://code.google.com/p/libass/
Source0:	http://libass.googlecode.com/files/%{name}-%{version}.tar.xz
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
Provides:	%{name}-devel = %{version}-%{release}

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

