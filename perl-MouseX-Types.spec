#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	MouseX
%define	pnam	Types
Summary:	MouseX::Types - Organize your Mouse types in libraries
Summary(pl.UTF-8):	MouseX::Types - Porządkuje typy Mouse w biblioteki
Name:		perl-MouseX-Types
Version:	0.02
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/Y/YA/YAPPO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b2d91d5ba7a7d8a1218f72a9dcc97b49
URL:		http://search.cpan.org/dist/MouseX-Types/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Mouse >= 0.15
BuildRequires:	perl-Test-Exception
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MouseX::Types - Organize your Mouse types in libraries

%description -l pl.UTF-8
MouseX::Types - Porządkuje typy Mouse w biblioteki

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MouseX/*.pm
%{perl_vendorlib}/MouseX/Types
%{_mandir}/man3/*
