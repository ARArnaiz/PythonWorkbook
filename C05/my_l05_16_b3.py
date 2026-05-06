from typing import Callable
d = {'a': 1, 'b': 2, 'c': 4, 'd': 4, 'x': 1, 'y': 2, 'z': 4}


def funqui(k, v) -> bool:
    return k.isalpha() and v % 2 == 0


def dx_partition(d: dict, f: object) -> tuple[dict, dict]:
    """dx_partition calls f(k, v) twice per item — once for the true dict,
    once for the false dict. partition_dict calls it once and branches. """
    d1 = {k: v for k, v in d.items() if f(k, v)}
    d2 = {k: v for k, v in d.items() if not f(k, v)}
    return d1, d2


print(dx_partition(d, funqui))


def partition_dict(d, f):
    """Lerner's"""
    output_true = {}
    output_false = {}

    for key, value in d.items():
        if f(key, value):
            output_true[key] = value
        else:
            output_false[key] = value

    return output_true, output_false


print(partition_dict(d, funqui))

def partition_dx(d: dict, f: Callable[[str, int], bool]) -> tuple[dict, dict]:
    """Claude: The (d_true if f(k, v) else d_false)[k] = v line selects
     which dict to write into based on the predicate — one call to f,
     one assignment, no if/else block needed."""
    d_true, d_false = {}, {}
    for k, v in d.items():
        (d_true if f(k, v) else d_false)[k] = v
    return d_true, d_false

print(partition_dx(d, funqui))