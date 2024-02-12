import numpy as np

# List comprehension method
x = [2, 3, 4, 5, 6]
y = [a + 2 for a in x]

# Direct addition using NumPy array
nums = np.array([2, 3, 4, 5, 6])
nums2 = nums + 2

# Checking the type of the NumPy array
nums_type = type(nums)

print("Using list comprehension:", y)
print("Using NumPy array:", nums2)
print("Type of nums array:", nums_type)
