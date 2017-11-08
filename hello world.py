import numpy as np

x_data1 = np.float32(np.random.rand(2, 3))
x_data = np.dot([[3, 2, 1],
                [9, 12, 3]], [[.3, .2],
                              [.3, .2],
                              [.3, .2]])

y_data = np.dot([[3, 2, 1],
                [9, 12, 3]], [.3, .2, .1])

z_data = np.dot([.3, .2, .1], [3, 9, 3])
z_data1 = np.power([[2, 2],
                    [3, 3]], [8, 16])
print(x_data1)
print(x_data)
print(y_data)
print(z_data)
print(z_data1)
