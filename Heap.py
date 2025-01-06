# HEAP AND HEAP SORT

# 1. Define a class Heap to implement Heap data structure with _init_method to create empty heap list.
# 2. In class Heap, define a method to create heap from a given list of elements.
# 3. In class Heap, define a method insert to insert a given element in the heap at appropriate position.
# 4. In class Heap, define a top method which returns the top element of the Heap. Raise an exception if Heap is empty.
# 5. Define a class EmptyHeapException to describe custom exception.
# 6. In class Heap, define a method delete which deletes the top element and returns it. Raise an exception if Heap is empty.
# 7. In class Heap, define a method heapSort to sort a given list with the help of Heap.

class Heap:
    def __init__(self):
        self.heap=[]
        
    def createHeap(self,list1):
        for e in list1:
            self.insert(e)
            
    def insert(self,e):
        index=len(self.heap)
        parentIndex=(index-1)//2
        while index>0 and self.heap[parentIndex]<e:
            if index==len(self.heap):
                self.heap.append(self.heap[parentIndex])
            else:
                self.heap[index]=self.heap[parentIndex]
            index==parentIndex
            parentIndex=(index-1)//2
        if index==len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index]=e
            
    def top(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        return self.heap[0]
    
    def delete(self):
        if len(self.heap) == 0:
            raise EmptyHeapException()  
        if len(self.heap) == 1:
            return self.heap.pop() 
        max_value = self.heap[0]  
        temp = self.heap.pop()  
        index = 0  
        leftChildIndex = 2 * index + 1
        rightChildIndex = 2 * index + 2

        while leftChildIndex < len(self.heap):  
            if rightChildIndex < len(self.heap):  
                if self.heap[leftChildIndex] > self.heap[rightChildIndex]:
                    if self.heap[leftChildIndex] > temp:
                        self.heap[index] = self.heap[leftChildIndex]
                        index = leftChildIndex
                    else:
                        break
                else:
                    if self.heap[rightChildIndex] > temp:
                        self.heap[index] = self.heap[rightChildIndex]
                        index = rightChildIndex
                    else:
                        break
            else:  # Only left child exists
                if self.heap[leftChildIndex] > temp:
                    self.heap[index] = self.heap[leftChildIndex]
                    index = leftChildIndex
                else:
                    break

            leftChildIndex = 2 * index + 1
            rightChildIndex = 2 * index + 2

        self.heap[index] = temp  
        return max_value  

    def heapSort(self,list1):
        self.createHeap(list1)
        list2=[]
        try:
            while True:
                list2.insert(0,self.delete())
        except EmptyHeapException:
            pass
        return list2
               
class EmptyHeapException(Exception):
    def __init__(self,msg="Emptyy heap"):
        self.msg=msg
    def __str__(self):
        return self.msg
    
list1=[4,56,12,78,54,16,32,96,84] 
h=Heap()
list1=h.heapSort(list1)
print(list1)
  
      
