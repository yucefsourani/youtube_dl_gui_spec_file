Name:          	python-twodict 
Version:        1.2
Release:        2%{?dist}
Summary:        Simple two way ordered dictionary for Python
License:        unlicense
URL:            https://github.com/MrS0m30n3/twodict
Source0:        https://github.com/MrS0m30n3/twodict/archive/master.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:	python2-rpm-macros

%description
Simple two way ordered dictionary for Python.


%prep
%autosetup -n twodict-master
touch __init__.py
echo "from twodict import *" > __init__.py

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{python2_sitelib}/twodict
cp twodict.py %{buildroot}%{python2_sitelib}/twodict/twodict.py
cp __init__.py %{buildroot}%{python2_sitelib}/twodict/__init__.py

%files
%license LICENSE
%doc README.md
# For noarch packages: sitelib
%{python2_sitelib}/*




%changelog
* Sun Nov 04 2018 youcefsourani <youssef.m.sourani@gmail.com> 1.2-2
- Release 2

* Wed Dec 13 2017 youcefsourani <youssef.m.sourani@gmail.com> 1.2-1
- Initial For fedora 27
