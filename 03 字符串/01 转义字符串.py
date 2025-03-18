# -*- coding: utf-8 -*-
# @Date：2025/3/18 22:37:57
# @Author：CJiaの用心
# @FileName：01 转义字符串.py
# @Editor：PyCharm2024
# @Remark：
"""
特殊字符, 进行转义
    \
    \'
    \"
    \b  退格
    \n  换行
    \t  横向制表符
    \r  回车
"""

print("I \nlove \nyou")
print("I \tlove \tyou")
print("I \'love \'you")
print("I \"love \"you")

"""
字符串拼接

必须+号两边的类型都相同才能运算, 否则报错

字符串复制 *
"sxt" * 3  => sxtsxtsxt
"""
print("a" + "b" + "c")
# 报错
# print("a" + 13)、
print(13 + 14)

"""
控制台读取字符串
input()
"""
name = input("请输入你的名称：")
print(name)
