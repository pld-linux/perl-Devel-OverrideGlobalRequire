#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Devel
%define		pnam	OverrideGlobalRequire
Summary:	Devel::OverrideGlobalRequire - override CORE::GLOBAL::require safely
Summary(pl.UTF-8):	Devel::OverrideGlobalRequire - nadpisywanie bezpieczeństwa CORE::GLOBAL::require
Name:		perl-Devel-OverrideGlobalRequire
Version:	0.001
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9cc9b7c3e39629d2f3ae22d347c29f1a
URL:		https://metacpan.org/dist/Devel-OverrideGlobalRequire
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Scalar-List-Utils
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module overrides CORE::GLOBAL::require with a code reference in a
way that plays nice with any existing overloading and ensures the
right calling package is in scope.

%description -l pl.UTF-8
Ten moduł nadpisuje CORE::GLOBAL::require referencją do kodu w taki
sposób, aby działał z dowolnym istniejącym nadpisaniem i zapewnia, że
właściwy pakiet wywołujący jest w kontekście.

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
%doc Changes
%{perl_vendorlib}/Devel/OverrideGlobalRequire.pm
%{_mandir}/man3/Devel::OverrideGlobalRequire.3pm*
