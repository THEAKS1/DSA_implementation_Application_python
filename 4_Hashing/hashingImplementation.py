# Implementing Hash Table 

class HashTable():
    def __init__(self):
        self.max_size = 100
        self.hTable = [None for _ in range(self.max_size)]

    # Implementing hash function to get index
    def get_hash_index(self, key):
        intermediateSum = 0
        for i in key:
            intermediateSum += ord(i)
        return (intermediateSum % self.max_size)
        
    # Add a (key, value) pair using syntax same as that in dict
    def __setitem__(self, key, value):
        hash_index = self.get_hash_index(key)
        self.hTable[hash_index] = value

    # Access a key using syntax same as that in dict
    def __getitem__(self, key):
        hash_index = self.get_hash_index(key)
        return self.hTable[hash_index]

    # Delete a key using del keyword followed by dict syntax
    def __delitem__(self, key):
        hash_index = self.get_hash_index(key)
        self.hTable[hash_index] = None
