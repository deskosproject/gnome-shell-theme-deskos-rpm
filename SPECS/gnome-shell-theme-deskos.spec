Name:           gnome-shell-theme-deskos
Version:        0.1
Release:        1
Summary:        GNOME Shell theme for DeskOS

Group:          User Interface/Desktops
License:        GPLv2
URL:            https://github.com/deskosproject/gnome-shell-theme-deskos-rpm
Source0:        https://dl.deskosproject.org/sources/%{name}/%{name}-%{version}.tar.xz

BuildArch:      noarch

%description
GNOME Shell theme for DeskOS.

%prep
%setup -q

%install
mkdir -p -m755 %{buildroot}%{_datadir}/themes/DeskOS/gnome-shell
cp -pr gnome-shell/* %{buildroot}%{_datadir}/themes/DeskOS/gnome-shell

%clean
rm -rf %{buildroot}

%files
%{_datadir}/themes/DeskOS/gnome-shell

%changelog
* Sat Apr 16 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.1-1
- Initial spec.
