import numpy as np

arr = np.array([4,5,6,7,8])
print(arr[arr>7])
print(np.where(arr > 6, "High", "Low"))
print(np.sort(arr))
print(np.sort(arr)[:-1])
print(np.sort(arr)[::-1])
# 	[::-1] → reverse
print(arr.argsort()[::-1])
indices = arr.argsort()[::-1]
print(indices)
print(arr[indices])
# argsort gives the order without losing original data.
#  Sort in-place (Modifies original array) (.sort())
print(arr.sort())  #arr.sort() sorts the array in-place and returns None. Because you are printing the return value and not the array.
# but if print it later it prints the modified array
print(arr) # because it says i will change the give array and return you nothing
# 2d array sort using argsort
# get indices row wise
arr2D = np.array([[7, 10, 2], [4, 50, 20]])
indicesRow = np.argsort(arr2D, axis=1)
print(indicesRow)
indicesRowDesc =  indicesRow[:, ::-1]
print(indicesRowDesc)
print(np.take_along_axis(arr2D, indicesRowDesc, axis=1))
# 2D sort using np.sort()
print(np.sort(arr2D, axis=1)) #asc
print(np.sort(arr2D, axis=1)[:, ::-1]) # desc
# 2D sort using
arr2D.sort(axis=1)
print(arr2D)
arr2D.sort(axis=1)
print(arr2D[:, ::-1])
# unique
arr2 = np.array([1, 555, 6, 6, 7, 9])
print(np.unique(arr2))
print(np.unique(arr2, return_counts=True))
# replace values conditionally
print(np.where(arr2>3, 99, arr2))
print(arr2)
print(np.clip(arr2, 100, 98))

#  Force every value in the array to stay between min and max.

# 	•	If value < min → change it to min
# 	•	If value > max → change it to max
# 	•	If value is already in range → leave it as-is


	# 1.	Filter even numbers from array
arr4 = np.array([1,2,3,4,5,6,7,80,-1,30])
print(np.where(arr4 % 2 == 0))
print(arr4[np.where(arr4 % 2 == 0)])
	# 2.	Replace values > 50 with 50
print(np.where(arr4 > 50, 50, arr4))    
	# 3.	Categorize numbers as High/Low
print(np.where(arr4 > 40, "High", "Low"))    
	# 4.	Find unique elements
print(np.unique(arr4))
	# 5.	Count frequency of elements
print(np.unique(arr4, return_counts=True))    
	# 6.	Sort array descending
indices4 = np.argsort(arr4)[::-1]
print(arr4[indices4])
	# 7.	Get indices of sorted array
arr4.sort()
indices4 = np.argsort(arr4)
print(indices4)
	# 8.	Replace negative values with 0
print(np.where(arr4 < 0, 0, arr4))
	# 9.	Clip values between 10 and 100
print(np.clip(arr4, 10, 100))
	# 10.	Find numbers divisible by 3
indices5 = np.where(arr4 % 3 == 0)
print(arr4[indices5])

# clean and interview ready version
arr4 = np.array([1,2,3,4,5,6,7,80,-1,30])

print(arr4[arr4 % 2 == 0])                     # even numbers
print(np.where(arr4 > 50, 50, arr4))            # cap at 50
print(np.where(arr4 > 40, "High", "Low"))       # categorize
print(np.unique(arr4))                          # unique
print(np.unique(arr4, return_counts=True))      # frequency

indices = np.argsort(arr4)[::-1]
print(arr4[indices])                            # descending sort

print(np.where(arr4 < 0, 0, arr4))              # replace negatives
print(np.clip(arr4, 10, 100))                   # clip range
print(arr4[arr4 % 3 == 0])                      # divisible by 3
