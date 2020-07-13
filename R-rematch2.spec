#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rematch2
Version  : 2.1.2
Release  : 23
URL      : https://cran.r-project.org/src/contrib/rematch2_2.1.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rematch2_2.1.2.tar.gz
Summary  : Tidy Output from Regular Expression Matching
Group    : Development/Tools
License  : MIT
Requires: R-tibble
BuildRequires : R-tibble
BuildRequires : buildreq-R

%description
results in tidy data frames.

%prep
%setup -q -c -n rematch2
cd %{_builddir}/rematch2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589586522

%install
export SOURCE_DATE_EPOCH=1589586522
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C.UTF-8
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
/usr/lib64/R/library/rematch2/tests/testthat/test-bind.R
/usr/lib64/R/library/rematch2/tests/testthat/test-exec-all.R
/usr/lib64/R/library/rematch2/tests/testthat/test-exec.R
/usr/lib64/R/library/rematch2/tests/testthat/test-indexing.R
/usr/lib64/R/library/rematch2/tests/testthat/test.R
