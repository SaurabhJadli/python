import numpy as np

a = np.array([1, 2, 3, 4, 5])

b = a + 1
c = a * 2
d = a / 3
print(b)
print(c)
print(d)

my_array = np.arange(12).reshape(4, 3)
print("Current array:")
print(my_array)

my_array[:, [0, 2]] = my_array[:, [2, 0]]
print("Array after the swaping:")
print(my_array)

import numpy as np