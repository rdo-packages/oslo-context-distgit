%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global pypi_name oslo.context
%global pkg_name oslo-context

%if 0%{?fedora} >= 24
%global with_python3 1
%endif

%global common_desc \
The OpenStack Oslo context library has helpers to maintain \
useful information about a request context. \
The request context is usually populated in the \
WSGI pipeline and used by various modules such as logging.

Name:           python-%{pkg_name}
Version:        XXX
Release:        XXX
Summary:        OpenStack Oslo Context library

License:        ASL 2.0
URL:            https://launchpad.net/oslo.context
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz

BuildArch:      noarch

%package -n python2-%{pkg_name}
Summary:        OpenStack Oslo Context library
%{?python_provide:%python_provide python2-%{pkg_name}}

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  git
BuildRequires:  openstack-macros

# test dependencies
BuildRequires:  python-hacking
BuildRequires:  python-oslotest
BuildRequires:  python-positional

Requires:       python-babel
Requires:       python-debtcollector >= 1.2.0
Requires:       python-positional
Requires:       python-pbr

%description -n python2-%{pkg_name}
%{common_desc}

%package -n python-%{pkg_name}-tests
Summary:   Tests for OpenStack Oslo context library

Requires:  python-%{pkg_name} = %{version}-%{release}

%description -n python-%{pkg_name}-tests
Tests for OpenStack Oslo context library

%package -n python-%{pkg_name}-doc
Summary:        Documentation for the OpenStack Oslo context library

BuildRequires:  python-sphinx
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-fixtures

%description -n python-%{pkg_name}-doc
Documentation for the OpenStack Oslo context library.

# python3
%if 0%{?with_python3}
%package -n python3-%{pkg_name}
Summary:        OpenStack Oslo Context library
%{?python_provide:%python_provide python3-%{pkg_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr

# test dependencies
BuildRequires:  python3-hacking
BuildRequires:  python3-oslotest
BuildRequires:  python3-positional

Requires:       python3-babel
Requires:       python3-debtcollector >= 1.2.0
Requires:       python3-positional
Requires:       python3-pbr

%description -n python3-%{pkg_name}
%{common_desc}

%endif

%if 0%{?with_python3}
%package -n python3-%{pkg_name}-tests
Summary:   Tests for OpenStack Oslo context library

Requires:  python3-%{pkg_name} = %{version}-%{release}

%description -n python3-%{pkg_name}-tests
Tests for OpenStack Oslo context library
%endif

%description
%{common_desc}

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git
%py_req_cleanup

%build
%py2_build

# doc
%{__python2} setup.py build_sphinx
# Remove the sphinx-build leftovers
rm -fr doc/build/html/.{doctrees,buildinfo}

%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install

%if 0%{?with_python3}
%py3_install
%endif

%check
%{__python2} setup.py test
%if 0%{?with_python3}
rm -rf .testrepository
%{__python3} setup.py test
%endif


%files -n python2-%{pkg_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/oslo_context
%{python2_sitelib}/*.egg-info
%exclude %{python2_sitelib}/oslo_context/tests

%if 0%{?with_python3}
%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/oslo_context
%{python3_sitelib}/*.egg-info
%exclude %{python3_sitelib}/oslo_context/tests
%endif

%files -n python-%{pkg_name}-doc
%license LICENSE
%doc doc/build/html

%files -n python-%{pkg_name}-tests
%license LICENSE
%{python2_sitelib}/oslo_context/tests

%if 0%{?with_python3}
%files -n python3-%{pkg_name}-tests
%license LICENSE
%{python3_sitelib}/oslo_context/tests
%endif

%changelog
