# Specfile used inside Github Action workflow opensuse-tw-ci

%global kf6_version 6
%define _qt_major_version 6
%define dev Bali10050
%define style Lightly
%define _style lightly

Name:           lightly
Version:        ${TAG}  # this line gets updated automatically by Github Actions inside workflow opensuse-tw-ci
Release:        0
Summary:        A modern style for qt applications
License:        GPL-3.0-or-later
URL:            https://github.com/%{dev}/%{style}
Source0:        https://github.com/%{dev}/%{style}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KDecoration2) >= 6.0
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6FrameworkIntegration) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KWayland) >= 6.0
BuildRequires:  cmake(Plasma) >= 6.0
BuildRequires:  cmake(Qt6DBus) >= %{_qt_major_version}
BuildRequires:  cmake(Qt6Quick) >= %{_qt_major_version}
BuildRequires:  cmake(Qt6Widgets) >= %{_qt_major_version}
BuildRequires:  pkgconfig(xcb)

%description
Lightly is a fork of breeze theme style that aims to be visually modern and minimalistic.

%prep
%autosetup -p1 -n Lightly-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%files
%license COPYING
%doc AUTHORS README.md

%{_bindir}/lightly-settings%{_qt_major_version}

%{_libdir}/cmake/%{style}/
%{_libdir}/lib%{_style}common%{_qt_major_version}.so.*

%{_kf6_plugindir}/kstyle_config/%{_style}styleconfig.so
%{_kf6_plugindir}/org.kde.kdecoration2/org.kde.%{_style}.so
%{_kf6_plugindir}/org.kde.kdecoration2.kcm/kcm_%{_style}decoration.so
%{_kf6_plugindir}/styles/%{_style}%{_qt_major_version}.so

%{_datadir}/applications/kcm_%{_style}decoration.desktop
%{_datadir}/applications/%{_style}styleconfig.desktop
%{_datadir}/color-schemes/%{style}.colors
%{_datadir}/icons/hicolor/scalable/apps/%{_style}-settings.svgz
%{_datadir}/kservices%{_qt_major_version}/%{_style}decorationconfig.desktop
%{_datadir}/kstyle/themes/%{_style}.themerc

%changelog
