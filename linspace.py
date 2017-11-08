#!/usr/bin/python

import numpy as np

#  在默认情况下，linspace函数可以生成元素为50的等间隔数列。
#  而前两个参数分别是数列的开头与结尾。
#  如果写入第三个参数，可以制定数列的元素个数。
#  这种方式相对来说也有一点欠缺规范，更好方式是指明第三个参数需要设定的属性。
#  dtype 设定数据类型
x1 = np.linspace(1, 10)
x2 = np.linspace(1, 10, 10, dtype=np.float32)
x3 = np.linspace(1, 10, num=10, dtype=np.float32)

print(x1)
print(x2)
print(x3)
print("length of x1 is %d" % len(x1))
print("length of x2 is %d" % len(x2))
print("length of x2 is %d" % len(x3))

#  结束点如果现在为True，那么输入的第二个参数将会成为数列的最后一个元素，反之则不一定。
#  而retstep会改变计算的输出，输出一个元组，而元组的两个元素分别是需要生成的数列和数列的步进差值。

x4 = np.linspace(1, 10, num=10, retstep=True)

print(x4)
print("length of x1 is %d" % len(x4))
