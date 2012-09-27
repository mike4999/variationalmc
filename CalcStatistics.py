import ReadData 
import numpy
import pylab
from math import *

myArray=ReadData.loadAscii("DataSet_PythonStatisticalAnalysis.txt")
print "I have read in myArray and the first element is ",myArray[0]

def Mean(myArray):
	for i in myArray:
        	print i 
    # this prints everything in the array.
    # let's change this to average things in a
	average = numpy.average (myArray)
	return average

def StandardDev(myArray):
	# do stuff
	standard_dev = numpy.std(myArray)
	return standard_dev

def NaiveStandardError(myArray):
	# calculate the standard error by calling the standard deviation function
	Neff = len(myArray)
	sig = StandardDev(myArray)
	se = sig/(numpy.sqrt(Neff-1))
	return standard_err
