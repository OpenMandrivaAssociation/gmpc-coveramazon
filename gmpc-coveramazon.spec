Summary:	An Amazon plugin for gmpc
Name:		gmpc-coveramazon
Version:	0.15.5.0
Release:	%mkrel 3
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl//amazon-provider
Source0:	http://download.sarine.nl/download/gmpc-0.15.5/%{name}-%{version}.tar.bz2
BuildRequires:	libmpd-devel
BuildRequires:	libxml2-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	gmpc-devel
Requires:	gmpc
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This plugin fetches cover art, and album information from amazon.

%prep
%setup -q

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/gmpc/plugins/caaplugin.la
%{_datadir}/gmpc/plugins/caaplugin.so
