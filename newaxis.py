import numpy as np

#  numpy中包含的newaxis可以给原数组增加一个维度
#  np.newaxis放的位置不同，产生的新数组也不同

#  一维数组
#  创建一个取值范围为1-8的，长度为5的一维随机数数组
# x = np.random.randint(1, 8, size=5)
# print(x)
# print(x.shape)
#
# x1 = x[np.newaxis, :]
# x2 = x[:, np.newaxis]
# print("x[np.newaxis, :] is")
# print(x1)
# print(x1.shape)
# print("x[:, np.newaxis] is")
# print(x2)
# print(x2.shape)

#  多维数组

y = np.random.randint(1, 8, size=(2, 3, 4))
print(y)
print(y.shape)

y1 = y[np.newaxis, :]
print(y1)
print(y1.shape)

y2 = y[:, np.newaxis, :]
print(y2)
print(y2.shape)

y3 = y[:, np.newaxis]
print(y3)
print(y3.shape)
