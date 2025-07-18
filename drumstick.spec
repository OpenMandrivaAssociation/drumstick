%define	major 2
%define	libalsa %mklibname %{name}-alsa
%define	oldlibalsa %mklibname %{name}-alsa 2
%define	libfile %mklibname %{name}-file
%define	oldlibfile %mklibname %{name}-file 2
%define	librt   %mklibname %{name}-rt
%define	oldlibrt   %mklibname %{name}-rt   2
%define	devname %mklibname %{name} -d

Summary:	C++/Qt6 wrapper around the ALSA library sequencer interface
Name:	drumstick
Version:	2.10.0
Release:	2
License:	GPLv2+
Group:	Sound
Url:		https://drumstick.sourceforge.net/
Source0:	https://downloads.sourceforge.net/project/drumstick/%{version}/%{name}-%{version}.tar.bz2
Source100:	drumstick.rpmlintrc
BuildRequires:	cmake >= 3.16
# To build the manpages
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtd-xml
BuildRequires:	doxygen >= 1.5.0
BuildRequires:	graphviz
BuildRequires:	gzip-utils
BuildRequires:	xsltproc
BuildRequires:	ninja
BuildRequires:	qt6-qtbase-theme-gtk3
BuildRequires:	shared-mime-info >= 0.30
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core) >= 6.2.0
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Help)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6UiPlugin)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(sonivox)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libpipewire-0.3)
BuildRequires:	pkgconfig(libpulse-simple)
BuildRequires:	pkgconfig(vulkan)
# vpiano example program needs it
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xkbcommon)

%description
The %{name} library is a C++ wrapper around the ALSA library sequencer
interface, using Qt6 objects, idioms and style. The ALSA sequencer
interface provides software support for MIDI technology on GNU/Linux.

%files
%doc AUTHORS ChangeLog COPYING NEWS readme.md TODO
%{_datadir}/mime/packages/%{name}.xml

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
%{_libdir}/lib%{name}-widgets.so.%{major}*
%{_prefix}/plugins/designer/lib%{name}-vpiano-plugin.so

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
%{_includedir}/%{name}/
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}-alsa.so
%{_libdir}/lib%{name}-file.so
%{_libdir}/lib%{name}-rt.so
%{_libdir}/lib%{name}-widgets.so
%{_libdir}/pkgconfig/%{name}-*.pc
%{_libdir}/cmake/%{name}/

#----------------------------------------------------------------------------

%package examples
Summary:	Example programs for %{name}
Group:		Sound
Requires:	%{name} = %{EVRD}

%description examples
This package contains the test/example programs for %{name}.

%files examples
%{_bindir}/%{name}-*
%{_datadir}/applications/net.sourceforge.%{name}-drumgrid.desktop
%{_datadir}/applications/net.sourceforge.%{name}-guiplayer.desktop
%{_datadir}/applications/net.sourceforge.%{name}-vpiano.desktop
%{_datadir}/metainfo/net.sourceforge.%{name}-drumgrid.metainfo.xml
%{_datadir}/metainfo/net.sourceforge.%{name}-guiplayer.metainfo.xml
%{_datadir}/metainfo/net.sourceforge.%{name}-vpiano.metainfo.xml
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}-*
%{_datadir}/%{name}/

#----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%cmake -G Ninja
%ninja

# (gvm) Make also the doxygen docs for the library
%ninja doxygen


%install
%ninja_install -C build

# Fix gzipped-svg-icon
(
cd %{buildroot}%{_iconsdir}/hicolor/scalable/apps/
zcat %{name}.svgz > %{name}.svg && rm -f %{name}.svgz
)
