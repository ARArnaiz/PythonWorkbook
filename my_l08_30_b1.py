# Claude
# != 0 instead of == 1 — correctly handles negative odd (integers
# (-3 % 2 is -1 in Python, not 1))

def flatten_odd(lst: list[list]) -> list[int]:
    """Flattens a list of lists into a single list."""
    return [ int(item)
             for sublist in lst
             for item in sublist
             if (isinstance(item, int) and not isinstance(item, bool) and item % 2 == 1) or
                (isinstance(item, str) and item.isdigit() and int(item) % 2 == 1) ]

def flatten_odd_c(lst: list[list]) -> list[int]:
    """
    Flattens one level of a list of lists, returning only odd integers.
    Accepts int and digit-string items; skips floats, nested lists, and non-numeric strings.
    """
    result = []
    for sublist in lst:
        for item in sublist:
            if isinstance(item, bool):       # bool is a subclass of int — exclude it
                continue
            if isinstance(item, int):
                if item % 2 != 0:
                    result.append(item)
            elif isinstance(item, str) and item.strip().lstrip('-').isdigit():
                value = int(item)
                if value % 2 != 0:
                    result.append(value)
            # floats, nested lists, "seven", etc. are intentionally skipped
    return result

def flatten_odd_ints(mylist):
    return [int(str(one_element))
            for one_sublist in mylist
            for one_element in one_sublist
            if str(one_element).strip().isdigit() and int(one_element) % 2 == 1]

print(flatten_odd([[1,2,"3"], [4,5,6], ["seven",8,9], [111, [11, 12], 13.9999, -25, "-25", True]])) # [1, 3, 5, 9, 111, -25]
print(flatten_odd_c([[1,2,"3"], [4,5,6], ["seven",8,9], [111, [11, 12], 13.9999, -25, "-25", True]])) # [1, 3, 5, 9, 111, -25, -25]
print(flatten_odd_ints([[1,2,"3"], [4,5,6], ["seven",8,9], [111, [11, 12], 13.9999, -25, "-25", True]])) # [1, 3, 5, 9, 111]