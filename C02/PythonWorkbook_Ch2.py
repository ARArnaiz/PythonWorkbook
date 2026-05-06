# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.22.4",
#     "mcp>=1",
#     "pydantic>=2",
#     "vegafusion==2.0.3",
#     "vl-convert-python==1.9.0.post1",
# ]
# ///

import marimo

__generated_with = "0.23.1"
app = marimo.App(
    width="medium",
    css_file="/usr/local/_marimo/custom.css",
    auto_download=["html"],
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #Lerner, R.M. (2026) *Python Workout*, Second Edition, Shelter Island: Manning Publications Co.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Chapter 2: Numeric Types
    ### Exercise 1: Number guessing game
    """)
    return


@app.cell
def _():
    # Number guessing game
    import random
    def guessing_game():
        ntog = random.randint(0,100)
        while True:
            un = int(input("Guess a number between 0 and 100"))
            if un > ntog:
                print(f"{un} - Too high")
            elif un < ntog:
                print(f"{un} - Too low")
            else:
                print(f"{un} - Just right")
                break
    guessing_game()
    return (random,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Beyond the exercise
    """)
    return


@app.cell
def _(random):
    # Number guessing game with limit number of chances
    def guessing_game_n_chances(n: int): 
        ntog = random.randint(0, 100) 
        while n:
            try: 
                un = int(input(f"Guess a number between 0 and 100 ({n} chances left): ")) 
                if not (0 <= un <= 100):
                    print("Please enter a number between 0 and 100.")
                    continue
            except ValueError: 
                print("Please enter a valid number.") 
                continue 
            n -= 1 
            if un > ntog: 
                print(f"{un} - Too high") 
            elif un < ntog: 
                print(f"{un} - Too low") 
            else: 
                print(f"{un} - Just right") 
                break 
        else: print(f"Sorry, bettter luck next time! The number was {ntog}.")

    guessing_game_n_chances(5)
    return


@app.cell
def _(random):
    # Random number, random base
    def to_base(n: int, base: int) -> str:
        if n == 0:
            return "0"
        digits = "0123456789abcdef"
        result = ""
        while n:
            result = digits[n % base] + result
            n //= base
        return result

    def print_range_in_base(base: int, block_size: int = 10):
        for i in range(0, 101):
            print(to_base(i, base), end="\t")
            if (i + 1) % block_size == 0:
                print()  # newline every block_size numbers

    def is_valid_base(s: str, base: int) -> bool:
        try:
            int(s, base)
            return True
        except ValueError:
            return False

    def guessing_game_base():
        base = int(random.randint(2,16))
        ntog = int(random.randint(0,100))
        ntog_in_base = to_base(ntog, base)
        print(f'Guess a number between {to_base(0, base)} and {to_base(100, base)} in base {base}')
        print_range_in_base(base)
        while True:
            un = input("Make your guess: ")
            if is_valid_base(un, base):
                if int(un, base) > int(ntog_in_base, base):
                    print(f"{un} - Too high")
                elif int(un, base) < int(ntog_in_base, base):
                    print(f"{un} - Too low")
                else:
                    print(f"{un} - Just right")
                    break

    guessing_game_base()
    return is_valid_base, print_range_in_base, to_base


@app.cell
def _(is_valid_base, print_range_in_base, random, to_base):
    # Random number, random base - Claude small improvement over mine
    def guessing_game_base2():
        base = int(random.randint(2,16))
        ntog = int(random.randint(0,100))
        ntog_in_base = to_base(ntog, base)
        print(f'Guess a number between {to_base(0, base)} and {to_base(100, base)} in base {base}')
        print_range_in_base(base)
        while True:
            un = input("Make your guess: ")
            if is_valid_base(un, base):
                if int(un, base) > ntog:
                    print(f"{un} - Too high")
                elif int(un, base) < ntog:
                    print(f"{un} - Too low")
                else:
                    print(f"{un} - Just right")
                    break
            else:
                print(f"'{un}' is not a valid base-{base} number. Try again.")  # ← add this

    guessing_game_base2()
    return


@app.cell
def _(is_valid_base, print_range_in_base, random, to_base):
    # Random number, random base - Claude further improvements

    def guessing_game_base3():
        base = random.randint(2, 16)        # int() wrapper not needed here
        ntog = random.randint(0, 100)
        print(f'Guess a number between {to_base(0, base)} and {to_base(100, base)} in base {base}')
        print_range_in_base(base)
        while True:
            un = input("Make your guess: ")
            if not is_valid_base(un, base):
                print(f"'{un}' is not a valid base-{base} number. Try again.")
                continue
            guess = int(un, base)
            if guess > ntog:
                print(f"{un} - Too high")
            elif guess < ntog:
                print(f"{un} - Too low")
            else:
                print(f"{un} - Just right!")
                break
    guessing_game_base3()
    return


@app.cell
def _(random):
    # Random word, hints earlier or later word [?]
    def guessing_word_game():
        with open("words.txt", "r") as f:
            words = {line.strip() for line in f}
        wToGuess = random.choice(list(words))
        #print(wToGuess)
        print('Guess a 5-letter word!')
        while True:
            un = input("Make your guess: ").upper()
            if not un.isalpha() or len(un) != 5:
                print(f"'{un}' is not a valid 5-letter word. Try again.")
            elif un not in words:
                print(f"'{un}' is not a valid dictionary word. Try again.")
            elif un > wToGuess:
                print(f"{un} - Later in the alphabet")
            elif un < wToGuess:
                print(f"{un} - Earlier in the alphabet")
            else:
                print(f"{un} - Just right!")
                break
    guessing_word_game()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercise 2: Summing numbers
    """)
    return


@app.cell
def _():
    # Lerner's answer
    def mysum(*numbers):
        output = 0
        for number in numbers:
                output += number
        return output

    print(mysum(10, 20, 30, 40))
    print(mysum(1,2,3))
    # print(mysum([1,2,3]))
    # print(mysum((1,2,3)))
    # print(mysum({1,2,3}))
    # print(mysum(1,2,3, [1,2,3], (1,2,3), {1,2,3}, {1:"a", 2: "b", 3: "c"}, {"a": 1, "b": 2, "c": 3}))
    return


@app.cell
def _():
    # Mi answer
    def misum(*args, **kwargs):
        total = 0
        for arg in args:
            if isinstance(arg, int):
                total += arg
            elif isinstance(arg, (list, tuple, set)):  # grouped — cleaner
                for i in arg:
                    if isinstance(i, int):             # guard against non-int elements
                        total += i
            else:
                print(f"unsupported: {type(arg).__name__}")
                # raise TypeError(f"unsupported: {type(arg).__name__}")
        return total


    print(misum(1,2,3))
    print(misum([1,2,3]))
    print(misum((1,2,3)))
    print(misum({1,2,3}))
    print(misum(1,2,3, [1,2,3], (1,2,3), {1,2,3}, {1:"a", 2: "b", 3: "c"}, {"a": 1, "b": 2, "c": 3}))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Beyond the exercise
    """)
    return


@app.cell
def _():
    # 1

    def mysum2(numbers, another=0):
        output = 0 
        for number in numbers:
                output += number
        return output + another

    print(mysum2([10, 20, 30, 40], 100))
    return


@app.cell
def _():
    # 2
    def myavg(*numbers):
        output = 0
        for number in numbers:
                output += number
        return output / len(numbers)

    print(myavg(10, 20, 30, 40, 100))
    return


@app.cell
def _():
    # 3
    def mytokens(*tokens):
        shortest = ""
        longest = ""
        cumlength = 0
        for i, w in enumerate(tokens):
            if i == 0:
                shortest = w
                longest = w
            else:
                if len(w) < len(shortest):
                    shortest = w
                if len(w) > len(longest):
                    longest = w                
            cumlength += len(w)
        avglength = cumlength / len(tokens)
        return (shortest, longest, avglength)

    print(mytokens("hose", "house", "mouse", "muse", "a", "antiegalitarianism"))
    return


@app.cell
def _():
    # 3 Claude's version
    def mytokens2(*tokens):
        if not tokens:
            raise ValueError("At least one token required.")
        shortest  = min(tokens, key=len)
        longest   = max(tokens, key=len)
        avglength = sum(len(w) for w in tokens) / len(tokens)
        return (shortest, longest, avglength)

    print(mytokens2("hose", "house", "mouse", "muse", "a", "antiegalitarianism"))
    return


@app.cell
def _():
    # 4 !!! misses the str float
    def mysumonlynums(*objs):
        output = 0
        for o in objs:
            if isinstance(o, (int, float)):
                output += o
            elif isinstance(o, str) and o.isdigit():
                output += int(o)
        return output

    print(mysumonlynums(10, {"a": 1}, 20, [23, 45], (39, 56), {1, 2}, "over", 30.60, 40, 100, "30", "30.34"))
    return


@app.cell
def _():
    # $ Claude's
    def mysumonlynums1(*objs):
        output = 0.0
        for o in objs:
            if isinstance(o, (int, float)):
                output += o
            elif isinstance(o, str):
                try:
                    output += float(o)
                except ValueError:
                    pass    # non-numeric string — silently skip
        return output

    print(mysumonlynums1(10, {"a": 1}, 20, [23, 45], (39, 56), {1, 2}, "over", 30.60, 40, 100, "30", "30.34"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercise 3: Run timing
    """)
    return


@app.cell
def _():
    def run_timing() -> str:
        times = []
        while True:
            entry = input('Enter the time for each of your 10K runs (Press "q" when done): ')
            if entry.lower() == "q":
                break
            try:
                times.append(float(entry))
            except ValueError:
                print("Not a number. Only numbers please.")
                continue
        result = sum(times) / len(times)
        return f'Average of {result}, over {len(times)} runs'

    print(run_timing())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Beyond the exercise
    """)
    return


@app.cell
def _():
    # My f
    def cut_float(n1: int, f: float, n2: int) -> float:
        """Returns float keeping last `n1` integer digits and first `n2` decimal digits."""
        w , d = str(f).split(".")
        newf = (".").join([w[-n1:], d[:n2]])
        return float(newf)

    print(cut_float(2, 1234.5678, 3))
    return


@app.cell
def _():
    # Claude's f
    def cut_float(before: int, f: float, after: int) -> float:
        """Returns float keeping last `before` integer digits and first `after` decimal digits."""
        w, d = str(f).split(".")
        return float(f"{w[-before:]}.{d[:after]}")

    print(cut_float(2, 1234.5678, 3))
    return


@app.cell
def _():
    # My solution
    from decimal import Decimal
    def sumdecimalns(str_numa: str, str_numb: str ) -> Decimal:
        """Returns sum of two Decimal numbers."""
        return Decimal(str_numa) + Decimal(str_numb)

    print(sumdecimalns("0.1" , "0.2"))
    print(0.1 + 0.2)
    return


@app.cell
def _():
    # Claude's solution
    from decimal import Decimal
    def sumdecimalns(*str_nums: str) -> Decimal:
        """Returns sum of any number of Decimal numbers passed as strings."""
        if not str_nums:
            return Decimal("0")
        try:
            return sum(Decimal(n) for n in str_nums)
        except Exception as e:
            raise ValueError(f"Invalid number: {e}")

    print(sumdecimalns("0.1" , "0.2", "0.001", "abc"))
    print(0.1 + 0.2 + 0.001)
    print(0)
    return


@app.cell
def _():
    # Junie's solution
    from decimal import Decimal
    def sumdecimalns(*str_nums: str) -> Decimal:
        """Returns sum of any number of Decimal numbers passed as strings.
        Skips invalid numeric strings."""
        output = Decimal("0")
        for n in str_nums:
            try:
                output += Decimal(n)
            except Exception:
                pass  # Skip non-numeric string
        return output

    print(sumdecimalns("0.1" , "0.2", "0.001", "abc"))
    print(0.1 + 0.2 + 0.001)
    print(0)
    return


@app.cell
def _():
    # Claude on Junie's solution
    from decimal import Decimal, InvalidOperation

    def sumdecimalns(*str_nums: str) -> Decimal:
        """Returns sum of any number of Decimal numbers passed as strings.
        Skips invalid numeric strings and reports them."""
        output = Decimal("0")
        for n in str_nums:
            try:
                output += Decimal(n)
            except InvalidOperation:
                print(f"Skipping invalid value: '{n}'")
        return output

    print(sumdecimalns("0.1" , "0.2", "0.001", "abc"))
    print(0.1 + 0.2 + 0.001)
    print(0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercise 4: Hexadecimal output
    """)
    return


@app.cell
def _():
    # My solution = Gemini + Claude
    def hex_output(hex_str: str) -> int:
        """Returns decimal integer value of hexadecimal string.
            Using Horner's method."""
        digits = "0123456789abcdef"
        hex_str = hex_str.lower().removeprefix("0x")  # handles "0x2AF" and "2AF"
        if not all(c in digits for c in hex_str):
            raise ValueError(f"Invalid hex string: '{hex_str}'")
        result = 0
        for char in hex_str:
            # Find the numerical value of the current character
            value = digits.index(char)
            # Shift the current result by the base and add the new value
            result = result * 16 + value
        return result

    def print_range_in_base(base: int, block_size: int = 10):
        for i in range(0, 101):
            print(to_base(i, base), end="\t")
            if (i + 1) % block_size == 0:
                print()  # newline every block_size numbers

    def to_base(n: int, base: int) -> str:
        if n == 0:
            return "0"
        digits = "0123456789abcdef"
        result = ""
        while n:
            result = digits[n % base] + result
            n //= base
        return result

    print_range_in_base(16, 10)
    to_base(0x0, 10)
    return print_range_in_base, to_base


@app.cell
def _():
    # Lerner's solution
    def hex_output(hexnum: str) -> int:
        digits = "0123456789abcdef"
        decnum = 0
        hexnum = hexnum.lower().removeprefix("0x")  # handles "0x2AF" and "2AF"

        if not all(c in digits for c in hexnum):
            raise ValueError(f"Invalid hex string: '{hexnum}'")

        for power, digit in enumerate(reversed(hexnum)):
            decnum += int(digit, 16) * (16 ** power)
        return decnum

    hex_output("0x1A")
    return


@app.cell
def _():
    # Claude's solution

    def name_triangle(name: str) -> str:
        """Returns a string representing a centered letter equilateral triangle of the given name.
        Each line adds 1 character of the name until the name is complete"""
        width = len(name) * 2 - 1  # Width of the widest row
        rows = []
        for i in range(1, len(name) + 1):
            row_chars = " ".join(name[:i])   # "A", "A B", "A B C", ...
            rows.append(row_chars.center(width))
        return "\n".join(rows)

    print(name_triangle("Alfredo"))
    return


if __name__ == "__main__":
    app.run()
