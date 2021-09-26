# Week 02

Create functions in the `solutions.py` script that perform specific actions detailed below. 

Run `pytest 02/tests/test_solutions.py` to run the tests to check your solutions give the correct answers. Use the `-x` option to stop pytest after the first failure i.e. `pytest 02/tests/test_solutions.py -x` which will be useful as you are working through the problems.

If you want to run the tests for a specific problem add `::<test function name>` after the filename e.g. use `pytest 02/tests/test_solutions.py::test_add_and_subtract` to run the test for the `add_and_subtract` function.

One possible answer for each problem is given in the `02/tests/answers.py` file.

## Problems

### add and subtract

Create a function called `add_and_subtract` which takes 4 arguments and returns the sum of the first 2 minus the sum of the second 2.

### square

Create a function called `square` which takes 1 argument and returns the square of the value.

### log base 10

Create a function called `log_10` which takes 1 argument and returns the log (base 10) of the value. Import the `math` module and use `dir(math)` to see which functions are available. Run `help(<function name>)` to get help for the function or find it online.

### sum list

Create a function called `sum_list` that sums all values passed in a list.

### check string type

Create a function called `check_string_type` with 1 argument that returns a value `1` if a `string` is passed or raises a `TypeError` if a non-string type is passed.


### long strings

Create a function called `long_string` which has 1 (string) argument that returns the input if the string has at least 10 characters, if not it returns nothing i.e. `None`.


### string contrains substring

Create a function called `string_contrains_substring` which takes 2 (string) argumnets that returns `True` if the first string contains the second and returns `False` if not.

### print int string

Create a function called `print_int_string` which takes 2 arguments, an int and a str, and prints the string value int value times i.e. if 3 and "abc" are passed then "abc" should be printed 3 times.

