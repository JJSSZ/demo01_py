# 省略字段名传递参数位号
print('我叫{}，今年{}岁，我爱吃{}和{}。'.format('JJSSZ', 99,'香蕉', '苹果'))

# 不省略字段名传递参数位号(在使用位号时，要么全部用，要么全部不用)
print('我叫{0}，今年{1}岁，我爱吃{2}和{3},{3}和{2}也爱吃我。'.format('JJSSZ', 99,'香蕉', '苹果'))
# 错误示范
# print('我叫{0}，今年{}岁，我爱吃{}和{3},{3}和{2}也爱吃我。'.format('JJSSZ', 99,'香蕉', '苹果'))

# 也可以用混合字段名，但是起了别名的参数位号不在可用，如下不可再用位号3传递‘苹果’这个参数
print('我叫{0}，今年{1}岁，我爱吃{my2}和{my1},{my1}和{my2}也爱吃我。'.format('JJSSZ', 99,my2 = '香蕉', my1 = '苹果'))



# format() 函数还可以使用 *元组 和 **字典 的形式传参，两者可以混合使用。
# 位号参数、关键字参数、*元组 和 **字典 也可以同时使用，但是，位置参数要在关键字参数前面，*元组 要在 **字典 前面。

# 使用元组传参(元组传递需要在元组名前面加上*)
jjssz = ('JJSSZ', 999, 'mo')
print('我是{}, 身价{}亿。' .format(*jjssz))
print('你是{2},身价{1}亿。' .format(*jjssz))

# 使用字典传参(字典传递需要在字典名前面加上**)
jjssz = {'name': 'JJSSZ', 'age':99, 'weakness': '美女'}
print('我是{name},我的弱点是{weakness},今年{age}岁。' .format(**jjssz))

# 同时使用元组和字典传参
hobby = ('搞钱', '学习', '美女')
jjssz = {'name': 'JJSSZ', 'feature': 'hobby'}
print('{0}, {1}和{2}是{name}最喜欢的{feature}'.format(*hobby, **jjssz))




'''
x = 5 
y = 4
z = 9.9999
a = pow(x,y,int(z))
print(a)

b = round(z,2)
print(b)

import math
h = math.hypot(5,12)
print(h)

h = math.acos(1/2)
print(math.degrees(h))

h = math.acosh(5)
print(h)
'''