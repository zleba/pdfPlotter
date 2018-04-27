#! /usr/bin/env python
import lhapdf
#p = lhapdf.mkPDF("CT10", 0)
#p = lhapdf.mkPDF("CT10/0")
#print(p.xfxQ2(21, 1e-3, 1e4))
#for pid in p.flavors():
    #print(p.xfxQ(pid, 0.01, 91.2))
# TODO: demonstrate looping over PDF set members

#pset = lhapdf.getPDFSet("MRST2007lomod")
#print(pset.description)
#pcentral = pset.mkPDF(0)
##pdfs1 = pset.mkPDFs()
##pdfs2 = lhapdf.mkPDFs("CT10nlo") # a direct way to get all the set's PDFs
#import numpy as np
#xs = [x for x in np.logspace(-7, 0, 5)]
#qs = [q for q in np.logspace(1, 4, 4)]
#gluon_xfs = np.empty([len(xs), len(qs)])
#for ix, x in enumerate(xs):
#    for iq, q in enumerate(qs):
#        gluon_xfs[ix,iq] = pcentral.xfxQ(21, x, q)
#print(gluon_xfs)


from flask import Flask
from flask import render_template
app = Flask(__name__)

import ast

@app.route('/')
def index():
    return render_template('graph.html')


flavMap = {"gluon" : 21,
           "down" : 1, "up" : 2, "strange" : 3, "charm" : 4, "bottom" : 5, "top" : 6,
           "anti-down" : -1, "anti-up" : -2, "anti-strange" : -3, "anti-charm" : -4, "anti-bottom" : -5, "anti-top" : -6,
           "down-val" : 33, "up-val" : 34
};


#pset = lhapdf.getPDFSet('NNPDF31_lo_as_0118')
#print(pset.description)
#pdfs = pset.mkPDFs()

pdfs = {}

pdfAvail = lhapdf.availablePDFSets()

@app.route('/pdfList')
def pdfList():
    return str(pdfAvail)



@app.route('/pdf/<string:Type>/<string:pdfSet>/<string:flavour>/<string:varFix>/<float:var>/<points>')
def sendPDF(Type, pdfSet, flavour, varFix, var,  points):

    if flavour not in flavMap:
        return ""

    if pdfSet not in pdfAvail:
        return ""

    if pdfSet not in pdfs:
        print "Getting pdf " 
        pdfs[pdfSet] = lhapdf.getPDFSet(pdfSet).mkPDFs();
        print "Done" 
    pdfNow = pdfs[pdfSet]

    def getPDF3(i, x, q):
        if flavour == "up-val":
            val = pdfNow[i].xfxQ(flavMap["up"],   x, q)   - pdfNow[i].xfxQ(flavMap["anti-up"], x, q)
        elif flavour == "down-val":
            val = pdfNow[i].xfxQ(flavMap["down"], x, q) - pdfNow[i].xfxQ(flavMap["anti-down"], x, q)
        else:
            val = pdfNow[i].xfxQ(flavMap[flavour], x, q)
        return val

    def getPDF(i, vNow):
        if varFix == "q":
            x = max(1e-8, vNow)
            x = min(1, x)
            return getPDF3(i, x, var)
        else:
            q = min(8e4, vNow)
            q = max(1, q)
            return getPDF3(i, var, q)


    points =  ast.literal_eval(points)
    pdfVals = []


    if Type == "central":
        for v in points:
            pdfVals.append(getPDF(0, v))
    elif Type == "errSigma":
        for v in points:
            sum2 = 0
            for i in range(1,len(pdfNow)):
                sum2 += getPDF(i, v)**2
            sum2 /= max(1, len(pdfNow)-1)
            cnt = getPDF(0, v)
            from math import sqrt
            err = sqrt(max(0,sum2 - cnt**2))
            pdfVals.append([cnt, err])

#    if varFix == "q":
#        for x in points:
#            x = max(1e-8, x)
#            x = min(1, x)
#            if flavour == "up-val":
#                val = pdfs[0].xfxQ(flavMap["up"], x, var) - pdfs[0].xfxQ(flavMap["anti-up"], x, var)
#            elif flavour == "down-val":
#                val = pdfs[0].xfxQ(flavMap["down"], x, var) - pdfs[0].xfxQ(flavMap["anti-down"], x, var)
#            else:
#                val = pdfs[0].xfxQ(flavMap[flavour], x, var)
#
#            pdfVals.append(val)
#    elif varFix == "x":
#        for q in points:
#            q = max(8e4, q)
#            q = min(1, q)
#            val = pdfs[0].xfxQ(flavMap[flavour], var, q)
#            pdfVals.append(val)
#
    return str(pdfVals)

if __name__ == "__main__":
    app.run(host='0.0.0.0')



#print(lhapdf.version())
#print(lhapdf.__version__)
#lhapdf.pathsPrepend("/path/to/extra/pdfsets")
#print(lhapdf.paths())
# ...
