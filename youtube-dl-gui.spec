%global debug_package %{nil}
Name:           youtube-dl-gui
Version:        0.4
Release:        2%{?dist}
Summary:        GUI For youtube-dl
License:        Unlicense
URL:            http://mrs0m30n3.github.io/youtube-dl-gui/
Source0:        https://github.com/MrS0m30n3/youtube-dl-gui/archive/master.tar.gz
Source1:        youtube-dl-gui.desktop
BuildRequires:  python2-devel
BuildRequires:  python2-rpm-macros
BuildRequires:  wxPython-devel
BuildRequires:  gettext
BuildRequires:  python-twodict
Requires:       python
Requires:       ffmpeg
Requires:       wxPython
Requires:       youtube-dl
Requires:       python-twodict
Provides:       youtube-dlG = %{version}-%{release}
Obsoletes:      youtube-dlG <= 0.4-1

%description
A cross platform front-end GUI of the popular youtube-dl written in wxPython.



%prep
%autosetup -n youtube-dl-gui-master

%build
%{__python2} setup.py build



%install
rm -rf $RPM_BUILD_ROOT
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/applications
cp %{SOURCE1} %{buildroot}%{_datadir}/applications
%find_lang  youtube_dl_gui



%files -f youtube_dl_gui.lang
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/youtube-dl-gui
%{_datadir}/applications/youtube-dl-gui.desktop
%{_datadir}/pixmaps/youtube-dl-gui.png
%{_datadir}/icons/hicolor/*/apps/youtube-dl-gui*
%{python_sitelib}/*

%changelog
* Sat Nov 03 2018 youcef sourani <youssef.m.sourani@gmail.com> - 0.4-2
- Release 2

* Wed Dec 13 2017 youcef sourani <youssef.m.sourani@gmail.com> - 0.4-1
- Update To v0.4

* Fri Oct 28 2016 youcef sourani <youssef.m.sourani@gmail.com> - 0.3.8-1
- Initial Package


