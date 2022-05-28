# List列表类似于C语言中的数组，list灵活度更高  可以允许元素不是同一个类型 list取名可以是复数名称

"""
# 访问list
bicycle = ["trek", "cannonble", "redline"]
print(bicycle)
print(bicycle[0])  # 输出trek
print(bicycle[1].title())   # 输出 Cannonble
print(bicycle[2])  # 输出redline
# 当要访问最后一个元素时可以使用-1
print(bicycle[-1])  # python列表的特殊用法(重要)

message = "My bicycle was a {}".format(bicycle[0].title())
print(message)  # My bicycle was a Trek
"""

"""
# list 修改、添加和删除元素
# 修改列表元素
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)    # 输出['honda', 'yamaha', 'suzuki']
motorcycles[0] = "ducati"
print(motorcycles)    # 输出['ducati', 'yamaha', 'suzuki']
# 添加元素
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.append("ducati")   # 将元素添加到list最末尾的地方
print(motorcycles)  # 输出['honda', 'yamaha', 'suzuki', 'ducati']
# 在列表中插入元素
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(1, "ducati")  # 将内容插入到列表index的位置
print(motorcycles)
motorcycles.insert(1, 1.0)  # list允许元素不是同一个类型
print(motorcycles[1]+2.0)  # 3.0

# 删除列表中的元素
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
del motorcycles[0]
print(motorcycles)   # 使用del语句进行删除，不支持使用这种方法
# 使用pop方法进行删除 (推荐使用，可以弹出list任何一个元素同时还可以获取到pop出的值)，
motorcycles = ["honda", "yamaha", "suzuki"]  # 当list中没有元素时使用pop会报错，当检索号大于实际list元素时也会报错
pop_data = motorcycles.pop(1)      # 使用pop方法将最后1个元素弹出
print("{}\n{}".format(pop_data, motorcycles))     # 输出yamaha \n ['honda', 'suzuki']
# 根据值删除元素
motorcycles = ["honda", "honda", "yamaha", "suzuki"]  # 使用remove时如果list无目标值将会报错,如果有多个目标值只删除第一个
motorcycles.remove("honda")
print(motorcycles)

"""

"""
# 组织列表
# 使用sort对列表永久排序
cars = ["bmw", "Audi", "Toyota", "subaru"]
cars.sort()   # 根据字母顺序从小到大，先大写后小写
print(cars)   # 根据字母顺序进行排序，List中不能是非字符串 ['Audi', 'Toyota', 'bmw', 'subaru']
cars.reverse()   # 根据字母顺序从大到小
print(cars)   # ['subaru', 'bmw', 'Toyota', 'Audi']

# 使用sorted对列表排序，临时的
cars = ["bmw", "Audi", "Toyota", "subaru"]
test = sorted(cars)
print(test)
print(cars)     # cars 并未变化

# 倒着打印list
cars = ["bmw", "Audi", "Toyota", "subaru"]
cars.reverse()     # 执行reverse方法之后并不会返回数据  而是直接将列表直接从大到小排列
print(cars)

# 确定列表的长度
cars = ["bmw", 1.0, "Toyota", "subaru"]
print(len(cars))   # 计算列表中有多少元素

# 判断列表是空的方法
cars = ["bmw", 1.0, "Toyota", "subaru"]
if len(cars) == 0:             # 判断列表是否为空
    print("List is empty")
else:
    print(cars[-1])           # 打印最后1个列表的元素
"""
"""
# 操作列表
# 遍历列表
magicians = ['alice', 1.0, 'carolina']
for magician in magicians:
    print("{}".format(magician))       # 遍历的元素允许不是字符串
print("{} is my favorite".format(magician))  # 有缩进就表示语句在for循环之中，否则在for循环之外

magicians = ['alice', 'liu qian', 'carolina']
for i, magician in enumerate(magicians):     # 包含list中的编号
    print("{},{}".format(i, magician))
"""

"""
# 创建数值列表
# 使用range创建数值列表
for value in range(1, 10, 2):   # 从1开始，到10结束，注意不包括10，每次加2
    print(value)
# 创建2维列表
test = []
for i in range(3):
    test.append([])
    for j in range(3):
        test[i].append(j)
print(test)    # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

test = [[1, 2, 3], [4, 5, 6]]
for i in range(0, 2):
    for j in range(0, 3):
        print(test[i][j])     # 对2维列表进行遍历

test = list(range(1, 10, 2))
print(test)

square = []
for i in range(1, 11):
    square.append(i**2)
print(square)             # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  1~10的平方

# 对数据进行简单统计
digits = []
for i in range(1, 21):
    digits.append(i)
print(digits)
print("min is {},max is {}, sum is {}".format(min(digits), max(digits), sum(digits)))

# 列表解析
square = [value**2 for value in range(1, 11)]  # 特殊用法，平常自己写代码不使用，但是别人写了能看懂，注意最后没有冒号
print(square)        # 输出[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

test = [value*0.1 for value in range(1, 11)]  # 特殊用法，平常自己写代码不使用，但是别人写了能看懂，注意最后没有冒号
print(test)      # 输出[0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6000000000000001, 0.7000000000000001, 0.8, 0.9, 1.0]



# 还有1个问题如何产生一个1~10，单位为0.1的列表？range只能实现整数
# 数据从0~10 步长为0.1
test = []
for i in range(101):
    test.append(i/10)
print(test)
"""

"""
# 使用列表的一部分
# 切片（重要）
plays = ['charls', 'martina', 'michael', 'florence', 'eli']
print(plays[1:3])    # 输出['martina', 'michael']  [start：stop] 不包含stop的内容
print(plays[:3])     # 输出['charls', 'martina', 'michael']
print(plays[2:])     # 输出['michael', 'florence', 'eli']
print(plays[-3:])    # 输出['michael', 'florence', 'eli'] -只是表示从结尾数起
print(plays[:-2])    # 输出['charls', 'martina', 'michael']
print(plays[-1])
# 遍历切片
plays = ['charls', 'martina', 'michael', 'florence', 'eli']
for play in plays[1:3]:
    print(play)   # 输出martina \n michael
# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
family_foods = my_foods          # 这种方式my_foods数据与family_foods关联，相当于是同一个列表
friends_foods = my_foods[:]      # 这种方式my_foods和friends_foods是两个列表，相互不影响
family_foods.append('tomato')
friends_foods.append('cannoli')
print(my_foods)       # ['pizza', 'falafel', 'carrot cake', 'tomato']
print(family_foods)   # ['pizza', 'falafel', 'carrot cake', 'tomato']
print(friends_foods)  # ['pizza', 'falafel', 'carrot cake', 'cannoli']
"""


# 元组
# 定义元组 元组与列表很像，但使用圆括号而非中括号来标识。
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 250 将报错  元组不允许修改元素的值

# 遍历所有元素
for dimension in dimensions:
    print(dimension)

# 修改元组变量
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)
# 元组相比于列表更简单，如果需要存储的一组值在程序的整个生命周期内不变就可以使用元组


