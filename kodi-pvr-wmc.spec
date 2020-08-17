%global kodi_addon pvr.wmc
%global kodi_version 18.0
%global kodi_codename Leia

%undefine __cmake_in_source_build

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        2.4.5
Release:        2%{?dist}
Summary:        WMC PVR for Kodi

License:        GPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        %{url}/archive/%{version}-%{kodi_codename}/%{kodi_addon}-%{version}.tar.gz

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  platform-devel
Requires:       kodi >= %{kodi_version}
ExcludeArch:    %{power64} ppc64le

%description
%{summary}.


%prep
%autosetup -n %{kodi_addon}-%{version}-%{kodi_codename}


%build
%cmake3
%cmake3_build


%install
%cmake3_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.4.5-1
- Update to 2.4.5

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.3.3-2
- Enable arm build

* Sat Sep 01 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.3.3-1
- Update to 2.3.3
- Enable aarch64 build

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.2.5-1
- Update to latest stable release for Kodi 18

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1:1.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.4.10-1
- Update to 1.4.10

* Sat Apr 29 2017 Mohamed El Morabity <melmorabity@fedorapeople.org> - 1:1.4.9-1
- Update to latest stable release for Kodi 17

* Sat Jul 23 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:0.6.21-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:0.5.8-1
- Initial RPM release
