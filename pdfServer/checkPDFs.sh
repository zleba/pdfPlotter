lhaDir=$PWD/../lhapdf/install
export PYTHONPATH=$lhaDir/lib/python2.7/site-packages/:$PYTHONPATH
echo $PYTHONPATH
export LD_LIBRARY_PATH=$lhaDir/lib/:$LD_LIBRARY_PATH
echo $LD_LIBRARY_PATH

../lhapdf/install/bin/lhapdf  ls
