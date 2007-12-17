%define module  Class-DBI-SQLite
%define name    perl-%{module}
%define version 0.11
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Class::DBI extension for sqlite
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Class/%{module}-%{version}.tar.gz
BuildRequires:	perl(Class::DBI)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBIx::ContextualFetch)
BuildArch:      noarch

%description
Class::DBI::SQLite is an extension to Class::DBI for DBD::SQLite. It allows you to populate an auto-incremented row id after insert.

%prep
%setup -q -n %{module}-%{version} 

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

