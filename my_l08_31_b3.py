from collections import Counter

d1 = {"name": "John", "hobbies": ["swimming", "reading"]}
d2 = {"name": "Mary", "hobbies": ["reading", "singing"]}
d3 = {"name": "Peter", "hobbies": ["eating", "dancing", "coding"]}
d4 = {"name": "Rose", "hobbies": ["singing", "coding"]}
d5 = {"name": "Paul", "hobbies": ["dancing", "coding", "swimming"]}
d6 = {"name": "Mary", "hobbies": ["swimming", "hiking", "coding", "singing"]}
d7 = {"name": "John", "hobbies": ["reading", "cooking", "baking"]}
d8 = {"name": "Mary", "hobbies": ["reading", "skiing"]}
d9 = {"name": " Rosalía", "hobbies": ["singing"]}
d10 = {"name": "Natalia", "hobbies": ["reading", "stamp collecting"]}

dlist = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]


def most_common_hobbies(lst: list[dict]) -> list[tuple[str, int]]:
    """Get the most common hobbies from a list of dictionaries."""
    return Counter([hobby
                   for d in lst
                   for hobby in d['hobbies']]).most_common(3)

print(most_common_hobbies(dlist))


def most_popular_hobbies(list_of_dicts):
    return Counter([one_hobby
                    for one_person in list_of_dicts
                    for one_hobby in one_person['hobbies']]).most_common(3)


print(most_popular_hobbies(dlist))
