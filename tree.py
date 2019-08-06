class Node:
    def __init__(self, value):
        self.__value = value
        self.__parent = None
        self.__children = set()

    @property
    def value(self):
        return self.__value

    @property
    def parent(self):
        return self.__parent

    @property
    def children(self):
        for child in self.__children:
            yield child

    @property
    def children_count(self):
        return len(self.__children)

    @property
    def has_parent(self):
        return self.parent is not None

    def _set_value(self, value):
        self.__value = value

    def has_child(self, child):
        return child in self.__children

    def __set_parent(self, parent):
        if self.has_parent:
            self.parent.remove_child(self)
        self.__parent = parent

    def __unset_parent(self):
        self.__parent = None

    def add_child(self, child):
        child.__set_parent(self)
        self.__children.add(child)

    def remove_child(self, child):
        child.__unset_parent()
        self.__children.remove(child)

