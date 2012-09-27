from VMCHelp import *
import numpy
import random
from VMC_template import *
 
H2=H2Class()
H2.SetParams([0.5])
H2.SetIons(SetBondLength(1.4))
coords=numpy.zeros((2,3),float)
coords[0,:]=[1.0,0.5,0.3]
coords[1,:]=[-0.2,0.1,-0.1]
energyVal=H2.WaveFunction(coords)
print "Your wavefunction is working if this is 0.496585",energyVal
