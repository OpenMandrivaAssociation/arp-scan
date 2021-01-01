Name:		arp-scan
Version:	1.9.7
Release:	1
Summary:	ARP scanning and fingerprinting tool
License:	BSD
Group:		Networking/Other
URL:		http://www.nta-monitor.com/tools/arp-scan
Source:		https://github.com/royhills/arp-scan/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pcap-devel

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
%{_mandir}/man1/arp-fingerprint.1*
%{_mandir}/man1/arp-scan.1*
%{_mandir}/man1/get-iab.1*
%{_mandir}/man1/get-oui.1*
%{_mandir}/man5/mac-vendor.5*
