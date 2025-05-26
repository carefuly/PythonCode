# -*- coding: utf-8 -*-
# @Date：2025/5/26 14:41:56
# @Author：CJiaの用心
# @FileName：09-生成器推导式.py
# @Editor：PyCharm2024
# @Remark：
"""
生成器推导式生成的不是列表也不算元组而是一个生成器对象
可以转换为列表和元组, 也可以使用生成器对象的_next_()方法进行遍历
"""

a = (x for x in range(10))
print(a)  # <generator object <genexpr> at 0x0000023553A14350>
print(type(a))  # <class 'generator'>
print(tuple(a))

b = (x for x in range(3))

print(b.__next__())  # 0
print(b.__next__())  # 1
print(b.__next__())  # 2
