lhaDir=$PWD/../lhapdf/install
export PYTHONPATH=$lhaDir/lib/python2.7/site-packages/:$PYTHONPATH
export LD_LIBRARY_PATH=$lhaDir/lib/:$LD_LIBRARY_PATH

export FLASK_APP=getPDF.py
python -m flask run
