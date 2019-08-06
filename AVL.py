class Node:
    def __init__(self, value):
        self.__value = value
        self.__parent = None
        self.__left_child = None
        self.__right_child = None

    @property
    def value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    @property
    def has_parent(self):
        if self.__parent is None or self is None:
            return False
        return True

    @property
    def get_left(self):
        return self.__left_child

    @property
    def get_right(self):
        return self.__right_child

    def is_left_child(self):
        if self.get_parent is not None:
            if self.get_parent.__get_left.value == self.value:
                return True
            return False

    @property
    def get_parent(self):
        if not self.has_parent:
            return None
        return self.__parent

    @property
    def get_children(self):
        if self:
            children = [self.get_left, self.get_right]
            return children

    def set_child(self, child):
        if child.value > self.value:
            if self.get_right is None:
                self.__right_child = child
                child.set_parent(self)
                print('{} right of {}'.format(child.value, self.value))
                return True, True
            else:
                return False, 'right'
        else:
            if self.get_left is None:
                self.__left_child = child
                child.set_parent(self)
                print('{} left of {}'.format(child.value, self.value))
                return True, None
            else:
                return False, 'left'

    def set_parent(self, parent):
        self.__parent = parent

    def unset_parent(self):
        if self.value < self.get_parent.value:
            self.get_parent.left_child = None
        else:
            self.get_parent.right_child = None
        self.__parent = None

    # Not done yet
    # def delete_node(self):
    #     # Check child
    #     # if children
    #     # check if right child, set parent of node to parent of right child
    #     # else if only left child, and set ,,,
    #     if self.left_child is not None or self.right_child is not None:
    #         if self.right_child is not None:
    #             self.right_child.set_parent(self.get_parent())
    #             self.unset_parent()
    #             self.right_child.left_child = self.left_child
    #     else:
    #         if self.left_child is not None:
    #             self.left_child.set_parent(self.get_parent())
    #             self.unset_parent()
    #
    #     print('deleted Node({})'.format(self.value))
    #     del self.value


class BinaryTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insert_node(self, node, parent=None):
        if self.root is None:
            self.root = Node(node)
            print('done', self.root.value, self.root.get_right)
        elif parent is not None:
            result, action = parent.set_child(Node(node))
            if action and result:
                pass
            elif not result:
                if action == 'right':
                    return self.insert_node(node, parent.get_right)
                else:
                    return self.insert_node(node, parent.get_left)
        else:
            return self.insert_node(node, self.root)

    def search_tree(self, node, current=None):
        if self.root is None:
            return 'Tree is empty'
        elif self.root.value == node:
            return self.root
        elif current is not None:
            if node == current.value:
                print('{} found as a child of {}'.format(node, current.get_parent.value))
                return current
            elif node <= current.value:
                return self.search_tree(node, current.get_left)
            elif node > current.value:
                return self.search_tree(node,  current.get_right)
            else:
                return 'Not found'
        else:
            return self.search_tree(node, self.root)


arr = [20, 40, 30, 10, 10, 32]
Tree = BinaryTree()
for i in arr:
    Tree.insert_node(i)
# Tree.del_node(10)
Tree.insert_node(5)
c = Tree.search_tree(30)
print(c.value)
