"""
# 使用input函数输入数据，输入的数据时字符串
name = input('please enter your name\n')
print('hello, {}'.format(name))

# 使用int将输入数据转化成整型
age = input('how old are you?\n')
age = int(age)  # 将输入数据转化成整数型
if age >= 18:
    print('you are an adult\n')
else:
    print('you are a juveniles\n')

# 求模运算
number = input('Enter a number, and I\'ll tell you if it\'s even or odd:\n')
number = int(number)
if number % 2 == 0:
    print('it is a odd number\n')
else:
    print('it is a even number\n')

"""

# while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number = current_number + 1

# 让用户选择退出,使用while死循环
while True:
    msg = input()
    if msg == 'q!':
        break
    else:
        print(msg)

# 如果进入死循环可以使用ctrl+C结束进程

# 使用while循环处理列表和字典
# 在列表之间移动元素
unconfirmed_users = ['alien', 'brian', 'candace']
comfirmed_users = []

while unconfirmed_users:
    current = unconfirmed_users.pop()
    print('verifying user:{}'.format(current))
    comfirmed_users.append(current)

for user in comfirmed_users:
    print(user)
print(unconfirmed_users)

# 删除特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'cat', 'goldfish']
i = 0;
while i < len(pets):
    if pets[i] == 'cat':
        print('{}\n'.format(i))
        pets.pop(i)
        continue
    i = i + 1
print(pets)

# 使用用户输入来填充字典
responses = {}

while True:
    name = input('\nwhat is your name?\n')
    response = input('which mountain would you like to climb someday?')
    responses[name] = response

    # 看看是否还有人要参加调查
    repeat = input('would you like to let another person respond?(yes/no)')
    if repeat == 'no':
        break

# 输出结果
print(responses)
