import numpy as np

# Initialization the numpy array 1d, 2d, or 3d

# 1D array
arrayValue = np.array([1,2,3,4])
print(arrayValue)

#2D array
coordinates = np.array([[1.0 ,2.0],[5.0 ,3.0]])
print(coordinates)


# To find the dimension of the np.array 
print(arrayValue.ndim)
print(coordinates.ndim)

# To find the shape dimension of the np.array
print(coordinates.shape)

# To find data type of numpy array
print(coordinates.dtype)

# Get size of numpy array
print(coordinates.itemsize)


# Get total size
print(coordinates.size * coordinates.itemsize)
# or 
print(coordinates.nbytes)


data = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(data)
print(data.shape)

# Access the element of  the numpy array
print(data[0,5])
print(data[0,-1])


# Get a specific row
print(data[0])
print(data[0, :])


# Get a specific column
print(data[:, 2])


# Get a little bit a data with a specific range
print(data[0, 1:6])
# Add a step in there
print(data[0, 1:6: 2])

# Change an element from numpy
data[1, 6] = 99
print(data)


# Change a specific column
data[:, 3] = 101

# Or
data[:,4] = [88, 44]
print(data)

# 3D Example
data3D = np.array([[[10, 20], [30, 40]], [[50,60], [70,80]]])
print(data3D)

# Get element data using work outside in
print(data3D[1,1,:])
# NOTESS
# should insert data to a specific size
# 2,2 -> 2,2 cannot with 2,1

# Change 3D data
data3D[0,1, :] = [99,100]
print(data3D)

# It will caused an error
# data3D[0,0, :] = [200, 300, 999]

# Create empty and full numpy array
# emptyArray = np.empty([3,4], dtype=int)
# filledArray = np.full([3,3], 55, dtype=int)
# print(emptyArray)
# print(filledArray)