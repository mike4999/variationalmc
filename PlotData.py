#!/bin/env python
import numpy
import pylab
 
d = pylab.load('test.dat')
pylab.plot(d[:500])
pylab.show()
