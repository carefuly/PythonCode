# -*- coding: utf-8 -*-
# @Date：2025/5/26 14:30:53
# @Author：CJiaの用心
# @FileName：04-列表元素的访问计数.py
# @Editor：PyCharm2024
# @Remark：
a = [10, 20, 30, 40, 50, 20, 20, 30, 40, 50, 20, 30, 10]

# 1. 索引 列表[0, len(列表) - 1]
print(a[0])  # 10
print(a[len(a) - 1])  # 10

# 2. index(value, [start, [end]]) 获取指定元素在列表首次出现的索引 -> [] 可变参数
print(a.index(30))  # 2
print(a.index(30, 1))  # 2 -> 从索引为1开始到结尾找第一次出现的元素
print(a.index(30, 2, 7))  # 2 -> 从索引为1到索引为7-1范围找第一次出现的元素

# 3. count() 元素出现的次数
print(a.count(20))  # 4
