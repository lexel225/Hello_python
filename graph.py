
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
    [vertex_6] -> vertex_2 -> vertex_6
    '''
    vertexs = []
    graph_list = []

    def __init__(self):

        for i in range(7):
            self.vertexs.append(Vertex(i))

        self.graph_list.append([(self.vertexs[1], 1), (self.vertexs[2], 2)])
        self.graph_list.append([(self.vertexs[0], 3), (self.vertexs[3], 4), (self.vertexs[4], 5)])
        self.graph_list.append([(self.vertexs[0], 6), (self.vertexs[5], 7), (self.vertexs[6], 8)])
        self.graph_list.append([(self.vertexs[1], 9), (self.vertexs[4], 10)])
        self.graph_list.append([(self.vertexs[1], 11), (self.vertexs[3], 12), (self.vertexs[5], 13)])
        self.graph_list.append([(self.vertexs[2], 14), (self.vertexs[4], 15), (self.vertexs[6], 16)])
        self.graph_list.append([(self.vertexs[2], 17), (self.vertexs[5], 18)])

    def printGraph(self):
        i = 0

        for vertex_list in self.graph_list:
            print('Vertext_{}: {}'.format(i, [(vertex.key,weight) for vertex,weight in vertex_list]))
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

            for vertex,_ in self.graph_list[vertex_index]:
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

        self.time = 0
        discover = [None] * len(self.vertexs)
        finish = [None] * len(self.vertexs)
        predecessor = [None] * len(self.vertexs)

        def DFSVisit(self, v_idx, predecessor_idx):

            if self.vertexs[v_idx].color != WHITE:
                return

            self.vertexs[v_idx].color = GRAY
            discover[v_idx] = self.time
            self.time += 1
            predecessor[v_idx] = predecessor_idx

            for vertex,_ in self.graph_list[v_idx]:
                DFSVisit(self, vertex.index, v_idx)
            self.vertexs[v_idx].color = BLACK
            finish[v_idx] = self.time
            self.time += 1
        
        DFSVisit(self, start, None)

        print(f'DFS start from vertex_{start}')
        print(f'discover: {discover}')
        print(f'predecessor: {predecessor}')
        print(f'finish: {finish}')

    def Dijkstra(self, start):
        
        ready = []

        distance = [None] * len(self.graph_list)
        predecessor = [None] * len(self.graph_list)

        


if __name__ == '__main__':

    graph = Graph()

    graph.printGraph()

    #graph.BFS(0)
    #graph.BFS(6)

    graph.DFS(6)
