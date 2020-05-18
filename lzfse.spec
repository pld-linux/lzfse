Summary:	LZFSE - Lempel-Ziv style data compression using Finite State Entropy coding
Summary(pl.UTF-8):	LZFSE - kompresja danych z stylu Lempel-Ziv przy użyciu kodowania entropijnego
Name:		lzfse
Version:	1.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/lzfse/lzfse/releases
Source0:	https://github.com/lzfse/lzfse/archive/%{name}-%{version}.tar.gz
# Source0-md5:	53e89f88d9cb0f4cb9c3f366dfb239a9
URL:		https://github.com/lzfse/lzfse
BuildRequires:	cmake >= 2.8.6
BuildRequires:	gcc >= 5:3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a reference C implementation of the LZFSE compressor
introduced in the Apple Compression library with OS X 10.11 and iOS 9.

%description -l pl.UTF-8
Ten pakiet zawiera wzorcową implementację w C kompresora LZFSE,
wprowadzonego w bibliotece Compression Apple'a wraz z OS X 10.11 oraz
iOS 9.

%package devel
Summary:	Header files for LZFSE library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LZFSE
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for LZFSE library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki LZFSE.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/lzfse
%attr(755,root,root) %{_libdir}/liblzfse.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/lzfse.h
