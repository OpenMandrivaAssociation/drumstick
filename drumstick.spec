Name:		drumstick
Summary:		C++/Qt4 wrapper around the ALSA library sequencer interface
Version:		0.5.0
Release:		2
Group:		Development/C++
License:		GPLv2+
URL:		http://drumstick.sourceforge.net/
Source0:		http://downloads.sourceforge.net/project/drumstick/%{version}/%{name}-%{version}.tar.bz2
Patch0:		drumstick-0.5.0-fix-gold-linker.patch
BuildRequires:	cmake >= 2.6.0
BuildRequires:	qt4-devel >= 4.4.0
BuildRequires:	libalsa-devel >= 1.0.0
# to build the manpages
BuildRequires:	doxygen >= 1.5.0
BuildRequires:	xsltproc
BuildRequires:	docbook-xsl
BuildRequires:	docbook-dtd-xml
BuildRequires:	graphviz
# See INSTALL file
BuildRequires:	shared-mime-info >= 0.3.0
# vpiano example program needs it
BuildRequires:	pkgconfig(x11)

%description
The %{name} library is a C++ wrapper around the ALSA library sequencer
interface, using Qt4 objects, idioms and style. The ALSA sequencer
interface provides software support for MIDI technology on GNU/Linux.


%package devel
Summary:		Developer files for %{name}
Group:		Development/C++
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name} library is a C++ wrapper around the ALSA library sequencer
interface, using Qt4 objects, idioms and style. This package contains
the files needed for build programs against %{name}.


%package	 examples
Summary:		Example programs for %{name}
Group:		Development/C++
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains the test/example programs for %{name}.


%prep
%setup -qn %{name}-%{version}
%apply_patches

%build
%cmake
%make
# (gvm) Make also the doxygen docs for the library
%make doxygen

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_datadir}/mime/packages/drumstick.xml
%{_libdir}/libdrumstick-alsa.so.0*
%{_libdir}/libdrumstick-file.so.0*

%files devel
%doc build/doc/html/*
%{_libdir}/libdrumstick*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/drumstick/
%{_includedir}/drumstick.h

%files examples
%{_bindir}/drumstick-*
%{_datadir}/applications/drumstick-*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/%{name}-*


%changelog
* Thu Oct 11 2012 Giovanni Mariani <mc2374@mclink.it> 0.5.0-1
- Removed BuildRoot, %%defattr, %%mkrel and %%clean section
- Added some BReqs according to the INSTALL file from sources
- Changed BReq for alsa devel package and hopefully fix the build
- Added BReq for libx11-devel as it is needed from vpiano example program
- Added P0 (taken from Debian) to try to resolve troubles with gold linker)
- Enabled building of doxygen-generated docs for the library and
  added them to the devel package (and made rpmlint more happy)
- Moved mime infos in the examples package (they refer to the example
  program, not to the library)

* Fri Sep 10 2010 Funda Wang <fwang@mandriva.org> 0.5.0-1mdv2011.0
+ Revision: 577123
- update to new version 0.5.0

* Tue Aug 03 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.4.1-1mdv2011.0
+ Revision: 565192
- update to 0.4.1
- add BR, docbook-dtd45-xml and xsltproc to build the manpages

* Mon Apr 26 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.3.1-1mdv2010.1
+ Revision: 539293
- new release, 0.3.1

* Mon Mar 15 2010 Funda Wang <fwang@mandriva.org> 0.3.0-1mdv2010.1
+ Revision: 519781
- new version 0.3.0

* Mon Feb 22 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.2.99-0.svn.1mdv2010.1
+ Revision: 509374
- fix spec
- Import drumstick for kmid2 (based on Fedora spec


