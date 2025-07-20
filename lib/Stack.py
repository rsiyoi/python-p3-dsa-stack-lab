class Stack:

    def __init__(self, items = [], limit = 100):
        if items is None:
            self.items = []
        else:
            self.items = items.copy()
        self.capacity = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.capacity is not None and len(self.items) >= self.capacity:
            return
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        if self.capacity is None:
            return False
        return len(self.items) >= self.capacity

    def search(self, target):
        try:
            index = len(self.items) - 1 - self.items[::-1].index(target)
           
            return len(self.items) - 1 - index
        except ValueError:
            
            return -1
