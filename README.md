
# About this fork

This fork attempts to revive lightly with a different approach from boehs, with the assumption that Luwx won't ever resume his project.

This means that this fork allows real changes, and not just maintainence.

![Lightly](https://github.com/user-attachments/assets/ae39fc7f-8277-48b1-b80c-9e307542b8b0)


## The to-do list

- [x] Make a new readme
- [x] Make install work on plasma 6
- [ ] Find ~~some~~ more people that can help with this project
- [ ] Build some community
- [ ] Make some meaningful commits
- [ ] Expand to-do list


## My plans for changes at the moment -- They are in progress, I'm just really slow
- [x] Redesign the tabbar
  - [ ] Fix the issues I caused with it
  - [x] Align it a little better, ~~now it's slightly too left,~~ it needs slightly larger margins for ~~both sides~~ the right side
  - [x] You can now set the old tabbar back if you dont like the new one in the settings
- [ ] Make the buttons sligthly larger
  - [x] The standard push button is now slightly larger
  - [x] Spinboxes and comboboxes
  - [x] Now the size of the buttons is adjustable by the user in the settings
- [x] Change the defaults to fit the normal use-cases better
- [x] Add my own colorscheme to it
- [ ] Use [klassy](https://github.com/paulmcauley/klassy) for window decorations (I don't know how to use make / cmake, so it'll take a while)
- [ ] Make installation in all major distros easy
  - [x] Can be built on most distros that support plasma 6 
- [ ] Rename the project to something like „Darkly” to reflect the changes, and for it to be installable alongside the other lightly
- [ ] Maintain the project

## Installation
## Automatic
### Thanks to @DeltaCopy, you can use one of these install methods:

#### Fedora copr

<https://copr.fedorainfracloud.org/coprs/deltacopy/lightly-qt6/>

#### AUR

<https://aur.archlinux.org/packages/lightly-qt6>

#### Pre-built packages

<https://github.com/Bali10050/Lightly/releases>


## Manual

#### Arch Linux

```
sudo pacman -S cmake extra-cmake-modules kdecoration qt6-declarative kcoreaddons kcmutils kcolorscheme kconfig kguiaddons kiconthemes kwindowsystem git
```
```
git clone --single-branch --depth=1 https://github.com/Bali10050/Lightly.git
cd Lightly && mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=lib -DBUILD_TESTING=OFF ..
cd ./kdecoration/config/
make -j $(nproc)
cd ../../
make -j $(nproc)
sudo make install
```

***

#### Fedora

#####  Fedora 40

```
sudo dnf install -y git cmake extra-cmake-modules "cmake(KDecoration2)" kwin-devel \
    kf6-kcolorscheme-devel kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel \
    kf6-kirigami-devel kf6-kcmutils-devel kf6-frameworkintegration-devel
```
```
git clone --single-branch --depth=1 https://github.com/Bali10050/Lightly.git
cd Lightly && mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=lib64 -DBUILD_TESTING=OFF ..
cd ./kdecoration/config/
make -j $(nproc)
cd ../../
make -j $(nproc)
sudo make install
```

***
#### openSUSE Tumbleweed

```
sudo zypper in --no-recommends ninja cmake kf6-extra-cmake-modules kf6-kconfig-devel kf6-frameworkintegration-devel gmp-ecm-devel kf6-kconfigwidgets-devel kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kwindowsystem-devel kf6-kcolorscheme-devel kf6-kcoreaddons-devel kf6-kcmutils-devel kcmutils qt6-quick-devel kf6-kirigami-devel qt6-base-devel kdecoration6-devel  qt6-tools qt6-widgets-devel gcc-c++ extra-cmake-modules libQt5Gui-devel libQt5DBus-devel libqt5-qttools-devel libqt5-qtx11extras-devel libQt5OpenGL-devel libQt5Network-devel libepoxy-devel kconfig-devel kconfigwidgets-devel kcrash-devel kglobalaccel-devel ki18n-devel kio-devel kservice-devel kinit-devel knotifications-devel kwindowsystem-devel kguiaddons-devel kiconthemes-devel kpackage-devel kwin5-devel xcb-util-devel xcb-util-cursor-devel xcb-util-wm-devel xcb-util-keysyms-devel git
```
```
git clone --single-branch --depth=1 https://github.com/Bali10050/Lightly.git
cd Lightly && mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=lib64 -DBUILD_TESTING=OFF ..
cd ./kdecoration/config/
make -j $(nproc)
cd ../../
make -j $(nproc)
sudo make install
```
***


#### KDE neon
```
sudo apt install git build-essential cmake kf6-extra-cmake-modules kf6-extra-cmake-modules kf6-frameworkintegration-dev kf6-kcmutils-dev kf6-kcolorscheme-dev kf6-kconfig-dev kf6-kconfigwidgets-dev kf6-kcoreaddons-dev kf6-kguiaddons-dev kf6-ki18n-dev kf6-kiconthemes-dev kf6-kirigami2-dev kf6-kpackage-dev kf6-kservice-dev kf6-kwindowsystem-dev kirigami2-dev kwayland-dev libx11-dev libkdecorations2-dev libkf5config-dev libkf5configwidgets-dev libkf5coreaddons-dev libkf5guiaddons-dev libkf5i18n-dev libkf5iconthemes-dev libkf5kcmutils-dev libkf5package-dev libkf5service-dev libkf5style-dev libkf5wayland-dev libkf5windowsystem-dev libplasma-dev libqt5x11extras5-dev qt6-base-dev qt6-declarative-dev qtbase5-dev qtdeclarative5-dev gettext qt6-svg-dev extra-cmake-modules qt3d5-dev
```
```
git clone --single-branch --depth=1 https://github.com/Bali10050/Lightly.git
cd Lightly && mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=lib -DBUILD_TESTING=OFF ..
cd ./kdecoration/config/
make -j $(nproc)
cd ../../
make -j $(nproc)
sudo make install
```
***


#### Distrobox (Fedora 40)
```
distrobox create --name lightly --image fedora-toolbox:40
distrobox enter lightly
```

```
sudo dnf install -y cmake extra-cmake-modules "cmake(KDecoration2)" kwin-devel \
    kf6-kcolorscheme-devel kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel \
    kf6-kirigami-devel kf6-kcmutils-devel

git clone --single-branch --depth=1 https://github.com/Bali10050/Lightly.git
cd Lightly
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=$HOME/.local \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_INSTALL_LIBDIR=lib64 \
      -DBUILD_TESTING=OFF ..

cd ./kdecoration/config/
make -j $(nproc)
cd ../../
make -j $(nproc)
make install
```

Set environment variable on plasma startup:
```
echo "export QT_PLUGIN_PATH=$HOME/.local/lib64/plugins:\$QT_PLUGIN_PATH" > $HOME/.config/plasma-workspace/env/localthemes.sh && chmod +x $HOME/.config/plasma-workspace/env/localthemes.sh
```
***

## Known issues & solutions

### Blurred icon rendering on Wayland with fractional scaling

As referenced in https://github.com/Bali10050/Lightly/issues/14

On Wayland when scaling is set to >100% some icons appear blurred.

The fix for now until QT is updated is to add `QT_SCALE_FACTOR_ROUNDING_POLICY=RoundPreferFloor` into the file `/etc/environment`

Restart to apply the changes.

For further details see: https://bugs.kde.org/show_bug.cgi?id=479891
