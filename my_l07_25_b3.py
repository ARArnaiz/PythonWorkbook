from collections.abc import Iterable


def any_join(iterable: Iterable, sep: str = ' ') -> str:
    """Join elements of an iterable into a string with an optional separator."""
    return sep.join(str(item) for item in iterable)


print(any_join([1, 2, 3]))
print(any_join('abc', sep='**'))


def anyjoin(seq, glue=' '):
    return glue.join([str(one_item)
                      for one_item in seq])


print(anyjoin([1, 2, 3]))
print(anyjoin('abc', glue='**'))
