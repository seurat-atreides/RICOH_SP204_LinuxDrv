#
# spec file for Ricoh Aficio SP1xx and 2xx printers
#
# Copyright (c) 2014 James Bottomley
#
Name:           RicohAficioSP1xx-2xx-PPD
Version:        0.3.1.g0678958
Release:        lp155.1.4
Summary:        Ricoh Aficio SP 100 and SP 204 PPD and filters
License:        MIT
Group:          Hardware/Printing
Url:            https://github.com/madlynx/ricoh-sp100
Source:         %{name}-%{version}.tar.gz
Patch1:		0001-pstoricohddst-gdi-Implement-dot-counts.patch
Patch2:		0002-pstoricohddst-gdi-make-DEBUG-an-environment-variable.patch
Patch3:		0003-sp204-add-hack-to-make-cartridges-last-longer.patch
Patch4:		0004-sp204-add-dNOSAFER-to-gs.patch
BuildArch:	noarch

BuildRequires:	cups

Requires:	jbigkit
Requires:	ImageMagick
Requires:	ghostscript


%description

PPD files and filters for the DDST printers in the Ricoh Aficio SP 1xx and 2xx
series of windows only printers

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build

%check

##
# Have to ignore the filters here, because it fails if not root owned
##
for f in `find %{buildroot}/usr/share/cups/model/RicohAficioSP1xx-2xx-PPDs -name \*.ppd -print`; do
    cupstestppd -R %{buildroot} -I filters $f
done

%install
install -d %{buildroot}/usr/lib/cups/filter/
install -m 0555 pstoricohddst-gdi %{buildroot}/usr/lib/cups/filter/
install -d %{buildroot}/usr/share/cups/model/RicohAficioSP1xx-2xx-PPDs/ricoh/
install -m 0644 RICOH_Aficio_SP_100.ppd %{buildroot}/usr/share/cups/model/RicohAficioSP1xx-2xx-PPDs/ricoh/
install -m 0644 RICOH_Aficio_SP_204.ppd %{buildroot}/usr/share/cups/model/RicohAficioSP1xx-2xx-PPDs/ricoh/

%files
%defattr(-,root,root,755)
%dir /usr/lib/cups
/usr/lib/cups
%dir /usr/share/cups
/usr/share/cups

%changelog
* Tue Jul 22 2014 James.Bottomley@HansenPartnership.com
- Initial add
