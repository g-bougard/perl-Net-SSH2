Name:           perl-Net-SSH2
Version:        0.70
Release:        2%{?dist}
Summary:        Support for the SSH 2 protocol via libSSH2
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Net-SSH2
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SALVA/Net-SSH2-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  libgcrypt-devel
BuildRequires:  libssh2-devel >= 0.18
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(inc::Module::Install) >= 1.17
BuildRequires:  perl(Module::Install::CheckLib)
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
BuildRequires:  zlib-devel
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
# IO::Socket::IP is preferred
# XXX: BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl(XSLoader)
# Tests only
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(IO::Scalar)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(IO::Socket::IP)
Recommends:     perl(Term::ReadKey)
Provides:       perl(Net::SSH2::Constants) = %{version}

%{?perl_default_filter}

%description
Net::SSH2 is a perl interface to the libssh2 (http://www.libssh2.org)
library. It supports the SSH2 protocol (there is no support for SSH1) with
all of the key exchanges, ciphers, and compression of libssh2.

%prep
%setup -q -n Net-SSH2-%{version}

# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
# note most of these tests will skip -- that's fine, they'd fail in the
# buildsys anyways as they require network access
make test

%files
%doc Changes README example
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Net*
%{_mandir}/man3/*

%changelog
* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.70-2
- Perl 5.30 rebuild

* Mon Mar 18 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.70-1
- 0.70 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.69-3
- Perl 5.28 rebuild

* Thu Mar  1 2018 Florian Weimer <fweimer@redhat.com> - 0.69-2
- Rebuild with new redhat-rpm-config/perl build flags

* Mon Feb 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.69-1
- 0.69 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.68-1
- 0.68 bump

* Mon Dec 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.67-1
- 0.67 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.66-1
- 0.66 bump

* Wed Jun 14 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.65-1
- 0.65 bump

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.63-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Petr Pisar <ppisar@redhat.com> - 0.63-1
- 0.63 bump

* Thu Jun 09 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.62-1
- 0.62 bump

* Fri Jun 03 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-1
- 0.61 bump

* Wed May 25 2016 Petr Pisar <ppisar@redhat.com> - 0.60-2
- Provide hidden Net::SSH2::Constants module (bug #1339341)

* Mon May 23 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-1
- 0.60 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.58-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Petr Šabata <contyk@redhat.com> - 0.58-1
- 0.58 bump

* Mon Dec 07 2015 Petr Šabata <contyk@redhat.com> - 0.56-2
- Work around a libssh2 agent bug (#1288774)

* Mon Oct 12 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-1
- 0.56 bump

* Tue Sep 29 2015 Petr Šabata <contyk@redhat.com> - 0.55-1
- 0.55 bump
- Source URL updated

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.53-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-5
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.53-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 02 2013 Petr Šabata <contyk@redhat.com> - 0.53-1
- 0.53 bump

* Mon Aug 26 2013 Petr Šabata <contyk@redhat.com> - 0.52-1
- 0.52 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Šabata <contyk@redhat.com> - 0.50-1
- 0.50 bump

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.48-2
- Perl 5.18 rebuild

* Thu Feb 21 2013 Petr Šabata <contyk@redhat.com> - 0.48-1
- 0.48 bump

* Tue Feb 12 2013 Petr Šabata <contyk@redhat.com> - 0.47-1
- 0.47 bump
- Patch the version check (#864102, rt#80065)
- Drop the useless excludedir
- Drop the tests subpackage

* Tue Nov 13 2012 Petr Šabata <contyk@redhat.com> - 0.46-1
- 0.46 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Petr Pisar <ppisar@redhat.com> - 0.45-2
- Perl 5.16 rebuild

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
