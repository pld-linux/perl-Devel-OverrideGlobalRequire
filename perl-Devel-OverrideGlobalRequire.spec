#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Devel
%define		pnam	OverrideGlobalRequire
Summary:	Devel::OverrideGlobalRequire - Override CORE::GLOBAL::require safely
Name:		perl-Devel-OverrideGlobalRequire
Version:	0.001
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9cc9b7c3e39629d2f3ae22d347c29f1a
URL:		http://search.cpan.org/dist/Devel-OverrideGlobalRequire/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module overrides CORE::GLOBAL::require with a code reference in a
way that plays nice with any existing overloading and ensures the
right calling package is in scope.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Devel/*.pm
%{_mandir}/man3/*
