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
