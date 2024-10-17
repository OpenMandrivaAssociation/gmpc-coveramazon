Summary:	An Amazon plugin for gmpc
Name:		gmpc-coveramazon
Version:	0.18.0
Release:	%mkrel 2
License:	GPLv2+
Group:		Sound
Url:		https://www.sarine.nl//amazon-provider
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	libmpd-devel >= 0.15.98
BuildRequires:	libxml2-devel
BuildRequires:	gtk+2-devel >= 2.4
BuildRequires:	gmpc-devel >= 0.16.2
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
%{_libdir}/gmpc/plugins/caaplugin.la
%{_libdir}/gmpc/plugins/caaplugin.so
