# context managers factor out administrative logic in try-finally blocks

# so, instead of this
f = open("data.txt")
try:
    data = f.read()
finally:
    f.close()

# do this
with open("data.txt") as f:
    data = f.read()

# instead of this
import asyncio


async def critical_work_with_locks():
    lock = asyncio.Lock()
    await lock.acquire()
    try:
        print("Critical section 1")
        print("Critical section 2")
    finally:
        lock.release()


# do this
async def critical_work_with_locks():
    lock = asyncio.Lock()
    async with lock:
        print("Critical section 1")
        print("Critical section 2")


# instead of this
import os

try:
    os.remove("somefile.tmp")
except FileNotFoundError:
    pass

# do this
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove("somefile.tmp")

# instead of this
import sys

with open("help.txt", "w") as f:
    oldstdout = sys.stdout
    sys.stdout = f
    try:
        help(pow)
    finally:
        sys.stdout = oldstdout

# do this
from contextlib import redirect_stdout

with open("help.txt", "w") as f:
    with redirect_stdout(f):
        help(pow)

# if a context manager does not exist for your use-case, you can create one
# be sure to check the Python documentation to see if a context manager exists for your use-case
from contextlib import contextmanager


@contextmanager
def print_blue():
    print("\033[34m")
    yield
    print("\033[39m")


with print_blue():
    print("all this text will be blue")
print("and this text will return to the normal font color")
