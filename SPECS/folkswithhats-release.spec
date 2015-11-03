Name:		folkswithhats-release
Version:	1.0.1
Release:	1%{?dist}
Summary:	Repository for Fedy.
Group:		System Environment/Base

License:	GPL-3
URL:		http://folkswithhats.org/

Requires:	system-release >= %{version}

BuildArch:	noarch

%description
 Repository for Fedy.


%install
%{__install} -d -m755 %{buildroot}%{_sysconfdir}/yum.repos.d
cat << EOF >>%{buildroot}%{_sysconfdir}/yum.repos.d/folkswithhats.repo
[folkswithhats]
name=Repository for Fedy
baseurl=http://folkswithhats.org/repo/\$releasever/
enabled=1
skip_if_unavailable=1
metadata_expire=1d
gpgcheck=0
EOF


%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/folkswithhats.repo

%changelog
* Tue Feb 17 2015 Satyajit Sahoo <satya164@fedoraproject.org> - 0.0-1
- Initial package for Fedora

