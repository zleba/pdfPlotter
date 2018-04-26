cd lhapdf
pwd=$PWD
#Download few PDFs
for pdf in NNPDF31_lo_as_0118 NNPDF31_lo_as_0130 NNPDF31_nlo_as_0118 NNPDF31_nnlo_as_0118
do
    curl -L http://www.hepforge.org/archive/lhapdf/pdfsets/6.2/$pdf.tar.gz  | tar xz -C $pwd/install/share/LHAPDF
done
