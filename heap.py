import random

class HeapNode:

    def __init__(self, key):
        self.key = key

class Heap:

    def __init__(self, heap_length):

        self.HeapArray = [None]

        for i in random.sample(range(1,100), heap_length):
            self.HeapArray.append(HeapNode(i))

        self.heap_length = heap_length
    
    def swap(self, i, j):
        tmp = self.HeapArray[i]
        self.HeapArray[i] = self.HeapArray[j]
        self.HeapArray[j] = tmp
 
    def MinHeapify(self, i):
        left = 2*i
        right = 2*i + 1

        smallest = i

        if left <= self.heap_length and self.HeapArray[left].key < self.HeapArray[smallest].key:
            smallest = left
        
        if right <= self.heap_length and self.HeapArray[right].key < self.HeapArray[smallest].key:
            smallest = right
        
        if smallest != i:
            self.swap(i, smallest)
            self.MinHeapify(smallest)


    def BuildMinHeapify(self):
        for i in range(self.heap_length//2, 0, -1):
            self.MinHeapify(i)

    
    def isMinHeap(self):
        for i in range(1, self.heap_length//2):
            root = self.HeapArray[i].key
            left = self.HeapArray[2*i].key
            right = self.HeapArray[2*i + 1].key
            
            if root > left or root > right:
                print("Not Min Heap!")
                return False
        
        print("It's Min Heap")
        return True

    def printHeap(self):
        for i in range(1, self.heap_length + 1):
            print(f'[{i}]: {self.HeapArray[i].key}')


if __name__ == '__main__':

    heap = Heap(10)

    heap.BuildMinHeapify()
    heap.isMinHeap()
    heap.printHeap()
        