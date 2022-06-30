# Stack in python

class stack():
    def __init__(self):
        self.arr = [1, 2, 3, 4 ,5 ,6, 7, 8, 9, 10]
        self.limit = len(self.arr)
        self.n_of_elements = 0

    def push(self, elementInsert):
        self.arr[self.n_of_elements] = elementInsert
        self.n_of_elements += 1
        return self.arr

    def pop(self):
        # In theory this is not reqiured
        self.arr[(self.n_of_elements) - 1] = 0

        self.n_of_elements -= 1

        return  self.arr

    def top(self):
        return self.arr[self.n_of_elements - 1]

if __name__ == '__main__':

    stack = stack()

    '''Example of each case'''


    # Top example
    print("\nGiven buffer in stack: ", stack.arr)
    print("Top result:")
    print(stack.top())

    # Pop example
    print("\nGiven buffer in stack: ", stack.arr)
    print("Pop result:")
    print(stack.pop())

    # Push example (element 11)
    print("\nGiven buffer in stack: ", stack.arr)
    print("Push element 11 result:")
    print(stack.push(11))




