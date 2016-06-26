#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : irqbalance
Version  : 1.1.0
Release  : 1
URL      : https://github.com/Irqbalance/irqbalance/archive/v1.1.0.tar.gz
Source0  : https://github.com/Irqbalance/irqbalance/archive/v1.1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: irqbalance-bin
Requires: irqbalance-doc
BuildRequires : numactl-dev
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libcap-ng)

%description
What is Irqbalance
==================
Irqbalance is a daemon to help balance the cpu load generated by interrupts
across all of a systems cpus.  Irqbalance identifies the highest volume
interrupt sources, and isolates them to a single unique cpu, so that load is
spread as much as possible over an entire processor set, while minimizing cache
miss rates for irq handlers.

%package bin
Summary: bin components for the irqbalance package.
Group: Binaries

%description bin
bin components for the irqbalance package.


%package doc
Summary: doc components for the irqbalance package.
Group: Documentation

%description doc
doc components for the irqbalance package.


%prep
%setup -q -n irqbalance-1.1.0

%build
export LANG=C
%autogen --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/irqbalance

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
