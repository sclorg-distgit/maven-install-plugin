%{?scl:%scl_package maven-install-plugin}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}maven-install-plugin
Version:        2.5.2
Release:        5.1%{?dist}
Summary:        Maven Install Plugin

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-install-plugin
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(commons-codec:commons-codec)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-artifact)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-artifact-manager)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-compat)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-core)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-model)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-project)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-utils)

%description
Copies the project artifacts to the user's local repository.

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{pkg_name}
Requires:       %{?scl_prefix}jpackage-utils

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q
# maven-core has scope "provided" in Plugin Testing Harness, so we
# need to provide it or tests will fail to compile.  This works for
# upstream because upstream uses a different version of Plugin Testing
# Harness in which scope of maven-core dependency is "compile".
%pom_add_dep org.apache.maven:maven-core::test

%pom_add_dep org.apache.maven:maven-compat

%build
%mvn_build -f -- -DmavenVersion=3.1.1

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 2.5.2-5.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.2-2
- Remove legacy Obsoletes/Provides for maven2 plugin

* Mon Sep  1 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.2-1
- Update to upstream version 2.5.2

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.1-5
- Fix build-requires on parent POM

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.5.1-3
- Use Requires: java-headless rebuild (#1067528)

* Fri Jan 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.1-2
- Update to Maven 3.x

* Mon Oct 21 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.1-1
- Update to upstream version 2.5.1

* Tue Sep 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-1
- Update to upstream version 2.5

* Wed Aug 07 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4-6
- Update to latest packaging guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

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
