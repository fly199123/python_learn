# 文件操作
# 读取文件
file_name = './digits.txt'  # 读取路径，
with open(file_name) as file_obj:
    contents = file_obj.read()
print(contents)

# 文件的路径
# 可以是相对路径，也可以是绝对路径
# windows系统使用反斜杠(\)而不是(/)，但是在代码中依然可以使用斜杠
# 如果使用反斜杠需要注意一个问题，字符串中的字符进行转义如'C:\\path\\to\\file.txt'

# 逐行读取
file_name = './digits.txt'  # 读取路径，
with open(file_name) as file_obj:
    for line in file_obj:
        print(line)


# 创建一个列表，将每一行数据放入该列表中(重要)，这个应该比较常用
file_name = './digits.txt'  # 读取路径，
with open(file_name) as file_obj:
    lines = file_obj.readlines()
    line = file_obj.readline()


for line in lines:
    print(line)


print(int(line)+1)  # 读进来的是字符串数据 需要转化成int类型才能进行数值运算

# 写入文件
# 写入空文件
file = 'programing.txt'

with open(file, 'w') as file_obj:      # mode默认是read 可以改为write ,w的写入是在整个文件每次运行时会重新写入
    file_obj.write('I love programming! 易涛')   # 默认是UTF-8格式写入

# 附加到文件
file = 'programing.txt'

with open(file, 'a') as file_obj:      # a 是附加模式，及在原来的内容基础上加入现有内容
    file_obj.write('加油！')

# 异常处理
# 处理zeroDivisionError异常
# 使用try-except代码块
# 使用异常避免崩溃
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")


while True:
    first_num = input('\n First number:')
    if first_num == 'q':
        break
    second_num = input('Second number:')
    if second_num == 'q':
        break
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(answer)


# 处理FileNotFoundError异常
def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass  # 异常发生之后什么也不处理
    else:  # 分析文本
        # 计算该文件大致包含了多少个单词
        words = contents.split()
        num_word = len(words)
        print('the file {} has about {} words'.format(filename, num_word))


file_name = 'alice.txt'
count_words(file_name)

# 存储数据
# 使用json.dump()和json.load()
import json

number = [1, 2, 3, 4, 5]

file_name = 'num.json'
with open(file_name, mode='w') as f:
    json.dump(number, f)

