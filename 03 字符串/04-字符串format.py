# -*- coding: utf-8 -*-
# @Date：2025/3/19 15:18:51
# @Author：CJiaの用心
# @FileName：04-字符串format.py
# @Editor：PyCharm2024
# @Remark：

a = "名字是：{0}, 年龄是：{1}"
b = "名字是：{name}, 年龄是：{age}"
c = "名字是：{0}, 存款有：{1:.2f}"

print(a.format("张三", 18))
print(b.format(name="李四", age=20))
print(c.format("王二", 3888.31454))
