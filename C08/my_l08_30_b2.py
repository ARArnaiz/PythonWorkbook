import itertools

SaraAA = {
    "Sara": ["Cecilia", "Ricardo", "Magali"],
    "Olga": ["Rosario", "José", "Carlos"],
    "Alfredo": ["Alfredo", "Álvaro", "Alexandra", "Adriana"]
}

def get_grandchildren(d: dict[str, list[str]]) -> list[str]:
    """Get all grandchildren from a dictionary of families."""
    return [name for names in d.values() for name in names]

def grandchildren_names(d):
    return [one_grandchild
            for grandchild_list in d.values()
            for one_grandchild in grandchild_list]

print(get_grandchildren(SaraAA))
print(grandchildren_names(SaraAA))

# Claude
# One small upgrade worth knowing — if you don('t need a list and just want to iterate
# over the result, itertools.chain.from_iterable(d.values()) is the idiomatic "flatten
# an iterable of iterables" tool. But for returning a list, the comprehension is perfect
# and more readable than list(chain.from_iterable(...)).)))

print(list(itertools.chain.from_iterable(SaraAA.values())))