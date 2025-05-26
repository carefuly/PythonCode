# -*- coding: utf-8 -*-
# @Date：2025/5/26 14:41:49
# @Author：CJiaの用心
# @FileName：08-元组的访问和操作.py
# @Editor：PyCharm2024
# @Remark：

""" 1. 元组的操作方式和列表基本一致, 唯一不同是不能修改元素 """
a = (1, 2, 3, 4, 5, 5, 7, 8, 9)

print(a[0])
print(a[1])

print(a[2: 4])
print(a.index(5))
print(a.count(5))

"""
    2. zip(多个列表...) 方法
    将多个列表对应位置的元素组合成为数组, 返回这个zip对象
"""
z1 = (10, 20, 30)
z2 = (40, 50, 60)
z3 = (70, 80, 90, 100)
z = zip(z1, z2, z3)
print(z)  # <zip object at 0x000001DE87BBA340>
print(list(z))  # [(10, 40, 70), (20, 50, 80), (30, 60, 90)]
