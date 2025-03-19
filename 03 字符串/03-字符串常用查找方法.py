# -*- coding: utf-8 -*-
# @Date：2025/3/18 22:54:52
# @Author：CJiaの用心
# @FileName：03-字符串常用查找方法.py
# @Editor：PyCharm2024
# @Remark：

test = """博客介绍：分享嵌入式开发领域的相关知识、经验、思考和感悟,欢迎关注。
提供嵌入式方向的学习指导、简历面试辅导、技术架构设计优化、开发外包等服务，有需要可私信联系。"""

# len() 长度
print(len(test))  # 81

# startswith() 以指定的字符串开头
print(test.startswith("博客介绍"))  # True
print(test.startswith("你好"))  # False

# endswith() 以指定的字符串结尾
print(test.endswith("联系。"))  # True
print(test.endswith("联系"))  # False

# find() 第一次出现字符串的位置
print(test.find("入"))  # 8

# rfind() 最后一次出现字符串的位置
print(test.rfind("入"))  # 38

# count() 指定字符串总共出现了几次
print(test.count("入"))  # 2

# isalnum() 所以字符串全是字母或者数字
print(test.isalnum())  # False

demo = "*s*t*r*"

# strip() 去除首尾信息
print(demo.strip("*"))  # s*t*r

# l strip() 去除左边信息
print(demo.lstrip("*"))  # s*t*r*
# r strip() 去除右边信息
print(demo.rstrip("*"))  # *s*t*r

a = "love post SQL, love TXT"

# capitalize() 产生新的字符串,首字母大写
print(a.capitalize())  # Love post sql, love txt

# title() 产生新的字符串,每个单词都首字母大写
print(a.title())  # Love Post Sql, Love Txt

# upper() 产生新的字符串,所有字符全转成大写
print(a.upper())  # LOVE POST SQL, LOVE TXT

# lower() 产生新的字符串,所有字符全转成小写
print(a.lower())  # love post sql, love txt

# swap case()产生新的,所有字母大小写转换
print(a.swapcase())  # LOVE POST sql, LOVE txt

b = "SXT"

# center(), ljust(), rjust() 这三个函数用于对字符串实现排版
print(b.center(10, "*"))  # ***SXT****
print(b.ljust(10, "*"))  # SXT*******
print(b.rjust(10, "*"))  # *******SXT
