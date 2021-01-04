
WHITE = 0
GRAY = 1
BLACK = 2


class Vertex:

    def __init__(self, val, color=WHITE, next_vertex=None):
        self.key = val
        self.index = val
        self.color = color
        self.next = next_vertex


class Graph:
    '''
    [vertex_0] -> vertex_1 -> vertex_2
    [vertex_1] -> vertex_0 -> vertex_3 -> vertex_4
    [vertex_2] -> vertex_0 -> vertex_5 -> vertex_6
    [vertex_3] -> vertex_1 -> vertex_4
    [vertex_4] -> vertex_1 -> vertex_3 -> vertex_5
    [vertex_5] -> vertex_2 -> vertex_4 -> vertex_6
    [vertex_6] -> vertex_2 -> vertext_6
    '''
    vertexs = []
    graph_list = []

    def __init__(self):

        for i in range(7):
            self.vertexs.append(Vertex(i))

        self.graph_list.append([self.vertexs[1], self.vertexs[2]])
        self.graph_list.append([self.vertexs[0], self.vertexs[3], self.vertexs[4]])
        self.graph_list.append([self.vertexs[0], self.vertexs[5], self.vertexs[6]])
        self.graph_list.append([self.vertexs[1], self.vertexs[4]])
        self.graph_list.append([self.vertexs[1], self.vertexs[3], self.vertexs[5]])
        self.graph_list.append([self.vertexs[2], self.vertexs[4], self.vertexs[6]])
        self.graph_list.append([self.vertexs[2], self.vertexs[5]])

    def printGraph(self):
        i = 0

        for vertex_list in self.graph_list:
            print('Vertext_{}: {}'.format(i, [vertex.key for vertex in vertex_list]))
            i += 1

    def clearGraph(self):
        for vertex in self.vertexs:
            vertex.color = WHITE

    def BFS(self, start):
        self.clearGraph()

        queue = []
        distance = [None] * len(self.graph_list)
        predecessor = [None] * len(self.graph_list)

        def enquene(queue, vertex_idx):
            if vertex_idx is not None:
                queue.append(vertex_idx)

        distance_count = 0

        predecessor[start] = None
        distance[start] = distance_count
        self.vertexs[start].color = BLACK
        enquene(queue, start)

        while len(queue) > 0:
            vertex_index = queue.pop(0)

            for vertex in self.graph_list[vertex_index]:
                if vertex.color == BLACK:
                    continue
                else:
                    idx = vertex.index
                    distance[idx] = distance[vertex_index] + 1
                    predecessor[idx] = vertex_index
                    vertex.color = BLACK
                    print(f'vertex_{vertex_index} enqueue vertex_{idx}')
                    enquene(queue, idx)

        print(f'BFS start from vertex_{start}')
        print(f'distance: {distance}')
        print(f'predecessor: {predecessor}')


    def DFS(self, start):
        self.clearGraph()

        def DFSVisit(self, v_idx):

            if self.vertexs[v_idx].color != WHITE:
                return

            self.vertexs[v_idx].color = GRAY
            discover[v_idx] = time
            time += 1

        time = 0
        discover = [None] * len(self.vertexs)
        finish = [None] * len(self.vertexs)
        predecessor = [None] * len(self.vertexs)

        discover[start] = time
        predecessor[start] = None







            





            




if __name__ == '__main__':

    graph = Graph()

    graph.printGraph()

    #graph.BFS(0)
    #graph.BFS(6)

    graph.DFS()
