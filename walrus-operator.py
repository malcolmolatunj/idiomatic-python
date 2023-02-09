f = open("file.txt")

# Instead of this
blocks = []
while True:
    block = f.read(32)
    if block == "":
        break
    blocks.append(block)

# or this
from functools import partial

block = []
for block in iter(partial(f.read, 32), ""):
    blocks.append(block)

# in Python 3.8+ we can use an assignment expression
block = []
while (block := f.read(32)) != "":
    blocks.append(block)
