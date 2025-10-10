"""
Data Casting
"""

# Number conversions
int("25")        # str to int
float("3.14")    # str to float
str(100)         # int to str
bool(0)          # int to bool → False
bool(1)          # int to bool → True

# String conversions
int("42")        # str to int (only if numeric)
float("2.5")     # str to float
bool("hello")    # str to bool → True
list("abc")      # str to list → ['a', 'b', 'c']

# Boolean conversions
int(True)        # → 1
float(False)     # → 0.0
str(True)        # → "True"

# List conversions
tuple([1, 2])    # list to tuple
set([1, 2, 2])   # list to set → {1, 2}
bool([])         # → False (empty list)

# Dictionary conversions
list({"a": 1})   # dict to list of keys → ['a']
str({"a": 1})    # dict to string → "{'a': 1}"
bool({})         # → False (empty dict)
