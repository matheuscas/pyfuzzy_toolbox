import arff
import time
import datetime
from addict import Dict


def create_arff_dict(list_of_attributes_and_data, relation):

	arff_dict = Dict()
	arff_dict.relation = relation
	arff_dict.attributes = []
	arff_dict.data = []

	arff_dict.attributes = list_of_attributes_and_data[0]['attributes']
	for att_data in list_of_attributes_and_data:
		arff_dict.data.append(att_data['data'])

	return arff_dict


def create_arff_file(arff_dict, name=None, timestamp=False):
	file_name = name if name else arff_dict.relation
	if timestamp:
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')
		file_name = file_name + '_' + st
	file_name = file_name + '.arff'
	raw_dict = arff_dict.to_dict()
	arff_file = open(file_name, 'w')
	arff.dump(raw_dict, arff_file)
