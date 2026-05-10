import operator
from typing import TypedDict

SaraAA = {
    "Sara": [
        {"name": "Cecilia", "age": 71},
        {"name": "Ricardo", "age": 70},
        {"name": "Magali", "age": 66}
    ],
    "Olga": [
        {"name": "Rosario", "age": 70},
        {"name": "José", "age": 68},
        {"name": "Carlos", "age": 66}
    ],
    "Alfredo": [
        {"name": "Alfredo", "age": 62},
        {"name": "Álvaro", "age": 61},
        {"name": "Alexandra", "age": 57},
        {"name": "Adriana", "age": 50}
    ]
}


def get_grandchildren_sorted(d: dict[str, list[dict[str, str | int]]]) -> list[str]:
    """Get all grandchildren from a dictionary of families, sorted by age: eldest first."""

    grandchildren = [child for family in d.values() for child in family]
    return [child['name'] for child in
            sorted(grandchildren,
                   key=operator.itemgetter('age'),
                   reverse=True)]


# Claude: One thing worth noting on your type hint — dict[str, str | int] is technically
# correct but slightly loose, since "age" is always int and "name" is always str.
# Python doesn't give you a way to express that constraint in a plain dict hint. If you wanted
# to be precise, that's exactly what TypedDict is for.
# That makes the signature self-documenting and gives type checkers like mypy or PyCharm's
# inspector real information to work with. It's the idiomatic solution when a dict has a
# fixed, known schema — which yours does.

class Grandchild(TypedDict):
    name: str
    age: int


def get_grandchildren_sorted_c(d: dict[str, list[Grandchild]]) -> list[str]:
    """Get all grandchildren from a dictionary of families, sorted by age: eldest first."""

    grandchildren = [child for family in d.values() for child in family]
    return [child['name'] for child in
            sorted(grandchildren,
                   key=operator.itemgetter('age'),
                   reverse=True)]


def sorted_grandchildren(d):
    grandchildren = [one_grandchild
                     for one_grandchild_list in d.values()
                     for one_grandchild in one_grandchild_list]

    return [one_grandchild['name']
            for one_grandchild in sorted(grandchildren,
                                         key=operator.itemgetter('age'))]


print(get_grandchildren_sorted(SaraAA))
print(get_grandchildren_sorted_c(SaraAA))
print(sorted_grandchildren(SaraAA))
