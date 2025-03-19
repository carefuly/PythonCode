# -*- coding: utf-8 -*-
# @Date：2025/3/19 15:24:09
# @Author：CJiaの用心
# @FileName：05-可变字符串.py
# @Editor：PyCharm2024
# @Remark：
import io

# io.StringIO(字符串) 创建可变的字符串
aio = io.StringIO("abc")
# 获取字符串值
print(aio.getvalue())
# 找到指定位置的值
aio.seek(1)
aio.write("d")
print(aio.getvalue())
