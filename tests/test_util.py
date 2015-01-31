from pyfuzzy_toolbox import transformation as trans
from pyfuzzy_toolbox import preprocessing as pre
from pyfuzzy_toolbox import util
import pyfuzzy_toolbox.features.base as features
import test_preprocessing as tpre
import pprint
import os


print 'Loading test text 1'
bow_sentences_1 = pre.start(tpre.text_1)
bow_sentences_1 = trans.start(bow_sentences_1)

print 'Loading test text 1a'
bow_sentences_1a = pre.start(tpre.text_1a)
bow_sentences_1a = trans.start(bow_sentences_1a)

print 'Loading test text 2a'
bow_sentences_2a = pre.start(tpre.text_2a)
bow_sentences_2a = trans.start(bow_sentences_2a)


def test_create_arff_dict():
	list_of_attributes_and_data = []

	list_of_attributes_and_data.append(features.start(bow_sentences_1, features.NOMINAL_NEGATIVE_POLARITY))
	list_of_attributes_and_data.append(features.start(bow_sentences_1a, features.NOMINAL_POSITIVE_POLARITY))
	list_of_attributes_and_data.append(features.start(bow_sentences_2a, features.NOMINAL_NEGATIVE_POLARITY))

	arff_dict = util.create_arff_dict(list_of_attributes_and_data, 'test')
	assert len(arff_dict.attributes) == 74
	assert len(arff_dict.data[0]) == len(arff_dict.data[1]) == len(arff_dict.data[2]) == 74

	# pprint.pprint(arff_dict)


def test_create_arff_file():

	if os.path.isfile('test.arff'):
		os.remove('test.arff')

	list_of_attributes_and_data = []

	list_of_attributes_and_data.append(features.start(bow_sentences_1, features.NOMINAL_NEGATIVE_POLARITY))
	list_of_attributes_and_data.append(features.start(bow_sentences_1a, features.NOMINAL_POSITIVE_POLARITY))
	list_of_attributes_and_data.append(features.start(bow_sentences_2a, features.NOMINAL_NEGATIVE_POLARITY))

	arff_dict = util.create_arff_dict(list_of_attributes_and_data, 'test')
	util.create_arff_file(arff_dict)
	assert os.path.isfile('test.arff') == True
