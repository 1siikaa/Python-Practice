
import numpy as np
# boolean masking

arr1 = np.array([10, 20, 30, 40, 50, 60, 70, 80])
mask = (arr1 > 20) & (arr1 < 50)
print(mask)
print(arr1[mask])

# np.all() and np.any()
print(np.any(arr1 > 40 ))
print(np.all(arr1 > 30))

# np.isnan
arr2 = np.array([1, 2, np.nan, 4])
print(np.isnan(arr2))
print(arr2[~np.isnan(arr2)])

#np.diff
print(np.diff(arr2))
print(np.diff(arr1))

#np.cumsum (running total)
print(np.cumsum(arr1))
print(np.cumsum(arr2))

# copy vs view
arr3 = np.array([4, 5, 6, 7, 8, 1, 2, 3])
arr3_copy = np.copy(arr3)
print(arr3_copy)
arr3_view = arr3
print(arr3_view)
arr3_view[0] = 7
#arr3_copy[0] = 7
print(arr3_view)
print(arr3_copy)
print(arr3)


	# 1.	Filter values between 20 and 80
mask = (arr1>20) & (arr1<80)
print(arr1[mask])
	# 2.	Check if any value is negative
print(np.any(arr1 < 0))
	# 3.	Check if all values are positive
print(np.all(arr1 > 0))
	# 4.	Replace NaN with 0
arr2[np.isnan(arr2)] = 0
print(arr2)
	# 5.	Find difference between consecutive elements
print(np.diff(arr1))
	# 6.	Calculate cumulative sum
print(np.cumsum(arr1))
	# 7.	Count number of NaN values
arr4 = np.array([1, 2, 3, 4, np.nan, np.nan, 7])
print(np.sum(np.isnan(arr4)))
	# 8.	Clip array between 10 and 100
arr5 = np.array([5, 10, 11, 200, 300])
print(np.clip(arr5, 10, 100))
	# 9.	Find unique rows in 2D array
arr6 = np.array(
[[1,2], [2, 3], [1, 2], [4, 5]]
)
print(np.unique(arr6, axis=0))
	# 10.	Compare loop vs vectorized sum
# python loop slow
# vectorized sum fast