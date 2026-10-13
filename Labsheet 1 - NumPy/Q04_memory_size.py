import sys
import numpy as np
values = [1, 2, 3, 4, 5]
python_list = values
numpy_array = np.array(values)
print("List object size:", sys.getsizeof(python_list), "bytes")
print("NumPy array object size:", sys.getsizeof(numpy_array), "bytes")
print("NumPy data buffer:", numpy_array.nbytes, "bytes")
# getsizeof(list) excludes the sizes of the referenced integer objects.
