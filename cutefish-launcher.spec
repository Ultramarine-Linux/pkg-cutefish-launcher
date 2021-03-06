%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

%define component_name launcher

Name: cutefish-%{component_name}
Version: 0.7
Release: 1%{?dist}
License: GPLv3
Summary: Application launcher for Cutefish Desktop

BuildRequires: cmake
BuildRequires: qt5-qtbase-devel qt5-qttools qt5-qttools-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel qt5-linguist qt5-qtx11extras-devel
BuildRequires: kf5-kwindowsystem-devel

Source0: https://github.com/cutefishos/%{component_name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
Cutefish Desktop's full-screen application launcher

%prep
%setup -qn %{component_name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
