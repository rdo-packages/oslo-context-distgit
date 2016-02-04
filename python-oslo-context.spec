%global pypi_name oslo.context
%global pname oslo-context
%{!?_licensedir:%global license %%doc}

%if 0%{?fedora}
%global with_python3 1
%endif

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-oslo-context
Version:        0.6.0
Release:        3%{?dist}
Summary:        OpenStack Oslo Context library

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/oslo.context
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
The OpenStack Oslo context library has helpers to maintain
useful information about a request context.
The request context is usually populated in the
WSGI pipeline and used by various modules such as logging.

%package -n python2-oslo-context
Summary:        OpenStack Oslo Context library
%{?python_provide:%python_provide python2-%{pname}}

BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires:       python-babel

%description -n python2-oslo-context
The OpenStack Oslo context library has helpers to maintain
useful information about a request context.
The request context is usually populated in the
WSGI pipeline and used by various modules such as logging.

%package -n python2-oslo-context-doc
Summary:    Documentation for the OpenStack Oslo context library
%{?python_provide:%python_provide python2-%{pname}-doc}

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-fixtures

%description -n python2-oslo-context-doc

Documentation for the OpenStack Oslo context library.

# python3
%if 0%{?with_python3}
%package -n python3-oslo-context
Summary:        OpenStack Oslo Context library
%{?python_provide:%python_provide python3-%{pname}}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr

Requires:       python3-babel

%description -n python3-oslo-context
The OpenStack Oslo context library has helpers to maintain
useful information about a request context.
The request context is usually populated in the
WSGI pipeline and used by various modules such as logging.

%package -n python3-oslo-context-doc
Summary:        Documentation for the OpenStack Oslo context library
%{?python_provide:%python_provide python3-%{pname}}
BuildRequires:  python3-sphinx
BuildRequires:  python3-oslo-sphinx
BuildRequires:  python3-fixtures

%description -n python3-oslo-context-doc
Documentation for the OpenStack Oslo context library.
%endif

%prep
%setup -q -n %{pypi_name}-%{version}
rm -f requirements.txt

%build
%{__python2} setup.py build
# doc
export PYTHONPATH="$( pwd ):$PYTHONPATH"
%{__python2} setup.py build_sphinx
# Remove the sphinx-build leftovers
rm -fr doc/build/html/.{doctrees,buildinfo}

%if 0%{?with_python3}
%{__python3} setup.py build
export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build-3 -b html -d build/doctrees   source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo
%endif

%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%if 0%{?with_python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
%endif

%files -n python2-oslo-context
%license LICENSE
%doc README.rst
%{python2_sitelib}/oslo_context
%{python2_sitelib}/*.egg-info

%if 0%{?with_python3}
%files -n python3-oslo-context
%license LICENSE
%doc README.rst
%{python3_sitelib}/oslo_context
%{python3_sitelib}/*.egg-info
%endif

%files -n python2-oslo-context-doc
%license LICENSE
%doc doc/build/html

%if 0%{?with_python3}
%files -n python3-oslo-context-doc
%license LICENSE
%doc doc/build/html
%endif

%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Sep 18 2015 Alan Pevec <alan.pevec@redhat.com> 0.6.0-1
- Update to upstream 0.6.0

* Tue Sep 08 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 0.5.0-4
- Fix provides and drop workarounds

* Mon Sep 07 2015 Chandan Kumar <chkumar246@gmail.com> 0.5.0-3
- fix obseletes
- fix package namespaces

* Thu Sep 03 2015 Chandan Kumar <chkumar246@gmail.com> 0.5.0-2
- Added python2 and python3 subpackages

* Mon Aug 17 2015 Alan Pevec <alan.pevec@redhat.com> 0.5.0-1
- Update to upstream 0.5.0

* Mon Jun 29 2015 Alan Pevec <alan.pevec@redhat.com> 0.4.0-1
- Update to upstream 0.4.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 27 2015 Chandan Kumar <chkumar246@gmail.com> - 0.2.0-5
- Fixed Doc issue and added missing dependencies

* Wed Mar 25 2015 Chandan Kumar <chkumar246@gmail.com> - 0.2.0-4
- Fixed docs

* Tue Mar 24 2015 Chandan Kumar <chkumar246@gmail.com> - 0.2.0-3
- Fixes typo in spec file

* Tue Mar 24 2015 Chandan Kumar <chkumar246@gmail.com> - 0.2.0-2
- Added docs

* Thu Mar 12 2015 Chandan Kumar <chkumar246@gmail.com> - 0.2.0-1
- Updated the spec file for oslo-context 0.2.0 release

* Sat Dec 20 2014 Dan Prince <dprince@redhat.com> -XXX
- Initial package.
