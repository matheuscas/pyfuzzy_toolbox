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


def k_fold_split_arff_dict(arff_dict, k=10):
    def is_positive(d):
    	return True if d[len(d) - 1] == 1.0 or d[len(d) - 1] == 'positive' else False

    def is_negative(d):
    	return True if d[len(d) - 1] == -1.0 or d[len(d) - 1] == 'negative' else False
    positive_data = []
    negative_data = []

    for data in arff_dict['data']:
        if is_positive(data):
            positive_data.append(data)
        elif is_negative(data):
            negative_data.append(data)

    size_fold = ((len(positive_data)) / k) if len(positive_data) >= len(negative_data) else ((len(negative_data)) / k)
    index_limit = len(positive_data) if len(positive_data) >= len(negative_data) else len(negative_data)
    k_folds_list = []
    fold = 1

    fold_data = []
    for dx in range(index_limit):
    	fold_data.append(positive_data[dx])
    	fold_data.append(negative_data[dx])
    	if dx == (fold * size_fold - 1):
    		k_folds_list.append(fold_data)
    		fold_data = []
    		fold += 1

    k_folds_arff_dicts = []
    for k_fold_data in k_folds_list:
    	k_folds_arff_dicts.append({'attributes': arff_dict['attributes'], 'data': k_fold_data})

    return k_folds_arff_dicts


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
