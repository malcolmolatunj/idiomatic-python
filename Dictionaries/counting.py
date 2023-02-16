colors = ["red", "green", "red", "blue", "green", "red"]

# instead of this
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1

# this is better
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1

# this is even better
from collections import defaultdict

d = defaultdict(int)
for color in colors:
    d[color] += 1

# though Counter is clearest
# although a Counter is NOT a dictionary, it is a subclass that specializes in counting
from collections import Counter

d = Counter(colors)
