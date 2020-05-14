class Heap(object):
    

    def __init__(self, comparation):
        self.heap = []
        self.comparation = comparation
        self.heapSize = 0

    def __validate_insert(self, newIndex):  
        parentIndex = (newIndex-1)/2 

        if self.comparation(self.heap[newIndex],self.heap[parentIndex]):
            self.heap[newIndex], self.heap[parentIndex] = self.heap[parentIndex], self.heap[newIndex]
            self.__validate_insert(parentIndex)

    def insert(self, data):
        self.heap.append(data)
        self.heapSize += 1
        
        if(len(self.heap) > 1):
            self.validate(heapSize-1)
    
    
        
    
    
        
                

        


        

