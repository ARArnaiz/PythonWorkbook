d1 = {"name": "John"}
d2 = {"name": "Mary"}
d3 = {"name": "Peter"}
d4 = {"name": "Rose"}
d5 = {"name": "Paul"}
d6 = { "name": "Mary"}
d7 = { "name" : "John"}
d8 = { "name": "Mary"}
d9 = { "name": " Rosalía"}
d10 = {"name": "Natalia"}

dlist = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]

def dict_list_to_tuple_list(lst: list[dict]) -> list[tuple]:
    """Convert a list of dictionaries to a list of tuples."""
    return [ d_tuple for d in lst for d_tuple in d.items()]
print(dict_list_to_tuple_list(dlist))

def dicts_to_tuples(list_of_dicts):
    return [one_tuple
            for one_dict in list_of_dicts
            for one_tuple in one_dict.items()]

print(dicts_to_tuples(dlist))