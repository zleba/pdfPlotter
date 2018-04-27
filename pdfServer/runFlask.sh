lhaDir=$PWD/../lhapdf/install
export PYTHONPATH=$lhaDir/lib/python2.7/site-packages/:$PYTHONPATH
#export PYTHONPATH=/home/radek/Dropbox/Helenka/test/pdfPlotter/lhapdf/install/lib/python2.7/site-packages/:$PYTHONPATH
echo $PYTHONPATH
export LD_LIBRARY_PATH=$lhaDir/lib/:$LD_LIBRARY_PATH
#export LD_LIBRARY_PATH=/home/radek/Dropbox/Helenka/test/pdfPlotter/lhapdf/install/lib/:$LD_LIBRARY_PATH
echo $LD_LIBRARY_PATH

export FLASK_APP=getPDF.py
python -m flask run --host=0.0.0.0
