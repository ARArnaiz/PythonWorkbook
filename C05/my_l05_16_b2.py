
def make_dx_from_tokens(*args) -> dict:
    d = {}
    if len(args) % 2:
        raise ValueError('Need an even number of args')
    for i, arg in enumerate(args):
        if i % 2 == 0:
         d[arg] = args[i + 1]
    return d

print(make_dx_from_tokens("a", 1, "b", 2, "c", 3, "d", 4))

def dict_from_list(*args):
    """Lerner's"""
    if len(args) % 2:
        raise ValueError('Need an even number of args')

    output = {}

    while args:
        output[args[0]] = args[1]
        args = args[2:]

    return output

print(dict_from_list("a", 1, "b", 2, "c", 3, "d", 4))

def dict_from_pairs(*args) -> dict:
    """Claude: cleanest — zip of slices"""
    if len(args) % 2:
        raise ValueError('Need an even number of args')
    return dict(zip(args[::2], args[1::2]))

print(dict_from_pairs("a", 1, "b", 2, "c", 3, "d", 4))