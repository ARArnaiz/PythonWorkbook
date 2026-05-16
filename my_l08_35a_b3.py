import json
from collections import defaultdict


def load_cities_to_dict(filename) -> dict[str,int]:
    with open(filename) as f:
        return { line['city'] : int(line['population']) for line in json.load(f) }

x = load_cities_to_dict("cities.json")
print(len(x))
# print(x)

def load_city_state_to_dict(filename) -> dict[str,int]:
    with open(filename) as f:
        return { (line['city'],line['state']) : int(line['population']) for line in json.load(f) }

y = load_city_state_to_dict("cities.json")
print(len(y))
# print(y)

cities = defaultdict(int)
for (c, s), v in y.items():
    cities[c] += 1
print(dict(filter(lambda x: x[1] > 1, cities.items())))
print(len(dict(filter(lambda x: x[1] > 1, cities.items()))))
print(sum(dict(filter(lambda x: x[1] > 1, cities.items())).values()))

repeated = {city: count for city, count in cities.items() if count > 1}
print(sorted(repeated.items(), key=lambda x: x[1], reverse=True)[:10])

repeated = {city: count for city, count in cities.items() if count > 1}
print(sum(repeated.values()))          # → 137  (all records)
print(sum(v - 1 for v in repeated.values()))  # → 75   (duplicates only)
print(len(repeated))                   # → 62  (unique city names)


# Understandable — but the two numbers are measuring different things:
#
# **75** — city names that are duplicated (i.e. `1000 - 925`: records lost when using city-only as key)
#
# **137** — *all records* belonging to those 62 repeated city names
#
# The difference is that 75 counts only the *overflow* (the duplicates beyond the first occurrence), while 137 counts *every record* for those cities including the first.
#
# ```
# "Springfield" in IL, MO, OH, MA, MN  → 5 records
#   contributes 4 to the 75 (duplicates)
#   contributes 5 to the 137 (all records)
# ```
#
# So the relationship is:
#
# ```
# 137 (all records for repeated cities)
# -62 (one "first" record per city name)
# = 75 ✅
# ```
#
# That's your 75. The 62 city names each had one record that "survived" into the 925-entry dict, plus 75 that got overwritten. `62 + 75 = 137`.
#
# **To verify directly:**
#
# ```python
# repeated = {city: count for city, count in cities.items() if count > 1}
# print(sum(repeated.values()))          # → 137  (all records)
# print(sum(v - 1 for v in repeated.values()))  # → 75   (duplicates only)
# print(len(repeated))                   # → 62  (unique city names)
# ```
