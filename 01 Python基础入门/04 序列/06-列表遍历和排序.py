# -*- coding: utf-8 -*-
# @Date：2025/5/26 14:37:07
# @Author：CJiaの用心
# @FileName：06-列表遍历和排序.py
# @Editor：PyCharm2024
# @Remark：
import random

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1. 遍历
for i in a:
    print(i)

# 2. sort() 排序
a.sort()  # 默认升序
print(a)
a.sort(reverse=True)  # 降序
print(a)

# 打乱排序
random.shuffle(a)
print(a)

# 3. sorted(列表) -> 产生新的对象进行排序, 不影响原对象
b = sorted(a)
print(b)

# 4. 最大、最小值、求和
print(max(a))
print(min(a))
print(sum(a))
