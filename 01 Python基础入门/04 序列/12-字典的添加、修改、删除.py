# -*- coding: utf-8 -*-
# @Date：2025/5/26 14:42:15
# @Author：CJiaの用心
# @FileName：12-字典的添加、修改、删除.py
# @Editor：PyCharm2024
# @Remark：

""" 1. 添加 """
# 1.1 直接添加
a = {"name": "qs", "age": 20}
a["price"] = 100
print(a)

# 1.2 使用update() -> 将新的字典覆盖旧的字典, 重复覆盖
b = {"name": "qs", "age": 18}
c = {"name": "qss", "age": 18, "address": "山卡卡"}
b.update(c)
print(b)

""" 2. 删除"""
# 2.1 del()
d = {"name": "qss", "age": 18, "address": "山卡卡"}
# del d["name"]
# del (d["age"])
print(d)

# 2.2 clear() -> 清空字典
# d.clear()
print(d)

# 2.3 pop() -> 指定删除
# d.pop("age")
print(d)

# popitem() -> 随机删除
print(d.popitem())
print(d)
