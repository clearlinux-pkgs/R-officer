#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-officer
Version  : 0.6.2
Release  : 15
URL      : https://cran.r-project.org/src/contrib/officer_0.6.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/officer_0.6.2.tar.gz
Summary  : Manipulation of Microsoft Word and PowerPoint Documents
Group    : Development/Tools
License  : MIT
Requires: R-R6
Requires: R-openssl
Requires: R-ragg
Requires: R-uuid
Requires: R-xml2
Requires: R-zip
BuildRequires : R-R6
BuildRequires : R-openssl
BuildRequires : R-ragg
BuildRequires : R-uuid
BuildRequires : R-xml2
BuildRequires : R-zip
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The package focuses on tabular and graphical reporting from R; it also provides two functions
  that let users get document content into data objects. A set of functions 
  lets add and remove images, tables and paragraphs of text in new or existing documents. 
  The package does not require any installation of Microsoft products to be able to write Microsoft 
  files.

%prep
%setup -q -n officer

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680051655

%install
export SOURCE_DATE_EPOCH=1680051655
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/officer/DESCRIPTION
/usr/lib64/R/library/officer/INDEX
/usr/lib64/R/library/officer/LICENSE
/usr/lib64/R/library/officer/Meta/Rd.rds
/usr/lib64/R/library/officer/Meta/features.rds
/usr/lib64/R/library/officer/Meta/hsearch.rds
/usr/lib64/R/library/officer/Meta/links.rds
/usr/lib64/R/library/officer/Meta/nsInfo.rds
/usr/lib64/R/library/officer/Meta/package.rds
/usr/lib64/R/library/officer/NAMESPACE
/usr/lib64/R/library/officer/NEWS.md
/usr/lib64/R/library/officer/R/officer
/usr/lib64/R/library/officer/R/officer.rdb
/usr/lib64/R/library/officer/R/officer.rdx
/usr/lib64/R/library/officer/doc_examples/example.docx
/usr/lib64/R/library/officer/doc_examples/example.pptx
/usr/lib64/R/library/officer/doc_examples/landscape.docx
/usr/lib64/R/library/officer/doc_examples/text.txt
/usr/lib64/R/library/officer/help/AnIndex
/usr/lib64/R/library/officer/help/aliases.rds
/usr/lib64/R/library/officer/help/figures/body_add_doc_1.png
/usr/lib64/R/library/officer/help/figures/body_end_block_section_doc_1.png
/usr/lib64/R/library/officer/help/figures/body_set_default_section_doc_1.png
/usr/lib64/R/library/officer/help/figures/logo.png
/usr/lib64/R/library/officer/help/figures/ph_with_doc_1.png
/usr/lib64/R/library/officer/help/figures/prop_section_doc_1.png
/usr/lib64/R/library/officer/help/figures/read_docx_doc_1.png
/usr/lib64/R/library/officer/help/figures/read_docx_doc_2.png
/usr/lib64/R/library/officer/help/officer.rdb
/usr/lib64/R/library/officer/help/officer.rdx
/usr/lib64/R/library/officer/help/paths.rds
/usr/lib64/R/library/officer/html/00Index.html
/usr/lib64/R/library/officer/html/R.css
/usr/lib64/R/library/officer/template/core.xml
/usr/lib64/R/library/officer/template/custom.xml
/usr/lib64/R/library/officer/template/footnotes.xml
/usr/lib64/R/library/officer/template/notesMaster.xml
/usr/lib64/R/library/officer/template/notesSlide.xml
/usr/lib64/R/library/officer/template/sheet.xml
/usr/lib64/R/library/officer/template/sheet.xml.rels
/usr/lib64/R/library/officer/template/slide.xml
/usr/lib64/R/library/officer/template/template.docx
/usr/lib64/R/library/officer/template/template.pptx
/usr/lib64/R/library/officer/template/template.xlsx
/usr/lib64/R/library/officer/tests/testthat.R
/usr/lib64/R/library/officer/tests/testthat/docs_dir/no_master.pptx
/usr/lib64/R/library/officer/tests/testthat/docs_dir/table-complex.docx
/usr/lib64/R/library/officer/tests/testthat/docs_dir/table-complex.pptx
/usr/lib64/R/library/officer/tests/testthat/docs_dir/test_empty.pptx
/usr/lib64/R/library/officer/tests/testthat/test-block_list.R
/usr/lib64/R/library/officer/tests/testthat/test-doc-summary.R
/usr/lib64/R/library/officer/tests/testthat/test-docx-add.R
/usr/lib64/R/library/officer/tests/testthat/test-docx-footnotes.R
/usr/lib64/R/library/officer/tests/testthat/test-docx-insert.R
/usr/lib64/R/library/officer/tests/testthat/test-docx-misc.R
/usr/lib64/R/library/officer/tests/testthat/test-docx-replace.R
/usr/lib64/R/library/officer/tests/testthat/test-docx-styles.R
/usr/lib64/R/library/officer/tests/testthat/test-docx-table.R
/usr/lib64/R/library/officer/tests/testthat/test-fp-text-misc.R
/usr/lib64/R/library/officer/tests/testthat/test-fp-text.R
/usr/lib64/R/library/officer/tests/testthat/test-fp_border.R
/usr/lib64/R/library/officer/tests/testthat/test-fp_cell.R
/usr/lib64/R/library/officer/tests/testthat/test-fp_par.R
/usr/lib64/R/library/officer/tests/testthat/test-fpar.R
/usr/lib64/R/library/officer/tests/testthat/test-hyperlinks.R
/usr/lib64/R/library/officer/tests/testthat/test-images.R
/usr/lib64/R/library/officer/tests/testthat/test-missing-tableStyles.R
/usr/lib64/R/library/officer/tests/testthat/test-ppt-notes.R
/usr/lib64/R/library/officer/tests/testthat/test-pptx-add-geom-ln.R
/usr/lib64/R/library/officer/tests/testthat/test-pptx-add.R
/usr/lib64/R/library/officer/tests/testthat/test-pptx-info.R
/usr/lib64/R/library/officer/tests/testthat/test-pptx-matrix.R
/usr/lib64/R/library/officer/tests/testthat/test-pptx-misc.R
/usr/lib64/R/library/officer/tests/testthat/test-pptx-move.R
/usr/lib64/R/library/officer/tests/testthat/test-pptx-selections.R
/usr/lib64/R/library/officer/tests/testthat/test-pptx-table.R
/usr/lib64/R/library/officer/tests/testthat/test-properties.R
/usr/lib64/R/library/officer/tests/testthat/test-relationships.R
/usr/lib64/R/library/officer/tests/testthat/test-rtf-add.R
/usr/lib64/R/library/officer/tests/testthat/test-sections.R
/usr/lib64/R/library/officer/tests/testthat/test-wml-chunks.R
/usr/lib64/R/library/officer/tests/testthat/test-xlsx-misc.R
/usr/lib64/R/library/officer/tests/testthat/test-xlsx.R
/usr/lib64/R/library/officer/tests/testthat/test-zip.R
/usr/lib64/R/library/officer/tests/testthat/utils.R
