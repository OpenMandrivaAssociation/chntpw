Name: chntpw
Version: 1.0.2
Release: 1
Source0: https://github.com/minacle/chntpw/archive/refs/tags/v%{version}.tar.gz
Patch0:  5adc4f48aa4ef624d481ff45b28fc998d7a9f2d5.patch
Summary: Offline NT Password & Registry Editor
Url: https://github.com/minacle/chntpw
License: GPLv2
Group: Tools
BuildRequires: pkgconfig(openssl)
BuildRequires: cmake ninja

%description
Chntpw (also known as Offline NT Password & Registry Editor)
is a small Windows password removal utility.

%prep
%autosetup -p1

%cmake -G Ninja

%build
%ninja_build -C build

%install
mkdir -p %{buildroot}%{_bindir}
cd build && install -m 755 chntpw cpnt reged samusrgrp sampasswd %{buildroot}%{_bindir}/

%files
%{_bindir}/*
