import weka.core.jvm as jvm
from weka.core.converters import Loader
from weka.attribute_selection import ASSearch, ASEvaluation, AttributeSelection


def extract_attributes(splitted_cv_results, min_folds_to_select):
	selected_attributes = []
	for idx, res in enumerate(splitted_cv_results):
		if idx >= 5 and idx <= len(splitted_cv_results) - 2:
			parts = res.split()
			num_folds = int(parts[0].split('(')[0])
			if len(parts) > 4:
				index = int(parts[3])
			else:
				index = int(parts[2])
			name = parts[len(parts) - 1]
			if num_folds >= min_folds_to_select:
				selected_attributes.append({'index':index, 'name':name})
	return selected_attributes


def select_attributes(arff_path_file, folds, seed, cross_validation, min_folds_to_select, class_is_last=True, search='BestFirst', evaluation='CfsSubsetEval'):
	jvm.start()
	loader = Loader(classname="weka.core.converters.ArffLoader")
	data = loader.load_file(arff_path_file)
	if class_is_last:
		data.class_is_last()
	else:
		data.class_is_first()
	search = ASSearch(classname="weka.attributeSelection." + search, options=["-D", "1", "-N", "5"])
	evaluator = ASEvaluation(classname="weka.attributeSelection." + evaluation)
	attsel = AttributeSelection()
	if cross_validation:
		attsel.folds(folds)
		attsel.seed(seed)
		attsel.crossvalidation(True)
	attsel.search(search)
	attsel.evaluator(evaluator)
	attsel.select_attributes(data)
	splitted_cv_results = attsel.cv_results.split('\n')
	jvm.stop()
	return extract_attributes(splitted_cv_results, min_folds_to_select)
