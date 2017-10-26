# coding=utf-8
# 数据类型
# comments ues'#' 注释，解释代码
# none 空值
# None
# numeric
# int 整数
# float 浮点数

# 计算符号
# +
# -
# *
# / 浮点数除法
# // 整数除法
# % 求余
# ** 幂 类似 ^

# str
# 引号使用
print('单引号内的str')
print("'双引号扩住的字符串，打印出单引号'")
print("双引号扩住的字符串's，打印字符串中间的单引号,实现\n换行符")
print('''三个单引号扩住的字符串's，打印出字符串中的单引号，实现\n换行符''')
# r 原生字符串 r开头，原生字符串中的转义字原样输出
print(r"r开头字符串，原样打出's，and \n换行符")
# 两个\\，表现\
print('两个\\，print出一个')
# str()数字转换成字符串函数
print(str(16))
print("---------------------------------------------------------------")

# 变量variable
a = 2
b = 3
c = a + b
print(c)
print("---------------------------------------------------------------")
# type()
a = 4
b = '8'
c = '3.1415'
print(type(a))
print(type(b))
print(type(c))
c = float(c)
print(type(c))
print("---------------------------------------------------------------")
# 字节bytes
print(b'hello')
s = b'hellos'
s.decode()
print(s)