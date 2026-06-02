
# class StringKeyDict(dict):
#     def __setitem__(self, key, value):
#         if isinstance(key, int):
#             key = str(key)
#         super().__setitem__(key, value)

# Claude's
class StringKeyDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(str(key), value)

skd = StringKeyDict()
skd[1] = "one"
skd[3.14] = "pi"
skd[True] = "yes"
print(skd)


# One thing neither solution handles
# __init__ and update(). Try this with either version:
# pythonskd = StringKeyDict({1: "one", 2: "two"})
# print(skd[1])    # Works — but shouldn't it be skd['1']?
# Initializing via the constructor bypasses your __setitem__, so integer keys sneak
# through unconverted. A complete implementation would also override __init__ (and
# arguably update) to funnel through your custom setter. Worth a glossary note —
# it's a classic gotcha when subclassing built-in types.