import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7])
b = np.array([1, 2, 3, 5, 5, 6, 7])
error = np.mean( a != b )
print(error)