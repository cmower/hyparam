import re
from itertools import product
from collections import namedtuple, OrderedDict

# PyYAML: https://pyyaml.org/
import yaml

# NumPy: https://numpy.org/
import numpy as np


class HyperParameters:
    def __init__(self):
        self.data = OrderedDict()

    @staticmethod
    def from_file(file_name):
        """Load parameter space from file.

        hp = HyperParameters.from_file(file_name)

        Parameters
        ----------

        file_name (str)
          YAML file containing parameter space specification.

        Returns
        -------

        hp (HyperParameters)
          Container defining the parameter space.

        """
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
        """Add switch parameter: True/False.

        hp = HyperParameters()
        hp.add_switch(name)

        Parameters
        ----------

        name (str)
          Name of the parameter.

        """
        name = self._ensure_name(name)
        self.data[name] = [True, False]

    def add_range(self, name, start, stop, step):
        """Add range parameter.

        hp = HyperParameters()
        hp.add_range(name, start, stop, step)

        Parameters
        ----------

        name (str)
          Name of the parameter.

        start (int)
          Start of integer sequence.

        stop (int)
          End of integer sequence.

        step (int)
          The integer sequence from start (inclusive) to stop
          (exclusive) by step.

        """
        name = self._ensure_name(name)
        self.data[name] = list(range(start, stop, step))

    def add_linspace(self, name, lower, upper, num):
        """Add linspace parameter.

        hp = HyperParameters()
        hp.add_linspace(name, lower, upper, num)

        Parameters
        ----------

        name (str)
          Name of the parameter.

        lower (float)
          The starting value of the sequence.

        upper (float)
          The end value of the sequence.

        num (int)
          Number of samples to generate. Must be non-negative.

        """
        name = self._ensure_name(name)
        self.data[name] = np.linspace(lower, upper, num=num, dtype=float).tolist()

    def add_list(self, name, values):
        """Add list parameter.

        hp = HyperParameters()
        hp.add_list(name, values)

        Parameters
        ----------

        name (str)
          Name of the parameter.

        values (list)
          List of values.

        """
        name = self._ensure_name(name)
        assert len(values) > 0, "values list must not be empty"
        self.data[name] = values

    def choices(self):
        """Iterate over parameter space.

        hp = HyperParameters()
        choices = hp.choices()

        Returns
        -------

        choices (generator)
           Generator that iterates over parameter space.

        """
        choice_tuple = namedtuple("choice", self.data.keys())
        for choice_data in product(*self.data.values()):
            yield choice_tuple(*choice_data)
