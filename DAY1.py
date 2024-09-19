#ARRAY AND LIST

from array import *
arr = [23,56,11]
type(arr)
print(arr)


for x in arr:
    print(x)
    
    
for i in range(3):
    print(arr[i],end=' ')
    

i=0
while(i<len(arr)):
    print(arr[i])
    i+=1
    

arr.append(45)
print(arr)

arr.count(20)
arr.count(11)
arr.index(11)
arr.pop()
arr.pop(2)
arr.remove(56)

print(arr)


import numpy as np
a=np.array([1,2,3])
print(a)

b=np.array([1,2,3],[10,20,30])
print(b)

# End Of Code