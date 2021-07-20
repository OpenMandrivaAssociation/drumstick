%define major 2
%define libalsa %mklibname %{name}-alsa %{major}
%define libfile %mklibname %{name}-file %{major}
%define librt   %mklibname %{name}-rt   %{major}
%define devname %mklibname %{name} -d

Summary:	C++/Qt5 wrapper around the ALSA library sequencer interface
Name:		drumstick
Version:	2.3.0
Release:	1
Group:		Development/C++
License:	GPLv2+
Url:		http://drumstick.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/drumstick/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	ninja
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Help)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiPlugin)
BuildRequires:	cmake(Qt5Widgets)
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
interface, using Qt5 objects, idioms and style. The ALSA sequencer
interface provides software support for MIDI technology on GNU/Linux.

%files
%doc AUTHORS ChangeLog COPYING NEWS readme.md TODO
%{_datadir}/mime/packages/drumstick.xml

#----------------------------------------------------------------------------

%package -n %{libalsa}
Summary:	Drumstick shared library
Group:		System/Libraries
Conflicts:	%{name} < 0.5.0-4

%description -n %{libalsa}
Drumstick shared library.

%files -n %{libalsa}
%{_libdir}/lib%{name}-alsa.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libfile}
Summary:	Drumstick shared library
Group:		System/Libraries
Conflicts:	%{name} < 0.5.0-4

%description -n %{libfile}
Drumstick shared library.

%files -n %{libfile}
%{_libdir}/lib%{name}-file.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{librt}
Summary:	Drumstick shared library
Group:		System/Libraries

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
interface, using Qt5 objects, idioms and style. This package contains
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
%{_datadir}/applications/drumstick-*.desktop
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
