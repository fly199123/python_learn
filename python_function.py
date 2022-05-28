# 定义函数
def green_user():
    """
    显示简单的问候语
    :return:
    """
    print("hello!")


# 向函数传递信息
def green_user(user_name):
    """
    显示简单的问候语
    :return:
    """
    print("hello,{}!".format(user_name))


# 传递实参
def describe_pet(animal_type, pet_name):
    """
    显示宠物信息
    :param animal_type:
    :param pet_name:
    :return:
    """
    print('\n I have a {}'.format(animal_type))
    print('\n my {}\'s name is {}'.format(animal_type, pet_name))


# 多次调用函数
describe_pet('dog', 'Tom')
describe_pet('cat', 'jerry')


# 关键字实参,函数声明：describe_pet(animal_type, pet_name)，通过关键字可以交换输入顺序
describe_pet(pet_name='jerry', animal_type='cat')


# 默认值
def describe_pet(pet_name, animal_type='dog'):
    """
    显示宠物信息
    :param animal_type:
    :param pet_name:
    :return:
    """
    print('\n I have a {}'.format(animal_type))
    print('\n my {}\'s name is {}'.format(animal_type, pet_name))


describe_pet('Tom')


# 返回值
def get_formatted_name(first_name, last_name):
    full_name = '{} {}'.format(first_name, last_name)
    return full_name


print(get_formatted_name('yi', 'tao'))


# 输入值可选 通过给与默认值就能实现
def get_formatted_name(first_name,  last_name, mid_name=''):
    full_name = '{} {} {}'.format(first_name, mid_name, last_name)
    return full_name


print('{} love {}\n'.format(get_formatted_name('yi', 'tao'), get_formatted_name('lai', mid_name='yu', last_name='shuang')))


# 返回一个字典
def build_person(first_name, last_name, age=None):
    person = {'first_name': first_name, 'last_name': last_name}

    if age:
        person['age'] = age

    return person


print(build_person('yi', 'tao', 30))


# 结合使用函数和while
def get_formatted_name(first_name, last_name):
    full_name = '{} {}'.format(first_name, last_name)
    return full_name


while True:
    first_name = input('first name:')
    if first_name == 'q':
        break
    last_name = input('last name:')
    if last_name == 'q':
        break
    name = get_formatted_name(first_name, last_name)
    print('hello! {}'.format(name))


# 传递列表
def greet_users(names):
    """ 向列表中的每位用户发出简单的问候"""
    for name in names:
        print('hello, {}'.format(name))


users = ['hannah', 'ty', 'margot']
greet_users(users)


# 在函数中修改列表
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('printing model:{}'.format(current_design))
        completed_models.append(current_design)


def show_completed_models(completed_models):
    for model in completed_models:
        print(model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []


# 禁止函数修改列表
print_models(unprinted_designs[:], completed_models)  # 将unprinted_designs的内容复制给他的副本，然后操作副本
show_completed_models(completed_models)
show_completed_models(unprinted_designs)  # unprinted_designs没有因为pop操作变成空列表，而是维持现状


# 传递任意数量的实参(重要)
def make_pizza(*toppings):  # *toppings 实际是创建1个toppings的元组，所有传入参数都放在元组中
    for topping in toppings:
        print(topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    print('cake size is {}'.format(size))
    for topping in toppings:
        print(topping)


make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 使用任意数量的关键字实参(特别重要) 其实就是键值对
def build_profile(first, last, **user_info):  # **user_info是创建1个空字典，所有键值对存入
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('yi', 'tao', location='changsha', field='math')
print(user_profile)  # 输出{'location': 'changsha', 'field': 'math', 'first_name': 'yi', 'last_name': 'tao'}


# 将函数存储在模块中
# 导入整个模块
# import module_name
# 导入模块中的特定函数
# from module_name import fuction_name, fuc_1, fuc_2   可以多个函数一同导入
# 使用as给函数指定别名
# from pizza import make_pizza as mp
# 使用as给模块指定别名
# import pizza as pz
# 导入模块中的所有函数
# from pizza import *

