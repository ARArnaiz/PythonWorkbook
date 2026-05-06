def dictdiff(dict1: dict, dict2: dict) -> dict:
    diffs = {}
    for key, value in dict1.items():
        if key in dict2 and dict1[key] != dict2[key]:
                diffs[key] = [dict1[key], dict2[key]]
        elif key not in dict2:
            diffs[key] = [dict1[key], None]
    for key, value in dict2.items():
        if key not in dict1:
            diffs[key] = [None, dict2[key]]

    return diffs

def dictdiffl(first, second):
    """Accepts two dicts as arguments.
Returns a dict describing the differences between the two arguments.
Each key-value pair in the returned dict represents a difference. Each
difference consists of a key and a two-element list, indicating the
values from the two input dicts.  If a key exists in one dict but not
another, then the corresponding value will be None.
"""
    output = {}
    all_keys = first.keys() | second.keys()

    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key), second.get(key)]
    return output

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
d5 = {'a':1, 'b':2, 'd':4}
d6 = {'x':1, 'y':2, 'z':4}

print(dictdiff(d1, d1))
assert dictdiff(d1, d1) == {}
print(dictdiff(d1, d2))
assert dictdiff(d1, d2) == {'c': [3, 4]}
print(dictdiff(d3, d4))
assert dictdiff(d3, d4) == {'c': [None, 4], 'd': [3, None]}
print(dictdiff(d1, d5))
assert dictdiff(d1, d5) == {'c': [3, None], 'd': [None, 4]}
print(dictdiff(d1, d6))
assert dictdiff(d1, d6) == {'a': [1, None], 'b': [2, None], 'c': [3, None], 'x': [None, 1], 'y': [None, 2], 'z': [None, 4]}
print(dictdiffl(d1, d1))
assert dictdiffl(d1, d1) == {}
print(dictdiffl(d1, d2))
assert dictdiffl(d1, d2) == {'c': [3, 4]}
print(dictdiffl(d3, d4))
assert dictdiffl(d3, d4) == {'c': [None, 4], 'd': [3, None]}
print(dictdiffl(d1, d5))
assert dictdiffl(d1, d5) == {'c': [3, None], 'd': [None, 4]}
print(dictdiffl(d1, d6))
assert dictdiffl(d1, d6) == {'a': [1, None], 'b': [2, None], 'c': [3, None], 'x': [None, 1], 'y': [None, 2], 'z': [None, 4]}