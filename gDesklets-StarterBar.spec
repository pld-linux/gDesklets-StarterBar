%define	pname	StarterBar
Summary:	An icon bar for GNOME
Summary(pl):	Pasek na ikony dla GNOME
Name:		gDesklets-%{pname}
Version:	0.11
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.pycage.de/download/gdesklets/starterbar-desklet-%{version}.tar.bz2
# Source0-md5:	4a9143a5d24d78f5fd1d9a5c7a72c2b8
URL:		http://www.pycage.de/software_gdesklets.html
Buildrequires:	python >= 2.3
BuildRequires:	python-pygtk >= 1.99.14
Requires:	gDesklets
Provides:	gDesklets-display
Provides:	gDesklets-sensor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_sensorsdir	%{_datadir}/gdesklets/Sensors
%define	_displaysdir	%{_datadir}/gdesklets/Displays

%description
An icon bar for GNOME. You can do the same with the GNOME panel, but
this one is pure eye candy.

%description -l pl
Pasek na ikony dla GNOME. Takie mo¿liwo¶ci ma tak¿e panel GNOME, ale
ten jest mi³y dla oka.

%prep
%setup -q -n starterbar-desklet-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sensorsdir},%{_displaysdir}/%{pname}}

./Install_%{pname}_Sensor.bin --nomsg \
	$RPM_BUILD_ROOT%{_sensorsdir}

cp -R gfx *.display $RPM_BUILD_ROOT%{_displaysdir}/%{pname}

%py_comp $RPM_BUILD_ROOT%{_sensorsdir}
%py_ocomp $RPM_BUILD_ROOT%{_sensorsdir}

rm -f $RPM_BUILD_ROOT%{_sensorsdir}/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_sensorsdir}/*
%{_displaysdir}/*
