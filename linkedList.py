
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.previous = None


class SingleLinkedListed:
    def __init__(self):
        self.head = None
        self.current = None

    def insert_node(self, node):
        if self.head is None:
            self.head = Node(node)
            self.current = self.head
        else:
            new_node = Node(node)
            new_node.previous = self.current
            self.current.next = new_node
            self.current = new_node

    def print_list(self):
        if self.head is None:
            return None
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.next

    def delete_node(self, position):
        if self.head is None:
            return None
        else:
            index = 1
            current = self.head
            while current:
                if index == (position - 1):
                    current.next = current.next.next
                    current.next.previous = current
                    break
                index += 1
                current = current.next

    def reset(self, position):
        if self.value is None:
            return None
        else:
            index = 1
            running = True
            current = self.value
            while running:
                if current.data == position:
                    print("Found equality: {} and {}".format(current.data, position))
                    if index == position:
                        pass
                        running = False
                    else:
                        while index <= position:
                            print("initial current {} and current.next {}".format(current.data, current.next.data))
                            first = current
                            current = current.next
                            current.next = first
                            print("final current {} and current.next {}".format(current.data, current.next.data))
                            running = False
                            index += 1
                index += 1
                current = current.next


li = SingleLinkedListed()
li.insert_node(1)
li.insert_node(2)
li.insert_node(3)
li.insert_node(4)
li.insert_node(5)
li.insert_node(6)
li.insert_node(7)
li.delete_node(7)
li.print_list()
