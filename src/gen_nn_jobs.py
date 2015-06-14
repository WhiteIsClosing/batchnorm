import numpy as np
import sys
import os
from os.path import expanduser, sep
		 expanduser("~")
sys.path.append(expanduser("~") + "/repos/PyScheduler/src")
from addjob import jobScheduler


def normLow(layers):
	weights=[
		np.random.randn(x,y)*np.sqrt(x) 
		for x,y in zip(layers[:-1],layers[1:])
	]

def normHigh(layers):
	weights=[
		np.random.randn(x,y) 
		for x,y in zip(layers[:-1],layers[1:])
	]	


def uniHigh(layers):
	weights=[np.random.uniform(-1.7322,1.7322,[x,y])
			 for x,y in zip(layers[:-1],layers[1:])]	

def uniLow(layers):
	bw = 1.7322
	weights=[np.random.uniform(-bw,bw,[x,y])*np.sqrt(x)
			 for x,y in zip(layers[:-1],layers[1:])]	




if __name__ == "__main__":

	layers=[28*28,100,100,100,10]  # This will break if the topology changes from what is specified in the initial_conf.pickle

	learning_rate_list = 0.01 * (2 ** np.arange(12))
	weight_func = {
		'uni':{'low':uniLow, 'high':uniHigh}, 
		'norm':{'low':normLow, 'high':normHigh}
	}

	dist_type = ('uni','norm')
	dist_var  = ('low', 'high')
#	network_type = ('baseline', 'bn_v0', 'bn_v1')
#	only the baseline network is ready to write to the DB. others need work, so we start with this.
	network_type = (baseline,)
	js = jobScheduler()
	repeats = 4

	allinp=[]
	comment=[]

	for rx in range(repeats):
		for dt in dist_type:
			for dv in dist_var:
				W = weight_func[dt][dv](layers)
				for lr in learning_rate_list:
					data={
						'train_check':False,
						'test_check':False,

					}
					data['learnrate']=lr
					data['weights']=W
					allinp.append(data)
					comment.append('learning rate: {0}, dist_type: {1}, dist_var: {2}, repeat: {3}'.format(lr,dt,dv,rx+1))


	for nn in network_type:
		# js.addJobs('jerlich@nyu.edu','batchnorm.src',nn,allinp,comment)
		pass
