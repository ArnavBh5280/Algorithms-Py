# SORTING

# Write a python function to implement bubble sort.
# Write a python function to implement modified bubble sort.
# Write a python function to implement Selection Sort

# BUBBLE SORT
def bubble_sort(data_list):
    for r in range(1,len(data_list)):
        for i in range(len(data_list)-r):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                
l=[34,67,12,89,25,50]
bubble_sort(l)
print("Bubble Sort :- ",l)


# MODIFIED BUBBLE SORT
def modified_bubble_sort(data_list):
    flag=False
    for r in range(1,len(data_list)):
        flag=False
        for i in range(len(data_list)-r):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                flag=True
        if not flag:
            break
                
m=[34,67,12,89,25,50]
modified_bubble_sort(m)
print("Modified Bubble Sort :- ",m)


# SELECTION SORT
def selection_sort(list1):
    n=len(list1)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if list1[j] < list1[min_index]:
                min_index=j
        list1[i],list1[min_index]=list1[min_index],list1[i]
        
n=[34,67,12,89,25,50]
selection_sort(n)
print("Selection Sort :- ",n)


# INSERTION SORT
def insertion_sort(list1):
    for i in range(1,len(list1)):
        temp=list1[i]
        j=i-1
        while j>=0 and temp<list1[j]:
            list1[j+1]=list1[j]
            j-=1
        list1[j+1]=temp

o=[34,67,12,89,25,50]
insertion_sort(o)
print("Insertion Sort :- ",o)
