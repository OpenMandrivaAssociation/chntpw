%define snap 080526

Summary:	The Offline NT Password Editor
Name:		chntpw
Version:	0.99.6
Release:	%mkrel 4
License:	GPL
Group:		File tools
URL:		http://home.eunet.no/~pnordahl/ntpasswd/
Source0:	http://home.eunet.no/~pnordahl/ntpasswd/chntpw-source-%{snap}.zip
Source1:	chntpw.8
BuildRequires:	openssl-devel
BuildRequires:	openssl-static-devel
BuildRequires:	glibc-static-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This little program will enable you to view some information and change user
passwords in a Windows NT SAM userdatabase file. You do not need to know the
old passwords. However, you need to get at the file some way or another
yourself. In addition it contains a simple registry editor with full write
support, and hex-editor which enables you to fiddle around with bits&bytes in
the file as you wish yourself.

%package -n	reged
Summary:	Simple Registry Edit Utility
Group:		File tools

%description -n	reged
This program is a command line utility to export of registry to .reg files.

%prep

%setup -q -n chntpw-%{snap}

cp %{SOURCE1} chntpw.8

# fix attribs
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;

%build
%serverbuild

make \
    CFLAGS="$CFLAGS -DUSEOPENSSL -I. -I%{_includedir}  -Wall" \
    OSSLLIB=%{_libdir} \
    LIBS="-L%{_libdir} -lcrypto"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man8

install -m0755 %{name} %{buildroot}%{_sbindir}/
install -m0755 %{name}.static %{buildroot}%{_sbindir}/
install -m0755 reged %{buildroot}%{_sbindir}/
install -m0755 reged.static %{buildroot}%{_sbindir}/
install -m0644 chntpw.8 %{buildroot}%{_mandir}/man8/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc HISTORY.txt README.txt regedit.txt
%{_sbindir}/%{name}*
%{_mandir}/man8/chntpw.8*

%files -n reged
%defattr(-,root,root)
%{_sbindir}/reged*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.99.6-4mdv2011.0
+ Revision: 610137
- rebuild

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 0.99.6-3mdv2010.1
+ Revision: 537505
- rebuild

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.99.6-2mdv2010.0
+ Revision: 424834
- rebuild

* Fri Jun 13 2008 Oden Eriksson <oeriksson@mandriva.com> 0.99.6-1mdv2009.0
+ Revision: 218800
- fix deps
- 0.99.6 (080526)
- added the reged sub package

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jun 26 2007 Oden Eriksson <oeriksson@mandriva.com> 0.99.4-1mdv2008.0
+ Revision: 44711
- 0.99.4
- use the %%mkrel and %%serverbuild macros
- drop upstream patches; P0
- added just the man page from the debian patch


* Fri Mar 17 2006 Oden Eriksson <oeriksson@mandriva.com> 0.99.3-4mdk
- rebuilt against openssl-0.9.8a

* Fri Sep 09 2005 Oden Eriksson <oeriksson@mandriva.com> 0.99.3-3mdk
- added P0 to make it compile again (debian)

* Wed Aug 25 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.99.3-2mdk
- fix group

* Wed Aug 25 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.99.3-1mdk
- initial mandrake package

