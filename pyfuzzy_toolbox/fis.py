import mf


class FuzzySet(object):

    """docstring for FuzzySet"""

    TRIMF = 'trimf'

    def __init__(self, name, params, _range, type=TRIMF):
        self.name = name
        self.type = type
        self.params = params
        self.range = _range

    def _get_mf(self, input_value):
        return mf.trimf(input_value, self.params)

    def defuzz(self):
        fmf = self._get_mf(self.range)
        return mf.centroid(self.range, fmf)

    def degree(self, input_value):
        return self._get_mf(input_value)

    def alpha_cut(self, input_value):
        top_value = self.degree(input_value)
        alpha_cut = self.degree(self.range)
        for i, a in enumerate(alpha_cut):
            if alpha_cut[i] > top_value:
                alpha_cut[i] = top_value
        return alpha_cut


class Antecedent(object):

    """docstring for Antecedent"""

    def __init__(self, input_name, input_value, fuzzy_set):
        self.input_name = input_name
        self.input_value = input_value
        self.fuzzy_set = fuzzy_set


class Output(Antecedent):

    """docstring for Output"""

    def __init__(self, input_name, input_value, fuzzy_set):
        Antecedent.__init__(self, input_name, input_value, fuzzy_set)


class Rule(object):

    """docstring for Rule"""

    def __init__(self, antecedents, outputs):
        self.antecedents = antecedents
        self.outputs = outputs

    def degree(self):
        rule_degree = 1
        for a in self.antecedents:
            # print 'a - degree', a.fuzzy_set.name, a.input_value,
            # a.fuzzy_set.params ,a.fuzzy_set.degree(a.input_value)
            rule_degree = rule_degree * a.fuzzy_set.degree(a.input_value)
            # print 'a - rule_degree', rule_degree

        # for o in self.outputs:
        # print 'o - degree', o.fuzzy_set.name, o.input_value, o.fuzzy_set.params ,o.fuzzy_set.degree(o.input_value)
        # 	rule_degree = rule_degree * o.fuzzy_set.degree(o.input_value)
        # print 'o - rule_degree', rule_degree
        return rule_degree

    def __str__(self):
        str_degree = 'if '
        for a in self.antecedents:
            str_degree = str_degree + a.input_name + \
                '(' + str(a.input_value) + ') is ' + a.fuzzy_set.name + ' AND '

        str_degree = str_degree[:len(str_degree) - 5]
        str_degree = str_degree + ' then '
        for o in self.outputs:
            str_degree = str_degree + o.input_name + \
                '(' + str(o.input_value) + ') is ' + o.fuzzy_set.name + ' AND '

        str_degree = str_degree[:len(str_degree) - 5]
        return str_degree


class FIS(object):

    """docstring for a Fuzzy Inference System"""

    def __init__(self, name, type='mamdani', version='2.0', andMethod='min', orMethod='max', impMethod='min', aggMethod='max', defuzzMethod='centroid'):
        self.name = name
        self.type = type
        self.version = version
        self.andMethod = andMethod
        self.orMethod = orMethod
        self.impMethod = impMethod
        self.aggMethod = aggMethod
        self.defuzzMethod = defuzzMethod
        self._numInputs = 0
        self._numOutputs = 0
        self._numRules = 0
        self._inputs = []
        self._outputs = []
        self._rules = []

    def save(self):
        fis_file = open(self.name + '.fis', 'w+')
        fis_file.write('[System]\n')
        fis_file.write('Name=' + "'" + self.name + "'" + '\n')
        fis_file.write('Type=' + "'" + self.type + "'" + '\n')
        fis_file.write('Version=' + self.version + '\n')
        fis_file.write('NumInputs=' + str(self._numInputs) + '\n')
        fis_file.write('NumOutputs=' + str(self._numOutputs) + '\n')
        fis_file.write('NumRules=' + str(self._numRules) + '\n')
        fis_file.write('AndMethod=' + "'" + self.andMethod + "'" + '\n')
        fis_file.write('OrMethod=' + "'" + self.orMethod + "'" + '\n')
        fis_file.write('ImpMethod=' + "'" + self.impMethod + "'" + '\n')
        fis_file.write('AggMethod=' + "'" + self.aggMethod + "'" + '\n')
        fis_file.write('DefuzzMethod=' + "'" + self.defuzzMethod + "'" + '\n')
        fis_file.write('\n')

        for idx, _input in enumerate(self._inputs):
            input_idx = idx + 1
            fis_file.write('[Input' + str(input_idx) + ']' + '\n')
            fis_file.write('Name=' + "'" + _input['name'] + "'" + '\n')
            fis_file.write('Range=' + '[' + str(_input['range'][0]) + ' ' + str(
                _input['range'][len(_input['range']) - 1]) + ']' + '\n')
            fis_file.write('NumMFs=' + str(len(_input['mfs'])) + '\n')
            for ri, _mf in enumerate(_input['mfs']):
                mf_idx = ri + 1
                fis_file.write('MF' + str(mf_idx) + "=" + "'" + _mf.name + "'" + ':' + "'" + _mf.type + "'," +
                               '[' + str(_mf.params[0]) + ' ' + str(_mf.params[1]) + ' ' + str(_mf.params[2]) + ']' + '\n')
            fis_file.write('\n')

        for idx, _output in enumerate(self._outputs):
            output_idx = idx + 1
            fis_file.write('[Output' + str(output_idx) + ']' + '\n')
            fis_file.write('Name=' + "'" + _output['name'] + "'" + '\n')
            fis_file.write('Range=' + '[' + str(_output['range'][0]) + ' ' + str(
                _output['range'][len(_output['range']) - 1]) + ']' + '\n')
            fis_file.write('NumMFs=' + str(len(_output['mfs'])) + '\n')
            for ri, _mf in enumerate(_output['mfs']):
                mf_idx = ri + 1
                fis_file.write('MF' + str(mf_idx) + "=" + "'" + _mf.name + "'" + ':' + "'" + _mf.type + "'," +
                               '[' + str(_mf.params[0]) + ' ' + str(_mf.params[1]) + ' ' + str(_mf.params[2]) + ']' + '\n')
            fis_file.write('\n')

        fis_file.write('[Rules]\n')
        for rule in self._rules:
            rule_str = ''
            for a in rule.antecedents:
                for _input in self._inputs:
                    if a.fuzzy_set in _input['mfs']:
                        a_index = _input['mfs'].index(a.fuzzy_set) + 1
                        rule_str = rule_str + str(a_index) + ' '
            rule_str = rule_str.strip() + ',' + ' '

            for o in rule.outputs:
                for _output in self._outputs:
                    if o.fuzzy_set in _output['mfs']:
                        o_index = _output['mfs'].index(o.fuzzy_set) + 1
                        rule_str = rule_str + str(o_index) + ' '

            # this part I aint got yet
            rule_str = rule_str.strip() + ' (1) : 1'
            fis_file.write(rule_str + '\n')

        fis_file.close()

    def set_inputs(self, inputs):
        self._inputs = inputs
        self._numInputs = len(self._inputs)

    def add_input(self, input):
        """A input must be a dictionary with the following structure

        name -- string
        range -- list or numpy array
        mfs -- list of FuzzySet objects
        """

        self._inputs.append(input)
        self._numInputs = self._numInputs + 1

    def set_outputs(self, outputs):
        self._outputs = outputs
        self._numOutputs = len(self._outputs)

    def add_output(self, output):
        """A output must be a dictionary with the following structure

        name -- string
        range -- list or numpy array
        mfs -- list of FuzzySet objects
        """

        self._outputs.append(output)
        self._numOutputs = self._numOutputs + 1

    def add_rule(self, rule):
        """A rule must be a FuzzySet object"""

        self.rules.append(rule)
        self._numRules = self._numRules + 1

    def set_rules(self, rules):
        self._rules = rules
        self._numRules = len(self._rules)
