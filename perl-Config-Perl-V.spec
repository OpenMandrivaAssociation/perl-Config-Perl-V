%define upstream_name    Config-Perl-V
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    A module that will return you the output of
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tgz

BuildRequires: perl(Config)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::NoWarnings)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
$conf = myconfig ()
    This function will collect the data described in the the hash structure
    manpage below, and return that as a hash reference. It optionally
    accepts an option to include more entries from %ENV. See the
    environment manpage below.

    Note that this will not work on uninstalled perls when called with
    '-I/path/to/uninstalled/perl/lib', but it works when that path is in
    '$PERL5LIB' or in '$PERL5OPT', as paths passed using '-I' are not known
    when the '-V' information is collected.

$conf = plv2hash ($text [, ...])
    Convert a sole 'perl -V' text block, or list of lines, to a complete
    myconfig hash. All unknown entries are defaulted.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml README Changelog
%{_mandir}/man3/*
%perl_vendorlib/*


