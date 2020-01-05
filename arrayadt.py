import ctypes
class Array:
    def __init__(self, size):
        assert size > 0, "Array size must be greater then zero"
        a = ctypes.py_object * size
        self._slots = a()
        self._size = size
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._slots[index]

    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._slots[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._slots[i] = value

    def __iter__(self):
        return _ArrayIterator(self._slots)


class _ArrayIterator:
    def __init__(self, slots):
        self._items = slots
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._items):
            item = self._items[self._curNdx]
            self._curNdx += 1
            return item
        else:
            raise StopIteration
    
    

