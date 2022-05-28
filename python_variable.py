
# 字符串
# print("hello Python world!")

"""
msg = "hello world"
print(msg)
"""

"""
name = "abc love"
print(name.title())  # 将每个单词的首字母变成大写
test = name.upper()
print(test)  # 将字符串变成大写
print(test.lower())  # 将字符串变成小写
"""

"""
first_name = "ada"
last_name = "lovelace"
full_name = "{} {}".format(first_name, last_name)  # 在字符串中使用变量
print(full_name)       # ada lovelace
print(full_name.title())  # Ada Lovelace
"""

"""
# 使用制表符或换行符添加空白
print("languages:\n\tPython\n\tC\n\tJavaScript")   # 在字符串中使用转义字符
"""

"""
# 删除字符串中多余空格
test = " I Love lys     "   # 加字符串后面的空格一共15个字符长度
print(len(test))        # 16
temp = test.rstrip()  # 删除字符串中多余空格
print(len(temp))  # 11,字符串后面空格字符被删除，字符串前面的未被删除
print(test.lstrip())  # 字符串前面的字符被删除
print(len(test.strip()))   # 删除字符串前面和后面多余的空格字符
"""

# 数
# 整数(加减乘除)
print("{} {} {} {}".format(3+2, 3-2, 2*3, 1/3))  # 5 1 6 0.3333333333333333
# 乘方
print("{} {} {}".format(3**2, 3**3, 10**6))   # 9 27 1000000  空格不影响计算结果
# 浮点数
print("{} {} {} {}".format(0.2+0.1, 0.2+0.2, 2*0.1, 2*0.2))   # 0.30000000000000004 0.4 0.2 0.4 浮点运算小数位可能不确定
# 整数和浮点数
print("{} {} {}".format(1+2.0, 2**3.0, 3.0**2))  # 3.0 8.0 9.0 无论哪种操作只要操作数有浮点数据则
# 数中的下划线
test = 12000000       # 虽然会提示存在问题，但还是能正常显示_用于分开数据
print("{}".format(test))  # 12000000
# 同时对多个变量赋值（重要）
x, y, z = 1, 2, 3
print(x, y, z)  # 输出多个变量





