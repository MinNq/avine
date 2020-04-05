import numpy as np

# appending 1 to coordinate
def augmented(coordinate):
	
	# making sure coordinate is ndarray
	coordinate = np.array(coordinate)
	
	coordinate = coordinate.reshape((coordinate.size, 1))
	return np.concatenate((coordinate, [[1]]))

'''
To facilitate composite functions, the following only
return augmented coordinates.
'''

# identity
def identity(data):

	matrix = np.array([[1, 0, 0],
						[0, 1, 0],
						[0, 0, 1]])

	return np.dot(matrix, data)

# translation
def translation(data, translate_by = [1.8, 1.5]):

	matrix = np.array([[1, 0, translate_by[0]],
						[0, 1, translate_by[1]],
						[0, 0, 1]])

	return np.dot(matrix, data)

# scaling about origin
def scaling(data, scale_factor = [1.8, 1.5]):

	matrix = np.array([[scale_factor[0], 0, 0],
						[0, scale_factor[1], 0],
						[0, 0, 1]])

	return np.dot(matrix, data)

# rotation about origin
def rotation(data, angle = np.pi/3):

	matrix = np.array([[np.cos(angle), np.sin(angle), 0],
						[-np.sin(angle), np.cos(angle), 0],
						[0, 0, 1]])

	return np.dot(matrix, data)

# shearing in x direction
def x_shearing(data, angle = np.pi/3):

	matrix = np.array([[1, np.tan(angle), 0],
						[0, 1, 0],
						[0, 0, 1]])

	return np.dot(matrix, data)

# shearing in y direction
def y_shearing(data, angle = np.pi/3):

	matrix = np.array([[1, 0, 0],
						[np.tan(angle), 1, 0],
						[0, 0, 1]])

	return np.dot(matrix, data)

# reflection about origin
def o_reflection(data):

	matrix = np.array([[-1, 0, 0],
						[0, -1, 0],
						[0, 0, 1]])

	return np.dot(matrix, data)

# reflection about x-axis
def x_reflection(data):

	matrix = np.array([[1, 0, 0],
						[0, -1, 0],
						[0, 0, 1]])

	return np.dot(matrix, data)

# reflection about y-axis
def y_reflection(data):

	matrix = np.array([[-1, 0, 0],
						[0, 1, 0],
						[0, 0, 1]])

	return np.dot(matrix, data)

# the list of all transformations in this script
func_list = [identity, translation, scaling, rotation, x_shearing, y_shearing, o_reflection, x_reflection, y_reflection]