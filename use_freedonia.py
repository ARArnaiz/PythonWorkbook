import freedonia

print(freedonia.calculate_tax(500, "Harpo", 12))
assert freedonia.calculate_tax(500, "Harpo", 12) == 625.0
print(freedonia.calculate_tax(500, "Harpo", 21))
assert freedonia.calculate_tax(500, "Harpo", 21) == 718.75
#print(freedonia.calculate_tax(99, "Amazonas", 13))
#print(freedonia.calculate_tax(-99, "Groucho", 13))
#print(freedonia.calculate_tax(99, "Zeppo", 13.5))

