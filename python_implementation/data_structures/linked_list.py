''' Linked list implemetation with basic operations in python'''

class node():
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class linked_list():
    def __init__(self):
        self.start = None

    def insert_at_start(self, element):
        Node = node(element, self.start)
        self.start = Node

    def display_linked_list(self):

        # check if the list is empty
        if self.start == None:
            print("Empty linked list.")
            return

        idx = self.start
        idx_element = ""
        while idx:
            idx_element += str(idx.value) + "--->"
            idx = idx.next

        print(idx_element)

    def get_length(self):
        count = 0

        idx = self.start
        while idx:
            idx = idx.next
            count += 1

        return count

    def insert_at_end(self, element):
        if self.start == None:
            Node = node(element, self.next)
            self.start = Node
            return

        idx = self.start
        while idx.next:
            idx = idx.next

        idx.next = node(element, None)

    def insert_between(self, index, element):
        if index < 0 or index > (int(self.get_length()) -1):
            raise Exception("Index out of bounds.")

        if self.start == None:
            self.insert_at_start(element)
            return

        if int(self.get_length()) - 1 == index:
            self.insert_at_end(element)
            return

        else:
            idx = self.start
            count = 0
            while idx:

                if count == index-1:
                    Node = node(element, idx.next)
                    idx.next = Node

                count += 1
                idx = idx.next

    def deletion_index(self, index):
        if index < 0 or index > (int(self.get_length()) -1):
            raise Exception("Index out of bounds.")

        idx = self.start
        count = 0
        while idx:
            if count == index - 1:
                idx.next = idx.next.next
                break
            idx = idx.next
            count += 1
        return

if __name__ == "__main__":

    # class object instantiation
    l1 = linked_list()

    # insert at start
    l1.insert_at_start(5)
    l1.insert_at_start(6)

    # insert at end
    l1.insert_at_end(23123)
    l1.insert_at_end(25)

    # insert between with index
    l1.insert_between(2, 444)

    l1.display_linked_list()

    # get the length of the list
    print(l1.get_length())

    l1.display_linked_list()

    # deletion in between
    l1.deletion_index(3)

    l1.display_linked_list()
