%define 	module	psutil
Summary:	Cross-platform process and system utilities module for Python
Name:		python-%{module}
Version:	1.2.1
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/p/psutil/%{module}-%{version}.tar.gz
# Source0-md5:	80c3b251389771ab472e554e6c729c36
URL:		http://code.google.com/p/psutil/
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module providing an interface for retrieving information on all
running processes and system utilization (CPU, disk, memory, network)
in a portable way by using Python, implementing many functionalities
offered by command line tools.

%package -n python3-%{module}
Summary:	Cross-platform process and system utilities module for Python
Group:		Development/Languages/Python
Requires:	python3-modules

%description -n python3-%{module}
Module providing an interface for retrieving information on all
running processes and system utilization (CPU, disk, memory, network)
in a portable way by using Python, implementing many functionalities
offered by command line tools.

%prep
%setup -qn %{module}-%{version}

%build
export CC="%{__cc}"
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build -b python
%{__python3} setup.py build -b python3

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py build -b python install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%{__python3} setup.py build -b python3 install \
	--optimize=2		\
	--root=$RPM_BUILD_ROOT	\
	--skip-build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS README

%{py_sitedir}/%{module}
%attr(755,root,root) %{py_sitedir}/_psutil_linux.so
%attr(755,root,root) %{py_sitedir}/_psutil_posix.so
%{py_sitedir}/%{module}-*.egg-info

%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitedir}/%{module}
%attr(755,root,root) %{py3_sitedir}/_psutil_linux.*.so
%attr(755,root,root) %{py3_sitedir}/_psutil_posix.*.so
%{py3_sitedir}/%{module}-*.egg-info
