# -*- coding: utf-8 -*-
# @Date：2024/12/28 01:02:57
# @Author：CJiaの用心
# @FileName：02 海龟绘图-奥运五环.py
# @Editor：PyCharm2024
# @Remark：
import turtle

# 第一个圆
turtle.width(5)
turtle.color("red")
turtle.circle(50)

# 第二个圆
turtle.penup()
turtle.goto(80, 0)
turtle.pendown()
turtle.color("blue")
turtle.circle(50)

# 第三个圆
turtle.penup()
turtle.goto(160, 0)
turtle.pendown()
turtle.color("green")
turtle.circle(50)

# 第四个圆
turtle.penup()
turtle.goto(40, -50)
turtle.pendown()
turtle.color("yellow")
turtle.circle(50)

# 第五个圆
turtle.penup()
turtle.goto(120, -50)
turtle.pendown()
turtle.color("black")
turtle.circle(50)

# 一直显示窗口
turtle.done()
