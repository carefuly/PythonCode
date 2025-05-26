# -*- coding: utf-8 -*-
# @Date：2025/5/26 14:42:02
# @Author：CJiaの用心
# @FileName：10-字典的创建.py
# @Editor：PyCharm2024
# @Remark：
a = {"name": "qs", "age": 18}
print(a)  # {'name': 'qs', 'age': 18}
print(type(a))  # <class 'dict'>

b = dict(name="qs", age=18)
print(b)  # {'name': 'qs', 'age': 18}
print(type(b))  # <class 'dict'>

c = dict([("name", "qs"), ("age", 18)])
print(c)  # {'name': 'qs', 'age': 18}
print(type(c))  # <class 'dict'>

key = ["name", "age"]
value = ["qs", 18]
d = dict(zip(key, value))
print(d)  # {'name': 'qs', 'age': 18}

# 创建的是空的字典
e = dict.fromkeys(["name", "age"])
print(e)  # {'name': None, 'age': None}
