''' Hash table implementation for 10 elements by default'''

# Without collisions handling
class hash_table():
    def __init__(self, number = 10, arr = None):
        self.number = number
        self.arr = [None for i in range(0, number)]

    def __setitem__(self, key, value):
        h = self.hash_function(key)
        self.arr[h] = value

    def __getitem__(self, item):
        h = self.hash_function(item)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.hash_function(key)
        self.arr[h] = None

    def hash_function(self, key):
        i = 0
        for idx in key:
            i += ord(idx)
        return i % self.number

if __name__ == "__main__":
    HT = hash_table()

    # Maps dates to days
    HT['01.02.2022'] = 'Monday'
    HT['06.02.1994'] = 'Wednesday'

    print(HT.arr)
    print(HT['06.02.1994'])