%define upstream_name    Class-DBI-SQLite
%define upstream_version 0.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Class::DBI extension for sqlite
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Class::DBI)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBIx::ContextualFetch)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Class::DBI::SQLite is an extension to Class::DBI for DBD::SQLite. It allows you
to populate an auto-incremented row id after insert.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL installdirs=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Class
%{_mandir}/*/*
