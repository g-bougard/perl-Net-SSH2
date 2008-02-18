Name:           perl-Net-SSH2
Version:        0.18
Release:        3%{?dist}
Summary:        Support for the SSH 2 protocol via libSSH2
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Net-SSH2/
Source0:        http://www.cpan.org/authors/id/D/DB/DBROBINS/Net-SSH2-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# non-perl
BuildRequires:  libssh2-devel >= 0.18

# core
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
#BuildRequires: perl(File::Basename) 
#BuildRequires: perl(IO::File) 
#BuildRequires: perl(Socket) 


%description
Net::SSH2 is a perl interface to the libssh2 (http://www.libssh2.org)
library. It supports the SSH2 protocol (there is no support for SSH1) with
all of the key exchanges, ciphers, and compression of libssh2.

%prep
%setup -q -n Net-SSH2-%{version}

perl -pi -e 's|^#!perl|#!/usr/bin/perl|' example/*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} +
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} +
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
# note most of these tests will skip -- that's fine, they'd fail in the
# buildsys anyways as they require network access
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README example/ t/
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Net*
%{_mandir}/man3/*

%changelog
* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.18-3
- Autorebuild for GCC 4.3

* Sun Dec 02 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.18-2
- bump

* Tue Nov 13 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.18-1
- update to 0.18
- drop old patches

* Sun Oct 14 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.10-2
- update with patch1
- update license tag: GPL -> GPL+

* Wed May 23 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.10-1
- Specfile autogenerated by cpanspec 1.71.
