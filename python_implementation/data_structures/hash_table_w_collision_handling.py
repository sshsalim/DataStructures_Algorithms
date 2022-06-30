''' Hash table implementation for 10 elements by default'''

# With collisions handling
class hash_table():
    def __init__(self, number = 10, arr = None):
        self.number = number
        self.arr = [[] for i in range(0, number)]

    def __setitem__(self, key, value):
        h = self.hash_function(key)

        flag = False
        for i, val in enumerate(self.arr[h]):
            if len(val) == 2 and val[0] == key:
                self.arr[h].append((key, value))
                flag = True
            break

        if not flag:
            self.arr[h].append((key, value))

    def __getitem__(self, item):
        h = self.hash_function(item)

        if len(self.arr[h]) > 1:
            for val in self.arr[h]:
                if val[0] == key:
                    return val[1]
        else:
            return self.arr[h]

    def __delitem__(self, key):
        h = self.hash_function(key)

        for i, val in enumerate(self.arr[h]):
            if val[0] == key:
                self.arr[h][1] = None

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

    # Collision
    HT['06.02.1994'] = 'Winter'

    print(HT.arr)