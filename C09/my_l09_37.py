from typing import Callable

def mymenu(**menu_choices: Callable) -> None:
    pass

# Lerner's answer
def menu(**options):
    while True:
        option_string = '/'.join(sorted(options))
        choice = input(
            f'Enter an option ({option_string}): ')
        if choice in options:
            return options[choice]()

        print('Not a valid option')

def func_a():
    return "A"

def func_b():
    return "B"
return_value = menu(a=func_a, b=func_b)
print(f'Result is {return_value}')

mymenu(a=func_a, b=func_b)

"""Claude's explanation
The `menu` function is a **generic dispatcher** — a reusable way to let the user 
pick which function to run, without the calling code needing to know anything about the input loop or validation.

---

## What it does, step by step

```python
def menu(**options):          # options = {"a": func_a, "b": func_b}
    while True:
        option_string = '/'.join(sorted(options))   # → "a/b"
        choice = input(f'Enter an option ({option_string}): ')
        if choice in options:
            return options[choice]()   # calls func_a() or func_b(), returns result
        print('Not a valid option')
```

1. `**options` collects the keyword arguments into a dict: `{"a": func_a, "b": func_b}`
2. The `while True` loop keeps asking until a valid choice is entered
3. `options[choice]` retrieves the *function object* — `func_a` or `func_b`
4. The `()` at the end *calls* it, and `return` passes the result back to the caller

---

## The key insight: functions as values

`menu(a=func_a, b=func_b)` passes functions *without calling them* (no `()` on `func_a`). 
They sit in the dict as callable values, waiting. The `()` only happens inside `menu` 
when the user makes their choice. This is the same `getattr` dispatch pattern from your 
glossary entry 136 — data (the dict) drives behavior (which function runs).

---

## Why it's a module

The purpose of putting it in `menu.py` is **reusability**. Any program that needs a text menu can do:

```python
from menu import menu

result = menu(quit=do_quit, save=do_save, load=do_load)
```

The input loop, validation, and error message are written once. The caller only specifies *what options 
exist* and *what function each one runs*. That's the separation of concerns: `menu.py` 
owns the UI logic; the calling program owns the business logic.

---

## In one sentence 

`menu` is a reusable input loop that maps user-typed strings to function calls — the caller just 
supplies the mapping, and `menu` handles everything else.

The functions passed to `menu` have to be **zero-argument callables** — because `menu` calls them
with just `options[choice]()`, no arguments.

So in practice they're either:

**Wrapper functions** that hardcode or already have their parameters:
```python
def save():
    save_file("output.txt")   # parameter baked in

def greet():
    print("Hello, Alfredo!")  # no parameters needed
```

**Lambda shortcuts** for the same idea:
```python
menu(save=lambda: save_file("output.txt"),
     load=lambda: load_file("input.txt"))
```

**Class constructors** (which Lerner hints at with "callable... function or class") that need no arguments:
```python
menu(dog=Dog, cat=Cat)   # Dog() and Cat() called with no args
```

---

The constraint is intentional. `menu` is a *navigation layer*, not an execution layer. Its job is just: 
present options → get choice → hand off. The actual work — including any parameters it needs — lives 
inside the function being called.

This is why Lerner says the functions passed in should be generic enough to stand alone. If a function 
needs parameters, it's not ready to be a menu action yet — it needs to be wrapped first.
"""