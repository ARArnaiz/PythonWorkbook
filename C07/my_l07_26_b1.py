import operator

def to_number(s: str) -> int | float:
    try:
        return int(s)
    except ValueError:
        return float(s)   # raises its own ValueError if truly invalid

def calc(to_solve: str) -> int | float:
    """
    Evaluate a prefix expression: '<op> <num1> <num2>'.
    Supports: +  -  *  /  **  %
    Raises ValueError for bad input, ZeroDivisionError for division by zero.
    """
    OPERATIONS = {
        '+':  operator.add,
        '-':  operator.sub,
        '*':  operator.mul,
        '/':  operator.truediv,
        '**': operator.pow,
        '%':  operator.mod,
    }

    parts = to_solve.split()
    if len(parts) != 3:
        raise ValueError(f"Expected '<op> <num1> <num2>', got: {to_solve!r}")

    op, first_s, second_s = parts

    if op not in OPERATIONS:
        raise ValueError(f"Unknown operator {op!r}. Valid: {set(OPERATIONS)}")

    def to_number(s: str) -> int | float:
        try:
            return int(s)
        except ValueError:
            return float(s)   # raises its own ValueError if truly invalid

    first  = to_number(first_s)
    second = to_number(second_s)

    if op in ('/', '%') and second == 0:
        raise ZeroDivisionError(f"Cannot divide by zero: {to_solve!r}")

    return OPERATIONS[op](first, second)

def calc_two_up(to_solve):
    """Evaluate a prefix expression with multiple operands: '<op> <num1> <num2> ...
    and uses the result of the previous operation as the first operand of the next using
    calc() function. Returns the final result.
    """

    parts = to_solve.split()
    op = parts[0]
    total = calc(op + " " + parts[1] + " " + parts[2])
    if len(parts) == 2:
        return total
    else:
        for i in range(3, len(parts)):
            total = calc(op + " " + str(total) + " " + parts[i])
        return total


print(calc_two_up("+ 3 5 7 10"))
print(calc_two_up("/ 100 5 5 2"))

def calc_multi_c(to_solve: str) -> int | float:
    """
    Evaluate a prefix expression with one or more operands: '<op> <num1> [num2 ...]'.
    With a single operand, returns it as-is.
    Reuses calc() for each step — inheriting its validation and float support.
    """
    parts = to_solve.split()

    if len(parts) < 2:
        raise ValueError(f"Expected '<op> <num1> [num2 ...]', got: {to_solve!r}")

    op, *rest = parts  # cleaner unpacking than index slicing

    total = to_number(rest[0])  # single operand: just return it
    for operand in rest[1:]:
        total = calc(f"{op} {total} {operand}")  # f-string, not string concatenation

    return total

print(calc_multi_c("+ 3 5 7 10"))
print(calc_multi_c("/ 100 5 5 2"))

def calc_args(to_solve):

    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}

    op, *numbers = to_solve.split()

    if not numbers:
        return 0

    output = int(numbers[0])
    for one_number in numbers[1:]:
        output = operations[op](output, int(one_number))

    return output

print(calc_args("+ 3 5 7 10"))
print(calc_args("/ 100 5 5 2"))
