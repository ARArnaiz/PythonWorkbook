
FREEDONIA_PROVINCE_TAXRATE = {
    "Chico" : 0.5,
    "Groucho" : 0.7,
    "Harpo" : 0.5,
    "Zeppo" : 0.4 }

def time_adjustment(time: int) -> int | float:
    return time / 24

def calculate_tax(original_price: float, province: str, time: int,) -> float:
    if original_price <= 0:
        raise ValueError("Original price must be positive")
    if province not in FREEDONIA_PROVINCE_TAXRATE:
        raise ValueError(
            f"Invalid province: {province!r}. "
            f"Choose from: {', '.join(FREEDONIA_PROVINCE_TAXRATE.keys())}."
        )
    if not isinstance(time, int) or not (0 <= time <= 23):
        raise ValueError("Time must be an integer between 0 and 23 inclusive.")
    return original_price * (1 + FREEDONIA_PROVINCE_TAXRATE[province] * time_adjustment(time))


