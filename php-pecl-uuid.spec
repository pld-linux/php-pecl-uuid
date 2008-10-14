%define		_modname	uuid
%define		_status		stable
Summary:	%{_modname} - UUID support functions
Summary(pl.UTF-8):	%{_modname} - funkcje obsługujące UUID
Name:		php-pecl-%{_modname}
Version:	1.0.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	c45246bccdaf5e77934be47637627e7f
URL:		http://pecl.php.net/package/uuid/
BuildRequires:	libuuid-devel
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This extension provides functions to generate and analyse universally
unique identifiers (UUIDs). It depends on external libuuid. This
library is available on most linux systems, its source is bundled with
ext2fs tools.

In PECL status of this package is: %{_status}.

%description -l pl.UTF-8
To rozszerzenie dostarcza funkcje do generowania i analizy
uniwersalnie unikalnych identyfikatorów (ang. UUIDs). Rozszerznie to
wymaga zewnętrznej biblioteki libuuid, dostępnej w większości
dystrybucji, której źródło jest dostarczane wraz z narzędziami ext2fs.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so
