
# def get_rainfall():
#
#     City_Rainfall = {}
#     while True:
#         city = input("Enter the city name (or enter to exit): ")
#         if not city:
#             break
#         print(city)
#         rainfall = input("Enter the city's rainfall: ")
#         if not rainfall:
#             break
#         print(rainfall)
#         City_Rainfall[city] = City_Rainfall.get(city, 0) + float(rainfall)
#
#     for k,v in City_Rainfall.items():
#         print(f'{k}: {v:.2f}')
#
# get_rainfall()

def get_rainfall() -> dict:
    city_rainfall = {}
    while True:
        city = input("Enter the city name (or enter to exit): ")
        if not city:
            break
        rainfall = input(f"Enter rainfall for {city}: ")
        if not rainfall:
            break
        city_rainfall[city] = city_rainfall.get(city, 0) + float(rainfall)
    return city_rainfall


def print_rainfall(city_rainfall: dict) -> None:
    for city, amount in city_rainfall.items():
        print(f'{city}: {amount:.2f}')

print_rainfall(get_rainfall())