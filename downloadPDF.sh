cd lhapdf
pwd=$PWD
#Download few PDFs
for pdf in  NNPDF31_lo_as_0118 NNPDF31_lo_as_0130 NNPDF31_nlo_as_0118 NNPDF31_nnlo_as_0118 H1PDF2017 HERAPDF20_LO_EIG  HERAPDF20_NLO_EIG  HERAPDF20_NNLO_EIG HERAPDF20_Jets_NLO_EIG
do
    if [ -e $pwd/install/share/LHAPDF/$pdf ]; then
        echo file exists
    else
        #echo not
        curl -L http://www.hepforge.org/archive/lhapdf/pdfsets/6.2/$pdf.tar.gz  | tar xz -C $pwd/install/share/LHAPDF
    fi
done
