# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global pypi_name oslo.context
%global pkg_name oslo-context
%global with_doc 1

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

BuildRequires:  git
BuildRequires:  openstack-macros

%package -n python%{pyver}-%{pkg_name}
Summary:        OpenStack Oslo Context library
%{?python_provide:%python_provide python%{pyver}-%{pkg_name}}

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
# test dependencies
BuildRequires:  python%{pyver}-fixtures
BuildRequires:  python%{pyver}-hacking
BuildRequires:  python%{pyver}-oslotest

Requires:       python%{pyver}-debtcollector >= 1.2.0
Requires:       python%{pyver}-pbr

%description -n python%{pyver}-%{pkg_name}
%{common_desc}

%package -n python%{pyver}-%{pkg_name}-tests
Summary:   Tests for OpenStack Oslo context library

Requires:  python%{pyver}-%{pkg_name} = %{version}-%{release}

%description -n python%{pyver}-%{pkg_name}-tests
Tests for OpenStack Oslo context library

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:        Documentation for the OpenStack Oslo context library

BuildRequires:  python%{pyver}-sphinx
BuildRequires:  python%{pyver}-openstackdocstheme

%description -n python-%{pkg_name}-doc
Documentation for the OpenStack Oslo context library.
%endif

%description
%{common_desc}

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git
%py_req_cleanup

%build
%{pyver_build}

%if 0%{?with_doc}
# doc
%{pyver_bin} setup.py build_sphinx
# Remove the sphinx-build-%{pyver} leftovers
rm -fr doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{pyver_install}

%check
%{pyver_bin} setup.py test

%files -n python%{pyver}-%{pkg_name}
%license LICENSE
%doc README.rst
%{pyver_sitelib}/oslo_context
%{pyver_sitelib}/*.egg-info
%exclude %{pyver_sitelib}/oslo_context/tests

%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%license LICENSE
%doc doc/build/html
%endif

%files -n python%{pyver}-%{pkg_name}-tests
%license LICENSE
%{pyver_sitelib}/oslo_context/tests

%changelog
# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/oslo.context/commit/?id=b91a48513937d60c64dd09e0c0f84283f8d4863e
