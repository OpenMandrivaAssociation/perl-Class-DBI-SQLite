%define upstream_name    Class-DBI-SQLite
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Class::DBI extension for sqlite
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::DBI)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBIx::ContextualFetch)
BuildArch:	noarch

%description
Class::DBI::SQLite is an extension to Class::DBI for DBD::SQLite. It allows you
to populate an auto-incremented row id after insert.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL installdirs=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Class
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 680802
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 403010
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.11-3mdv2009.0
+ Revision: 241184
- rebuild
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Sep 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2008.0
+ Revision: 83820
- import perl-Class-DBI-SQLite


* Sat Sep 08 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2008.0
- first mdv release
