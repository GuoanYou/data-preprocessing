from sklearn import preprocessing
import numpy as np
def zscore(inputfile,outputfile):
	x=np.loadtxt(inputfile, delimiter=',')
	#print x.dtype
	x_scaled = preprocessing.scale(x)
	#print x
	#print x_scaled
	np.savetxt(outputfile, x_scaled, fmt="%f", delimiter=",")

zscore("synapse-1.2_py.txt","synapse-1.2_zs_py.txt")