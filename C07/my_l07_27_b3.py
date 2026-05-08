from typing import Callable, Any

def doboth(func1: Callable, func2: Callable) -> Callable:
    """
    Composes two functions, applying func1 first and then func2.
    """
    def composite(x):
        return func2(
            func1(x)
        )
    return composite

def doboth(f1, f2):
    def inner(data):
        return f2(f1(data))
    return inner


"""
[Claude: examples + improvement]
Given your work, the most natural use case is **text processing pipelines** — 
chaining two transforms where the output of one feeds the next.

A concrete example from your Syllabify world:

```python
normalize = doboth(str.lower, str.strip)
print(normalize("  Hola  "))  # 'hola'
```

Or chaining more meaningful linguistic steps:

```python
remove_punctuation = lambda s: ''.join(c for c in s if c.isalpha() or c.isspace())
tokenize = str.split

clean_and_split = doboth(remove_punctuation, tokenize)
print(clean_and_split("¡Hola, mundo!"))  # ['Hola', 'mundo']
```

But `doboth` is limited to exactly two functions. The natural next step — and a worthwhile 
exercise — is generalizing it to a **pipeline of arbitrary length**:

```python
def pipe(*funcs):
    def pipeline(data):
        for f in funcs:
            data = f(data)
        return data
    return pipeline

normalize = pipe(str.strip, str.lower, remove_punctuation, tokenize)
```

This is essentially what your `word_transform_pipeline` design already does architecturally — 
`doboth` is just the two-function seed of that idea. Recognizing that continuity is the 
real payoff of this exercise.
"""