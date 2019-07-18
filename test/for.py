# for循环
# for语句可以用来遍历序列或可迭代对象的每一个元素
# 可迭代对象：
# 字符串：str  列表：list  元组 tuple   字典:dict 集合：set
# 固定集合： forzenset   迭代器
#
# 语法：for 变量 in 可迭代对象 :
#               语句块1

# b=int(input("请输入数字"))
# list=[1,2,3]
# for：
#     if b in list:
#          print("你赢了")
#     else:
#          print("输入有误")
# str = 'hello world'
# for i in s*r:
#     print(i)
#
# else:
#      print("循环结束")
# import random
# menu = '''(0)石头
# (1)剪刀
# (2)布
# (q)结束游戏
# '''
#
# #存放所有的出拳
# all_list = ["石头","剪刀","布"]
# c = random.choice(all_list)
# y = input(menu)
#
# if y in ['0','1','2','q']:
#     if y == 'q':
#         print("游戏结束")
#     else:

#         you = all_list[int(y)]           此句不理解
#         if you == c:
#             print("平局")
#         elif (you == "石头" and c == "剪刀") \
#             or (you == "剪刀" and c == "布") \
#             or (you == "布" and c == "石头"):
#             print("你赢了")
#         else:
#             print("电脑赢了")
# else:
#     print("输入无效")
# a=int(input("请输入一个整数"))
# b=1
# c=0
# for b in range(1,a+1):
#     c=c+b
# print(c)



# import random
# mima='qwertyuiopasdfghjklzxcvbnm1234567890_'
# c=random.choice(mima)
# d=''
# a=input(input("请输入密码位数"))
# b=1
# for b in range(a):


# 现有一个已经设定好登录名和密码的系统，现有一个用户忘记登录账号及密码
# 此登录系统只有三次尝试机会，请编写一个用户登录系统，如果在3次之内当用户
# 输入账号密码跟设定密码匹配，则登录成功，否则登录失败，并且当你在输错的时
# 提示还有几次机会。
#
# a=(123)
# b=(456)
# e=1
# while e<=3:
#     c=int(input("请输入用户名"))
#     d=int(input("请输入密码"))
#     if (c==a and d==b):
#         print("登录成功")
#         break
#     elif (c!=a or d!=b and e==1):
#         print("输入错误,还剩2次机会")
#         e=e+1
#         # continue
#     elif (c!=a  or d!=b and e==2):
#         print("输入错误，还剩1次机会")
#         e=e+1
#         continue
#     elif (c!=a  or d!=b and e==3):
#         print("输入错误，您的账户已被锁定")
#         break


# a=123
# b=456
# e=1
# while e<=3:
#     c=int(input("请输入用户名"))
#     d=int(input("请输入密码"))
#     if (c==a and d==b):
#         print("登录成功")
#         break
#     elif (c!=a or d!=b and e==1):
#         print("输入错误,还剩2次机会")
#         e=e+1
#         # continue
#     elif (c!=a  or d!=b and e==2):
#         print("输入错误，还剩1次机会")
#         e=e+1
#         # continue
#     elif (c!=a  or d!=b and e==3):
#         print("输入错误，您的账户已被锁定")
#         e=e+1

# a=''
# b=''
# for m in range(1,10):
#   for n in range(1,10):
#     print("%d *%d =%d " %(m,n,m*n))
#
#   print()
# c=1
# a="a a a cd fda fa "
# for m in a:
#
#   prin("%s=%s (c,m))
#   c=c+1



# str="hello world"
#
# for i in str:
#
#   print(i)
#   if i=="o":
#     break

# 1   2  3    4     5
# 10  5  2.5  2.5/2 2.5/2/2


# a=int(input("请输入一个整数"))
#
# c=a
#
# for b in range(1,3):
#   a=a/2
#   c+=a*2
# print(c,a/2)

h = int(input("请输入初始高度"))
sum = h
for i in range(2):
    h = h/2
    sum += h*2
    print(sum, h / 2)

