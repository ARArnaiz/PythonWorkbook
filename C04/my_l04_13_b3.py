from collections import namedtuple

Movie = namedtuple("Movie", ['name', 'runtime', 'director'])

Oscar2026 = [
    Movie("Bugonia", "1h 58m", "Yorgos Lanthimos"),
    Movie("F1", "2h 35m", "Joseph Kosinski"),
    Movie("Frankenstein", "2h 29m", "Guillermo del Toro"),
    Movie("Hamnet", "2h 5m", "Chloé Zhao"),
    Movie("Marty Supreme", "2h 29m", "Josh Safdie"),
    Movie("One Battle After Another", "2h 41m", "Paul Thomas Anderson"),
    Movie("The Secret Agent", "1h 41m ", "Kleber Mendonça Filho"),
    Movie("Sentimental Value", "2h 13m", "Joachim Trier"),
    Movie("Sinners", "2h 17m", "Ryan Coogler"),
    Movie("Train Dreams", "1h 42m", "Clint Bentley")
]


# print(Oscar2026)

def format_sort_records2(lst: list, *sort_fields) -> list:
    output = []
    if not sort_fields:
        sort_fields = ('name',)  # Default to 'name' if no fields specified
    for item in sorted(lst, key=lambda x: tuple(getattr(x, field) for field in sort_fields)):
        output.append(f'{item.name:25} {item.runtime:8} {item.director:15}')
    return output


# Examples of usage:
# Sort by name only (default)
# print('\n'.join(format_sort_records2(Oscar2026)))

# Sort by director, then by name
print('\n'.join(format_sort_records2(Oscar2026, 'director', 'name')))

# Sort by runtime, then by director
# print('\n'.join(format_sort_records2(Oscar2026, 'runtime', 'director')))