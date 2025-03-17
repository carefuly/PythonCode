# -*- coding: utf-8 -*-
# @Date：2025/3/17 14:56:26
# @Author：CJiaの用心
# @FileName：04-时间.py
# @Editor：PyCharm2024
# @Remark：
# 计算机的时间从1970年1月1号0点0时0分开始计算
import time

"""从1970年1月1号0点0时0分到现在的时间"""
date = int(time.time())

# 时间戳
print(date)
# 分钟
minutes = date // 60
print(minutes)
# 天数
days = minutes // (60 * 24)
print(days)
# 年
year = days // 365
print(year)
