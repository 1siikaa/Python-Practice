import numpy as np

arr = np.arange(1, 7)
print(arr)
reshaped = arr.reshape(2, 3)
reshaped = arr.reshape(-1, 3)
print(reshaped)
reshaped = arr.reshape(3, -1)
print(reshaped)
# error scenario for reshape
arr1= np.arange(1, 8)
print(arr1)
# reshaped1 = arr1.reshape(3, -1) this will throw error because 7 is not divisible by 3
# print(reshaped1) this will throw error because 7 is not divisible by 3
# -1 means -> -1 tells NumPy to automatically infer the missing dimension based on the total number of elements.
arr2 = np.array([[1, 2, 3],
              [4, 5, 6]])
print(np.sum(arr2, axis=0)) #column wise axis
print(np.prod(arr2, axis=1)) # row wise axis
# axis = direction you collapse

# broadcasting
arr3 = np.array([10, 20, 30])
print(arr3 + [11, 22, 33])
print(arr3 + [[10, 20, 30], [30, 40, 50]])
# print(arr3 + [[1, 2],[3, 4], [5, 6]]) error scenario
# Broadcasting -> NumPy stretches smaller array to match shape automatically.

# row or column wise operation
print(np.mean(arr3, axis=0))
print(np.mean(arr2, axis=1))
print(np.max(arr2))
print(np.max(arr2, axis=1))

	# 1.	Create array from 1 to 12 and reshape into 3×4
arr4 = np.arange(1, 13)
print(arr4)
print(arr4.reshape(3, -1))
	# 2.	Find column-wise sum of a 2D array
arr5 = np.arange(1, 9)
reshaped2 = arr5.reshape(2, -1)
print(reshaped2)
print(np.sum(reshaped2, axis=0))
	# 3.	Find row-wise mean
print(np.mean(reshaped2, axis=1))
	# 4.	Add 10 to every element using broadcasting
print(reshaped2 + [10])
	# 5.	Subtract column vector from 2D array
vectorCol = np.array([2, 3]).reshape(2, 1)
print(reshaped2-vectorCol)

    # not getting this. please teach me.
	# 6.	Use -1 in reshape
reshaped3 = arr5.reshape(4, -1)
print(reshaped3)  
	# 7.	Find max of each row
print(np.max(reshaped3, axis=1))
	# 8.	Multiply 2D array by scalar
# scalar means a single number
# vector means 1D array
# matrix means 2D array
print(reshaped2*3)
	# 9.	Flatten a 2D array
print(reshaped3.flatten())
print(reshaped3.ravel()) # no copy method
print(reshaped3.reshape(-1))
	# 10.	Find overall mean and row-wise mean
print(np.mean(reshaped3))    #overall mean
print(np.mean(reshaped3, axis=1)) # row-wise mean