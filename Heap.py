# Coming back here for adjustment
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.sorted = False

    def heaped(self):
        self.sorted = True

    def value(self):
        return self.value

    def set_value(self, value):
        self.value = value


class Heap(Node):
    def __init__(self):
        self.root = None
        self.heap_array = []
        self.heap = []
        self.index = 1
        super().__init__(self)

    def insert_node(self, node):
        if self.root is None:
            self.root = Node(node)
            self.heap.append(self.root)
            self.root.set_value(node)
            self.heap_array.append(self.root.value)
            self.index += 1
        else:
            if self.index % 2 == 0:
                j = int(self.index / 2) - 1
                self.heap[j].left = Node(node)
                self.heap[j].left.set_value(node)
                self.heap.append(self.heap[j].left)
                self.heap_array.append(self.heap[j].left.value)
                self.index += 1
            else:
                j = int(self.index / 2) - 1
                self.heap[j].right = Node(node)
                self.heap[j].right.set_value(node)
                self.heap.append(self.heap[j].right)
                self.heap_array.append(self.heap[j].right.value)
                self.index += 1

    def return_heap(self):
        return self.heap

    def return_heap_array(self):
        return self.heap_array

    def min_heapify(self, array, node):
        k = node - 1
        if self.heap[k].left is not None:
            if self.heap[k].left.value < self.heap[k].value:
                if self.heap[k].right is not None:
                    if self.heap[k].left.value < self.heap[k].right.value or self.heap[k].right.sorted is False:
                        if self.heap[k].left.sorted is False:
                            temp1 = self.heap[k].value
                            temp2 = array[k]
                            k_to_swap = (k + 1) * 2
                            array[k] = array[k_to_swap - 1]
                            array[k_to_swap - 1] = temp2
                            self.heap[k].set_value(self.heap[k].left.value)
                            self.heap[k].left.set_value(temp1)
                            return self.min_heapify(array, ((k + 1) * 2))
                else:
                    if self.heap[k].left.sorted is False:
                        temp1 = self.heap[k].value
                        temp2 = array[k]
                        k_to_swap = (k + 1) * 2
                        array[k] = array[k_to_swap - 1]
                        array[k_to_swap - 1] = temp2
                        self.heap[k].set_value(self.heap[k].left.value)
                        self.heap[k].left.set_value(temp1)

        if self.heap[k].right is not None:
            if self.heap[k].right.value < self.heap[k].value:
                if self.heap[k].right.value < self.heap[k].left.value and self.heap[k].right.sorted is False:
                    temp = self.heap[k].value
                    temp2 = array[k]
                    k_to_swap = ((k + 1) * 2) + 1
                    array[k] = array[k_to_swap - 1]
                    array[k_to_swap - 1] = temp2
                    self.heap[k].set_value(self.heap[k].right.value)
                    self.heap[k].right.set_value(temp)
                    return self.min_heapify(array, ((k + 1) * 2) + 1)

        return array

    def max_heapify(self, array, node):
        k = node - 1
        if self.heap[k].left is not None:
            if self.heap[k].left.value > self.heap[k].value:
                if self.heap[k].right is not None:
                    if self.heap[k].left.value > self.heap[k].right.value or self.heap[k].right.sorted is True:
                        if self.heap[k].left.sorted is False:
                            temp1 = self.heap[k].value
                            temp2 = array[k]
                            k_to_swap = (k + 1) * 2
                            array[k] = array[k_to_swap - 1]
                            array[k_to_swap - 1] = temp2
                            self.heap[k].set_value(self.heap[k].left.value)
                            self.heap[k].left.set_value(temp1)
                            return self.max_heapify(array, ((k + 1) * 2))
                else:
                    if self.heap[k].left.sorted is False:
                        temp1 = self.heap[k].value
                        temp2 = array[k]
                        k_to_swap = (k + 1) * 2
                        array[k] = array[k_to_swap - 1]
                        array[k_to_swap - 1] = temp2
                        self.heap[k].set_value(self.heap[k].left.value)
                        self.heap[k].left.set_value(temp1)

        if self.heap[k].right is not None:
            if self.heap[k].right.value > self.heap[k].value:
                if self.heap[k].right.value > self.heap[k].left.value:
                    if self.heap[k].right.sorted is False:
                        temp = self.heap[k].value
                        temp2 = array[k]
                        k_to_swap = ((k + 1) * 2) + 1
                        array[k] = array[k_to_swap - 1]
                        array[k_to_swap - 1] = temp2
                        self.heap[k].set_value(self.heap[k].right.value)
                        self.heap[k].right.set_value(temp)
                        return self.max_heapify(array, ((k + 1) * 2) + 1)

        return array

    def build_max_heap(self, array):
        start = int(len(self.heap) / 2)

        while start > 0:
            self.max_heapify(array, start)
            start -= 1

        return array

    def heap_sort(self, array):
        for i in array:
            self.insert_node(i)
        array = self.build_max_heap(array)
        length = len(array)
        while length > 1:
            temp = array[0]
            temp_heap = self.heap[0].value
            h_l = length - 1
            array[0] = array[length - 1]
            self.heap[0].set_value(self.heap[h_l].value)
            array[length - 1] = temp
            self.heap[h_l].set_value(temp_heap)
            self.heap[h_l].heaped()
            array = self.max_heapify(array, 1)
            length -= 1
        return array


# arr = [4, 1, 3, 20, 16, 9, 10, 14, 8, 7, 0]
# arr = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
# arr = [5, 4, 8, 2, 1, 6]
arr = [2, 1, 3, 4, 6, 5]
heap = Heap()
heap.heap_sort(arr)
print(arr)
