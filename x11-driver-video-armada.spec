%define snap    20150420

Summary:        X.org driver for KMS based systems
Name:           x11-driver-video-armada
Version:        0.0.0
Release:        0.%{snap}.1
Group:          System/X11
License:        MIT
Url:            http://xorg.freedesktop.org
# git clone http://ftp.arm.linux.org.uk/cgit/xf86-video-armada.git/ -b unstable-devel
Source0:        http://xorg.freedesktop.org/releases/individual/driver/xf86-video-armada-%{version}-%{snap}.tar.xz
Patch0:		xf86-video-armada-1.17.1-include-fix.patch

BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xorg-server)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(libdrm_armada)
Requires:       x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
%{name} is the X.org driver for Freescale and Armada devices.

%prep
%setup -qn xf86-video-armada-%{version}-%{snap}
%apply_patches

%build
autoreconf -fiv
%configure
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/etnadrm_gpu.so
%{_libdir}/xorg/modules/drivers/armada_drv.so
%{_libdir}/xorg/modules/drivers/etnaviv_gpu.so
%{_mandir}/man4/armada.*
