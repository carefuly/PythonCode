# -*- coding: utf-8 -*-
# @Date：2025/5/26 14:42:23
# @Author：CJiaの用心
# @FileName：13-集合.py
# @Editor：PyCharm2024
# @Remark：
a = {1, 2, 3, 4, 5}
a.add(6)
print(a)
print(type(a))

b = {1, 2, 3, 4, 5}
b.remove(5)
print(set(b))

a.clear()
b.clear()
print(a)
print(b)
