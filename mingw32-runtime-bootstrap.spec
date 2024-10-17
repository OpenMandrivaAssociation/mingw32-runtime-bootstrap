# NOTE: NOT a Mandriva package. This contains binaries which are needed
# just to bootstrap the whole system if you build everything from scratch.

%define __os_install_post /usr/lib/rpm/brp-compress %{nil}

%define runtime_version 3.15.1

Name: mingw32-runtime-bootstrap
Version: 1
Release: %mkrel 4
Summary: MinGW Windows bootstrap (binary package)

Group: Development/Other
License: Public Domain
URL: https://www.mingw.org/

Source0: http://dl.sourceforge.net/sourceforge/mingw/mingwrt-%{runtime_version}-mingw32.tar.gz
Source1:  mingw32-runtime-bootstrap.rpmlintrc

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch: noarch

Provides: mingw32-runtime = %{runtime_version}
Provides: mingw-runtime = %{runtime_version}


%description
MinGW bootstrap (binary package).

%prep
%setup -q -c

%build
rm -rf i586-pc-mingw32

# Setup sys-root.
mkdir -p i586-pc-mingw32/sys-root/mingw
cp -a include lib i586-pc-mingw32/sys-root/mingw


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_prefix}
cp -a i586-pc-mingw32 $RPM_BUILD_ROOT%{_prefix}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%dir %{_prefix}/i586-pc-mingw32
%{_prefix}/i586-pc-mingw32/sys-root


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1-4mdv2011.0
+ Revision: 620358
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1-3mdv2010.0
+ Revision: 439939
- rebuild

* Wed Feb 04 2009 Jérôme Soyer <saispo@mandriva.org> 1-2mdv2009.1
+ Revision: 337632
- Readd Provides

* Wed Feb 04 2009 Jérôme Soyer <saispo@mandriva.org> 1-1mdv2009.1
+ Revision: 337609
- import mingw32-runtime-bootstrap


