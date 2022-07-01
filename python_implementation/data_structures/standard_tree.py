''' General tree implementation in python '''


class stdTree():
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def add_child_node(self, child):
        child.parent = self
        self.children.append(child)

    def display_tree(self):

        lvl = self.tree_level()
        prefix = "---" * (int(lvl) * 3) if self.parent else "|"
        print(prefix + str(self.value))

        if self.children != []:
            for child in self.children:
                child.display_tree()

    def tree_level(self):
        element = self.parent
        level = 0
        while element:
            level += 1
            element = element.parent

        return level

def build_tree():

    root =  stdTree("Vehicles")

    cars = stdTree("Cars")
    cars.add_child_node(stdTree("VW"))
    cars.add_child_node(stdTree("Mercedes"))
    cars.add_child_node(stdTree("Audi"))

    trucks = stdTree("Trucks")
    trucks.add_child_node(stdTree("MAN"))
    trucks.add_child_node(stdTree("Volvo"))

    root.add_child_node(cars)
    root.add_child_node(trucks)
    return root

if __name__ == "__main__":

    # default tree for vehicles
    def_tree = build_tree()

    # display
    stdTree.display_tree(def_tree)



