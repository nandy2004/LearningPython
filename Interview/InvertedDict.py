def invert_dict(d):
    inverted = {}
    for key in d:
        value = d[key]
        inverted[value] = key
    return inverted

# Example
data = {'a': 1, 'b': 2, 'c': 3}
print(invert_dict(data))
