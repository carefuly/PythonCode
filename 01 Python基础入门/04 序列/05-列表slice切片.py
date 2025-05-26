# -*- coding: utf-8 -*-
# @Date：2025/5/26 14:35:25
# @Author：CJiaの用心
# @FileName：05-列表slice切片.py
# @Editor：PyCharm2024
# @Remark：
""" 和字符串切片一模一样的 """
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(a[:])  # 提取全部 -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[1:])  # 从索引到结尾 -> [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[:8])  # 从头到end-1 -> [1, 2, 3, 4, 5, 6, 7, 8]
print(a[0:3])  # 从start到end-1 -> [1, 2, 3]
print(a[0:6:2])  # 从start到end-1, 步长为step -> [1, 2, 3]
