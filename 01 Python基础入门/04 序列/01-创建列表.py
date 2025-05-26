# -*- coding: utf-8 -*-
# @Date：2025/5/26 14:12:26
# @Author：CJiaの用心
# @FileName：01-创建列表.py
# @Editor：PyCharm2024
# @Remark：
# 1. 字面量
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c", "d"]
print(a)
print(b)

# 2. list() 方法
print(list("Hello"))

# 3. range(start, end, step) -> 取start到end-1减一的数，步长为step
c = range(0, 5)  # 0, 1, 2, 3, 4
print(c)  # range(0, 5) 对象
print(list(c))  # [0, 1, 2, 3, 4]

# 4. 列表推导式
d = [i for i in range(0, 10)]
e = [i for i in range(0, 100) if i % 2 == 0]
print(e)
