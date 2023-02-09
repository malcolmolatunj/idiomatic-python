colors = ["red", "green", "blue", "yellow"]

# no need to do this
for i in range(len(colors) - 1, -1, -1):
    print(colors[i])

# or this
for color in colors[::-1]:
    print(color)

# do this instead
for color in reversed(colors):
    print(color)
