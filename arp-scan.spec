Name:		arp-scan
Version:	1.10.0
Release:	1
Summary:	ARP scanning and fingerprinting tool
License:	BSD
Group:		Networking/Other
URL:		https://github.com/royhills/arp-scan
Source:		https://github.com/royhills/arp-scan/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	pcap-devel
BuildRequires:	pkgconfig(libcap)

%description
arp-scan is a command-line tool that uses the ARP protocol to discover and
fingerprint IP hosts on the local network. It is available for Linux and BSD
under the GPL licence.

%prep
%autosetup -p1
autoheader
%configure

%build
%make_build

%install
%make_install

%files
%defattr(-,root,root)
%{_bindir}/arp-fingerprint
%{_bindir}/arp-scan
%{_bindir}/get-iab
%{_bindir}/get-oui
%{_datadir}/arp-scan
%config(noreplace) %{_sysconfdir}/arp-scan/mac-vendor.txt
%{_mandir}/man1/arp-fingerprint.1*
%{_mandir}/man1/arp-scan.1*
%{_mandir}/man1/get-oui.1*
%{_mandir}/man5/mac-vendor.5*
