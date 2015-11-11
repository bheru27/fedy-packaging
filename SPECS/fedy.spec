Name:		fedy
Version:	4.0.9
Release:	1%{?dist}
Summary:	Software, codec installs and system tweaks
Group:		System/Management

License:	GPL-3
URL:		http://folkswithhats.org/

Source0:	%{name}-%{version}.tar.gz

Requires:	fedy-core
Requires:	fedy-plugins

BuildArch:	noarch

%description
Fedy lets you install multimedia codecs and additional software that Fedora
doesn't want to ship, like mp3 support, Adobe Flash, Oracle Java etc., and
much more with just a few clicks.

%prep
%setup -q

%build
# Nothing to build

%install
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root)



%package core

Summary: Core files for Fedy

Requires:	gjs
Requires:	gtk3
Requires:	coreutils
Requires:	sed
Requires:	tar
Requires:	wget
Requires:	dnf
Requires:	dnf-plugins-core

%description core
Core files for Fedy which can load and display plugins.

%post core
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun core
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files core
%defattr(-,root,root)
%doc COPYING CREDITS README.md
%exclude %{_datadir}/%{name}/plugins
%{_datadir}/%{name}
%{_datadir}/applications/org.folkswithhats.%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}-symbolic.svg
%{_datadir}/polkit-1/actions/org.folkswithhats.pkexec.run-as-root.policy
%{_datadir}/appdata/%{name}.appdata.xml
%{_bindir}/%{name}



%package plugins

Summary: Plugins for Fedy

Requires:	rpmfusion-free-release
Requires:	rpmfusion-nonfree-release
Requires:	folkswithhats-release

%description plugins
Collection of various plugins for fedy to install multimedia codecs,
additional software etc.

%files plugins
%defattr(-,root,root)
%{_datadir}/%{name}/plugins



%changelog
* Wed Nov 11 2015 Abhinav Kulshreshtha <AbhinavOther@gmail.com> 4.0.9
- Update Packages.
* Tue Nov 03 2015 Abhinav Kulshreshtha <AbhinavOther@gmail.com> 4.0.8
- Release for Fedora 23. Updated packages.
* Tue Nov 03 2015 Abhinav Kulshreshtha <AbhinavOther@gmail.com> 4.0.8
- Updated packages. Now under FolksWithHats.org
* Wed May 27 2015 Satyajit Sahoo <satyajit.happy@gmail.com> 4.0.2
- split package into core and plugins
* Sun May 17 2015 Satyajit Sahoo <satyajit.happy@gmail.com> 4.0.0
- major rewrite
* Sun Jan 26 2014 Satyajit Sahoo <satyajit.happy@gmail.com> 3.1.6
- renamed to fedy
* Sun Jan 26 2014 Satyajit Sahoo <satyajit.happy@gmail.com> 3.1.5
- added fedy repo
* Tue Jul 23 2013 Satyajit Sahoo <satyajit.happy@gmail.com> 3.1.1
- moved repofile to another package
* Wed Nov 21 2012 Satyajit Sahoo <satyajit.happy@gmail.com> 2.3.0
- various updates
* Thu Jun 28 2012 Satyajit Sahoo <satyajit.happy@gmail.com> 2.1.1
- cleanup, removed repo from postinstall and added as a config file
* Sun Jan 22 2012 Satyajit Sahoo <satyajit.happy@gmail.com> 1.8.1
- policykit support
* Fri Nov 11 2011 Satyajit Sahoo <satyajit.happy@gmail.com> 1.7.6
- added license file
* Tue Oct 25 2011 Satyajit Sahoo <satyajit.happy@gmail.com> 1.7.3
- added postinstall script for adding the repo
* Thu Oct 06 2011 Satyajit Sahoo <satyajit.happy@gmail.com> 1.7.0
- rpm package built with the help of dangermouse


