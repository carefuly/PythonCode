# -*- coding: utf-8 -*-
# @Date：2025/3/18 22:41:21
# @Author：CJiaの用心
# @FileName：02 字符串操作.py
# @Editor：PyCharm2024
# @Remark：
demo = "ABCDEF"

# replace(旧字符串, 新字符串) 替换字符串
# 返回新的字符串
new_demo = demo.replace("B", "b")
print(demo)
print(new_demo)

# str() 其他类型转为字符串
print(13, type(13))
print(str(13), type(str(13)))

"""
slice(起始偏移量:终止偏移量:步长) 字符串切片 顾头不顾尾
    [:] 提取整个字符串
    [start:] 从start索引开始到结尾
    [:end] 从头到end-1
    [start:end] 从start到end-1
    [start:end:step] 从start到end-1, 步长为step

# 如果为负数则反过来取
"""
a = "abcdef"
print(a[:])  # abcdef
print(a[2:])  # cdef
print(a[:2])  # ab
print(a[2:4])  # cd
print(a[1:5:2])  # bd

# split("自定义分割符") 分割为数组
# 默认分割空字符串" "
b = "package"
new_b = b.split("a")
print(b)  # package
print(new_b)  # ['p', 'ck', 'ge']

# "指定符号".join() 拼接字符串hello
c = ["h", "e", "l", "l", "o"]
new_c = "".join(c)
new_c2 = "*".join(c)
print(c)  # ['h', 'e', 'l', 'l', 'o']
print(new_c)  # hello
print(new_c2)  # h*e*l*l*o
