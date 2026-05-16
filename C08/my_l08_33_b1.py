import hashlib

sample_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
def hash_element(elem: str) -> str:
    return hashlib.md5(str(elem).encode()).hexdigest()

def excluded(k: str, v: str) -> bool:
    return k not in v


def transform_values_filter(a_dict: dict, f1: Callable, f2)-> dict:
    return { key: f1(value) for key, value in a_dict.items() if f2(key, f1(value)) }

# {'a': 'c4ca4238a0b923820dcc509a6f75849b', 'b': 'c81e728d9d4c2f636f067f89cc14862c', 'c': 'eccbc87e4b5ce2fe28308fd9f2a7baf3', 'd': 'a87ff679a2f3e71d9181a67b7542122c'}
print(transform_values_filter(sample_dict, hash_element, excluded))

def transform_values2(func1, func2, a_dict):
    return {key: func(value)
            for key, value in a_dict.items()
            if func2(key, value)}