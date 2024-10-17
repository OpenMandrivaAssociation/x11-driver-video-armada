%define snap    20191215

Summary:        X.org driver for KMS based systems
Name:           x11-driver-video-armada
Version:        0.0.0
Release:        0.%{snap}.1
Group:          System/X11
License:        MIT
Url:            https://xorg.freedesktop.org
# git clone http://ftp.arm.linux.org.uk/cgit/xf86-video-armada.git/ -b unstable-devel
# git archive -o ~/x11-driver-video-armada/x11-driver-video-armada-20191215.tar --prefix x11-driver-video-armada-20191215/ origin/unstable-devel
Source0:        x11-driver-video-armada-20191215.tar.xz
Source1:	https://github.com/etnaviv/etna_viv/archive/master.tar.gz
Source2:	https://github.com/etnaviv/galcore_headers/archive/master/galcore.tar.gz

BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xorg-server)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(libdrm_armada)
BuildRequires:  pkgconfig(libfakedrm_etnaviv)
Requires:       x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
%{name} is the X.org driver for Freescale and Armada devices.

%prep
%setup -n x11-driver-video-armada-%{snap} -a 1 -a 2
%autopatch -p1

%build
autoreconf -fiv
%configure --with-etnaviv-source="$(pwd)/etna_viv-master" --with-libgal-include="$(pwd)/galcore_headers-master/include_v4" --disable-vivante
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/armada_drv.so
%{_libdir}/xorg/modules/drivers/etnadrm_gpu.so
%{_mandir}/man4/armada.*
