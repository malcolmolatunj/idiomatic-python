colors = ["red", "green", "blue", "yellow"]

# instead of this
for i in range(len(colors)):
    print(i, "-->", colors[i])

# do this
for i, color in enumerate(colors):
    print(i, "-->", color)

# Python 3.6+
for i, color in enumerate(colors):
    print(f"{i} --> {color}")
