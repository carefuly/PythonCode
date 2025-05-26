# -*- coding: utf-8 -*-
# @Date：2025/3/17 14:41:36
# @Author：CJiaの用心
# @FileName：02-常量.py
# @Editor：PyCharm2024
# @Remark：
# 1. 常量
PI = 3.141592653589793
MAX_SPEED = 6371
print(PI)
print(MAX_SPEED)

# 2. 链式赋值
# a=1 b=3 c=5
a, b, c = 1, 3, 5
print(a, b, c)

# 3. 交换两个变量的值
x = 100
y = 200
print("交换之前：", x, y)
x, y = y, x
print("交换之后：", x, y)
print(x, y)
