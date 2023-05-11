import re
import numpy as np
from itertools import product
from collections import namedtuple, OrderedDict


class HyperParameters:
    def __init__(self):
        self.data = OrderedDict()

    def _ensure_name(self, name):
        assert name not in self.data, f"'{name}' is not a unique name"
        return re.sub(r"\W+", "_", name)

    def add_switch(self, name):
        name = self._ensure_name(name)
        self.data[name] = [True, False]

    def add_range(self, name, start, stop, step):
        name = self._ensure_name(name)
        self.data[name] = list(range(start, stop, step))

    def add_linspace(self, name, lower, upper, num):
        name = self._ensure_name(name)
        self.data[name] = np.linspace(lower, upper, num=num, dtype=float).tolist()

    def add_list(self, name, values=[]):
        name = self._ensure_name(name)
        assert len(values) > 0, "values list must not be empty"
        self.data[name] = values

    def choices(self):
        choice_tuple = namedtuple("choice", self.data.keys())
        for choice_data in product(*self.data.values()):
            yield choice_tuple(*choice_data)
