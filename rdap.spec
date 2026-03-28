Summary:	Registration Data Access Protocol (RDAP) client
Name:		rdap
Version:	0.9.1
Release:	1
License:	MIT
Group:		Networking/Utilities
Source0:	https://github.com/openrdap/rdap/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	0e32caf6e63607dce4376bea3fbd863a
# cd rdap-%{version} && go mod vendor && cd .. && tar cJf rdap-vendor-%{version}.tar.xz rdap-%{version}/vendor
Source1:	%{name}-vendor-%{version}.tar.xz
URL:		https://www.openrdap.org/
BuildRequires:	golang >= 1.19
ExclusiveArch:	%go_arches
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	_debugsource_packages

%description
Registration Data Access Protocol (RDAP) client.

%prep
%setup -q -a1

%build
%__go build -v -mod=vendor -o bin/rdap ./cmd/rdap

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

chmod 755 bin/rdap
cp -p bin/rdap $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/rdap
