%define shortname	scratch
Summary:	Scratch is a Lua module that provides a basic drop-down applications and scratchpad manager for awesome v3.4
Summary(hu.UTF-8):	Scatch egy Lua module, amely egy lenyiló alkalmazás- és scratchpad manager-t valósít meg az awesome 3.4-hez
Name:		awesome-plugin-scratch
Version:	20100129
Release:	0.1
License:	WTFPL v2
Group:		X11/Window Managers/Tools
Source0:	http://carme.pld-linux.org/~uzsolt/sources/%{name}-%{version}.tar.bz2
# Source0-md5:	f19b8a4d067e2fb26eb492070b001459
URL:		http://awesome.naquadah.org/wiki/Scratchpad_manager
Requires:	awesome >= 3.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scratch is a Lua module that provides a basic drop-down applications
and scratchpad manager for awesome v3.4

%description -l hu.UTF-8
Scatch egy Lua module, amely egy lenyiló alkalmazás- és scratchpad
manager-t valósít meg az awesome 3.4-hez

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/awesome/lib/%{shortname}
install *.lua $RPM_BUILD_ROOT%{_datadir}/awesome/lib/%{shortname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/awesome/lib/%{shortname}
