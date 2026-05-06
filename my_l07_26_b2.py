from typing import Callable, Iterable

from es_syllabifier import es_syllabify


def apply_to_each(f: Callable, seq: Iterable) -> list:
    return [f(item) for item in seq]


print(apply_to_each(es_syllabify, ['hola', 'mundo', 'cruel']))
