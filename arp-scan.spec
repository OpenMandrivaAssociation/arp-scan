Name:		arp-scan
Version:	1.7
Release:	%mkrel 1
Summary:	ARP scanning and fingerprinting tool
License:	BSD
Group:		Networking/Other
URL:		http://www.nta-monitor.com/tools/arp-scan
Source:	http://www.nta-monitor.com/tools/arp-scan/download/arp-scan-%{version}.tar.gz
BuildRequires:	pcap-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
arp-scan is a command-line tool that uses the ARP protocol to discover and
fingerprint IP hosts on the local network. It is available for Linux and BSD
under the GPL licence.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

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

