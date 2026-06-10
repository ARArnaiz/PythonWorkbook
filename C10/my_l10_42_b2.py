
class RecentDict(dict):
    def __init__(self, max_size):
        super().__init__()
        self.max_size = max_size

    # def __setitem__(self, key, value):
    #     if len(self) >= self.max_size:
    #         self.popitem()  # Remove the least recently added item
    #     super().__setitem__(key, value)

    # Claude's bug fix
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if len(self) > self.max_size:
            self.pop(next(iter(self)))

rd = RecentDict(3)
rd['a'] = 1
rd['b'] = 2
rd['c'] = 3
print(rd)  # Output: {'a': 1, 'b': 2, 'c': 3}
rd['d'] = 4
print(rd)  # Output: {'b': 2, 'c': 3, 'd': 4}
rd['e'] = 5
print(rd)
