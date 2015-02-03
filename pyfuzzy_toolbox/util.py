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
	return file_name


# UNTESTED

def split_arff_dict(arff_dict, train_ratio=0.8):
	data_length = len(arff_dict['data'])
	split_index = data_length - int((data_length * train_ratio) / 10)
	train_arff_dict = Dict()
	test_arff_dict = Dict()
	train_arff_dict.relation = 'train_data_' + arff_dict.relation
	test_arff_dict.relation = 'test_data_' + arff_dict.relation
	train_arff_dict['attributes'] = arff_dict['attributes']
	test_arff_dict['attributes'] = arff_dict['attributes']
	train_arff_dict['data'] = arff_dict['data'][:split_index]
	test_arff_dict['data'] = arff_dict['data'][split_index:]
	return train_arff_dict, test_arff_dict


def equalizer_unfiltered_arff_data(unfiltered_arff, filtered_arff):
	filtered_attributes = []
	for fa in filtered_arff['attributes']:
		filtered_attributes.append(fa[0])

	new_filtered_attributes = []
	new_filtered_data = []

	for d in unfiltered_arff['data']:
		new_filtered_data_line = []
		for idx, dd in enumerate(d):
			if unfiltered_arff['attributes'][idx][0] in filtered_attributes:
				new_filtered_data_line.append(dd)
		new_filtered_data.append(new_filtered_data_line)

	for a in unfiltered_arff['attributes']:
		if a[0] in filtered_attributes:
			new_filtered_attributes.append(a)

	new_filtered_arff_dict = {}
	new_filtered_arff_dict['relation'] = 'equalized_arff_file'
	new_filtered_arff_dict['attributes'] = new_filtered_attributes
	new_filtered_arff_dict['data'] = new_filtered_data

	return new_filtered_arff_dict
