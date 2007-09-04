Name: libnes
Version: 0.5
Release: 0.1.ofed20070823
Summary: NetEffect RNIC Userspace Library

Group: System Environment/Libraries
License: GPL/BSD
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/libnes-0.5-0.1.ofed20070823.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: libibverbs-devel

%description
libnes provides a device-specific userspace driver for NetEffect RNICs
for use with the libibverbs library.

%package devel-static
Summary: Development files for the libnes driver
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description devel-static
Static version of libnes that may be linked directly to an
application, which may be useful for debugging.

%prep
%setup -q -n %{name}-0.5

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot} install
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la $RPM_BUILD_ROOT%{_libdir}/libnes.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/libnes*.so
%{_sysconfdir}/libibverbs.d/nes.driver
%doc AUTHORS COPYING

%files devel-static
%defattr(-,root,root,-)
%{_libdir}/libnes*.a

%changelog
* Wed Aug 29 2007 Glenn Grundstrom <ggrundstrom@neteffect.com> - 0.5
- Updated for OFED-1.3

* Fri Feb 16 2007 Glenn Grundstrom <ggrundstrom@neteffect.com> - 0.3
- Updated for OFED-1.2

* Wed May 10 2006 Glenn Grundstrom <ggrundstrom@neteffect.com> - 0.1
- First development effort
