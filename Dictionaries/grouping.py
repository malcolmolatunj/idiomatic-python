colors = ["blue", "green", "red", "orange", "yellow", "purple"]

# instead of this
d = {}
for color in colors:
    key = len(color)
    if key not in d:
        d[key] = []
    d[key].append(color)

# this is better
d = {}
for color in colors:
    key = len(color)
    d.setdefault(key, []).append(color)

# this is even better
from collections import defaultdict

d = defaultdict(list)
for color in colors:
    key = len(color)
    d[key].append(color)

# if you don't need to store the results in memory, there is also this
from itertools import groupby

sorted_colors = sorted(colors, key=len)
groupby(sorted_colors, len)  # returns an iterator of key, group pairs
d = {
    k: list(g) for k, g in groupby(sorted_colors, len)
}  # returns a dictionary of key, group pairs
