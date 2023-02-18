colors = ["blue", "green", "red", "orange", "yellow", "purple"]

# try to avoid modifying the left side of a list
del colors[0]
colors.pop(0)
colors.insert(0, "grey")

# if you're mostly updating the left side of your list
# consider sorting the list in reverse order to update it from the right instead
# if you're updating the list from both ends, consider using a deque instead

from collections import deque

colors = deque(["blue", "green", "red", "orange", "yellow", "purple"])
# now we can efficiently update both ends
del colors[0]
colors.popleft()
colors.appendleft("grey")
