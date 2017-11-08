import numpy as np

# rand #
# 生成一个[0,1)之间的随机浮点数或N维浮点数组
#  无参数  生成一个[0,1)之间随机浮点数
rand = np.random.rand()
print(rand)

#  一个参数  生成一个轴长度为5的一维数组
rand1 = np.random.rand(5)
print(rand1)

#  两个参数  生成2x3的二维数组
rand2 = np.random.rand(2, 3)
print(rand2)

# randn #
# 生成一个浮点数或N维浮点数组，取数范围：正态分布的随机样本数。
#  无参数  生成一个随机浮点数
randn = np.random.randn()  # 1.4872544578730051，不一定是[0,1)之间的随机数
print(randn)

#  一个参数  生成一个轴长度为5的一维数组
randn1 = np.random.randn(5)
print(randn1)

#  两个参数  生成2x3的二维数组
randn2 = np.random.randn(2, 3)
print(randn2)

# standard_normal #
# 生成一个浮点数或N维浮点数组，取数范围：标准正态分布随机样本。
#  无参数  生成一个随机浮点数
standard_normal = np.random.standard_normal()  # 1.4872544578730051，不一定是[0,1)之间的随机数
print(standard_normal)

#  一个参数  生成一个轴长度为5的一维数组
standard_normal1 = np.random.standard_normal(5)
print(standard_normal1)

#  两个参数  生成2x3的二维数组
standard_normal2 = np.random.standard_normal((2, 3))  # 写法一样 np.random.standard_normal([2, 3])
print(standard_normal2)

# randint #
# numpy.random.randint(low, high=None, size=None, dtype='l')
# 生成一个整数或N维整数数组，取数范围：若high不为None时，取[low,high)之间随机整数，否则取值[0,low)之间随机整数。
# low=2
np.random.randint(2)  # 生成一个[0,2)之间随机整数
# low=2,size=5
np.random.randint(2, size=5)  # array([0, 1, 1, 0, 1])
# low=2,high=2
# np.random.randint(2,2)#报错,high必须大于low
# low=2,high=6
np.random.randint(2, 6)  # 生成一个[2,6)之间随机整数
# low=2,high=6,size=5
np.random.randint(2, 6, size=5)  # 生成形状为5的一维整数数组
# size为整数元组
np.random.randint(2, size=(2, 3))  # 生成一个2x3整数数组,取数范围：[0,2)随机整数
np.random.randint(2, 6, (2, 3))  # 生成一个2x3整数数组,取值范围：[2,6)随机整数
# dtype参数：只能是int类型
np.random.randint(2, dtype='int32')
np.random.randint(2, dtype=np.int32)

# numpy.random.random_integers(low, high=None, size=None)
# 生成一个整数或一个N维整数数组，取值范围：若high不为None，则取[low,high]之间随机整数，否则取[1,low]之间随机整数。

# low=2
np.random.random_integers(2)  # 生成一个[1,2]之间随机整数
# low=2、size=5
np.random.random_integers(2, size=5)  # array([2, 1, 1, 1, 1])
# low=2、high=6
np.random.random_integers(2, 6)  # 生成一个[2,6]之间随机整数
# low=2、high=6、size=5
np.random.random_integers(2, 6, size=5)  # 生成一个形状为5的一维整数数组组
# size为整数元组
np.random.random_integers(2, size=(2, 3))  # 生成一个2x3数组,取数范围：[1,2]随机整数
np.random.random_integers(2, 6, (2, 3))  # 生成一个2x3数组，取数范围：[2,6]随机整数

# numpy.random.random_sample(size=None)
# 生成一个[0,1)之间随机浮点数或N维浮点数组。
# size=None
np.random.random_sample()  # 生成一个[0,1)之间随机浮点数
# size=2
np.random.random_sample(2)  # 生成shape=2的一维数组
# size为整数元组
np.random.random_sample((2,))  # 等同np.random.random_sample(2)
# np.random.random_sample((,2))#报错
np.random.random_sample((2, 3))  # 生成2x3数组
np.random.random_sample((3, 2, 2))  # 3x2x2数组

# numpy.random.choice(a, size=None, replace=True, p=None)
# 从序列中获取元素，若a为整数，元素取值为np.range(a)中随机数；若a为数组，取值为a数组元素中随机元素。
# a为整数，size为None
np.random.choice(2)  # 生成一个range(2)中的随机数
# a为整数,size为整数
np.random.choice(2, 2)  # 生成一个shape=2一维数组
# a为整数,size为整数元组
np.random.choice(5, (2, 3))  # 生成一个2x3数组
# a为数组,size为None
np.random.choice(np.array(['a', 'b', 'c', 'f']))  # 生成一个np.array(['a','b','c','f']中随机元素
# a为数组,size为整数
np.random.choice(5, (2, 3))  # 生成2x3数组
# a为数组,size为整数元组
np.random.choice(np.array(['a', 'b', 'c', 'f']), (2, 3))  # 生成2x3数组
# p参数：可以理解成a中元素出现的概率，p的长度和a的长度必须相同，且p中元素之和为1，否则报错
# np.random.choice(2,p=[1])#报错，a和p长度不一致
np.random.choice(5, p=[0, 0, 0, 0, 1])  # 生成的始终是4
np.random.choice(5, 3, p=[0, 0.5, 0.5, 0, 0])  # 生成shape=3的一维数组，元素取值为1或2的随机数

# numpy.random.shuffle(x)
# 对X进行重排序，如果X为多维数组，只沿第一条轴洗牌，输出为None。
list1 = [1, 2, 3, 4, 5]
np.random.shuffle(list1)  # 输出None
list1  # [1, 2, 5, 3, 4],原序列的顺序也被修改
arr = np.arange(9).reshape(3, 3)
np.random.shuffle(arr)  # 对于多维数组，只沿着第一条轴打乱顺序

# numpy.random.permutation(x)
# 与numpy.random.shuffle(x)函数功能相同，两者区别：peumutation(x)不会修改X的顺序。
# x=5
np.random.permutation(5)  # 生成一个range(5)随机顺序的数组
# x为列表或元组
list1 = [1, 2, 3, 4]
np.random.permutation(list1)  # array([2, 1, 4, 3])
# list1#[1, 2, 3, 4]
# x为数组
arr = np.arange(9)
np.random.permutation(arr)
arr2 = np.arange(9).reshape(3, 3)
np.random.permutation(arr2)  # 对于多维数组，只会沿着第一条轴打乱顺序
