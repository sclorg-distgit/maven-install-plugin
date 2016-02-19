%global pkg_name maven-install-plugin
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        2.4
Release:        7.11%{?dist}
Summary:        Maven Install Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-install-plugin
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: maven30-maven-plugin-plugin
BuildRequires: maven30-maven-jar-plugin
BuildRequires: maven30-maven-install-plugin
BuildRequires: maven30-maven-resources-plugin
BuildRequires: maven30-maven-compiler-plugin
BuildRequires: maven30-maven-javadoc-plugin
BuildRequires: maven30-maven-surefire-plugin
BuildRequires: maven30-maven-surefire-provider-junit
BuildRequires: maven30-maven-doxia-sitetools
BuildRequires: maven30-maven-plugin-testing-harness
BuildRequires: maven30-plexus-utils
BuildRequires: maven30-plexus-digest
BuildRequires: %{?scl_prefix_java_common}junit
BuildRequires: maven30-maven-archiver
BuildRequires: maven30-maven-reporting-impl
BuildRequires: maven30-mvn(org.apache.maven:maven-artifact:2.0.6)
BuildRequires: maven30-mvn(org.apache.maven:maven-model:2.0.6)


%description
Copies the project artifacts to the user's local repository.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.


%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
# maven-core has scope "provided" in Plugin Testing Harness, so we
# need to provide it or tests will fail to compile.  This works for
# upstream because upstream uses a different version of Plugin Testing
# Harness in which scope of maven-core dependency is "compile".
%pom_add_dep org.apache.maven:maven-core::test
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 2.4-7.11
- maven33 rebuild

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-7.10
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 2.4-7.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 2.4-7.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-7.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-7.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-7.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-7.4
- Rebuild to fix incorrect auto-requires

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-7.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-7.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-7.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.4-7
- Mass rebuild 2013-12-27

* Fri Aug 23 2013 Michal Srb <msrb@redhat.com> - 2.4-6
- Migrate away from mvn-rpmbuild (Resolves: #997497)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-5
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Mar 11 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-2
- Add missing requires on maven2 artifact and model
- Add maven-core to test dependencies
- Resolves: rhbz#914169

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.4-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sat Jan 07 2013 David Xie <david.scriptfan@gmail.com> - 2.4-1
- Upgrade to 2.4

* Mon Dec 10 2012 Weinan Li <weli@redhat.com> - 2.3.1-7
- Install license files

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec  5 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.3.1-4
- Fixes for pure maven 3 build without maven 2 in buildroot
- Guideline fixes

* Fri Jun 3 2011 Alexander Kurtakov <akurtako@redhat.com> 2.3.1-3
- Build with maven v3.
- Guidelines fixes.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 14 2010 Alexander Kurtakov <akurtako@redhat.com> 2.3.1-1
- Update to 2.3.1.
- Install License.

* Thu Sep 09 2010 Hui Wang <huwang@redhat.com> 2.3-8
- Add pom.patch

* Fri May 21 2010 Alexander Kurtakov <akurtako@redhat.com> 2.3-7
- BR: plexus-digest.

* Fri May 21 2010 Alexander Kurtakov <akurtako@redhat.com> 2.3-6
- Requires: plexus-digest.

* Wed May 19 2010 Hui Wang <huwang@redhat.com> - 2.3-5
- Added missing BR : maven-shared-reporting-impl

* Wed May 19 2010 Hui Wang <huwang@redhat.com> - 2.3-4
- Added missing obsoletes/provides

* Wed May 19 2010 Hui Wang <huwang@redhat.com> - 2.3-3
- Added missing BR : maven-archiver

* Mon May 17 2010 Hui Wang <huwang@redhat.com> - 2.3-2
- Fixed install -pm 644 pom.xml

* Fri May 14 2010 Hui Wang <huwang@redhat.com> - 2.3-1
- Initial version of the package
