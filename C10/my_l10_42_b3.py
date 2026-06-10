
class FlatList(list):
#
#     def append(self, item):
#         if isinstance(item, str):
#             super().append(item)
#             return
#         try:
#             #iter(item)
#             for i in item:
#                 super().append(i)
#         except TypeError:
#             super().append(item)

# Claude's
    def append(self, item):
        if isinstance(item, str):
            super().append(item)   # done — store it, don't inspect it further
            return
        try:
            for i in item:
                self.append(i)     # unknown — send it back through the gate
        except TypeError:
            super().append(item)   # done — it's a scalar, store it

fl = FlatList()
fl.append([1, 2, 3])
fl.append(4)
fl.append(["a", "b", "c"])
fl.append("d")
fl.append("hello")
fl.append(["world", ["nested", "list"]])
print(fl)

