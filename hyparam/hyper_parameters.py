import re
import yaml
import numpy as np
from itertools import product
from collections import namedtuple, OrderedDict


class HyperParameters:
    def __init__(self):
        self.data = OrderedDict()

    @staticmethod
    def from_file(file_name):
        # Load configuration from file
        with open(file_name, "r") as f:
            config = yaml.load(f, Loader=yaml.FullLoader)

        # Setup parameter space
        hp = HyperParameters()
        for name, spec in config.items():
            param_type = spec["type"]

            if param_type == "switch":
                hp.add_switch(name)
            elif param_type == "range":
                setup = spec["setup"]
                hp.add_range(name, setup["start"], setup["stop"], setup["step"])
            elif param_type == "linspace":
                setup = spec["setup"]
                hp.add_linspace(name, setup["lower"], setup["upper"], setup["num"])
            elif param_type == "list":
                setup = spec["setup"]
                hp.add_list(name, setup["values"])

        return hp

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
