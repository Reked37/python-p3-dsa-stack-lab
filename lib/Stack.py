class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)
        else:
            return False
        
    def pop(self):
        if not self.items:
            return None
        else:
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        total = len(self.items)
        for idx, value in enumerate((self.items), start=1):
            if value == target:
                return total -idx  
        return -1

