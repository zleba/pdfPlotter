[![Build Status](https://travis-ci.org/zleba/pdfPlotter.svg?branch=master)](https://travis-ci.org/zleba/pdfPlotter)
# pdfPlotter
The online tool for plotting of PDFs from LHAPDF6 library.
Currently the central values of all PDFs are included.

Experimental version built from this repository may run on

http://pdfplotter.eu

## Technical description
The front-end is written in Javascript, the most crucial is the ROOTJS which is used for interactive plotting.

The back-end represents small Flask server written in Python.
This server can calculated PDF points if needed, e.g. when zooming.
This is done on the fly using AJAX GET request for the PDF values to the server.

The url address describes the plot and can be shared with others.


## Known issues
1) The position of the legend not spored in the URL
2) When curve color/style is changed, it don't affect ratio and legend
3) When moving with arrows both plots are moved, the ratio needs to be frozen.

## Possible improvments
1) Allowing for different q + scale-factor for various pdfs
2) Adding errors of PDFs
3) Adding q2-dependence plots + luminosity plots
