# Numpy is numerical python

import numpy as np
list = [1, 2, 3, 4]
arr = np.array([1, 2, 3, 4])
arr2 = np.array(["s", "t"])
# print(arr2 * 2) restricted in newer versions
print(np.strings.multiply(arr2, 23)) 
print(arr)
print(arr*1.2) #vectorization
print(arr>2)
print(arr[arr > 2])
print(arr.ndim)
print(arr2.ndim)
print(arr.dtype)
print(arr2.dtype)
print(arr.size)
print(arr2.size)
print(arr.shape)
print(arr2.shape)


# NumPy – 10 Questions
# 	1.	Create a NumPy array of first 10 natural numbers
firstN = np.array([1,2,3,4,5,6,7,8,9, 10])
# 	2.	Find square of each number
print(firstN*firstN)
# 	3.	Filter numbers greater than 5
print(firstN[firstN > 5])
# 	4.	Convert list [1,2,3] to NumPy array
list1 = [1,2,3,4,5,6,7,8,9,10]
numpyArray = np.array(list1)
print(numpyArray)
# 	5.	Add 5 to all elements
print(firstN+5)
# 	6.	Multiply two arrays element-wise
print(firstN*list1)
# 	7.	Find mean of array
print(np.sum(firstN)/firstN.size)
# 	8.	Create array of zeros of size 5
# 	8.	Create array of zeros of size 5
list2 = np.zeros(5)
print(list2)
# 	9.	Create array from 1 to 20 with step 2
list3 = np.arange(1, 21, 2)
print(list3)
# 	10.	Find max and min
print(np.max(firstN))
print(np.min(firstN))


#Solution
firstN = np.arange(1, 11)

print(firstN ** 2)
print(firstN[firstN > 5])

numpyArray = np.array(firstN)
print(firstN + 5)
print(firstN * numpyArray)

print(np.mean(firstN))
print(np.zeros(5))
print(np.arange(1, 21, 2))

print(np.max(firstN), np.min(firstN))