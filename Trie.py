class Node:
    def __init__(self, val=''):
        self.__value = val
        self.__children = dict()

    def __str__(self):
        return str(self.__children)

    def __repr__(self):
        return self.__str__()

    def has_child(self, child):
        return child in self.__children

    def add_child(self, child):
        self.__children[child] = Node(child)

    def get_child(self, child):
        return self.__children[child]

    @property
    def get_value(self):
        return self.__value

    @property
    def chill(self):
        return self.__children

    def get_str(self, string=''):
        if self.__value == '$':
            return [string]
        else:
            arr = []
            for i in self.__children:
                # arr += self.children[i].get_str(string + self.value)
                child = self.__children[i]
                child_string = child.get_str(string + self.__value)
                arr = arr + child_string
            return arr


class Trie:
    def __init__(self):
        self.root = Node()

    def check_word(self, query):
        query += '$'
        current_node = self.root
        for letter in query:
            if current_node.has_child(letter):
                current_node = current_node.get_child(letter)
            else:
                return False
        return True

    def get_str(self, query=''):
        current_node = self.root
        for letter in query:
            letter = letter.lower()
            if current_node.has_child(letter):
                current_node = current_node.get_child(letter)
            else:
                return None
        return current_node.get_str(query[:-1])

    def insert(self, text):
        text += '$'
        current_node = self.root
        for letter in text:
            if letter.isalnum():
                letter = letter.lower()
                if not current_node.has_child(letter):
                    current_node.add_child(letter)
                current_node = current_node.get_child(letter)
            else:
                letter = '$'
                if not current_node.has_child(letter):
                    current_node.add_child(letter)
                current_node = self.root


def contacts(queries):
    if queries is None:
        return 0
    return len(queries)
