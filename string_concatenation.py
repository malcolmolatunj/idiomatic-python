colors = ["red", "green", "purple", "blue", "yellow"]

# instead of this
s = colors[0]
for color in colors[1:]:
    s += f", {color}"
print(s)

# or this
s = ""
for color in colors:
    s += f"{color}, "
s = s[:-2]
print(s)

# do this
s = ", ".join(colors)
print(s)
