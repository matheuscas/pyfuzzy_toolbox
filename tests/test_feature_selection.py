import pyfuzzy_toolbox.features.selection as selection
import os

path_name = os.path.dirname(os.path.realpath(__file__))
arff_file_test = path_name + '/cornell_movies_test.arff'


def test_features_selection_10_fold_crossvalidation_seed_1_min_folds_10_CfsSubsetEval():
	selected_attributes = selection.select_attributes(arff_file_test, 10, 1, True, 10, search='BestFirst', evaluation='CfsSubsetEval')
	assert len(selected_attributes) == 6
	assert selected_attributes[0]['name'] == 'positive_to_negative_ratio_of_adjectives_count_and_bigrams_with_adjectives'
	assert selected_attributes[1]['name'] == 'positive_to_negative_ratio_of_adjectives_sum'
	assert selected_attributes[2]['name'] == 'positive_adjectives_sum_and_bigrams_with_adjectives'
	assert selected_attributes[3]['name'] == 'positive_to_negative_ratio_of_adjectives_sum_and_bigrams_with_adjectives'
	assert selected_attributes[4]['name'] == 'positive_to_negative_ratio_of_unigrams_and_bigrams_sum'
	assert selected_attributes[5]['name'] == 'sum_ratio_of_negative_unigrams_bigrams_and_trigrams'


def test_features_selection_10_fold_crossvalidation_seed_1_min_folds_9_CfsSubsetEval():
	selected_attributes = selection.select_attributes(arff_file_test, 10, 1, True, 9, search='BestFirst', evaluation='CfsSubsetEval')
	assert len(selected_attributes) == 7
	assert selected_attributes[0]['name'] == 'positive_to_negative_ratio_of_adjectives_count_and_bigrams_with_adjectives'
	assert selected_attributes[1]['name'] == 'positive_to_negative_ratio_of_adjectives_sum'
	assert selected_attributes[2]['name'] == 'positive_adjectives_sum_and_bigrams_with_adjectives'
	assert selected_attributes[3]['name'] == 'positive_to_negative_ratio_of_adjectives_sum_and_bigrams_with_adjectives'
	assert selected_attributes[4]['name'] == 'sum_ratio_of_positive_adjectives_and_bigrams_with_adjectives'
	assert selected_attributes[5]['name'] == 'positive_to_negative_ratio_of_unigrams_and_bigrams_sum'
	assert selected_attributes[6]['name'] == 'sum_ratio_of_negative_unigrams_bigrams_and_trigrams'
