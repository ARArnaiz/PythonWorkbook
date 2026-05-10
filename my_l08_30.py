
def flatten(lst: list[list]) -> list:
    """Flattens a list of lists into a single list."""
    return [ item for sublist in lst for item in sublist ]

print(flatten([[1,2], [3,4]]))

def flatten_l(mylist):
    return [one_element
            for one_sublist in mylist
             for one_element in one_sublist]

print(flatten_l([[1,2], [3,4]]))

