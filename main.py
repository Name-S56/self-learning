# coding=utf-8

# 输入两个正整数a,b
a = int(input())
b = int(input())

# 请在此添加代码，求两个正整数的最小公倍数
########## Begin ##########
def lcm(x, y):
    c =x*y
    while (y != 0):
        temp = y
        y = x % y
        x = temp
    return c//x

print(lcm(a,b))
