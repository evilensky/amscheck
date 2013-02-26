Name:		amscheck
Version:	5
Release:	1%{?dist}
Summary:	an RPM to install the amscheck binary that ships with Adobe Media Server 5

#Group:		
License:	Unlicensed
#URL:		
Source0:	amscheck
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:
#Be sure to build for 32-bit because that's what this binary is.
Requires:	libgcc
Requires:	libstdc++
Requires:	glibc
Requires:	libcurl

%description
This package contains the amscheck binary.

%prep
%setup -q -c -T

install -pm 755 %{SOURCE0} .

%build


%install
rm -rf $RPM_BUILD_ROOT

#binary
install -Dpm 755 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_bindir}/amscheck


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/bin/amscheck
%doc



%changelog

