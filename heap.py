class Heap(object):
    
    def __init__(self, comparation, heap_type, finding = lambda x,y: x==y):
        super().__init__()
        self.__heap = []
        self.comparation = comparation
        self.heap_size = 0
        self.heap_type = heap_type
        self.finding = finding


    def __heapify_up_util(self, new_index):  
        parent_index = (int)((new_index-1)/2) 

        if parent_index < self.heap_size and self.comparation(self.__heap[new_index],self.__heap[parent_index]):
            self.__heap[new_index], self.__heap[parent_index] = self.__heap[parent_index], self.__heap[new_index]
            self.__heapify_up_util(parent_index)


    def __heapify_down_util(self, index):
        left_child = (2*index)+1
        right_child = (2*index)+2
        new_index = index

        if left_child < self.heap_size and self.comparation(self.__heap[left_child],self.__heap[index]):
            new_index = left_child

        if  right_child < self.heap_size and self.comparation(self.__heap[right_child],self.__heap[new_index]):
            new_index = right_child
        
        if  new_index != index:
            self.__heap[new_index], self.__heap[index] = self.__heap[index], self.__heap[new_index]
            self.__heapify_down_util(new_index)


    def heapify(self):
        for i in range(self.heap_size//2, -1, -1):
            self.__heapify_down_util(i)


    def insert(self, data):
        self.__heap.append(data)
        self.heap_size += 1
        
        if(self.heap_size > 1):
            self.__heapify_up_util(self.heap_size-1)


    def update(self, index, data):
        element = self.__heap[index]
        self.__heap[index] = data

        if self.heap_type == True: #Max Heap
            if self.comparation(data, element): # a > b
                self.__heapify_up_util(index)
            else:
                self.__heapify_down_util(index)    
        else:  #Min Heap
            if self.comparation(data, element): # a < b
                self.__heapify_up_util(index)
            else: 
                self.__heapify_down_util(index)    



    def update_v2(self, index ,new_data):
        self.delete(index)
        self.insert(new_data)


    def get_element(self, data):
        for index, i in enumerate(self.__heap):
            if self.finding(data, i):
                return (index,i)
        return (None,None)

    def delete(self, index):
        self.__heap[index] = self.__heap[self.heap_size-1]
        self.__heap.pop()
        self.heap_size-=1

        self.__heapify_down_util(index)


    def extract(self):
        if self.heap_size > 0:
            element = self.__heap[0]
            self.__heap[0] = self.__heap[self.heap_size-1]
            self.__heap.pop()
            self.heap_size -= 1

            self.__heapify_down_util(0)
            return element
        else:
            return None
        

    def get_top(self):
        return self.__heap[0] if self.heap_size > 0 else None


    def get_heap(self):
        return self.__heap

    def set_heap(self, arr):
        self.__heap = arr
        self.heap_size = len(arr)

    def append(self, data):
        self.heap_size += 1
        self.__heap.append(data)

    def get_element_by_index(self, index):
        return self.__heap[index]

    


    

    
        
    
    
        
                

        


        

