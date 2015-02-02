import operators as ops
import operator
import random
import wm
import evaluation


def eval_examples(examples):

    TP = 0.0
    TN = 0.0
    FP = 0.0
    FN = 0.0
    NONE = 0.0

    for e in examples:
        if e['predicted_class']:
            if e['known_class'] == 1.0 and e['predicted_class'].name == 'positive':
                TP = TP + 1.0
            elif e['known_class'] == -1.0 and e['predicted_class'].name == 'negative':
                TN = TN + 1.0
            elif e['known_class'] == 1.0 and e['predicted_class'].name == 'negative':
                FN = FN + 1.0
            elif e['known_class'] == -1.0 and e['predicted_class'].name == 'positive':
                FP = FP + 1.0
        else:
            NONE += 1

    return {'precision': evaluation.precision(TP, FP),
            'recall': evaluation.recall(TP, FN),
            'f1': evaluation.f1(TP, FP, TN, FN),
            'accuracy': evaluation.accuracy(TP, FP, TN, FN),
            'non classified': NONE}


def __rule_compatibility(example, rule):
    """
    Calculates the compatibility degree between example and rule

    example - numeric array with input values
    rule - sets.Rule object
    """

    compatibility = 1
    for ei, e in enumerate(example):
        example_part = e
        if ei == 0 and example_part < rule.antecedents[ei].fuzzy_set.params[0]:
            example_part = float(rule.antecedents[ei].fuzzy_set.params[0])

        if ei == (len(rule.antecedents) - 1) and example_part > rule.antecedents[ei].fuzzy_set.params[2]:
            example_part = float(rule.antecedents[ei].fuzzy_set.params[2])

        compatibility = ops.t_norm(
            compatibility, rule.antecedents[ei].fuzzy_set.degree(example_part))
    return compatibility


def cfrm(examples, rules, verbose=False):
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
            e_rule[r] = __rule_compatibility(e['inputs'], r)
        rule_compatibility = max(
            e_rule.iteritems(), key=operator.itemgetter(1))

        print e_rule.values()
        print 'rule_compatibility:', rule_compatibility[0].outputs[0].fuzzy_set.name, rule_compatibility[1]
        print '--------------------------------'
        max_rule = rule_compatibility[0]
        if rule_compatibility[1] == 0:
            e['predicted_class'] = None
        else:
            e['predicted_class'] = max_rule.outputs[0].fuzzy_set


def gfrm(examples, rules, verbose=False):
    """
    Classifies examples using the class that has the highest compatibility degree with the example. The function fills 'predicted_class' field in each example with the predicted FuzzySet class.

            **Binary classfication only
            ** It is a messy code. PLEASE REFACTOR!!!!!

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
            rule_compat = __rule_compatibility(e['inputs'], r)
            for o in r.outputs:
                if o.fuzzy_set.name not in e_rule:
                    e_rule[o.fuzzy_set.name] = []

                degrees = e_rule[o.fuzzy_set.name]
                degrees.append(rule_compat)
                e_rule[o.fuzzy_set.name] = degrees

        # print 'class compatibilities', e_rule
        # print '--------------------------------'

        for (key, value) in e_rule.iteritems():
            e_rule[key] = float(sum(value)) / len(value)

        print 'class compatibilities', e_rule

        rule_compatibility = max(
            e_rule.iteritems(), key=operator.itemgetter(1))
        max_class_name = rule_compatibility[0]
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

        if rule_compatibility[1] == 0:
            e['predicted_class'] = None
            print 'predicted_class', None
        else:
            print 'predicted_class', max_class.name
            e['predicted_class'] = max_class
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
