class Vertex:
    def __init__(self, value):
        self.__value = value
        self.__edges = set()
        self.isVisited = False

    def visit(self):
        return self.isVisited is True

    def edges(self, edge):
        edge.__edges.add(self)
        return self.__edges.add(edge)


class Graph:
    def __init__(self, name):
        self.__name = name
        self.__vertices = set()
        self.__edges = dict()

    def get_name(self):
        return self.__name

    def add_vertex(self, value):
        self.__vertices.add(value)

    def get_vertices(self):
        return self.__vertices

    def get_edge(self):
        return self.__edges

    def is_vertices_empty(self):
        if len(self.__vertices) == 0:
            return True
        else:
            return False

    # Directed graph edges
    def add_edges(self, v1, v2, edge):
        if self.is_vertices_empty():
            print('Vertices is Empty')
        else:
            if v1 in self.__vertices and v2 in self.__vertices:
                if (v1, v2) not in self.__edges:
                    self.__edges[(v1, v2)] = edge
                else:
                    print('Edge ({}, {}) already exist'.format(v1, v2))
            else:
                print('Vertex {} or {} does not exist'.format(v1, v2))

    def degree_of_vertex(self, vertex):
        count = 0
        if vertex in self.__vertices:
            for i in self.__edges.keys():
                if vertex in i[0]:
                    count += 1
            return count
        else:
            return '{} is not a vertex in graph {}'.format(vertex, self.get_name())

    # Undirected graph edges
    # def add_edges(self, v1, v2):
    #     if self.is_vertices_empty():
    #         print('Vertices is empty')
    #     else:
    #         if v1 in self.__vertices and v2 in self.__vertices:
    #             if (v1, v2) not in self.__edges:
    #                     self.__edges[v1] = v2
    #             else:
    #                 print('Edge already exist')
    #         else:
    #             print('Vertex {} or {} does not exist'.format(v1, v2))

    def clear_edges(self):
        return self.__edges.clear()
