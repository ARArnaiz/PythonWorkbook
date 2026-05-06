MENU = {
    "soup": 5.99,
    "salad": 6.99,
    "sandwich": 8.99,
    "coffee": 3.50,
    "tea": 2.50,
    "pie": 2.50,
    "french fries": 3.50,
    "chili": 3.99,
    "soda": 2.75,
    "milk": 1.00,
    "lemonade": 2.25,
    "eggs": 2.35,
    "sausages": 3.50,
    "hash browns": 2.99,
    "pancakes": 2.35,
}

def restaurant():
    total = 0
    while True:
        order = input("Order: ").strip().casefold()
        if not order:
            break
        if order in MENU:
            price = MENU[order]
            total += MENU[order]
            print(f"{order.capitalize()} costs {price:.2f}, total is {total:.2f}")
        else:
            print(f'Sorry, we are out of {order} today.')
    print(f'Your total is {total:.2f}')

restaurant()