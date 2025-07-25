%undefine _debugsource_packages

%define major 9
%define libname %mklibname ass %{major}
%define devname %mklibname ass -d

Summary:	Library for SSA/ASS subtitles rendering
Name:		libass
Version:	0.17.3
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		https://github.com/libass/libass
Source0:	https://github.com/libass/libass/archive/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  nasm
BuildRequires:	pkgconfig(enca)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:  pkgconfig(libunibreak)

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
%autosetup -p1

%build
%meson \
        -Ddirectwrite=disabled \
        -Dcoretext=disabled \
        -Ddefault_library=shared
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/libass.so.%{major}*

%files -n %{devname}
%doc Changelog
%{_libdir}/libass.so
%{_includedir}/ass
%{_libdir}/pkgconfig/%{name}.pc
