Summary:	Simple text-mode ICQ client
Name:		vicq
Version:	0.4.1
Release:	0.4
Epoch:		0
License:	GPL
Group:		Applications/Networking
Source0:	http://www.gonzo.kiev.ua/projects/vicq/%{name}-%{version}.tar.gz
# Source0-md5:	ba18dc9c0f9b20efa2eb6accc2d38283
URL:		http://www.gonzo.kiev.ua/projects/vicq/
BuildRequires:	perl-devel >= 1:5.8.0
Requires:	perl-Net-vICQ
Requires:	perl-Term-ReadLine-Gnu
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vICQ is a simple text-mode ICQ client written with look and feel of
micq in mind.
Its features: PERL source code suitable for hacking and scripting,
text-only look & feel, and ICQ v7 protocol support.

%package -n perl-Net-vICQ
Summary:	Net::vICQ - simple text-mode ICQ based on Based on Net::ICQ2000
Group:      Development/Languages/Perl
Requires:	perl-base

%description -n perl-Net-vICQ
Simple text-mode ICQ based on Based on Net::ICQ2000.

%prep
%setup -q -n %{name}

%build
cd Net/vICQ
%{__perl} Makefile.PL \
    INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}rc.example $RPM_BUILD_ROOT%{_sysconfdir}/%{name}rc

cd Net/vICQ
%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README  TODO 
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*

%files -n perl-Net-vICQ
%defattr(644,root,root,755)
%{perl_vendorlib}/Net/vICQ.pm
