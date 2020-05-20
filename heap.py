class Heap(object):
    
    def __init__(self, comparation, heap_type):
        super().__init__()
        self.__heap = []
        self.comparation = comparation
        self.heap_size = 0
        self.heap_type = heap_type


    def __heapify_up_util(self, new_index):  
        parent_index = (int)((new_index-1)/2) 

        if parent_index < self.heap_size and self.comparation(self.__heap[new_index],self.__heap[parent_index]):
            self.__heap[new_index], self.__heap[parent_index] = self.__heap[parent_index], self.__heap[new_index]
            self.__heapify_up_util(parent_index)


    def __heapify_down_util(self, index):
        left_child = (2*index)+1
        right_child = (2*index)+2
        new_index = index

        if left_child < self.heap_size and self.comparation(self.__heap[index],self.__heap[left_child]):
            new_index = left_child

        if  right_child < self.heap_size and self.comparation(self.__heap[new_index],self.__heap[right_child]):
            new_index = right_child
        
        if  new_index != index:
            self.__heap[new_index], self.__heap[index] = self.__heap[index], self.__heap[new_index]
            self.__heapify_down_util(new_index)


    def heapify(self):
        if self.heap_size > 1:
            self.__heapify_down_util(0)


    def insert(self, data):
        self.__heap.append(data)
        self.heap_size += 1
        
        if(self.heap_size > 1):
            self.__heapify_up_util(self.heap_size-1)


    def update(self, index, data):
        element = self.__heap[index]
        self.__heap[index] = data

        if self.heap_type == True: #Max Heap
            if data > element:
                self.__heapify_down_util(index)
            elif data < element:
                self.__heapify_up_util(index)    
        else:  #Min Heap
            if data < element:
                self.__heapify_down_util(index)
            elif data > element:
                self.__heapify_up_util(index)    


    def update_v2(self, index, new_data):
        aux = self.get_element(index)
        self.delete(index)
        self.insert(new_data)


    def delete(self, index):
        self.__heap[index] = self.__heap[self.heap_size-1]
        self.__heap.pop()
        self.heap_size-=1

        self.__heapify_down_util(index)


    def extract(self):
        element = self.__heap[0]
        self.__heap[0] = self.__heap[self.heap_size-1]
        self.__heap.pop()
        self.heap_size -= 1

        self.heapify()
        return element
        

    def get_top(self):
        return self.__heap[0]


    def get_heap(self):
        return self.__heap

    def set_heap(self, arr):
        self.__heap = arr
        self.heap_size = len(arr)

    def append(self, data):
        self.heap_size += 1
        self.__heap.append(data)

    def get_element(self, index):
        return self.__heap[index]

    


    

    
        
    
    
        
                

        


        

