import numpy as np
import fis


def __max_value_index(list):
    """
    Find the idx of the max value in list

    list -- numeric list
    """

    max_val = max(list)
    max_idx = list.index(max_val)
    return max_idx


def generate_regions(_range, N):
    """
    Generates 2N + 1 regions in the passed range

    range -- numpy array defining the range of the regions
    N -- integer that defines the 2N + 1 regions in the passed range
    """

    if not type(_range) == np.ndarray:
        raise TypeError()

    if not type(N) == int:
        raise TypeError('N must be a integer number')

    # array split does not result in an equal division

    num_regions = float((2 * N) + 1)
    max_value_range = _range[len(_range) - 1]
    min_value_range = _range[0]

    regions = []

    if num_regions == 1:
        regions.append(fis.FuzzySet(
            'R0', [min_value_range, np.median(_range), max_value_range], _range))
    elif num_regions == 3:
        medium_region = fis.FuzzySet(
            'R1', [min_value_range, np.median(_range), max_value_range], _range)
        lower_region = fis.FuzzySet(
            'R0', [min_value_range, min_value_range, medium_region.params[1]], _range)
        higher_region = fis.FuzzySet(
            'R2', [medium_region.params[1], max_value_range, max_value_range], _range)
        regions.append(lower_region)
        regions.append(medium_region)
        regions.append(higher_region)
    else:
        # minus 2, due to the two triangular sets in the lower values and the
        # higher values
        num_regions = num_regions - 2
        regions_size = round(
            (max_value_range - min_value_range) / num_regions, 4)
        if abs(round(max_value_range - min_value_range, 4)) != abs(round(regions_size * num_regions, 4)):
            raise ValueError(
                'Array split does not result in an equal division')

        regions_size = regions_size + (regions_size / 2.0)
        prev_a = min_value_range
        regions.append(fis.FuzzySet('R0', [
                       min_value_range, min_value_range, prev_a + float(regions_size / 2.0)], _range))
        for r in range(1, int(num_regions) + 1):
            region_name = 'R' + str(int(r))
            regions.append(fis.FuzzySet(region_name, [
                           prev_a, prev_a + float(regions_size / 2.0), prev_a + regions_size], _range))
            prev_a = prev_a + float(regions_size / 2.0)

        regions.append(fis.FuzzySet('R' + str(int(num_regions) + 2),
                                    [prev_a, max_value_range, max_value_range], _range))

    return regions


def wang_mendel(inputs, inputs_names, inputs_regions, output_name, outputs_regions, discrete_class_beginning=True):
    """
    The Wang & Mendel Method is the well known method for the automatic generation of FRBs (Fuzzy Rule Based).
    It returns a dictionary with generated rules, where the values are fis.Rule objects and keys are string compositions of the each rule antecedents

    inputs -- 2d list with the features data. The file must contain data in the following structure:
                                    y, x1, x2, x3, x4,... ,xn (or x1, x2, x3, x4,... ,xn,y)
                                    y -- numeric known output for xi...xn input features data
                                    xi...xn -- numeric input features data
    inputs_names -- list of string names for each input feature. x1 has a name, x2 has another and go on.
    inputs_regions -- a list of list of fuzzy regions (sets of fis.FuzzySet type) for each input feature.
                                            E.g. x1_regions = [x1_region_0, x1_region_1, x1_region_2]
                                                     x2_regions = [x2_region_0, x2_region_1, x2_region_2, , x2_region_3]
                                                     inputs_regions = [x1_regions, x2_regions]
    output_name -- string name for the output feature.
    outputs_regions -- a list of fuzzy regions (sets of fis.FuzzySet type) for the output feature.
                                            E.g. outputs_regions = [y_region_0, y_region_1, y_region_2]
    """

    rules = []
    for input in inputs:
        # splitted = line.strip().split(',')
        # y = float(splitted[0]) if discrete_class_beginning else float(splitted[len(splitted) - 1])
        # xs = map(float, splitted[1:]) if discrete_class_beginning else map(float, splitted[:len(splitted) - 1])
        y = input[0] if discrete_class_beginning else input[len(input) - 1]
        xs = input[1:] if discrete_class_beginning else input[:len(input) - 1]
        rule = fis.Rule([], [])
        for i, xi in enumerate(xs):
            xi_degrees = []
            for set in inputs_regions[i]:
                xi_degrees.append(set.degree(xi))
            max_idx = __max_value_index(xi_degrees)
            rule.antecedents.append(
                fis.Antecedent(inputs_names[i], xi, inputs_regions[i][max_idx]))
        y_degrees = []
        for set in outputs_regions:
            y_degrees.append(set.degree(y))
        max_idx = __max_value_index(y_degrees)
        rule.outputs.append(
            fis.Output(output_name, y, outputs_regions[max_idx]))
        rules.append(rule)

    combined_fuzzy_rule_base = {}
    for rule in rules:
        rule_key = ''
        for a in rule.antecedents:
            rule_key = rule_key + a.fuzzy_set.name + '/'
        rule_key = rule_key[:len(rule_key) - 1]
        rule_degree = rule.degree()
        if rule_key in combined_fuzzy_rule_base.keys():
            if abs(rule_degree) > abs(combined_fuzzy_rule_base[rule_key].degree()):
                combined_fuzzy_rule_base[rule_key] = rule
        else:
            combined_fuzzy_rule_base[rule_key] = rule

    return combined_fuzzy_rule_base
