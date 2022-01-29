Name: chntpw
Version: 140201
Release: 1
Source0: http://pogostick.net/~pnh/ntpasswd/chntpw-source-%{version}.zip
Source1: chntpw.8
Summary: Tool for resetting Windows passwords
Url: http://pogostick.net/~pnh/ntpasswd
License: GPLv2
Group: Tools
BuildRequires: pkgconfig(openssl)
BuildRequires: make

%description
Tool for resetting Windows passwords.

This can be useful when recovering a Windows installation from
a booted Live Linux image, or on dual boot systems.

%prep
%autosetup -p1
%make_build clean

%build
%make_build chntpw cpnt reged samusrgrp sampasswd CC=%{__cc} CFLAGS="%{optflags} -DUSEOPENSSL" OSSLLIB="%{_libdir}"

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man8
install -m 755 chntpw cpnt reged samusrgrp sampasswd %{buildroot}%{_bindir}/
install -c -m 644 %{S:1} %{buildroot}%{_mandir}/man8/

%files
%{_bindir}/*
%{_mandir}/man8/chntpw.8*
