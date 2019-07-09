#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'这里是注释信息'

__author__ = 'Mat K'

'''
print("你好")

print('ABC'.encode("ascii"))
print('中文'.encode("utf-8"))

print(b'abc'.decode("ascii"))

print(len('abc'))
print(len(b'abc'))
print(len('你好'))

print(len('abc'.encode("ascii")))

# 格式化输出
print('hello %s' % 'world')
print('hello %s, this is %d year' % ('world', 2018))


# list 使用, 使用中括号 []
# list 的成员也可以是另外一个成员

# list 的方法 :
# list.pop()  用于删除尾部成员
# list.append('aa') 添加新成员
# list ....

# tuple 使用，使用小括号，相当于只读的 list
# tuple 的成员中可通过包含 list 来实现可变 tuple ：
#   douzhk=[4, 5, 6];  (1, 2, 3, douzhk)
'''

'''
print ("input your age : ")
age = int(input())
if age == 30:
    print ("而立")
elif age == 40:
    print ("不惑")
elif age == 50:
    print ("知天命")
else:
    print ("孔子不知道")

print ("身高 : ")
height=float(input())
print ("体重 : ")
weight=float(input())
bmi=weight/(height * height)
print ("bmi : %s" % bmi)

if bmi < 18.5:
    print ("过轻")
elif bmi < 25:
    print ("正常")
elif bmi < 28:
    print ("过重")
elif bmi < 32:
    print ("肥胖")
else:
    print ("严重肥胖")
'''


'''
sum=0
for x in (1, 2, 3):
    sum+=x
print ("sum : %d" % sum)

# range 使用
# range (value) 每次返回一个值, 从 0 到 value - 1
# range ()
sum = 0
for x in tuple(range(1,4)):
    sum+=x
print ("sum : %d" % sum)
'''

sum = 0
for x in range(101):
    sum += x
print ("sum : %d" % sum)


sum = 0
x = 0
while True:
    sum += x
    x   += 1
    if (x <= 100):
        continue
    break

print ("sum : %d" % sum)

