# hyparam

Container for hyper parameter tuning in machine learning.

# Example

## Load programmatically

You can add parameters to the parameter search space by using the following methods.

```python
hp = HyperParameters()
hp.add_linspace("learning_rate", 0.1, 0.3, 3)
hp.add_switch("use_test_dataset")
hp.add_range("epochs", 10, 30, 10)
hp.add_list("myvar", [1.0, 12.0, 8.0])
```

## Load from file

You can instead specify a parameter space in a YAML configuration file.

```yaml
learning_rate:
  type: linspace
  setup:
    lower: 0.1
    upper: 0.3
    num: 3

use_test_dataset:
  type: switch

epochs:
  type: range
  setup:
    start: 10
    stop: 30
    step: 10

myvar:
  type: list
  setup:
    values: [1.0, 12.0, 8.0]
```

This is loaded into Python as follows.

```python
hp = HyperParameters.from_file(file_name)
```

## Iterating over the parameter space

In both the above examples, you can iterate over the parameter space using the `choices` method.
See the examples in the [example](example/) directory.
You should expect the following output when you run these.

```
choice(learning_rate=0.1, use_test_dataset=True, epochs=10, myvar=1.0)
choice(learning_rate=0.1, use_test_dataset=True, epochs=10, myvar=12.0)
choice(learning_rate=0.1, use_test_dataset=True, epochs=10, myvar=8.0)
choice(learning_rate=0.1, use_test_dataset=True, epochs=20, myvar=1.0)
choice(learning_rate=0.1, use_test_dataset=True, epochs=20, myvar=12.0)
choice(learning_rate=0.1, use_test_dataset=True, epochs=20, myvar=8.0)
choice(learning_rate=0.1, use_test_dataset=False, epochs=10, myvar=1.0)
choice(learning_rate=0.1, use_test_dataset=False, epochs=10, myvar=12.0)
choice(learning_rate=0.1, use_test_dataset=False, epochs=10, myvar=8.0)
choice(learning_rate=0.1, use_test_dataset=False, epochs=20, myvar=1.0)
choice(learning_rate=0.1, use_test_dataset=False, epochs=20, myvar=12.0)
choice(learning_rate=0.1, use_test_dataset=False, epochs=20, myvar=8.0)
choice(learning_rate=0.2, use_test_dataset=True, epochs=10, myvar=1.0)
choice(learning_rate=0.2, use_test_dataset=True, epochs=10, myvar=12.0)
choice(learning_rate=0.2, use_test_dataset=True, epochs=10, myvar=8.0)
choice(learning_rate=0.2, use_test_dataset=True, epochs=20, myvar=1.0)
choice(learning_rate=0.2, use_test_dataset=True, epochs=20, myvar=12.0)
choice(learning_rate=0.2, use_test_dataset=True, epochs=20, myvar=8.0)
choice(learning_rate=0.2, use_test_dataset=False, epochs=10, myvar=1.0)
choice(learning_rate=0.2, use_test_dataset=False, epochs=10, myvar=12.0)
choice(learning_rate=0.2, use_test_dataset=False, epochs=10, myvar=8.0)
choice(learning_rate=0.2, use_test_dataset=False, epochs=20, myvar=1.0)
choice(learning_rate=0.2, use_test_dataset=False, epochs=20, myvar=12.0)
choice(learning_rate=0.2, use_test_dataset=False, epochs=20, myvar=8.0)
choice(learning_rate=0.3, use_test_dataset=True, epochs=10, myvar=1.0)
choice(learning_rate=0.3, use_test_dataset=True, epochs=10, myvar=12.0)
choice(learning_rate=0.3, use_test_dataset=True, epochs=10, myvar=8.0)
choice(learning_rate=0.3, use_test_dataset=True, epochs=20, myvar=1.0)
choice(learning_rate=0.3, use_test_dataset=True, epochs=20, myvar=12.0)
choice(learning_rate=0.3, use_test_dataset=True, epochs=20, myvar=8.0)
choice(learning_rate=0.3, use_test_dataset=False, epochs=10, myvar=1.0)
choice(learning_rate=0.3, use_test_dataset=False, epochs=10, myvar=12.0)
choice(learning_rate=0.3, use_test_dataset=False, epochs=10, myvar=8.0)
choice(learning_rate=0.3, use_test_dataset=False, epochs=20, myvar=1.0)
choice(learning_rate=0.3, use_test_dataset=False, epochs=20, myvar=12.0)
choice(learning_rate=0.3, use_test_dataset=False, epochs=20, myvar=8.0)
```

# Install

## From source

In a new terminal:
1. Clone repository:
   - (ssh) `$ git clone git@github.com:cmower/hyparam.git`, or
   - (https) `$ git clone https://github.com/cmower/hyparam.git`
2. Change directory: `$ cd hyparam`
3. Ensure `pip` is up-to-date: `$ python -m pip install --upgrade pip`
3. Install: `$ pip install .`
