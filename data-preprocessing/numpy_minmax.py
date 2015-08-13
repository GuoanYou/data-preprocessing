from sklearn import preprocessing
import numpy as np
def zscore(inputfile,outputfile):
	x=np.loadtxt(inputfile, delimiter=',')
	#print x.dtype
	min_max_scaler = preprocessing.MinMaxScaler()
	#x_scaled = preprocessing.scale(x)
	x_minmax = min_max_scaler.fit_transform(x)
	#print x
	#print x_scaled
	np.savetxt(outputfile, x_minmax, fmt="%f", delimiter=",")

zscore("camel-1.6_py.txt","camel-1.6_mm_py.txt")