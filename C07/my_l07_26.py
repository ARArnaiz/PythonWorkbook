import operator

def calc(op_nums: str) -> int|float:
    operator, operand1, operand2 = op_nums.split()
    return eval(f'{operand1} {operator} {operand2}')

print(calc("+ 2 3"))
print(calc("- 10 5"))
print(calc("* 4 6"))
print(calc("/ 10 2"))
print(calc("% 10 3"))
print(calc("** 2 3"))
print(calc("// 10 10"))

def calc_c(to_solve: str) -> int | float:
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

print(calc_c("+ 2 3"))
print(calc_c("- 10 5"))
print(calc_c("* 4 6"))
print(calc_c("/ 10 2"))
print(calc_c("% 10 3"))
print(calc_c("** 2 3"))

def calc_l(to_solve):
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}

    op, first_s, second_s = to_solve.split()
    first = int(first_s)
    second = int(second_s)

    return operations[op](first, second)

print(calc_l('+ 2 3'))