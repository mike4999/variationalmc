from VMCHelp import *
import numpy
import random
from VMC_template import *
 
import stats
CalcStatistics=stats
 
H2=H2Class()
H2.SetParams([0.5])
H2.SetIons(SetBondLength(1.4))
R=numpy.zeros((2,3),float)
R[0]=[1.0,0.3,0.2]
R[1]=[2.0,-0.2,0.1]
print "The Local Energy should be -1.819",H2.LocalEnergy(R)
energyList=VMC(H2,1000)
if energyList==None:
	exit()
print "A short run gives ",CalcStatistics.Stats(numpy.array(energyList))
print "The correct answer is approximately -0.86"
energyList=VMC(H2,100000)
print "A longer run gives ",CalcStatistics.Stats(numpy.array(energyList))
pylab.plot(energyList)
pylab.savefig("EnergyGraph.png")
