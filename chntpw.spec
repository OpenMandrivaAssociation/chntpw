Summary:	The Offline NT Password Editor
Name:		chntpw
Version:	0.99.3
Release:	4mdk
License:	BSD-like
Group:		File tools
URL:		http://home.eunet.no/~pnordahl/ntpasswd/
Source0:	%{name}-source-040818.tar.bz2
Patch:		chntpw_0.99.2-4.diff
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This little program will enable you to view some information and
change user passwords in a Windows NT SAM userdatabase file.
You do not need to know the old passwords.
However, you need to get at the file some way or another yourself.
In addition it contains a simple registry editor with full write support,
and hex-editor which enables you to
fiddle around with bits&bytes in the file as you wish yourself.

%prep

%setup -c -q -n %{name}-source-040818
%patch0 -p1

# fix attribs
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;

%build

make \
    CFLAGS="%{optflags} -DUSEOPENSSL -I. -I%{_includedir}" \
    LIBS="-L%{_libdir} -lcrypto"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man8

install -m0755 %{name} %{buildroot}%{_sbindir}/
install -m0644 debian/chntpw.8 %{buildroot}%{_mandir}/man8/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt
%{_sbindir}/%{name}
%{_mandir}/man8/chntpw.8*

