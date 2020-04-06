import numpy as np


'''
Preprocessing
'''

def augmented(coordinates):

	'''
	> Append 1 to coordinates.

	Parameters:
	- coordinates: array_like. A list of unaugmented
	data points.
	'''

	# making sure coordinate is ndarray
	coordinates = np.array(coordinates)
	
	coordinates = coordinates.reshape((2, -1))
	
	return np.concatenate((coordinates, [[1]*coordinates.shape[1]]))

'''
Affine Transformations
'''

# list of all affine transformations
transformations = []

# identity
def identity(data, *arg):

	'''
	> Return data points as they are.

	Parameters:
	- data: array_like. A matrix where each column
	is an augmented data point.
	'''

	matrix = np.array([[1, 0, 0],
						[0, 1, 0],
						[0, 0, 1]])

	return np.dot(matrix, data)
transformations.append(identity)

# translation
def translate(data, translate_by):

	'''
	> Return translated data points by given vector.

	Parameters:
	- data: array_like. A matrix where each column
	is an augmented data point.
	- translate_by: array_like. Translation vector.
	'''

	matrix = np.array([[1, 0, translate_by[0]],
						[0, 1, translate_by[1]],
						[0, 0, 1]])

	return np.dot(matrix, data)
transformations.append(translate)

# scaling
def scale(data, scale_factor):

	'''
	> Return scaled data points by factor.

	Parameters:
	- data: array_like. A matrix where each column
	is an augmented data point.
	- scale_factor: array_like. Scale factor.
	'''

	matrix = np.array([[scale_factor[0], 0, 0],
						[0, scale_factor[1], 0],
						[0, 0, 1]])

	return np.dot(matrix, data)
transformations.append(scale)

# rotation around origin
def rotate(data, angle):

	'''
	> Return rotated data points around origin.

	Parameters:
	- data: array_like. A matrix where each column
	is an augmented data point.
	- angle: float. Rotation angle in radiant.
	'''

	matrix = np.array([[np.cos(angle), np.sin(angle), 0],
						[-np.sin(angle), np.cos(angle), 0],
						[0, 0, 1]])

	return np.dot(matrix, data)
transformations.append(rotate)

# shearing in x direction
def x_shear(data, angle):

	'''
	> Return sheared data points in x direction.

	Parameters:
	- data: array_like. A matrix where each column
	is an augmented data point.
	- angle: float. Shear angle in radiant.
	'''

	matrix = np.array([[1, np.tan(angle), 0],
						[0, 1, 0],
						[0, 0, 1]])

	return np.dot(matrix, data)
transformations.append(x_shear)

# shearing in y direction
def y_shear(data, angle):

	'''
	> Return sheared data points in y direction.

	Parameters:
	- data: array_like. A matrix where each column
	is an augmented data point.
	- angle: float. Shear angle in radiant.
	'''

	matrix = np.array([[1, 0, 0],
						[np.tan(angle), 1, 0],
						[0, 0, 1]])

	return np.dot(matrix, data)
transformations.append(y_shear)

# reflection through origin
def o_reflect(data, *arg):

	'''
	> Return reflected data points through origin.

	Parameters:
	- data: array_like. A matrix where each column
	is an augmented data point.
	'''

	matrix = np.array([[-1, 0, 0],
						[0, -1, 0],
						[0, 0, 1]])

	return np.dot(matrix, data)
transformations.append(o_reflect)

# reflection through x-axis
def x_reflect(data, *arg):

	'''
	> Return reflected data points through x-axis.

	Parameters:
	- data: array_like. A matrix where each column
	is an augmented data point.
	'''

	matrix = np.array([[1, 0, 0],
						[0, -1, 0],
						[0, 0, 1]])

	return np.dot(matrix, data)
transformations.append(x_reflect)

# reflection through y-axis
def y_reflect(data, *arg):

	'''
	> Return reflected data points through y-axis.

	Parameters:
	- data: array_like. A matrix where each column
	is an augmented data point.
	'''

	matrix = np.array([[-1, 0, 0],
						[0, 1, 0],
						[0, 0, 1]])

	return np.dot(matrix, data)
transformations.append(y_reflect)


def standardize(transformation_list):

	'''
	> Return transformation list where all
	elements are 2-tuple.
	- transformation_list: array_like. A list of
	transformations to apply, including
	transformation codes (from 0 to 8) and 
	corresponding parameters in a 2-tuple. If
	there are no parameters, just use an integer.
	'''
	
	flag = True

	for (index, func) in enumerate(transformation_list):
		# checking for parameters
		try:
			if len(func) == 1:
				transformation_list[index] = 0
		except:
			transformation_list[index] = (func, 0)
			flag = False

		if flag:
			transformation_list[index] = (func[0], func[1])

	return transformation_list


def series(data, transformation_list):

	'''
	> Return all outputs from each component
	transformations, also including identity
	at beginning.

	Parameters:
	- data: array_like. A matrix where each column
	is an augmented data point.
	- transformation_list: array_like. A list of
	transformations to apply, including
	transformation codes (from 0 to 8) and 
	corresponding parameters in a 2-tuple. If
	there are no parameters, just use an integer.
	'''

	results = [data]
	transformation_list = standardize(transformation_list)

	for (func_name, arg) in transformation_list:

		latest = results[-1]
		# moving forward
		results.append(transformations[func_name](latest, arg))

	return results
