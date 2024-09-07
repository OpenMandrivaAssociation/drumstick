%define major 2
%define libalsa %mklibname %{name}-alsa
%define oldlibalsa %mklibname %{name}-alsa 2
%define libfile %mklibname %{name}-file
%define oldlibfile %mklibname %{name}-file 2
%define librt   %mklibname %{name}-rt
%define oldlibrt   %mklibname %{name}-rt   2
%define devname %mklibname %{name} -d

Summary:	C++/Qt6 wrapper around the ALSA library sequencer interface
Name:		drumstick
Version:	2.9.1
Release:	1
Group:		Development/C++
License:	GPLv2+
Url:		https://drumstick.sourceforge.net/
Source0:	https://downloads.sourceforge.net/project/drumstick/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	ninja
BuildRequires:	cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Help)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	qt6-qtbase-theme-gtk3
BuildRequires:  cmake(sonivox)
BuildRequires:	pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(libpulse-simple)
# vpiano example program needs it
BuildRequires:	pkgconfig(x11)
# to build the manpages
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtd-xml
BuildRequires:	doxygen >= 1.5.0
BuildRequires:	graphviz
BuildRequires:	xsltproc
# See INSTALL file
BuildRequires:	shared-mime-info >= 0.3.0

%description
The %{name} library is a C++ wrapper around the ALSA library sequencer
interface, using Qt6 objects, idioms and style. The ALSA sequencer
interface provides software support for MIDI technology on GNU/Linux.

%files
%doc AUTHORS ChangeLog COPYING NEWS readme.md TODO
%{_datadir}/mime/packages/drumstick.xml

#----------------------------------------------------------------------------

%package -n %{libalsa}
Summary:	Drumstick shared library
Group:		System/Libraries
Conflicts:	%{name} < 0.5.0-4
%rename %{oldlibalsa}

%description -n %{libalsa}
Drumstick shared library.

%files -n %{libalsa}
%{_libdir}/lib%{name}-alsa.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libfile}
Summary:	Drumstick shared library
Group:		System/Libraries
Conflicts:	%{name} < 0.5.0-4
%rename %{oldlibfile}

%description -n %{libfile}
Drumstick shared library.

%files -n %{libfile}
%{_libdir}/lib%{name}-file.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{librt}
Summary:	Drumstick shared library
Group:		System/Libraries
%rename %{oldlibrt}

%description -n %{librt}
Drumstick shared library.

%files -n %{librt}
%{_libdir}/lib%{name}-rt.so.%{major}*
%{_libdir}/%{name}2/
%{_libdir}/libdrumstick-widgets.so.%{major}*
%{_prefix}/plugins/designer/libdrumstick-vpiano-plugin.so
#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libalsa} = %{EVRD}
Requires:	%{libfile} = %{EVRD}
Requires:	%{librt} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{name}-devel < 0.5.0-4
Obsoletes:	%{name}-devel < 0.5.0-4

%description -n %{devname}
The %{name} library is a C++ wrapper around the ALSA library sequencer
interface, using Qt6 objects, idioms and style. This package contains
the files needed for build programs against %{name}.

%files -n %{devname}
%doc build/doc/html/*
%{_libdir}/libdrumstick-alsa.so
%{_libdir}/libdrumstick-file.so
%{_libdir}/libdrumstick-rt.so
%{_libdir}/libdrumstick-widgets.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/%{name}/
%{_includedir}/drumstick/
%{_includedir}/drumstick.h

#----------------------------------------------------------------------------

%package examples
Summary:	Example programs for %{name}
Group:		Development/C++
Requires:	%{name} = %{EVRD}

%description examples
This package contains the test/example programs for %{name}.

%files examples
%{_bindir}/drumstick-*
%{_datadir}/applications/net.sourceforge.drumstick-drumgrid.desktop
%{_datadir}/applications/net.sourceforge.drumstick-guiplayer.desktop
%{_datadir}/applications/net.sourceforge.drumstick-vpiano.desktop
%{_datadir}/metainfo/net.sourceforge.drumstick-drumgrid.metainfo.xml
%{_datadir}/metainfo/net.sourceforge.drumstick-guiplayer.metainfo.xml
%{_datadir}/metainfo/net.sourceforge.drumstick-vpiano.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/%{name}-*
%{_datadir}/%{name}/

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%cmake -G Ninja
%ninja
# (gvm) Make also the doxygen docs for the library
%ninja doxygen

%install
%ninja_install -C build
