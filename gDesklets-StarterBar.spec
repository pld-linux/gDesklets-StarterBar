%define		pname	StarterBar
Summary:	An icon bar for GNOME
Summary(pl.UTF-8):   Pasek na ikony dla GNOME
Name:		gDesklets-%{pname}
Version:	0.31.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://gdesklets.gnomedesktop.org/files/starterbar-desklet-%{version}.tar.gz
# Source0-md5:	fee42cc50af5ac9fc4957719d6e7e1f0
URL:		http://www.pycage.de/software_gdesklets.html
BuildRequires:	python >= 1:2.3
BuildRequires:	python-pygtk-gtk >= 1.99.14
Requires:	gDesklets >= 0.31
%pyrequires_eq	python-libs
Requires:	python-gnome-vfs
Provides:	gDesklets-display
Provides:	gDesklets-sensor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sensorsdir	%{_libdir}/gdesklets/Sensors
%define		_displaysdir	%{_libdir}/gdesklets/Displays

%description
An icon bar for GNOME. You can do the same with the GNOME panel, but
this one is pure eye candy.

%description -l pl.UTF-8
Pasek na ikony dla GNOME. Takie możliwości ma także panel GNOME, ale
ten jest miły dla oka.

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

#rm -f $RPM_BUILD_ROOT%{_sensorsdir}/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_sensorsdir}/*
%{_displaysdir}/*
