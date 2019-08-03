Name:     ocaml-mm
Version:  0.4.1
Release:  0.0%{dist}
Summary:  OCAML multimedia library

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:  GPLv2+
URL:      https://github.com/savonet/ocaml-mm
Source0:  https://github.com/savonet/ocaml-mm/releases/download/%{version}/ocaml-mm-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-mad-devel
BuildRequires: ocaml-findlib
Requires:      ocaml-mad


%description
ocaml-mm is a library dedicated to performing operations on multimedia contents.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}

%build
./configure \
   --prefix=%{_prefix} \
   --disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export OCAMLFIND_LDCONF=ignore
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
make install

%files
%license COPYING
%{_libdir}/ocaml/%{libname}
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.o
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%exclude %{_libdir}/ocaml/%{libname}/*.ml
%exclude %{_libdir}/ocaml/%{libname}/*.mli
%endif

%files devel
%license COPYING
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.mli
%endif

%changelog
* Sat Aug  3 2019 Lucas Bickel <hairmare@rabe.ch> - 0.4.1-0.0
- Bump to 0.4.1

* Sun Dec  9 2018 Lucas Bickel <hairmare@rabe.ch> - 0.4.0-0.1
- Cleanup and add separate -devel subpackage

* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.4.0-0.0
- Bump to 0.4.0

* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch> - 0.3.1-1
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-mm.spec
