from VMCHelp import *
import numpy
import random
import CalcStatistics
 
 
class H2Class:
	def SetParams(self,params):
		self.params=copy(params)
		self.BondLength = copy(params)
	def SetIons(self,ions):
		self.ions=ions.copy()
	def SetBondLength(self,BondLength):
		self.BondLength=BondLength
		TempIon=numpy.zeros((2,3),float)
		TempIon[0][0]=-BondLength/2.0
		TempIon[1][0]=BondLength/2.0
		self.SetIons(TempIon)
	def WaveFunction(self,R):
		alpha=self.params[0]
		# write code to evaluate your wavefunction here
		ionOne = self.ions[0]
		ionTwo = self.ions[1]
		electronOne = R[0]
		electronTwo = R[1]
		# attempt to calculate the midpoint:
		vecSumOne = numpy.add(ionOne, electronOne)
		midPOne  = numpy.divide(vecSumOne,2)
		vecSumTwo = numpy.add(ionTwo,electronTwo)
		midPTwo = numpy.divide(vecSumTwo,2)
		### Get the vector between the electron and the center of the bond:
		vecOne = numpy.subtract(electronOne,midPOne)
		vecTwo = numpy.subtract(electronTwo,midPTwo)
		#### Get the magnitudes of those vectors:
		elecOneAbs = numpy.dot(vecOne,vecOne)
		elecTwoAbs = numpy.dot(vecTwo,vecTwo)
		wfc = math.exp (-alpha*(elecOneAbs + elecTwoAbs))
		return wfc 
	
	def LocalEnergy(self,R):
		KE=-0.5*LaplacianPsiOverPsi(R,self.WaveFunction)
		V= potentialE(self.ions,R)  #change this to actually calculate V
		return V+KE
 
 
def VMC(WF,numSteps):
	seed=5   ### my random number seed
	EnergyList=[]  #### dont know
	R=numpy.zeros((2,3),float)   ### positions of two particles
	movesAttempted=0.0
	movesAccepted=0.0
	print "num-steps: ",numSteps
	for i in range(numSteps):  ##### performing all the required number of steps         #for step in xrange(0,numSteps)
		
		OldPos= R.copy()
		oldWfc= WF.WaveFunction(R)
		for ptcl in xrange(0,len(R)):         		 #### looping over the partices
			R[ptcl] = numpy.add( R[ptcl], (numpy.random.rand(3) - 0.6)*1.5 ) ## new pos?
		newWfc= WF.WaveFunction(R) 		 #### finding wavefunction for the new pos
#		print "newWfc:" , newWfc, "  oldWfc:", oldWfc
		ratio = (newWfc**2/oldWfc**2)
#		print "ratio: ", ratio 
		rander = numpy.random.rand(1)
		if ratio > rander:
			Eloc = WF.LocalEnergy(R)
			EnergyList.append(Eloc)
			movesAttempted+=1
			movesAccepted+=1
		else:
			movesAttempted+=1
			R = OldPos                	 # restore R to before the now rejected move
	print "movesAcepted: ",  movesAccepted, ",   movesAttempted: ", movesAttempted				
	print "Acceptance Ratio", movesAccepted/movesAttempted
	return EnergyList
 
 
def Optimize(H2):
	optimizeList=[]
   #add things here to loop over alpha and do optimization
	return (optimizeList,bestAlpha)
 
 
def BondLength(H2):
	bondList=[]
   # add things here to loop over bondlengths
	return (bondList,bestBond)
 
############added by me 

def potentialE(ions, elecs):
	ionOne=ions[0]
	ionTwo=ions[1]
	elecOne=elecs[0]
	elecTwo=elecs[1]
	ionElec = -invDistance(ionOne,elecOne) - invDistance(ionOne,elecTwo)  -invDistance(ionTwo,elecOne) - invDistance(ionTwo,elecTwo) 
	elecElec= invDistance(elecOne,elecTwo)*2
	ionIon = invDistance(ionOne,ionTwo)*2 
	v = ionElec + elecElec + ionIon	
	return v

def invDistance(posa, posb):
	diff = numpy.subtract(posb,posa)
	dis = numpy.dot(diff,diff)
	inv = numpy.divide(1,dis)
	return dis
 
 
class H2JastrowClass:
	def SetParams(self,params):
		self.params=copy(params)
		self.alpha = params[0]
		self.beta  = params[1]
		self.a_ee = 0.5
		self.a_ep = 1.0
		self.b_ee = sqrt(self.a_ee/self.beta)
		self.b_ep = sqrt(self.a_ep/self.beta)
	def SetIons(self,ions):
		self.ions=ions.copy()
	def LocalEnergy(self,R):
		KE=-0.5*LaplacianPsiOverPsi(R,self.WaveFunction)
	def WaveFunction(self, R):
		return 0.0
 
#def OptimizeJastrow(H2):
#fill this in


