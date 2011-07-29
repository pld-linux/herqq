Summary:	A library for building UPnP devices and control points
Name:		herqq
Version:	1.0.0
Release:	3
License:	GPL v3+
Group:		Applications
Source0:	http://downloads.sourceforge.net/hupnp/%{name}-%{version}.zip
# Source0-md5:	45a0632f7c7b64bc0fdab852d36c1e61
URL:		http://www.herqq.org/
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Herqq UPnP (HUPnP) is a software library for building UPnP devices and
control points conforming to the UPnP Device Architecture version 1.1.
It is designed to be simple to use and robust in operation. It is
built using C++ and the Qt Framework following many of the design
principles and programming practices used in the Qt Framework. It
integrates into Qt-based software smoothly and enables truly rapid
UPnP development.

%package devel
Summary:	Header files for herqq library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki herqq
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for herqq library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki herqq.

%prep
%setup -q

%build
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}

cp -a hupnp/bin/lib* $RPM_BUILD_ROOT%{_libdir}
cp -a hupnp/deploy/include/HUpnpCore $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libHUpnp.so.*.*.*
%attr(755,root,root) %{_libdir}/libHUpnp.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libHUpnp.so.1
%attr(755,root,root) %{_libdir}/libQtSolutions_SOAP-2.7.so.*.*.*
%attr(755,root,root) %{_libdir}/libQtSolutions_SOAP-2.7.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtSolutions_SOAP-2.7.so.1

%files devel
%defattr(644,root,root,755)
%doc hupnp/docs
%{_libdir}/libHUpnp.so
%{_libdir}/libQtSolutions_SOAP-2.7.so
%{_includedir}/HUpnpCore
