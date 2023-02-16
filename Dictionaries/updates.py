dict1 = {"a": 1}
dict2 = {"b": 2}
dict3 = {"b": 3}

# don't do this
d = dict1.copy()
d.update(dict2)
d.update(dict3)

# do this instead
# ChainMap is NOT a dictionary, but support dict methods
from collections import ChainMap

d = ChainMap(dict3, dict2, dict1)

# in Python 3.9+ you can use the following syntax
# though it's advisable to restrict this to shorter scripts
d = dict1 | dict2 | dict3
