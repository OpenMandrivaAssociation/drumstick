Name:		drumstick
Summary:	C++/Qt4 wrapper around the ALSA library sequencer interface
Version:	0.3.0
Release:	%mkrel 1
Group:		Development/C++
License:	GPLv2+
URL:		http://drumstick.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/drumstick/%{version}svn/drumstick-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	alsa-lib-devel


%description
The drumstick library is a C++ wrapper around the ALSA library sequencer
interface, using Qt4 objects, idioms and style. The ALSA sequencer interface
provides software support for MIDI technology on GNU/Linux.

%package devel
Summary: Developer files for %{name}
Group:   Development/C++
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.


%package examples
Summary: Example programs for %{name}
Group:   Development/C++
Requires: %{name} = %{version}-%{release}

%description examples
This package contains the test/example programs for %{name}.


%prep
%setup -q -n %{name}-%{version}

%build
%cmake
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING
%{_datadir}/mime/packages/drumstick.xml
%{_libdir}/libdrumstick*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libdrumstick*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/drumstick/
%{_includedir}/drumstick.h

%files examples
%defattr(-,root,root,-)
%{_bindir}/drumstick-*
%{_datadir}/applications/drumstick-*.desktop
%{_datadir}/icons/hicolor/*/apps/*
