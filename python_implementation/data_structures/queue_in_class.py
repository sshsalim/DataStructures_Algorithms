# Queue in python

class que():
    def __init__(self):
        self.arr = [1, 2, 3, 4 ,5 ,6, 7, 8, 9, 10]
        self.limit = len(self.arr)
        self.n_of_elements = 0

    def push(self, elementInsert):
        self.arr.append(elementInsert)
        return self.arr

    def pop(self):
        # In theory this is not reqiured
        self.arr[0] = []

        self.n_of_elements -= 1

        return  self.arr

    def top(self):
        return self.arr[0]

if __name__ == '__main__':

    Que = que()

    '''Example of each case'''


    # Top example
    print("\nGiven buffer in Queue: ", Que.arr)
    print("Top result:")
    print(Que.top())

    # Pop example
    print("\nGiven buffer in Queue: ", Que.arr)
    print("Pop result:")
    print(Que.pop())

    # Push example (element 11)
    print("\nGiven buffer in Queue: ", Que.arr)
    print("Push element 11 result:")
    print(Que.push(11))




