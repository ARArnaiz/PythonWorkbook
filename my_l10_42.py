
# class FlexibleDict(dict):
#     def __getitem__(self, key):
#         try:
#             if isinstance(key, int) and key not in self:
#                 return super().__getitem__(str(key))
#             elif isinstance(key, str) and key.isdigit() and key not in self:
#                 return super().__getitem__(int(key))
#             else:
#                 return super().__getitem__(key)
#         except KeyError:
#             return None

#Claude's
class FlexibleDict(dict):
    def __getitem__(self, key):
        if key in self:
            return super().__getitem__(key)

        candidates = [str(key)]
        try:
            candidates.append(int(key))
        except (ValueError, TypeError):
            pass

        for candidate in candidates:
            if candidate in self:
                return super().__getitem__(candidate)

        raise KeyError(key)


fd = FlexibleDict()

fd['a'] = 100
print(fd["a"])

fd[5] = 500
print(fd[5])

fd[1] = 100
print(f"{fd['1']} fd['1'] from fd[1] = 100")

fd['2'] = 200
print(f'{fd[2]}  fd[2] from fd["2"] = 200')

# class FlexibleDict(dict):
#     def __getitem__(self, key):
#         try:
#             if key in self:
#                 pass
#             elif str(key) in self:
#                 key = str(key)
#             elif int(key) in self:
#                 key = int(key)
#         except ValueError:
#             pass
#
#         return dict.__getitem__(self, key)
#
#
# fd = FlexibleDict()
#
# fd['a'] = 100
# print(fd['a'])
#
# fd[5] = 500
# print(fd[5])
#
# fd[1] = 100
# print(fd['1'])
#
# fd['2'] = 200
# print(fd[2])