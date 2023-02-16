d = {"a": "blue", "b": "green", "c": "red"}

# looping over a dictionary will iterate over its keys
for k in d:
    print(k)

# you can loop over the keys explicitly
# but reserve this for when mutating the dictionary
for k in d.keys():
    if k == "a":
        del d[k]

# looping over keys and values

# instead of this
for k in d:
    print(f"{k} --> {d[k]}")

# do this
for k, v in d.items():
    print(f"{k} --> {v}")
