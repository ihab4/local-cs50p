class Jar:
    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size