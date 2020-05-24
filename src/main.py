import pandas as pd
from os import path
from rocket_module import *

''' Load a list of rockets from a csv file '''
def load_rockets (filename) :
	if(not path.exists(filename)):
		return []
	data = pd.read_csv(filename, sep=',')
	rocket_list = []

	i_row = len(data.index)
	for i in range(0,i_row):
		name = data.iat[i, 0]
		info = [data.iat[i, 1], data.iat[i, 2], data.iat[i, 3]]
		spec = [data.iat[i, 4], data.iat[i, 5], data.iat[i, 6], data.iat[i, 7], 
				data.iat[i, 8], data.iat[i, 9], data.iat[i, 10], data.iat[i, 11],
				data.iat[i, 12], data.iat[i, 13] ,data.iat[i, 14], data.iat[i, 15], 
				data.iat[i, 16], data.iat[i, 17], data.iat[i, 18], data.iat[i,19]]
		ri = Rocket(name, info, spec)
		rocket_list.append(ri)

	return rocket_list

''' Save a list of rockets. We suppose the file existing '''
def save_rockets(rocket_list, filename, erase):
	if(not path.exists(filename)):
		return
	data = pd.read_csv(filename, sep=',', index_col=False)
	if (erase):
		data = data[0:0]
	n_row = len(data.index)
	
	for i in range(0, len(rocket_list)):
		ri = rocket_list[i]
		name = ri.get_name()
		info = ri.get_info()
		spec = ri.get_spec()
		if (len(spec) == 10):
			spec.extend([0,0,0,0,0,0])
		data.loc[n_row + i] = [name] + info + spec
	    
	data.to_csv(filename, na_rep='', float_format='%.2f', index=False)
