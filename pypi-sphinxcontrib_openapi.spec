#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-sphinxcontrib_openapi
Version  : 0.7.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/13/52/5b4c985cbecbdb8c88720e5ab47c765835b3f00bcfe5099e50009cbcf1e6/sphinxcontrib-openapi-0.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/13/52/5b4c985cbecbdb8c88720e5ab47c765835b3f00bcfe5099e50009cbcf1e6/sphinxcontrib-openapi-0.7.0.tar.gz
Summary  : OpenAPI (fka Swagger) spec renderer for Sphinx
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause
Requires: pypi-sphinxcontrib_openapi-license = %{version}-%{release}
Requires: pypi-sphinxcontrib_openapi-python = %{version}-%{release}
Requires: pypi-sphinxcontrib_openapi-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jsonschema)
BuildRequires : pypi(m2r)
BuildRequires : pypi(py)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(sphinx)
BuildRequires : pypi(sphinxcontrib_httpdomain)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
sphinxcontrib-openapi
        =====================
        
        **sphinxcontrib-openapi** is a `Sphinx`_ extension to generate APIs docs from
        `OpenAPI`_ (fka Swagger) spec. It depends on `sphinxcontrib-httpdomain`_ that
        provides an HTTP domain for describing RESTful HTTP APIs, so we don't need to
        reinvent the wheel.

%package license
Summary: license components for the pypi-sphinxcontrib_openapi package.
Group: Default

%description license
license components for the pypi-sphinxcontrib_openapi package.


%package python
Summary: python components for the pypi-sphinxcontrib_openapi package.
Group: Default
Requires: pypi-sphinxcontrib_openapi-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinxcontrib_openapi package.


%package python3
Summary: python3 components for the pypi-sphinxcontrib_openapi package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_openapi)
Requires: pypi(jsonschema)
Requires: pypi(m2r)
Requires: pypi(pyyaml)
Requires: pypi(sphinx)
Requires: pypi(sphinxcontrib_httpdomain)

%description python3
python3 components for the pypi-sphinxcontrib_openapi package.


%prep
%setup -q -n sphinxcontrib-openapi-0.7.0
cd %{_builddir}/sphinxcontrib-openapi-0.7.0
pushd ..
cp -a sphinxcontrib-openapi-0.7.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653853864
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_openapi
cp %{_builddir}/sphinxcontrib-openapi-0.7.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_openapi/a5942e608cfbf73a853f27fa8bdbc3f2a6ca3b35
cp %{_builddir}/sphinxcontrib-openapi-0.7.0/tests/OpenAPI-Specification/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_openapi/9733a6d8ca0bc862c5bd91bbffb0441c7f75c5aa
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinxcontrib_openapi/9733a6d8ca0bc862c5bd91bbffb0441c7f75c5aa
/usr/share/package-licenses/pypi-sphinxcontrib_openapi/a5942e608cfbf73a853f27fa8bdbc3f2a6ca3b35

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
