import os
import re

version = os.environ['version']
develop, production = version == 'dev', version == 'prod'


class AnalysisData:
    def __init__(self, data:object=None):
        """ :param data: results of the anylysis """
        self._data = data

    @property
    def data(self) -> object:
        return self._data


class Analysis:
    def __init__(self, local_object: object=None):
        """ :param local_object: object being analyzed """
        self._object = local_object
        self._data = AnalysisData()

    @property
    def object(self) -> object:
        return self._object

    @property
    def data(self) -> AnalysisData:
        if self._data is not None:
            return self._data
        else:
            raise ValueError('Analysis._data is empty because no analysis was done so far.')


class Analyzer:
    def __init__(self):
        self._analysis = Analysis()
        self._analysis_data = AnalysisData()

    def analyze(self, local_object: object=None) -> None:
        self._analysis = Analysis(local_object)
        self._analysis_data = self._analysis.data

    @property
    def analysis(self) -> Analysis:
        return self._analysis

    @property
    def analysis_data(self) -> AnalysisData:
        return self._analysis_data


class ErrorAnalysisData(AnalysisData):
    def __init__(self, error_data: object=None):
        AnalysisData.__init__(self)
        self._data = error_data


class ErrorAnalysis(Analysis):
    def __init__(self, local_object: object=None):
        Analysis.__init__(self, local_object=local_object)
        self._data = ErrorAnalysisData()

    @property
    def data(self) -> ErrorAnalysisData:
        if self._data is not None:
            return self._data
        else:
            # TODO: perform analysis
            raise ValueError('ErrorAnalysis._data is empty because no analysis was done so far.')


class ErrorAnalyzer(Analyzer):
    def __init__(self):
        Analyzer.__init__(self)
        self._analysis = ErrorAnalysis()
        self._analysis_data = ErrorAnalysisData()

    def analyze(self, local_object: object=None) -> None:
        self._analysis = ErrorAnalysis(local_object)
        self._analysis_data = self._analysis.data

    @property
    def analysis(self) -> ErrorAnalysis:
        return self._analysis

    @property
    def analysis_data(self) -> ErrorAnalysisData:
        return self._analysis_data


def absolute_error(s: str='') -> str:
    if set(s) & {'[', ']', '{', '}', '^', '&', '|', '\\'}:
        raise ValueError('Incorrect expression: not supported symbols.')

    s = ''.join(s.split())

    depth = [0 for _ in s]
    for i, c in enumerate(s):
        if c == '(':
            depth[i] = depth[i - 1] + 1 if i > 0 else 1
        elif c == ')':
            depth[i] = depth[i - 1] - 1
        else:
            depth[i] = depth[i - 1] if i > 0 else 0
    if depth[-1] != 0 or any(map(lambda di: di < 0, depth)):
        raise ValueError('Incorrect expression: parenthesises do not math.')

    # remove enclosing parenthesises
    while s[0] == '(' and s[-1] == ')' and all(map(lambda di: di > 0, depth[1:-1])):
        s = s[1:-1]

    depth = [0 for _ in s]
    for i, c in enumerate(s):
        if c == '(':
            depth[i] = depth[i - 1] + 1 if i > 0 else 1
        elif c == ')':
            depth[i] = depth[i - 1] - 1
        else:
            depth[i] = depth[i - 1] if i > 0 else 0

    sequence = list(filter(lambda _: depth[_] == 0 and s[_] in {'+', '-'}, range(len(s))))

    if sequence:
        pos = min(sequence)
        s_left, s_right = s[:pos], s[pos+1:]
        ae_left, ae_right = absolute_error(s_left), absolute_error(s_right)
        if ae_left and ae_right:
            return f'{ae_left} + {ae_right}'
        elif ae_left and not ae_right:
            return ae_left
        elif not ae_left and ae_right:
            return ae_right
        else:  # if not ae_left and not ae_right:
            return ''

    sequence = list(filter(lambda _: depth[_] == 0 and s[_] in {'*', '/'}, range(len(s))))

    if sequence:
        pos = min(sequence)
        op = s[pos]
        s_left, s_right = s[:pos], s[pos+1:]

        if not s_left or not s_right:
            raise ValueError('Incorrect expression: * and / should have two operands.')

        ae_left, ae_right = absolute_error(s_left), absolute_error(s_right)
        if op == '*':
            if ae_left and ae_right:
                return f'({s_left}) * ({ae_right}) + ({s_right}) * ({ae_left})'
            elif ae_left and not ae_right:
                return f'({s_right}) * ({ae_left})'
            elif not ae_left and ae_right:
                return f'({s_left}) * ({ae_right})'
            else:  # if not ae_left and not ae_right:
                return ''
        if op == '/':

            if ae_left and ae_right:
                return f'(({s_left}) * ({ae_right}) + ({s_right}) * ({ae_left})) / ({s_right})^2'
            elif ae_left and not ae_right:
                return f'(({s_right}) * ({ae_left})) / ({s_right})^2'
            elif not ae_left and ae_right:
                return f'(({s_left}) * ({ae_right})) / ({s_right})^2'
            else:  # if not ae_left and not ae_right:
                return ''

    try:
        float(s)
        return ''
    except ValueError:
        return f'Δ{s}'


def absolute_error_answer_wrapper(s: str='') -> str:
    s = absolute_error(s)
    s = re.sub(r'\(\([^\(\)]*\)\)', lambda x: x.group(0)[1:-1], s)
    return s.replace(' + ', '+').replace('+', ' + ')\
            .replace(' - ', '-').replace('-', ' - ')\
            .replace(' * ', '*').replace('*', ' * ')\
            .replace(' / ', '/').replace('/', ' / ')
