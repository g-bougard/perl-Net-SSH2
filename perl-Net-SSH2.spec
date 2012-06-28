Name:           perl-Net-SSH2
Version:        0.45
Release:        1%{?dist}
Summary:        Support for the SSH 2 protocol via libSSH2
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Net-SSH2/
Source0:        http://search.cpan.org/CPAN/authors/id/R/RK/RKITOVER/Net-SSH2-%{version}.tar.gz
# Avoid the EE::MM CCFLAGS bug
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
# non-perl
BuildRequires:  zlib-devel
BuildRequires:  openssl-devel
BuildRequires:  libssh2-devel >= 0.18

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
Net::SSH2 is a perl interface to the libssh2 (http://www.libssh2.org)
library. It supports the SSH2 protocol (there is no support for SSH1) with
all of the key exchanges, ciphers, and compression of libssh2.

%prep
%setup -q -n Net-SSH2-%{version}
perl -pi -e 's|^#!perl|#!%{__perl}|' example/*

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} +
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
# note most of these tests will skip -- that's fine, they'd fail in the
# buildsys anyways as they require network access
make test

%files
%doc Changes README TODO example/
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto
%{_mandir}/man3/*

%changelog
* Thu Jun 28 2012 Petr Šabata <contyk@redhat.com> - 0.45-1
- 0.45 bump (docs update)

* Thu Jun 07 2012 Petr Pisar <ppisar@redhat.com> - 0.44-2
- Perl 5.16 rebuild

* Fri Apr 27 2012 Petr Šabata <contyk@redhat.com> - 0.44-1
- 0.44 bump

* Tue Apr 24 2012 Petr Šabata <contyk@redhat.com> - 0.43-1
- 0.43 bump

* Mon Apr 23 2012 Petr Šabata <contyk@redhat.com> - 0.42-1
- 0.42 bump

* Thu Apr 19 2012 Petr Šabata <contyk@redhat.com> - 0.41-1
- 0.41 bump

* Fri Jan 13 2012 Petr Šabata <contyk@redhat.com> - 0.40-1
- 0.40 bump
- Spec cleanup

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.33-3
- Perl mass rebuild

* Thu Jun 09 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.33-2
- Perl 5.14 mass rebuild

* Fri Mar 18 2011 Iain Arnell <iarnell@gmail.com> 0.33-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.28-4
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.28-3
- Mass rebuild with perl-5.12.0

* Fri Mar 12 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.28-2
- spec file touch-up

* Wed Jan 20 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.28-1
- auto-update to 0.28 (by cpan-spec-update 0.01)

* Thu Jan 14 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.27-3
- bump for libssh2 rebuild

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.27-2
- rebuild against perl 5.10.1

* Tue Sep 22 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.27-1
- alter filtering
- auto-update to 0.27 (by cpan-spec-update 0.01)

* Mon Sep 21 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.21-5
- rebuild for libssh2 1.2

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.21-4
- rebuilt with new openssl

* Wed Aug 05 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.21-3
- Fix mass rebuild breakdown: Add BR: zlib-devel, openssl-devel.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.21-1
- auto-update to 0.21 (by cpan-spec-update 0.01)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)

* Sat Feb 28 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.18-7
- Stripping bad provides of private Perl extension libs

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jun 30 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.18-5
- apply patch for 5.10

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.18-4
Rebuild for new perl

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
