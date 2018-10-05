%define		php_name	php%{?php_suffix}
%define		modname		uuid
%define		status		stable
Summary:	%{modname} - UUID support functions
Summary(pl.UTF-8):	%{modname} - funkcje obsługujące UUID
Name:		%{php_name}-pecl-%{modname}
Version:	1.0.4
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	1695511daf585fcaf7816a401a6216f6
URL:		http://pecl.php.net/package/uuid/
BuildRequires:	%{php_name}-devel >= 3:5.0.4
BuildRequires:	libuuid-devel
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Provides:	php(%{modname}) = %{version}
Obsoletes:	php-pecl-uuid < 1.0.3-5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This extension provides functions to generate and analyse universally
unique identifiers (UUIDs). It depends on external libuuid. This
library is available on most linux systems, its source is bundled with
ext2fs tools.

In PECL status of this package is: %{status}.

%description -l pl.UTF-8
To rozszerzenie dostarcza funkcje do generowania i analizy
uniwersalnie unikalnych identyfikatorów (ang. UUIDs). Rozszerznie to
wymaga zewnętrznej biblioteki libuuid, dostępnej w większości
dystrybucji, której źródło jest dostarczane wraz z narzędziami ext2fs.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
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
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
