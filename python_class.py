# 创建类
class Dog:
    def __init__(self, name, age):  # init是类中特殊的方法，创建一个类时就会被调用
        self.name = name   # name属性
        self.age = age    # 年龄属性
    #  只隔1行

    def sit(self):
        print('{} is now sitting'.format(self.name))

    def roll_over(self):
        print('{} rolled over!'.format(self.name))


my_dog = Dog('wangwang', 3)  # 创建1个dog实例
print('my doy\'s name is {}'.format(my_dog.name))
my_dog.sit()      # 调用Dog类中sit方法

# 创建多个实例
your_dog = Dog('tiantian', 2)
print('your dog\'s name is {}'.format(your_dog.name))
print(your_dog)  # 可以理解your_dog是一个指针的地址

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # 给属性指定默认值
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = '{} {} {}'.format(self.year, self.make, self.model)
        return long_name

    def read_odometer(self):  # 读取公里数
        return self.odometer_reading

    def update_odometer(self, odometer):  # 通过方法修改属性值
        if odometer > self.odometer_reading:   # 输入的里程数必须比之前的大才有效
            self.odometer_reading = odometer
        else:
            print('your can\'t roll back an odometer!')

    def fill_gas_tank(self, gas):
        print('fill {} gas in tank'.format(gas))


my_new_car = Car('audi', 'a4', 2019)
print('{}'.format(my_new_car.get_descriptive_name()))
print('{}'.format(my_new_car.read_odometer()))

# 修改属性的值
my_new_car.odometer_reading = 20
print('{}'.format(my_new_car.read_odometer()))

# 通过方法修改属性的值,这样的好处是可以在函数中增加处理，例如输入值有效性的判断
my_new_car.update_odometer(23)
print('{}'.format(my_new_car.read_odometer()))

my_new_car.update_odometer(20)
print('{}'.format(my_new_car.read_odometer()))  # your can't roll back an odometer!

# 继承
"""
class ElectricCar(Car):  # electriccar 继承car
    
    # 初始化父类所有属性
    # 再初始化子类的特有属性
    

    def __init__(self, make, model, year):
        super().__init__(make, model, year)   # 调用父类的初始化函数
        self.battery = 75

    def describe_battery(self):
        # 打印一条描述电瓶信息的消息 
        print('This car has a {}-kwh battery'.format(self.battery))

    # 重写父类的fill_gas_tank方法,输入的参数可以与父类的有所不太
    def fill_gas_tank(self):
        print('this car doesn\'t need gas tank')


my_tesla = ElectricCar('tesla', 'model', 2019)
print(my_tesla.get_descriptive_name())  # 调用父类中的get_descriptive_name方法
my_tesla.describe_battery()  # 描述电量
my_tesla.fill_gas_tank()
"""

# 将实例用作属性
class ElectricCar(Car):  # electriccar 继承car

    # 初始化父类所有属性
    # 再初始化子类的特有属性

    def __init__(self, make, model, year):
        super().__init__(make, model, year)  # 调用父类的初始化函数
        self.battery = Battery()     # 将Battery实例作为battery的属性(重要)

    # 重写父类的fill_gas_tank方法,输入的参数可以与父类的有所不太
    def fill_gas_tank(self):
        print('this car doesn\'t need gas tank')

# 单独定义一个Battery的类
class Battery:

    def __init__(self, battery_size=70):
        self.battery = battery_size

    def describe_battery(self):
        # 打印一条描述电瓶信息的消息
        print('This car has a {}-kwh battery'.format(self.battery))

# 使用from car import Car 从car.py这个文件中导入Car这个类
# 使用from car import Car, ElectricCar导入多个类
# 使用from module_name import * 导入所有类
# 使用别名from electric_car import ElectricCar as ES


from random import randint,choice


num = randint(1, 6)  # 得到1~6之间的一个整数
print(num)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)  # 随机取列表中的数据
print(first_up)

