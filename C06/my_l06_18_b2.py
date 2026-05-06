def sum_cols(filename: str)-> int:
    total = 0
    with open(filename) as f:
        for line in f:
            line =  line.strip().split("\t")
            if len(line) == 2 and line[0].isdigit() and line[1].isdigit():
                total += int(line[0]) * int(line[1])
        return total

def sum_cols2(filename: str)-> int:
    with open(filename) as f:
        return sum(
            int(parts[0]) * int(parts[1])
            for line in f
                if (parts := line.split())
                and len(parts) == 2
                and parts[0].isdigit()
                and parts[1].isdigit()
        )
""""
Claude:
The remaining genuine differences are:

|                              | Compound `if` | Guard clauses  |
|------------------------------|---------------|-----------------|
| Per-condition error messages | ❌ harder     | ✅ trivial     |
| Adding conditions            | gets long     | just add a line |
| Readability at a glance      | compact       | more explicit   |
| Early exit performance       | ✅ same       | ✅ same        |

So the choice really comes down to style and how much you anticipate the 
validation growing — not efficiency.
+
Splits on any whitespace (split() with no arg) — handles tabs, multiple 
spaces, mixed whitespace all at once
"""

def sum_mult_columns(filename):
    total = 0

    for one_line in open(filename):
        fields = one_line.split()

        if len(fields) != 2:
            continue

        first, second = fields

        if not first.isdigit():
            continue

        if not second.isdigit():
            continue

        total += int(first) * int(second)

    return total

print(sum_cols("../numeric_tab_data.txt"))
print(sum_cols2("../numeric_tab_data.txt"))
print(sum_mult_columns("../numeric_tab_data.txt"))

