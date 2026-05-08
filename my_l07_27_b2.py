
def getitem(kindex):
    """Retrieve an item from the list by index or key."""
    def get_seq(seq):
        return seq[kindex]
    return get_seq

d = {'a':1,'b':2, 'z': 'zoo'}
l = [[1,2],3]
t = ({'a': 1},2,3)
f = getitem('a')
print(f(d))
f = getitem('z')
print(f(d))
f = getitem(0)
print(f(l))
f = getitem(0)
print(f(t))


def getitem_q(kindex):
    """Retrieve an item from the collection by index or key."""

    def get_item(collection, kindex):
        if isinstance(collection, (list, tuple)):
            return collection[kindex]
        elif isinstance(collection, dict):
            return collection.get(kindex)
        else:
            raise TypeError("Unsupported collection type")

    return lambda seq: get_item(seq, kindex)

# Example usage
get_list_item = getitem(0)
print(get_list_item([1, 2, 3]))  # Output: 1

get_dict_item = getitem('key')
print(get_dict_item({'key': 'value'}))  # Output: value

def getitem_l(index):
    def inner(data):
        return data[index]
    return inner

f = getitem_l('a')
print(f(d))
f = getitem_l('z')
print(f(d))
f = getitem_l(0)
print(f(l))
f = getitem_l(0)
print(f(t))

def getitem_safe(kindex, default=None):
    def get_seq(seq):
        try:
            return seq[kindex]
        except (KeyError, IndexError):
            return default
    return get_seq

f = getitem_safe('w')
print(f(d))
f = getitem_safe('z')
print(f(d))
f = getitem_safe(0)
print(f(l))
f = getitem_safe(0)
print(f(t))