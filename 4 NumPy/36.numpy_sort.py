import numpy as np

x = [4,2,1,4,2]
y = np.array(x)

print(np.sort(y))
x.sort()
print(x)

print(np.sort(y)[::-1])
x.sort(reverse=True)
print(x)

# ============================================

x = [
    [10, 2, 39],
    [21, 7, 9],
    [3, 1, 12]
]
x = np.array(x)
print(x)
y = np.sort(x, axis=1)  # 0 by col, 1 by row, axis default 1
print(y)
y = np.sort(x, axis=0)
print(y)
y = np.sort(x, axis=None)
print(y)

# ============================================

# sort along the first axis 
a = np.array([[12, 15], [10, 1]]) 
arr1 = np.sort(a, axis = 0)         
print ("Along first axis : \n", arr1)         
  
# sort along the last axis 
a = np.array([[10, 15], [12, 1]]) 
arr2 = np.sort(a, axis = -1)         
print ("\nAlong last axis : \n", arr2) 
  
a = np.array([[12, 15], [10, 1]]) 
arr1 = np.sort(a, axis = None)         
print ("\nAlong none axis : \n", arr1) 

# Get a sorted copy of numpy array (Descending Order)
arr = np.array([6, 1, 4, 2, 18, 9, 3, 4, 2, 8, 11])
arr = np.sort(arr)[::-1]
print('Sorted Array in Descending Order: ', arr)