Name:           gnome-backgrounds-bitday
Version:        1.0.3
Release:        1%{?dist}
Summary:        A beautiful dynamic pixel wallpaper for the GNOME desktop

License:        Public Domain
URL:            https://github.com/ghisvail/gnome-backgrounds-bitday/
Source0:        %{name}-%{version}.tar.gz
Buildarch:      noarch
BuildRequires:  meson
#Requires:       

%description
A GNOME desktop background which animates through the BitDay wallpaper images
as the day progresses.

%prep
%autosetup


%build
%meson


%install
%meson_install


%files
%license COPYING
%{_datadir}/backgrounds/bitday
%{_datadir}/gnome-background-properties/bitday*.xml



%changelog
* Wed Feb 19 2025 Sam Morris <sam@robots.org.uk> 1.0.3-1
- new package built with tito
