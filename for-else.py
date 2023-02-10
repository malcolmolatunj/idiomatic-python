# instead of this
def find(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
    if not found:
        return -1
    return i


# there is an alternative
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:  # no break
        return -1
    return i


# though perhaps more readable still
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            return i
    return -1


# note that if `seq` is a string, str.find() should be used

"""
similarly try to refactor your code to avoid this for-else
pattern, often by extracting branching logic or shifting
where a return happens.
"""

import time


# For example, instead of this
def process_for_5_seconds():
    start = time.perf_counter()
    target_time = start + 5

    while (now := time.perf_counter()) < target_time:
        print(f"keep working, it's only been {now - start:.2f}s")
        if random_error():
            break
        time.sleep(0.5)
    else:  # no break
        print("done!")
        return
    print("handling error...")


# you can define another function to return early
# which can make the logic clearer
def process_for_5_seconds():
    start = time.perf_counter()
    target_time = start + 5

    if processed_for_period(start, target_time):
        print("done!")
        return


def processed_for_period(start_time, target_time):
    while (now := time.perf_counter()) < target_time:
        print(f"keep working, it's only been {now - start_time:.2f}s")
        if random_error():
            print("handling error...")
            return False
        time.sleep(0.5)
    return True
