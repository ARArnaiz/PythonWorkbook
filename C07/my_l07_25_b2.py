import math


def my_factors_prod(*args: int | float) -> int | float:
    """Calculates the product of all factors of given numbers."""
    product = 1

    for num in args:
        product *= num
    return product


print(my_factors_prod(1, 2, 3, 4, 5, -6.34))
print(my_factors_prod(1.5, 2.5, 3.5, 100))
print(my_factors_prod())


def my_factors_prod_c1(*args: int | float) -> int | float:
    """Calculates the product of all given numbers. Returns 1 for no arguments (empty product)."""
    return math.prod(args)


print(my_factors_prod_c1(1, 2, 3, 4, 5, -6.34))
print(my_factors_prod_c1(1.5, 2.5, 3.5, 100))
print(my_factors_prod_c1())


def my_factors_prod_c2(*args: int | float) -> int | float:
    """Calculates the product of all given numbers. Returns 1 for no arguments (empty product)."""
    product = 1
    for num in args:
        product *= num
    return product


print(my_factors_prod_c2(1, 2, 3, 4, 5, -6.34))
print(my_factors_prod_c2(1.5, 2.5, 3.5, 100))
print(my_factors_prod_c2())


def factorialish(*args):
    if not args:
        return 0

    total = args[0]
    for one_number in args[1:]:
        total *= one_number

    return total


print(factorialish(1, 2, 3, 4, 5, -6.34))
print(factorialish(1.5, 2.5, 3.5, 100))
print(factorialish())
