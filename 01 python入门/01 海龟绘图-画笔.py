# -*- coding: utf-8 -*-
# @Date：2025/3/16 23:24:57
# @Author：CJiaの用心
# @FileName：01 海龟绘图-画笔.py
# @Editor：PyCharm2024
# @Remark：
import turtle

# 显示箭头
turtle.showturtle()
turtle.write("用心")
# 前进指定像素
turtle.forward(300)
# 改变画笔的颜色
turtle.color("red")
# 箭头左转90度
turtle.left(90)
turtle.forward(300)
# 回到坐标原点
turtle.goto(0, 0)
# 抬起笔
turtle.penup()
turtle.goto(0, 50)

turtle.pendown()
turtle.circle(100)
# 一直显示窗口
turtle.done()
