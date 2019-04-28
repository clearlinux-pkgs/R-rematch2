#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rematch2
Version  : 2.0.1
Release  : 11
URL      : https://cran.r-project.org/src/contrib/rematch2_2.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rematch2_2.0.1.tar.gz
Summary  : Tidy Output from Regular Expression Matching
Group    : Development/Tools
License  : MIT
BuildRequires : R-cli
BuildRequires : R-pillar
BuildRequires : R-pkgconfig
BuildRequires : R-tibble
BuildRequires : buildreq-R

%description
# rematch2
> Match Regular Expressions with a Nicer 'API'
[![Linux Build Status](https://travis-ci.org/r-lib/rematch2.svg?branch=master)](https://travis-ci.org/r-lib/rematch2)
[![Windows Build status](https://ci.appveyor.com/api/projects/status/github/r-lib/rematch2?svg=true)](https://ci.appveyor.com/project/gaborcsardi/rematch2)
[![](http://www.r-pkg.org/badges/version/rematch2)](http://www.r-pkg.org/pkg/rematch2)
[![CRAN RStudio mirror downloads](http://cranlogs.r-pkg.org/badges/rematch2)](http://www.r-pkg.org/pkg/rematch2)
[![Coverage Status](https://img.shields.io/codecov/c/github/r-lib/rematch2/master.svg)](https://codecov.io/github/r-lib/rematch2?branch=master)

%prep
%setup -q -c -n rematch2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556480358

%install
export SOURCE_DATE_EPOCH=1556480358
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rematch2
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rematch2
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rematch2
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rematch2 || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rematch2/DESCRIPTION
/usr/lib64/R/library/rematch2/INDEX
/usr/lib64/R/library/rematch2/LICENSE
/usr/lib64/R/library/rematch2/Meta/Rd.rds
/usr/lib64/R/library/rematch2/Meta/features.rds
/usr/lib64/R/library/rematch2/Meta/hsearch.rds
/usr/lib64/R/library/rematch2/Meta/links.rds
/usr/lib64/R/library/rematch2/Meta/nsInfo.rds
/usr/lib64/R/library/rematch2/Meta/package.rds
/usr/lib64/R/library/rematch2/NAMESPACE
/usr/lib64/R/library/rematch2/NEWS.md
/usr/lib64/R/library/rematch2/R/rematch2
/usr/lib64/R/library/rematch2/R/rematch2.rdb
/usr/lib64/R/library/rematch2/R/rematch2.rdx
/usr/lib64/R/library/rematch2/README.Rmd
/usr/lib64/R/library/rematch2/README.markdown
/usr/lib64/R/library/rematch2/help/AnIndex
/usr/lib64/R/library/rematch2/help/aliases.rds
/usr/lib64/R/library/rematch2/help/paths.rds
/usr/lib64/R/library/rematch2/help/rematch2.rdb
/usr/lib64/R/library/rematch2/help/rematch2.rdx
/usr/lib64/R/library/rematch2/html/00Index.html
/usr/lib64/R/library/rematch2/html/R.css
/usr/lib64/R/library/rematch2/tests/testthat.R
/usr/lib64/R/library/rematch2/tests/testthat/helper.R
/usr/lib64/R/library/rematch2/tests/testthat/test-all.R
/usr/lib64/R/library/rematch2/tests/testthat/test-exec-all.R
/usr/lib64/R/library/rematch2/tests/testthat/test-exec.R
/usr/lib64/R/library/rematch2/tests/testthat/test-indexing.R
/usr/lib64/R/library/rematch2/tests/testthat/test.R
