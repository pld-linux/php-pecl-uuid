%define		_modname	uuid
%define		_status		beta

Summary:	%{_modname} - UUID support functions
Summary(pl):	%{_modname} - funkcje obs³uguj±ce UUID
Name:		php-pecl-%{_modname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	83140b6acd662db86755b9474d25fc7c
URL:		http://pecl.php.net/package/uuid/
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	php-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
This extension provides functions to generate and analyse universally
unique identifiers (UUIDs). It depends on external libuuid. This
library is available on most linux systems, its source is bundled with
ext2fs tools.

This extension has in PEAR status: %{_status}.

%description -l pl
To rozszerzenie dostarcza funkcje do generowania i analizy
uniwersalnie unikalnych identyfikatorów (ang. UUIDs). Rozszerznie to
wymaga zewnêtrznej biblioteki libuuid, dostêpnej w wiêkszo¶ci
dystrybucji, której ¼ród³o jest dostarczane wraz z narzêdziami ext2fs.

To rozszerzenie ma w PEAR status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
