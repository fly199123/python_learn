# python中字典是重要的一个概念

# 一个简单的字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# 使用字典
# 字典是用{}一系列键值对表示

# 访问字典中的值
alien_0 = {'color': 'green'}
print(alien_0['color'])

# 添加键值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 创建一个空的字典
alien = {}
alien['color'] = 'green'
alien['points'] = 5
print(alien)

# 修改字典里面的值
alien_0 = {'color': 'green'}
print('the alien is {}'.format(alien_0['color']))

alien_0['color'] = 'yellow'
print('the alien is {}'.format(alien_0['color']))

alien_0 = {'x_position': 25, 'y_position': 25, 'speed': 'medium'}
print('original x_position :{}'.format(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# 新的位置为旧的位置加上移动距离
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('new x_position is {}'.format(alien_0['x_position']))


# 删除键值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# 使用get来访问值
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points']) 将报错，因为没有points键
print(alien_0.get('points'))   # 返回是None

# 遍历字典
for key, value in alien_0.items():
    print('{}:{}\n'.format(key, value))

# 遍历字典中所有值,keys可以省略，遍历字典时默认遍历key值
for key in alien_0.keys():
    print('{}\n'.format(alien_0[key]))

for key in alien_0:
    print('{}\n'.format(alien_0[key]))

print(alien_0.keys())

# 按照特定顺序遍历字典中所有键值,按照keys值的字母从小到大排序
for key in sorted(alien_0.keys()):
    print('{}\n'.format(alien_0[key]))

# 遍历字典中的所有值
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for value in favorite_languages.values():
    print('{}\n'.format(value))
print('------------------------\n')
# 剔除字典中一致的值
for value in set(favorite_languages.values()):
    print('{}\n'.format(value))

print('------------------------\n')
# 嵌套
# 创建一个用于存放外星人的字典
aliens = []
for alien_num in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    alien['color'] = 'yellow'
    alien['points'] = 10
    alien['speed'] = 'fast'
for alien in aliens:
    print('{}\n'.format(alien))

for i, alien in enumerate(aliens):
    if alien.get('color') == 'yellow':  # 打印出黄色alien
        print('{}'.format(i))

# 在字典中存储列表
pizza = {'crust': 'thick',
         'toppings': ['mushroom', 'extra cheese'],
         }
print('your ordered a {} pizza'.format(pizza['crust']))

for topping in pizza['toppings']:
    print('\t' + topping)

toppings = pizza['toppings']
for topping in toppings:
    print('\t' + topping)


# 字典中存储字典 很像json数据
users = {
        'aeinstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton'
        },
        'mcurie': {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris'
        }
}
for name, info in users.items():
    print('Username:{}'.format(name))
    print('first:{}'.format(info['first']))
    print('last:{}'.format(info['last']))
    print('location:{}'.format(info['location']))
