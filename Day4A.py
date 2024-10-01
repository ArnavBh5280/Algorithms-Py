# DOUBLY LINKED LIST

# Assignment Questions -
# 1. Define a class Node to describe a node of a doubly linked list.
# 2. Define a class DLL to implement Doubly Linked List with init() method to create and initialise start reference variable.
# 3. Define a method is_empty() to check if the linked list is empty in DLL class.
# 4. In class DLL, define a method insert_at_start() to insert an element at the starting of the list.
# 5. In class DLL, define a method insert_at_last() to insert an element at the end of the list.
# 6. In class DLL, define a method search() to find the node with specified element value.
# 7. In class DLL, define a method insert_after() to insert a new node after a given node of the list.
# 8. In class DLL, define a method to print all the elements of the list.
# 9. In class DLL, implement iterator for DLL to access all the elements of the list in a sequence.
# 10. In class DLL., define a method delete first() to delete first element from the list.
# 11. in class DLL, define a method delete last() to delete last element from the list.
# 12. In class DLL. define a method delete item() to delete specified element from the list.

class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item 
        self.next=next
class DLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n 
    def insert_at_last(self,data):
        temp=self.start
        if self.start!=None:
            while temp.next!=None:
                temp=temp.next
        
        n=Node(temp,data,None)
        if temp==None:
            self.start=n
        else:
            temp.next=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.utem,end=' ')
            temp=temp.next
    
    
        
        