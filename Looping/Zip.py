names = ["raymond", "rachel", "matthew"]
colors = ["red", "green", "blue", "yellow"]

# instead of this
n = min(len(names), len(colors))
for i in range(n):
    print(names[i], "-->", colors[i])

# do this
for name, color in zip(names, colors):
    print(name, "-->", color)

# Python 3.6+
for name, color in zip(names, colors):
    print(f"{name} --> {color}")
