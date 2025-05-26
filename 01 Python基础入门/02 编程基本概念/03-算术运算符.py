# -*- coding: utf-8 -*-
# @Date：2025/3/17 14:53:12
# @Author：CJiaの用心
# @FileName：03-算术运算符.py
# @Editor：PyCharm2024
# @Remark：
"""
+   加法  1+1=2
-   减法  1-1=0
*   乘法  1*2=2
/   浮点数除法   8/2=4.0
//  整数除法    7/2=3 => 3.5(取整数)
%   模(取余)   7%4=3
**  幂   2**3=8 => 2的三次方
"""

# 同时得到商和余数
num = divmod(13, 3)
print(num)  # (4, 1) (商, 余数)

# round 进行四舍五入，产生新的对象
c = 8.3
d = round(c)
print(c, d)
