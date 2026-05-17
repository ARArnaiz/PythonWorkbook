
brackets = [{'start': 0, 'end': 1000, 'tax': 0},
            {'start': 1000, 'end': 10000, 'tax': .1},
            {'start': 10000, 'end': 20000, 'tax': .2},
            {'start': 20000, 'end': 999999999999, 'tax': .5}]

def calc_tax_rate_with_brackets(income: float) -> float:
    """Calculate tax rate based on income brackets.

    Args:
        income (float): The income amount.

    Returns:
        float: The calculated tax rate.
    """
    tax_owed = 0

    for bracket in brackets:
        if income < bracket['start']:
            continue
        taxed_amount = min(income, bracket['end'])
        taxed_amount -= bracket['start']
        tax_owed += taxed_amount * bracket['tax']

    return tax_owed

print(calc_tax_rate_with_brackets(50000))

def tax_brackets(amount, brackets):
    tax_owed = 0

    for one_bracket in brackets:
        if amount < one_bracket['start']:
            continue

        taxed_amount = min(amount, one_bracket['end'])
        taxed_amount -= one_bracket['start']

        tax_owed += taxed_amount * one_bracket['tax']

    return tax_owed


print(tax_brackets(50000, brackets))