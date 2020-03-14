# Unit Testing

#### Testing for exceptions

For example if you want to split data into train and test set, usually you need to have a two dimensional data (rows by columns). Hence if you pass a one dimensional data to the function that splits the data into training and data set it should raise a ValueError. How do we test for this?

Goal: Test if the function, lets call it splitting_function() raises ValueError with one dimensional argument:
```Python
def test_value_error():
  example_argument = np.array([323, 3434, 5464, 65656 ,756, 6564, 6565])
  with pytest.raises(ValueError) as exception_info:
    splitting_function(example_argument)
  # Check if ValueError contains correct message
  assert exception_info.match("Argument data array must be two dimensional"
                              "Got 1 dimensional array instead!")
```
```Python
try:
    # Fill in with a context manager that raises Failed if no OSError is raised
    with pytest.raises(OSError):
        raise ValueError
except:
    print("pytest raised an exception because no OSError was raised in the context.")
```
```Python
with pytest.raises(ValueError) as exc_info:
    raise ValueError("Silence me!")
# Check if the raised ValueError contains the correct message
assert exc_info.match("Silence me!")
```

#### Test Driven development

In general unit tests never get written, why? Because a fast development is always prioritised and tests remains unwritten.

That is why we have test driven development so that we always try to right unit tests before development.

This way unit tests are never deprioritized
    - Have to worry about Special argument, boundary values etc.
### Organizing Unit tests
```
src/
|-- data/
|   |-- __init__.py
|   |-- preprocessing_helpers.py
|-- features
|   |-- __init__.py
|   |-- as_numpy.py
|-- models
|   |   |
```

For testing:

xfail decorator used to except some tests

skipif decorator used to skip tests if a condition is met
