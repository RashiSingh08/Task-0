import time

import numpy as np

python_list = [1, 2, 3, 4, 5]
print("Python lists require loops :", [x*4 for x in python_list])
numpy_array = np.array([1, 2, 3, 4, 5])
print("Numpy arrays support vectorized operations :", numpy_array * 4)

start = time.time()
result_python_list = [x * 4 for x in python_list]
end = time.time()
print("Time taken by Python lists:", end - start)

start = time.time()
result_numpy_array = numpy_array * 4
end = time.time()
print("Time taken by Numpy arrays:", end - start)

arr = np.array([[1, 2, 3], [44, 55, 66]])
print("Orignal array:\n", arr)
print("first element of first row:", arr[0, 0])
print(" second element of second row:", arr[1, 1])
print("Last element of last row:", arr[-1, -1])