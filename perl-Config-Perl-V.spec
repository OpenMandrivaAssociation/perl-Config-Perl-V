%define upstream_name    Config-Perl-V
%define upstream_version 0.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	A module that will return you the output of
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Config/Config-Perl-V-%{upstream_version}.tgz

BuildRequires:	perl-devel
BuildRequires:	perl(Config)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::NoWarnings)
BuildArch:	noarch

%description
$conf = myconfig ()
    This function will collect the data described in the the hash structure
    manpage below, and return that as a hash reference. It optionally
    accepts an option to include more entries from the ENV hash. See the
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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml README Changelog
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.120.0-2mdv2011.0
+ Revision: 654899
- rebuild for updated spec-helper

* Tue Mar 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2011.0
+ Revision: 521780
- import perl-Config-Perl-V


* Tue Mar 16 2010 cpan2dist 0.12-1mdv
- initial mdv release, generated with cpan2dist

