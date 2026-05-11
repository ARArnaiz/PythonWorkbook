d = {'a':1, 'b':2, 'c':3}

def flip_dict(d: dict) -> dict:
    return {v: k for k, v in d.items()}

print(flip_dict(d))

def flipped_dict(a_dict):
    return {value: key
            for key, value in a_dict.items()}

print(flipped_dict({'a':1, 'b':2, 'c':3}))
