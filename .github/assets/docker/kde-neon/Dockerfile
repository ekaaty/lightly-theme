FROM invent-registry.kde.org/neon/docker-images/plasma:user
MAINTAINER DeltaCopy
USER root
RUN apt-get update && \
    apt-get dist-upgrade -y --allow-downgrades && \
    apt-get install -y -qq checkinstall git build-essential cmake kf6-extra-cmake-modules \
            kf6-frameworkintegration-dev kf6-kcmutils-dev kf6-kcolorscheme-dev kf6-kconfig-dev \
            kf6-kconfigwidgets-dev kf6-kcoreaddons-dev kf6-kguiaddons-dev kf6-ki18n-dev \
            kf6-kiconthemes-dev kf6-kirigami2-dev kf6-kpackage-dev kf6-kservice-dev \
            kf6-kwindowsystem-dev kirigami2-dev kwayland-dev libx11-dev \
            libkdecorations2-dev libplasma-dev qt6-base-dev qt6-declarative-dev \
            gettext qt6-svg-dev extra-cmake-modules qt3d5-dev && \
    userdel neon
