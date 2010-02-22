Name:		drumstick
Summary:	C++/Qt4 wrapper around the ALSA library sequencer interface
Version:	0.2.99
Release:	%mkrel -c svn 1
Group:		Development/C++
License:	GPLv2+
URL:		http://drumstick.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/drumstick/%{version}svn/drumstick-%{version}svn.tar.bz2
# use patch from svn to make it work with kmid2
# svn diff -r 137:141 https://drumstick.svn.sourceforge.net/svnroot/drumstick/trunk
Patch0:		drumstick-0.2.99-20100208svn.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	desktop-file-utils


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
%setup -q -n %{name}-%{version}svn
%patch0 -p0
# don't create .la file
sed -i -e 's/CREATE_LIBTOOL_FILE/#CREATE_LIBTOOL_FILE/g' library/CMakeLists.txt


%build
%cmake_kde4
%make


%install
rm -rf %{buildroot}
%makeinstall_std -C build


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING
%{_libdir}/libdrumstick.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libdrumstick.so
%{_libdir}/pkgconfig/drumstick.pc
%{_includedir}/drumstick/
%{_includedir}/drumstick.h

%files examples
%defattr(-,root,root,-)
%{_bindir}/drumstick-*
%{_datadir}/applications/drumstick-*.desktop
%{_datadir}/icons/hicolor/*/apps/*
