# Credits: hazel-bunny (https://github.com/hazel-bunny)
# Specfile used inside workflow fedora-ci
%define style Lightly
%define _style lightly
%define dev Bali10050
%define _qt_major_version 6
%define release_tag ${TAG} # this line gets updated automatically by Github Actions inside workflow fedora-ci
%define forgeurl https://github.com/%{dev}/%{style}/archive/refs/tags/%{release_tag}.tar.gz
%define version %{release_tag}
%forgemeta

Name:           %{_style}-qt%{_qt_major_version}
Version:        %{version}
Release:        1%{?dist}
Summary:        A modern style for qt applications
License:        GPL-2.0-or-later
Group:          System/GUI/KDE

URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 5.240.0

BuildRequires:  kf%{_qt_major_version}-rpm-macros
BuildRequires:  kf%{_qt_major_version}-filesystem

BuildRequires:  cmake(Qt%{_qt_major_version}Core)
BuildRequires:  cmake(Qt%{_qt_major_version}DBus)
BuildRequires:  cmake(Qt%{_qt_major_version}Gui)
BuildRequires:  cmake(Qt%{_qt_major_version}Quick)
BuildRequires:  cmake(Qt%{_qt_major_version}UiTools)
BuildRequires:  cmake(Qt%{_qt_major_version}Widgets)

BuildRequires:  cmake(KF%{_qt_major_version}CoreAddons)
BuildRequires:  cmake(KF%{_qt_major_version}Config)
BuildRequires:  cmake(KF%{_qt_major_version}ConfigWidgets)
BuildRequires:  cmake(KF%{_qt_major_version}Crash)
BuildRequires:  cmake(KF%{_qt_major_version}FrameworkIntegration)
BuildRequires:  cmake(KF%{_qt_major_version}GuiAddons)
BuildRequires:  cmake(KF%{_qt_major_version}GlobalAccel)
BuildRequires:  cmake(KF%{_qt_major_version}I18n)
BuildRequires:  cmake(KF%{_qt_major_version}IconThemes)
BuildRequires:  cmake(KF%{_qt_major_version}KCMUtils)
BuildRequires:  cmake(KF%{_qt_major_version}KIO)
BuildRequires:  cmake(KF%{_qt_major_version}Kirigami2)
BuildRequires:  cmake(KF%{_qt_major_version}Notifications)
BuildRequires:  cmake(KF%{_qt_major_version}Package)
BuildRequires:  cmake(KF%{_qt_major_version}WindowSystem)

BuildRequires:  cmake(KDecoration2)
BuildRequires:  cmake(KWayland)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Plasma5Support)

BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)

BuildRequires:  kwin-devel
BuildRequires:  libepoxy-devel
BuildRequires:  kf%{_qt_major_version}-kpackage-devel

Obsoletes:      %{_style} <= %{version}

%description
Lightly is a fork of breeze theme style that aims to be visually modern and minimalistic.

%prep
%forgeautosetup -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION=%{_qt_major_version}
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc AUTHORS README.md

%{_bindir}/lightly-settings%{_qt_major_version}

%{_libdir}/cmake/%{style}/
%{_libdir}/lib%{_style}common%{_qt_major_version}.so.*

%{_qt6_plugindir}/kstyle_config/%{_style}styleconfig.so
%{_qt6_plugindir}/org.kde.kdecoration2/org.kde.%{_style}.so
%{_qt6_plugindir}/org.kde.kdecoration2.kcm/kcm_%{_style}decoration.so
%{_qt6_plugindir}/styles/%{_style}%{_qt_major_version}.so

%{_datadir}/applications/kcm_%{_style}decoration.desktop
%{_datadir}/applications/%{_style}styleconfig.desktop
%{_datadir}/color-schemes/%{style}.colors
%{_datadir}/icons/hicolor/scalable/apps/%{_style}-settings.svgz
%{_datadir}/kservices%{_qt_major_version}/%{_style}decorationconfig.desktop
%{_datadir}/kstyle/themes/%{_style}.themerc

%changelog
%autochangelog
