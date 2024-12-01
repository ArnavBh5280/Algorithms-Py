# IMPLEMENTATION OF PRIORITY QUEUE USING LIST

# 1. Define a class PriorityQueue to implement priority queue data structure using list. Provide_init_() method to create a list object (initially empty).
# 2. Define a push method in PriorityQueue class to insert new data with given priority.
# 3. Define a pop method in PriorityQueue class, which returns the highest priority data stored in the priority queue data structure. Raise exception if priority queue is empty.
# 4. Define is_empty method in PriorityQueue class to check if the priority queue is empty.
# 5. In class PriorityQueue, define a method size to return the number of elements present in the priority queue.

class PriorityQueue:
    def __init__(self):
        self.items=[]
        
    def push(self,data,priority):
        index=0
        while index<len(self.items) and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index,(data,priority))
        
    def is_empty(self):
        return len(self.items)==0
    
    def pop(self):
        if self.is_empty():
            raise IndexError("PQ is empty")
        return self.items.pop(0)[0]
        
    def size(self):
        return len(self.items)
    
p=PriorityQueue()
p.push("Ayushman",4)
p.push("Siddharth",5)
p.push("Ujjwal",1)
p.push("Shrey",3)
p.push("Arnav",2)

while not p.is_empty():
    print(p.pop())
    
