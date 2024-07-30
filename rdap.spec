Summary:	Registration Data Access Protocol (RDAP) client
Name:		rdap
Version:	0.9.1
Release:	0.1
License:	MIT
Group:		Networking/Utilities
Source0:	https://github.com/openrdap/rdap/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	0e32caf6e63607dce4376bea3fbd863a
URL:		https://www.openrdap.org/
BuildRequires:	golang
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Registration Data Access Protocol (RDAP) client.

%prep
%setup -q

%build

%_go build -v -mod=vendor -o bin/rdap

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp -p bin/rdap $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/rdap
