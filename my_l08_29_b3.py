d1 = { "name": "John", "age": 10}
d2 = { "name": "Mary", "age": 15}
d3 = { "name": "Peter", "age": 40}
d4 = { "name": "Rose", "age": 35}
d5 = { "name": "Paul", "age": 18}

d_lst = [d1, d2, d3, d4, d5]

def add_age_in_months(lst: list[dict]) -> list[dict]:
    return [dict(one_dict, age_in_months=one_dict['age'] * 12)
            for one_dict in lst
            if one_dict['age'] < 20]

print(add_age_in_months(d_lst))

# The | operator reads naturally as "this dict, plus this addition" and is now
# the idiomatic way to merge/extend dicts in modern Python.

def add_age_in_months_c(people: list[dict]) -> list[dict]:
    return [
        person | {'age_in_months': person['age'] * 12}
        for person in people
        if person['age'] < 20
    ]
print(add_age_in_months_c(d_lst))


def age_in_months(list_of_people):
    return [dict(**one_person, age_in_months=one_person['age'] * 12)
            for one_person in list_of_people
            if one_person['age'] <= 20]

print(age_in_months(d_lst))