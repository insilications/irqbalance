#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : irqbalance
Version  : 1.6.0
Release  : 16
URL      : https://github.com/Irqbalance/irqbalance/archive/v1.6.0/irqbalance-1.6.0.tar.gz
Source0  : https://github.com/Irqbalance/irqbalance/archive/v1.6.0/irqbalance-1.6.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: irqbalance-autostart = %{version}-%{release}
Requires: irqbalance-bin = %{version}-%{release}
Requires: irqbalance-license = %{version}-%{release}
Requires: irqbalance-man = %{version}-%{release}
Requires: irqbalance-services = %{version}-%{release}
BuildRequires : numactl-dev
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libcap-ng)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(ncursesw)
Patch1: 0001-Run-irqbalance-as-oneshot-by-default-without-env.patch

%description
What is Irqbalance
==================
Irqbalance is a daemon to help balance the cpu load generated by interrupts
across all of a systems cpus.  Irqbalance identifies the highest volume
interrupt sources, and isolates them to a single unique cpu, so that load is
spread as much as possible over an entire processor set, while minimizing cache
miss rates for irq handlers.

%package autostart
Summary: autostart components for the irqbalance package.
Group: Default

%description autostart
autostart components for the irqbalance package.


%package bin
Summary: bin components for the irqbalance package.
Group: Binaries
Requires: irqbalance-license = %{version}-%{release}
Requires: irqbalance-services = %{version}-%{release}

%description bin
bin components for the irqbalance package.


%package license
Summary: license components for the irqbalance package.
Group: Default

%description license
license components for the irqbalance package.


%package man
Summary: man components for the irqbalance package.
Group: Default

%description man
man components for the irqbalance package.


%package services
Summary: services components for the irqbalance package.
Group: Systemd services

%description services
services components for the irqbalance package.


%prep
%setup -q -n irqbalance-1.6.0
cd %{_builddir}/irqbalance-1.6.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579118057
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1579118057
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/irqbalance
cp %{_builddir}/irqbalance-1.6.0/COPYING %{buildroot}/usr/share/package-licenses/irqbalance/dfac199a7539a404407098a2541b9482279f690d
%make_install
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
install -m0644 misc/irqbalance.service %{buildroot}/usr/lib/systemd/system/
ln -s ../irqbalance.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/irqbalance.service
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/irqbalance.service

%files bin
%defattr(-,root,root,-)
/usr/bin/irqbalance
/usr/bin/irqbalance-ui

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/irqbalance/dfac199a7539a404407098a2541b9482279f690d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/irqbalance.1

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/irqbalance.service
/usr/lib/systemd/system/irqbalance.service
