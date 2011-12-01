%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-transaction
Version:        1.0.1
Release:        1%{?dist}
Summary:        Transaction management for Python

Group:          Development/Languages
License:        ZPLv2.1
URL:            http://pypi.python.org/pypi/transaction
Source0:        http://pypi.python.org/packages/source/t/transaction/transaction-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-zope-interface

%description
This package contains a generic transaction implementation for Python. It is
mainly used by the ZODB, though.


%prep
%setup -q -n transaction-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.txt LICENSE.txt COPYRIGHT.txt
%{python_sitelib}/transaction/
%{python_sitelib}/*.egg-info



%changelog
* Mon Jun 28 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.1-1
- 1.0.1
- use %%global rather than %%define

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Luke Macken <lmacken@redhat.com> - 1.0-0.3.a1
- Fix the license tag

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0-0.2.a1
- Rebuild for Python 2.6

* Tue Oct 21 2008 Luke Macken <lmacken@redhat.com> - 1.0-0.1.a2
- Initial package
