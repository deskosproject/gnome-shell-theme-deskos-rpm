Name:           gnome-shell-theme-deskos
Version:        0.2
Release:        2%{?dist}
Summary:        GNOME Shell theme for DeskOS

Group:          User Interface/Desktops
License:        GPLv2
URL:            https://github.com/deskosproject/gnome-shell-theme-deskos-rpm
Source0:        https://dl.deskosproject.org/sources/%{name}/%{name}-%{version}.tar.xz

# Hide upstream logo
Patch1:         hide-logo.patch

# Calendar: For "All day" events, text can overlap in non-English locales
# https://bugzilla.gnome.org/show_bug.cgi?id=743438
# Also: https://bugzilla.gnome.org/show_bug.cgi?id=742414
Patch2:         events-table-day-time-width.patch

BuildArch:      noarch

%description
GNOME Shell theme for DeskOS.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%install
mkdir -p -m755 %{buildroot}%{_datadir}/themes/DeskOS/gnome-shell
cp -pr gnome-shell/* %{buildroot}%{_datadir}/themes/DeskOS/gnome-shell

%clean
rm -rf %{buildroot}

%files
%{_datadir}/themes/DeskOS/gnome-shell

%changelog
* Sun Dec 18 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.2-2
- Fix events table text overlap with a patch

* Wed Dec 14 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.2-1
- Updated to the GNOME 3.14.4 theme included in upstream

* Sat Apr 16 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.1-1
- Initial spec.
