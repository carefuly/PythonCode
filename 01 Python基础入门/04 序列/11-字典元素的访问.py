# -*- coding: utf-8 -*-
# @Date：2025/5/26 14:42:09
# @Author：CJiaの用心
# @FileName：11-字典元素的访问.py
# @Editor：PyCharm2024
# @Remark：
a = {"name": "qs", "age": 18}

# 1. 获取指定的键 -> 推荐get方法(指定不存在的默认值)
print(a["name"])
print(a.get("age"))
print(a.get("price", None))

# 2. 列出所有的键值对
print(a.items())
# 3. 列出所有的键、值
print(a.keys())
print(a.values())
