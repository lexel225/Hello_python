
class HeapNode:

    def __init__(self, key):
        self.key = key

class Heap:

    def __init__(self, num_of_nodes):

        self.HeapArray = [None]

        for i in range(1, num_of_nodes + 1):
            self.HeapArray.append(HeapNode(i))
        
        self.num_of_nodes = num_of_nodes
    
    def swap(self, i, j):
        tmp = self.HeapArray[i]
        self.HeapArray[i] = self.HeapArray[j]
        self.HeapArray[j] = tmp
 
    def MinHeapify(self):
        for i in range(1, self.num_of_nodes//2 ):
            root = self.HeapArray[i].key
            left = self.HeapArray[2*i].key
            right = self.HeapArray[2*i + 1].key

            if root < left and root < right:
                continue
            elif root > left and root < right:
                self.swap(i, 2*i)
                continue
            elif root > right and root < left:
                self.swap(i, 2*i + 1)
            else:
                if right > left:
                    self.swap(i, 2*i)
                else:
                    self.swap(i, 2*i + 1)
    
    def isMinHeap(self):
        for i in range(1, self.num_of_nodes//2):
            root = self.HeapArray[i].key
            left = self.HeapArray[2*i].key
            right = self.HeapArray[2*i + 1].key
            
            if root > left or root > right:
                print("Not Min Heap!")
                return False
        
        print("It's Min Heap")
        return True

    def printHeap(self):
        for i in range(1, self.num_of_nodes + 1):
            print(self.HeapArray[i].key)




if __name__ == '__main__':

    heap = Heap(10)

    heap.MinHeapify()
    heap.isMinHeap()
    heap.printHeap()
        
            




