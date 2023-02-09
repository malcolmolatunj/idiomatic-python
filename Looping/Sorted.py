colors = ["red", "green", "blue", "yellow"]

# loops over the colors in alphabetical order
for color in sorted(colors):
    print(color)

# loops over the colors in reverse-alphabetical order
for color in sorted(colors, reverse=True):
    print(color)

# to alphabetical sorting is default sorting behavior for
# strings, but we can provide a custom sorting function
# the code below loops over the colors in increasing order
# of their length
for color in sorted(colors, key=len):
    print(color)

# loops over the colors in decreasing order
# of their length
for color in sorted(colors, key=len, reverse=True):
    print(color)
