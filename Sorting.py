# SORTING

# Write a python function to implement bubble sort.
# Write a python function to implement modified bubble sort.
# Write a python function to implement Selection Sort.
# Write a python function to implement Quick Sort.


# BUBBLE SORT
def bubble_sort(data_list):
    for r in range(1,len(data_list)):
        for i in range(len(data_list)-r):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                
l=[42, 87, 15, 73, 56, 32, 98, 67, 11, 49]
bubble_sort(l)
print("Bubble Sort :- ",l)
print()


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
                
m=[42, 87, 15, 73, 56, 32, 98, 67, 11, 49]
modified_bubble_sort(m)
print("Modified Bubble Sort :- ",m)
print()


# SELECTION SORT
def selection_sort(list1):
    n=len(list1)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if list1[j] < list1[min_index]:
                min_index=j
        list1[i],list1[min_index]=list1[min_index],list1[i]
        
n=[42, 87, 15, 73, 56, 32, 98, 67, 11, 49]
selection_sort(n)
print("Selection Sort :- ",n)
print()


# INSERTION SORT
def insertion_sort(list1):
    for i in range(1,len(list1)):
        temp=list1[i]
        j=i-1
        while j>=0 and temp<list1[j]:
            list1[j+1]=list1[j]
            j-=1
        list1[j+1]=temp

o=[42, 87, 15, 73, 56, 32, 98, 67, 11, 49]
insertion_sort(o)
print("Insertion Sort :- ",o)
print()


# QUICK SORT
def quick_sort(list1):
    if len(list1)<=1:
        return list1
    else:
        pivot=list1[0]
        lesser=[x for x in list1[1:] if x<=pivot]
        greater=[x for x in list1[1:] if x>pivot]
        return quick_sort(lesser)+[pivot]+quick_sort(greater)
    
p=[42, 87, 15, 73, 56, 32, 98, 67, 11, 49]
p=quick_sort(p)
print("Quick Sort :- ",p)
print()


# MERGE SORT
def merge_sort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        leftlist=list1[:mid]
        rightlist=list1[mid:]
        
        merge_sort(leftlist)
        merge_sort(rightlist)
        
        i=j=k=0
        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                list1[k]=leftlist[i]
                i+=1
            else:
                list1[k]=rightlist[j]
                j+=1
            k+=1
        while i<len(leftlist):
            list1[k]=leftlist[i]
            i+=1
            k+=1
        while j<len(rightlist):
            list1[k]=rightlist[j]
            j+=1
            k+=1

q=[42, 87, 15, 73, 56, 32, 98, 67, 11, 49]
p=merge_sort(q)
print("Merge Sort :- ",q)
print()
