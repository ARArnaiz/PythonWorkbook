from typing import Callable

# This is done with: dict(zip(lst, map(func, lst)))

def char_types_c2(s: str) -> dict[str, int]:
    methods = ["isdigit", "isalpha", "isspace"]
    return {m: sum(getattr(c, m)() for c in s) for m in methods}

def dict_construction(lst: list, func: Callable) -> dict:
    return { x: func(x) for x in lst }

print(dict_construction(["Hello, world!","123 456", "   "], char_types_c2))

def apply_to_each(items: list, func: Callable) -> dict:
    """Claude: Map each item to func(item). Equivalent to {x: func(x) for x in items}."""
    return {x: func(x) for x in items}

print(apply_to_each(["Hello, world!","123 456", "   "], char_types_c2))

def fromkeys_func(s, func):
    output = {}

    for one_item in s:
        output[one_item] = func(one_item)

    return output


print(fromkeys_func(["Hello, world!","123 456", "   "], char_types_c2))