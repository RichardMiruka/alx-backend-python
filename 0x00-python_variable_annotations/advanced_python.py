# Python is a dynamically-typed language.
# That means that variable types are dynamically set at run-time, upon assignment of a value to a variable.

# For example, in 
def fn(a, b):
    return a + b

# the function fn can take any two arguments, as long as they can be added together.
# The '+' operator will automatically convert them into integers, floats, or strings, as needed.
# print(fn("Hello", "World"))  # "HelloWorld"

# This is a powerful feature, but it can also lead to bugs if you're not careful.
# For example, the following code will raise an exception:
try:
    print(1 + "Hello")
except Exception as e:
    print(e)

# In this case, Python tries to add an integer to a string, which is not allowed.
# If you're not careful, this can lead to bugs that are hard to find.

# To avoid these kinds of errors, you can use type hints.
# Type hints are a way of indicating what kind of value a variable should hold.
# They don't affect the behavior of the code, but they can help catch bugs early on.

def fn_with_hints(a: int, b: int) -> int:
    return a + b

print(fn_with_hints(1, 2))  # 3

# print(fn_with_hints("Hello", "World"))  # This will raise a TypeError

# So with type hints, the above code will raise a TypeError at runtime, instead of silently producing the wrong result.

# Type hints are not enforced by Python, but they can be checked using a tool called mypy.
# Type hints are also used by many IDEs to provide better code completion and error checking.

# There are other built-in types, such as float, str, bool, and list, as well as more complex types like Tuple, Dict, and Set.
# You can also define your own types using the typing module.
from typing import List, Tuple, Dict, Set

# A list of integers
int_list = List[int]

# A tuple of three strings
str_tuple = Tuple[str, str, str]

# A dictionary with strings as keys and integers as values
str_dict = Dict[str, int]

# A set of unique strings
unique_strings = Set[str]
