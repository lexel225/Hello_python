
class Vertex:

    def __init__(self, val, color=0, next_vertex=None):
        self.key = val
        self.color = color
        self.next = next_vertex


class Graph:
    '''
    [vertex_0] -> vertex_1 -> vertex_2
    [vertex_1] -> vertex_0 -> vertex_3 -> vertex_4
    [vertex_2] -> vertex_0 -> vertex_5 -> vertex_6
    [vertex_3] -> vertex_1
    [vertex_4] -> vertex_1
    [vertex_5] -> vertex_2
    [vertex_6] -> vertex_2
    '''
    graph_list = []

    def __init__(self):

        vertex_0 = Vertex(0)
        vertex_1 = Vertex(1)
        vertex_2 = Vertex(2)
        vertex_3 = Vertex(3)
        vertex_4 = Vertex(4)
        vertex_5 = Vertex(5)
        vertex_6 = Vertex(6)

        self.graph_list.append([vertex_1, vertex_2])
        self.graph_list.append([vertex_0, vertex_3, vertex_4])
        self.graph_list.append([vertex_0, vertex_5, vertex_6])
        self.graph_list.append([vertex_1])
        self.graph_list.append([vertex_1])
        self.graph_list.append([vertex_2])
        self.graph_list.append([vertex_2])

    def printGraph(self):
        i = 0

        for vertex_list in self.graph_list:
            print('Vertext_{}: {}'.format(i, [vertex.key for vertex in vertex_list]))
            i += 1



if __name__ == '__main__':

    graph = Graph()

    graph.printGraph()
