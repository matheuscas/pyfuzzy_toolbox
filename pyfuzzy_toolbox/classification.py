import operators as ops
import operator
import random
import wm
import evaluation
import fis
import pprint


def eval_examples(examples):

    TP = 0.0
    TN = 0.0
    FP = 0.0
    FN = 0.0
    NONE = 0.0
    NUM_POSITIVES = 0.0
    NUM_NEGATIVES = 0.0

    for e in examples:
        if e['predicted_class']:
            if (e['known_class'] == 1.0 or e['known_class'] == 'positive') and e['predicted_class'].name == 'positive':
                TP = TP + 1.0
                NUM_POSITIVES += 1
            elif (e['known_class'] == -1.0 or e['known_class'] == 'negative') and e['predicted_class'].name == 'negative':
                TN = TN + 1.0
                NUM_NEGATIVES += 1
            elif (e['known_class'] == 1.0 or e['known_class'] == 'positive') and e['predicted_class'].name == 'negative':
                FN = FN + 1.0
                NUM_POSITIVES += 1
            elif (e['known_class'] == -1.0 or e['known_class'] == 'negative') and e['predicted_class'].name == 'positive':
                FP = FP + 1.0
                NUM_NEGATIVES += 1
        else:
            NONE += 1

    return {'precision': evaluation.precision(TP, FP),
            'recall': evaluation.recall(TP, FN),
            'f1': evaluation.f1(TP, FP, TN, FN),
            'accuracy': evaluation.accuracy(TP, FP, TN, FN),
            'non classified': NONE,
            'TP': TP,
            'TN': TN,
            'FP': FP,
            'FN': FN,
            'NUM_POSITIVES': NUM_POSITIVES,
            'NUM_NEGATIVES': NUM_NEGATIVES,
            'TPR': evaluation.tpr(TP, FN),
            'TNR': evaluation.tnr(TN, FP)}


def __rule_compatibility(example, rule):
    """
    Calculates the compatibility degree between example and rule

    example - numeric array with input values
    rule - sets.Rule object
    """

    compatibility = 1
    for ei, input_example in enumerate(example):
        # checks if the antecedent fuzzy set is the highest set
        temp_input_example = input_example
        antecedent_fuzzy_set = rule.antecedents[ei].fuzzy_set
        if (antecedent_fuzzy_set.params[len(antecedent_fuzzy_set.params) - 1] == antecedent_fuzzy_set.range[len(antecedent_fuzzy_set.range) - 1]) and \
                (antecedent_fuzzy_set.params[len(antecedent_fuzzy_set.params) - 1] == antecedent_fuzzy_set.params[len(antecedent_fuzzy_set.params) - 2]):
            if temp_input_example > antecedent_fuzzy_set.params[len(antecedent_fuzzy_set.params) - 1]:
                temp_input_example = float(
                    antecedent_fuzzy_set.params[len(antecedent_fuzzy_set.params) - 1])

        # checks if the antecedent fuzzy set is the lowest set
        if (antecedent_fuzzy_set.params[0] == antecedent_fuzzy_set.range[0]) and \
                (antecedent_fuzzy_set.params[0] == antecedent_fuzzy_set.params[1]):
            if temp_input_example < antecedent_fuzzy_set.params[0]:
                temp_input_example = float(antecedent_fuzzy_set.params[0])

        compatibility = ops.t_norm(
            compatibility, rule.antecedents[ei].fuzzy_set.degree(temp_input_example))
    return compatibility


def cfrm(examples, rules, verbose=False, weights=None):
    """
    Classifies examples using the rule that has the highest compatibility degree with the example. The function fills 'predicted_class' field in each example with the predicted FuzzySet class.

    examples -- list of dicts with the following structure:
                            {'inputs': [x1, x2, x3, ..., xn],
                            'known_class': 'positive',
                            'predicted_class:' None}
    rules -- list of Rule objects to classify examples
    """

    for ei, e in enumerate(examples):
        if verbose:
            print str(ei), '/', str(len(examples))
        e_rule = {}
        for r in rules:
            if not weights:
                e_rule[r] = __rule_compatibility(e['inputs'], r)
            else:
                e_rule[r] = __rule_compatibility(e['inputs'], r)
                for rule_weight in weights:
                    if r in rule_weight:
                        e_rule[r] = e_rule[r] * rule_weight[r]
                        break
        rule_compatibility = max(
            e_rule.iteritems(), key=operator.itemgetter(1))
        max_rule = rule_compatibility[0]
        if rule_compatibility[1] == 0:
            e['predicted_class'] = None
        else:
            e['predicted_class'] = max_rule.outputs[0].fuzzy_set


def gfrm(examples, rules, verbose=False, weights=None):
    """
    Classifies examples using the class that has the highest compatibility degree with the example.
    The function fills 'predicted_class' field in each example with the predicted FuzzySet class.

            **Binary classfication only
            ** It is a messy code. PLEASE REFACTOR!!!!!

    examples -- list of dicts with the following structure:
                            {'inputs': [x1, x2, x3, ..., xn],
                            'known_class': 'positive',
                            'predicted_class:' None}
    rules -- list of Rule objects to classify examples
    """

    for ei, example in enumerate(examples):
        if verbose:
            print str(ei), '/', str(len(examples))
        example_rule = {}
        for rule in rules:
            rule_compat = __rule_compatibility(example['inputs'], rule)
            if weights:
                for rule_weight in weights:
                    if rule in rule_weight:
                        rule_compat = rule_compat * rule_weight[rule]
                        break

            for output in rule.outputs:
                if output.fuzzy_set.name not in example_rule:
                    example_rule[output.fuzzy_set.name] = []

                degrees = example_rule[output.fuzzy_set.name]
                degrees.append(rule_compat)
                example_rule[output.fuzzy_set.name] = degrees

        # print 'class compatibilities', example_rule
        # print '--------------------------------'

        for (key, value) in example_rule.iteritems():
            example_rule[key] = float(sum(value)) / len(value)

        if verbose:
            print 'class compatibilities', example_rule

        rule_compatibility = max(
            example_rule.iteritems(), key=operator.itemgetter(1))
        max_class_name = rule_compatibility[0]
        if verbose:
            print 'max_class_name:', max_class_name
        max_class = None
        for r in rules:
            for o in r.outputs:
                if max_class_name == o.fuzzy_set.name:
                    max_class = o.fuzzy_set
                    break
            else:
                continue
            break

        if verbose:
            print 'known_class: ', example['known_class']
        if rule_compatibility[1] == 0:
            example['predicted_class'] = None
            if verbose:
                print 'predicted_class', None
        else:
            if verbose:
                print 'predicted_class', max_class.name
            example['predicted_class'] = max_class
        if verbose:
            print '--------------------------------'


def _k_folds(_list, k):

    fold_size = len(_list) / k
    folds = []
    start = 0
    end = fold_size
    for ki in xrange(1, k + 1):
        folds.append(_list[start:end])
        start = end
        end = fold_size * (ki + 1)

    return folds


def _create_examples(inputs, discrete_class_beginning):

    examples = []
    for input in inputs:
        y = input[0] if discrete_class_beginning else input[len(input) - 1]
        xs = input[1:] if discrete_class_beginning else input[:len(input) - 1]
        examples.append(
            {'inputs': xs, 'known_class': y, 'predicted_class': None})

    return examples


def cfrm_cross_validation(inputs, inputs_names, inputs_regions, output_name, outputs_regions, discrete_class_beginning=True, verbose=False, k=10, scramble=True):

    if len(inputs) % k != 0:
        raise ValueError("Cannot split inputs in " + str(k) + " equal parts.")

    if k < 2:
        raise ValueError(
            "Cannot make k-fold cross validation with k less than 2")

    if scramble:
        random.shuffle(inputs)

    folds = _k_folds(inputs, k)

    accuracies = []
    for fi, fold in enumerate(folds):
        if verbose:
            print '===>', "fold ", fi, '<==='
        fold_rules = []
        for i_fi, i_fold in enumerate(folds):
            if fi != i_fi:
                i_fold_rules = wm.wang_mendel(
                    i_fold, inputs_names, inputs_regions, output_name, outputs_regions, discrete_class_beginning)
                fold_rules = fold_rules + i_fold_rules.values()

        examples = _create_examples(fold, discrete_class_beginning)
        cfrm(examples, fold_rules, verbose=False)
        fi_accuracy = eval_examples(examples)['accuracy']
        if verbose:
            print '--->', "fold_accuracy", fi, fi_accuracy, '<---'
        accuracies.append(fi_accuracy)

    return sum(accuracies) * 1.0 / len(accuracies)


def average(examples):
    for example in examples:
        avg = reduce(
            lambda x, y: x + y, example['inputs']) / len(example['inputs'])
        if avg > 0:
            example['predicted_class'] = fis.FuzzySet('positive', [], [])
        elif avg < 0:
            example['predicted_class'] = fis.FuzzySet('negative', [], [])
        else:
            example['predicted_class'] = None


def rules_weights(combined_fuzzy_rule_base_list, list_of_modified_fold_test_data):

    combined_fuzzy_rule_base_weights = []
    for fold_rules_idx, fold_rules in enumerate(combined_fuzzy_rule_base_list):
        fold_rules_weights = []
        for rule_key in fold_rules:
            rule = fold_rules[rule_key]
            pos_beta = 0
            neg_beta = 0
            examples_data = _create_examples(
                list_of_modified_fold_test_data[fold_rules_idx], False)
            for example in examples_data:
                if example['known_class'] == 1.0:
                    pos_beta += __rule_compatibility(example['inputs'], rule)
                elif example['known_class'] == -1.0:
                    neg_beta += __rule_compatibility(example['inputs'], rule)

            if pos_beta == neg_beta:
                cf = 0
            else:
                cf = abs(pos_beta - neg_beta) / (pos_beta + neg_beta)

            fold_rules_weights.append({rule: cf})
        combined_fuzzy_rule_base_weights.append(fold_rules_weights)
    return combined_fuzzy_rule_base_weights
