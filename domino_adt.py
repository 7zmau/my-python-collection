class Domino:
    
    def __init__(self):
        self._theList = list()
        print("Now add items in the list.\nYou cannot remove an item once it is inserted.")
        
    def add(self, item):
        self._theList.append(item)

    def __getitem__(self, index):
        assert not index > len(self._theList), 'Index out of range.'
        return self._theList[index]
        
    def __iter__(self):
        return _DominoIterator(self._theList)
    

class _DominoIterator:
    
    def __init__(self, theItems):
        self._theItems = theItems
        self._curItem = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curItem < len(self._theItems):
            item = self._theItems[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration

    
    
