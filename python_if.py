# if语句 简单例子
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 条件测试
# 比较时有大小写区分
car = 'Audi'
print('{}'.format(car == 'audi'))   # 数据有大小写区分

# 检查不相等
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('hold the anchovies')

# 数值比较
age = 18
print("{}\n{}\n{}\n".format((age < 21), (age <= 21), (age > 21)))  # True True  False

# 检查多个条件
# 使用and 和or连接
age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 21:
    print("true")
else:
    print("false")

# 检查特定值是否在列表中
requested_topping = ['mushrooms', 'onions', 'pineapple']

temp = 'mushrooms' in requested_topping   # for循环中常常使用，返回值为True or False
print(temp)

# 检查特定值不包含在列表中
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print("{},you can post a response if you wish".format(user.title()))

# if语句
age = 19
if age >= 18:
    print("you are old enough to vote")


# if-else语句
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you register to vote yet?")
else:
    print("sorry, you are too young to vote")
    print("please register to vote as soon as you turn 18 !")


# if-elif-else结构
age = 12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40")

# 使用多个elif 省略else代码块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(" Your admission cost is {}".format(price))


# 使用if语句处理列表
# 检查特殊元素
requested_topping = ['mushrooms', 'onions', 'pineapple']
for request in requested_topping:
    if request == 'onions':
        print("sorry, we are out of onions right now")
    else:
        print("adding {}".format(request))

# 判断空列表
test = []
if len(test) == 0:            # 判断列表为空   test is None 不起作用
    print("list is empty")
else:
    print("list have element")


# 使用多个列表
available_toppings = ['mushrooms', 'onions', 'pineapple']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested in requested_toppings:
    if requested in available_toppings:
        print("add {}".format(requested))
    else:
        print("sorry, we don't have {}".format(requested))
print("\n finished making your pizza!")
