colors = ["red", "green", "purple", "blue", "yellow"]

# instead of this
s = colors[0]
for color in colors[1:]:
    s += f", {color}"  # `s += ', ' + color` in Python 3.5 or lower
print(s)

# or this
s = ""
for color in colors:
    s += f"{color}, "  # `s += color + ', '` in Python 3.5 or lower
s = s[:-2]
print(s)

# do this
s = ", ".join(colors)
print(s)
