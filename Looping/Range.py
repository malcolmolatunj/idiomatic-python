for i in range(6):
    print(i**2)

"""
The code above would replace this similar construct
in other languages:

for (var i=0; i<6; i++) {
    print(i**2)
}

However, when iterating over a collection
Python's `for` loop acts more like a `foreach`
so there is no need to keep track of the index
"""
colors = ["red", "green", "blue", "yellow"]

# instead of this
for i in range(len(colors)):
    print(colors[i])

# do this
for color in colors:
    print(color)
