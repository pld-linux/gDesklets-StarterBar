%define	pname	StarterBar
%define	pver	0_1
Summary:	An icon bar for GNOME
Summary(pl):	Pasek na ikony dla GNOME
Name:		gDesklets-%{pname}
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.pycage.de/download/gdesklets/%{pname}-%{pver}.tar.bz2
# Source0-md5:	47ddce700300f59a6fdfc2d619fb66a8
URL:		http://www.pycage.de/software_gdesklets.html
Buildrequires:	python >= 2.3
Requires:	gDesklets
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An icon bar for GNOME. You can do the same with the GNOME panel, but
this one is pure eye candy.

%description -l pl
Pasek na ikony dla GNOME. Takie mo¿liwo¶ci ma tak¿e panel GNOME, ale
ten jest mi³y dla oka.

%prep
%setup -q -n %{pname}
tail -c 10240 Install_StarterBar_Sensor.bin 2>&1 | tar -xz 2>&1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gdesklets/{Sensors,Displays/%{pname}}

cp -R StarterBar $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors
cp -R gfx *.display $RPM_BUILD_ROOT%{_datadir}/gdesklets/Displays/%{pname}

%py_comp $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors

rm -f $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/gdesklets/Sensors/*
%{_datadir}/gdesklets/Displays/*
