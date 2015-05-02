%define major 5
%define libname %mklibname ass %{major}
%define devname %mklibname ass -d


Summary:	Library for SSA/ASS subtitles rendering
Name:		libass
Version:	0.12.1
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://code.google.com/p/libass/
Source0:	https://github.com/libass/libass/archive/0.12.1.tar.gz
BuildRequires:	pkgconfig(enca)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fribidi)

%description
Libass is a portable library for SSA/ASS subtitles rendering.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for SSA/ASS subtitles rendering
Group:		System/Libraries

%description -n %{libname}
Libass is a portable library for SSA/ASS subtitles rendering.

%files -n %{libname}
%doc Changelog README.md
%{_libdir}/libass.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for libass development
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	ass-devel = %{EVRD}

%description -n %{devname}
Libass is a portable library for SSA/ASS subtitles rendering.

This package contains the files for developing applications which
will use libass.

%files -n %{devname}
%doc Changelog README.md
%{_libdir}/libass.so
%{_includedir}/ass
%{_libdir}/pkgconfig/%{name}.pc

#----------------------------------------------------------------------------

%prep
%setup -q

%build
sh autogen.sh
%configure2_5x --disable-static
%make

%install
%makeinstall_std