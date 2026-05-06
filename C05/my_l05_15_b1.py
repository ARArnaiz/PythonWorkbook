def add_entry(d: dict, city: str, amount: float) -> None:
    d.setdefault(city, {"count": 0, "total": 0.0})
    d[city]["count"] += 1
    d[city]["total"] += amount


def get_rainfall() -> dict:
    city_rainfall = {}
    while True:
        city = input("Enter the city name (or enter to exit): ")
        if not city:
            break
        rainfall = input(f"Enter rainfall for {city}: ")
        if not rainfall:
            break
        add_entry(city_rainfall, city, float(rainfall))
    return city_rainfall


def print_rainfall(city_rainfall: dict) -> None:
    for city, d in city_rainfall.items():
        entries = 'entry' if d["count"] == 1 else 'entries'
        print(f'{city}: {d["total"]:.2f} (average: {d["total"] / d["count"]:.2f}, over {d["count"]} {entries})')


def print_rainfall2(city_rainfall: dict) -> None:
    for city, d in city_rainfall.items():
        print(f'{city}: {d["total"]:.2f} '
              f'(average: {d["total"] / d["count"]:.2f}, '
              f'over {d["count"]} {"entry" if d["count"] == 1 else "entries"})')


print_rainfall(get_rainfall())
# print_rainfall2(get_rainfall())
