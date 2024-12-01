# SINGLY CIRCULAR LINKED LIST

# ASSIGNMENT QUESTIONS 
# 1. Define a class Node to describe a node of a circular linked list.
# 2. Define a class CLL to implement Circular Linked List with init() method to create and initialise last reference variable.
# 3. Define a method is_empty() to check if the linked list is empty in CLL class. I
# 4. In class CLL, define a method insert_at_start() to insert an element at the starting of the list.
# 5. In class CLL, define a method insert_at_last() to insert an element at the end of the list.
# 6. In class CLL, define a method search() to find the node with specified element value.
# 7. In class CLL, define a method insert_after() to insert a new node after a given node of the list.
# 8. In class CLL, define a method to print all the elements of the list.
# 9. In class CLL, implement iterator for CLL to access all the elements of the list in a sequence.

class Node:
    def __int__(self,item=None,next=None):
        self.item=item
        self.next=next
class CLL:
    def __init__(self,last=None):
        self.last=last
    def is_empty(self):
        return self.start==None
    def insert_at_first(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_enpty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
    def search(self,data):
        if self.is_empty():
            return None
        temp=self.last.next
        while  temp!=self.last:
            if temp.item == data:
                return temp
            temp=temp.next
        if temp.item==data:
            return temp
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            if temp==self.last:
                self.last=n
    def print_list(self):
        if not self.is_empty():
            temp=self.last.next
            while temp!=self.last:
                print(temp.item,end=' ')
                temp=temp.next
            print(temp.item)
    def delete_first(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next.next
            
                
# Code abhi baaki hai ...krege baad me 
