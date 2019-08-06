"""
    frequency of characters in the text
"""


class Node:
    def __init__(self):
        self.freq = None
        self.right = None
        self.left = None

    def set_right(self, val):
        self.right = val

    def set_left(self, val):
        self.left = val

    def set_freq(self, val):
        self.freq = val

    @property
    def get_right(self):
        return self.right

    @property
    def get_left(self):
        return self.left

    @property
    def get_weight(self):
        return self.freq


class Huffman:
    def __init__(self):
        self.root = None
        self.letters = set()
        self.ascii = dict()
        self.frequency = dict()

    def set_frequency(self, text):
        for i in text:
            self.letters.add(i)
            if i in self.frequency.keys():
                self.frequency[i] += 1
            else:
                self.frequency[i] = 1

    def build_tree(self, current=None):
        freq = []
        for i in self.frequency:
            freq.append(self.frequency[i])
        nodes = sorted(self.frequency, key=self.frequency.get, reverse=True)
        freq.sort(reverse=True)

        if len(freq) > 1:
            node_a, freq_a = nodes.pop(), freq.pop()
            node_b, freq_b = nodes.pop(), freq.pop()

            # print(node_a, node_b)

            del self.frequency[node_a]
            del self.frequency[node_b]

            head = Node()
            head.set_freq(freq_a + freq_b)
            head.set_left(node_a)
            head.set_right(node_b)

            self.frequency[head] = head.get_weight
            return self.build_tree(head)
        else:
            self.root = current

    def transverse(self, node, path):
        if node:
            if node in self.letters and node is not None:
                self.ascii[node] = int(path)
            else:
                self.transverse(node.get_left, path + '0')
                self.transverse(node.get_right, path + '1')


if __name__ == '__main__':
    text = input()
    huffman = Huffman()
    stack = []
    huffman.set_frequency(text)
    huffman.build_tree()
    huffman.transverse(huffman.root, '')
    print(huffman.ascii)
    # print(huffman.root.get_left.get_left)
#