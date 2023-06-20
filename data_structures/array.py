import numpy as np   # to use array module

################
# ARRAY BASICS #
################

# by default, np arrays can only store integers and float
arr = np.array([1, 2, 3, 4])    # 1-D array
print(type(arr))
print(arr)

arr_2d = np.array([[1.2,2.3], [3.4,4.5]])   # 2-D array
print(arr_2d)

# get dimensions of array
print("Dimension of array = ", arr.ndim)
print("Dimension of array = ", arr_2d.ndim)

# arr_t = np.array([[1,2,3], [4,5]]) # ERROR: cannot create ragged arrays unless it's mentioned as an dtype=object

arr = np.arange(1, 11, 2) # array of odd numbers, arange(start, stop, step)
print(arr)

arr = np.linspace(1, 20, 5) # array of 5 numbers evenly spaced b/w 1 and 20, linspace(start, end, num of elements)
print(arr)

arr = np.ones(4)    # 1-D array of 4 1's
print(arr)

arr = np.zeros(4)   # 1-D array of 4 0's
print(arr)

# accessing array
arr = np.array([5, 3, 4, 7, 2, 1, 6, 8])
print(arr[0])   # first element, i.e. 5
print(arr[-1])  # last element, i.e. 8

arr_2d = np.array([[1.2,2.3], [3.4,4.5]])
print(arr_2d[0, 0])    # 1st element on 1st row, i.e. 1.2
print(arr_2d[1, 0])    # 1st element on 2nd row, i.e. 3.4

# sorting array
arr = np.sort(arr)
print(arr)

# slicing arrays -> similar to lists
print(arr[1:5]) # 2nd element till 5th element
print(arr[5:])  # 6th element till end
print(arr[:3])  # starting element till 3rd element
print(arr[::2]) # get every 2nd element
print(arr[1:8:3])   # get every 3rd element from 1st index till 7th index
