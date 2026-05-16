from typing import Callable
import hashlib

sample_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
def hash_element(elem: str) -> str:
    return hashlib.md5(str(elem).encode()).hexdigest()

def transform_values(a_dict: dict, f: Callable)-> dict:
    return { key: f(value) for key, value in a_dict.items() }

print(transform_values(sample_dict, hash_element))

def transform_values(func, a_dict):
    return {key: func(value)
             for key, value in a_dict.items()}

d = {'a':1, 'b':2, 'c':3}
print(transform_values(lambda x: x*x, d))