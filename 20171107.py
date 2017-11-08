import numpy as np

data0 = np.zeros((3, 4))
# data1 = np.arange(50).reshape(2, 5, 5)
# data2 = np.array([1, 2, 3, 4])
#
# print(data0)
# print(data1)
# print(data2)
#
# # 数组轴的个数，在python的世界中，轴的个数被称作秩
# print("--------->数组轴的个数(秩):")
# print(data0.ndim)
# print(data1.ndim)
# print(data2.ndim)
#
# # 数组的维度。这是一个指示数组在每个维度上大小的整数元组。例如一个n排m列的矩阵，它的shape属性将是(2,3),这个元组的长度显然是秩，即维度或者ndim属性
# print("--------->数组的维度:")
# print(data0.shape)
# print(data1.shape)
# print(data2.shape)
#
# # 数组元素的总个数，等于shape属性中元组元素的乘积。
# print("--------->数组元素的总个数:")
# print(data0.size)
# print(data1.size)
# print(data2.size)
#
# # 一个用来描述数组中元素类型的对象，可以通过创造或指定dtype使用标准Python类型。另外NumPy提供它自己的数据类型。
# print("--------->一个用来描述数组中元素类型的对象:")
# print(data0.dtype)
# print(data1.dtype)
# print(data2.dtype)
#
# # 数组中每个元素的字节大小。例如，一个元素类型为float64的数组itemsiz属性值为8(=64/8),又如，一个元素类型为complex32的数组item属性为4(=32/8).
# print("--------->数组中每个元素的字节大小:")
# print(data0.itemsize)
# print(data1.itemsize)
# print(data2.itemsize)
#
# # 包含实际数组元素的缓冲区，通常我们不需要使用这个属性，因为我们总是通过索引来使用数组中的元素。
# print("--------->包含实际数组元素的缓冲区:")
# print(data0.data)
# print(data1.data)
# print(data2.data)

a = np.array([[20, 30],
              [40, 50]])
b = np.array([[20, 30],
              [40, 50]])
print(a)
print(b)
data0 = a * b
print("--------->a * b = ")
print(data0)
print("--------->a dot b = ")
data0 = np.dot(a, b)
print(data0)



