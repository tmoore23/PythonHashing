class ChainingHashTable:
    def __init__(self, size=10):
        self.size = size
        """
        self.table = [
          [('Key1', 'Value1')],  # Index 0
          [('Key2', 'Value2')],  # Index 1
        ]
        """
        self.table = [[] for _ in range(size)]
        self.count = 0

    def insert(self, key, value):
        index = self._hash_function(key)
        # Make sure each key remains unique
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])
        self.count += 1
        load_factor = self.count / self.size
        if load_factor > 1.5:
            self._rehash()

    def get(self, key):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        raise KeyError(key)

    def _hash_function(self, key):
        return hash(key) % self.size  # Built-in python hash function

    def _rehash(self):
        old_table = self.table
        self.size *= 2  # dobule the size
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        # Refill
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)


class LinearProbingHashTable:
    def __init__(self, size=10):
        self.size = size
        """
        self.table = [
            ('Key', 'Value'),  # 0
            None               # 1
        ]
        """
        self.table = [None] * size
        self.count = 0

    def insert(self, key, value):
        index = self._hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size  # when a collision occurs, use the next index to find an empty slot
        self.table[index] = (key, value)
        self.count += 1
        load_factor = self.count / self.size
        if load_factor > 0.75:
            self._rehash()

    def get(self, key):
        index = self._hash_function(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start_index:
                break
        raise KeyError(key)  # Built-in python exception

    def _hash_function(self, key):
        return hash(key) % self.size

    def _rehash(self):
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0
        for item in old_table:
            if item is not None:
                self.insert(item[0], item[1])
