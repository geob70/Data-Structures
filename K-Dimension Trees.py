class Node:
    def __init__(self):
        self.__level = None
        self.__parent = None
        self.__value = None
        self.__right = None
        self.__left = None

    @property
    def level(self):
        return self.__level

    @property
    def value(self):
        return self.__value

    @property
    def right_child(self):
        return self.__right

    @property
    def left_child(self):
        return self.__left

    @property
    def parent(self):
        return self.__parent

    def set_value(self, child, index, parent=None):
        self.__value = child
        self.__level = index
        self.__parent = parent

    def set_right(self, node):
        self.__right = node

    def set_left(self, node):
        self.__left = node

    def sort_key(self, value):
        return value[self.level]

    def delete(self):
        del self


class KDTrees:
    def __init__(self, dimension):
        self.__dimension = dimension
        self.root = None

    def insert(self, node, parent=None):
        if self.root is None:
            self.root = Node()
            self.root.set_value(node, 0)
        elif parent is not None:
            index = parent.level
            if node[index] <= parent.value[index]:
                if parent.left_child is None:
                    parent.set_left(Node())
                    if (index + 1) == self.__dimension:
                        index = -1
                    parent.left_child.set_value(node, index + 1, parent)
                else:
                    return self.insert(node, parent.left_child)
            elif node[index] > parent.value[index]:
                if parent.right_child is None:
                    parent.set_right(Node())
                    if (index + 1) == self.__dimension:
                        index = -1
                    parent.right_child.set_value(node, index + 1, parent)
                else:
                    return self.insert(node, parent.right_child)
        else:
            self.insert(node, self.root)

    def search(self, node, query=None, position=None):
        if query is None and position is None:
            if node == self.root.value:
                print('found at {} on level {}'.format(self.root.value, self.root.level))
                return self.root, None, position
            else:
                index = self.root.level
                if node[index] <= self.root.value[index]:
                    return self.search(node, self.root.left_child, 'left')
                else:
                    return self.search(node, self.root.right_child, 'right')
        elif query:
            if node == query.value:
                print('found at {} on level {}'.format(query.value, query.level))
                return query, query.parent, position
            else:
                index = query.level
                if node[index] <= query.value[index]:
                    return self.search(node, query.left_child, 'left')
                else:
                    return self.search(node, query.right_child, 'right')
        return None, None, None

    def delete(self, node, query=None, position=None):
        node, parent, position = self.search(node, query, position)
        if node is not None:
            if node.right_child is not None:
                arr = []
                kd.subtree_search(node.right_child, arr)
                arr.sort(key=node.sort_key, reverse=True)
                minimum = arr[len(arr) - 1]
                node.set_value(minimum, node.level)
                return self.delete(minimum, node.right_child, 'right')
            elif node.left_child is not None:
                arr = []
                kd.subtree_search(node.left_child, arr)
                arr.sort(key=node.sort_key)
                minimum = arr[len(arr) - 1]
                node.set_value(minimum, node.level)
                return self.delete(minimum, node.left_child, 'left')
            else:
                if position == 'left':
                    node.delete()
                    parent.set_left(None)
                else:
                    parent.set_right(None)
                    node.delete()
        else:
            print('What you want to delete does not exist')

    def subtree_search(self, node, arr):
        if node is None:
            return
        arr.append(node.value)
        self.subtree_search(node.right_child, arr)
        self.subtree_search(node.left_child, arr)

    def printout(self, node, space):
        if node is not None:
            space += 10
            self.printout(node.right_child, space)
            for j in range(10, space):
                print(end=" ")
            print(node.value)
            self.printout(node.left_child, space)


if __name__ == '__main__':
    d = int(input("Enter Tree Dimension: "))
    # j = [[51, 75], [25, 40], [70, 70], [10, 30], [35, 90], [55, 1], [60, 80], [1, 10], [50, 50]]
    kd = KDTrees(d)
    # for i in j:
    #     kd.insert(i)
    n = int(input())
    for i in range(n):
        nodes = list(map(int, input('Enter {}-D item: '.format(d)).rstrip().split()))
        kd.insert(nodes)
    kd.printout(kd.root, 0)
    for m in range(3):
        t = list(map(int, input('Delete: ').rstrip().split()))
        kd.delete(t)
    kd.printout(kd.root, 0)
