#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# pass use


def nop():
	pass

age = 0
if age > 12:
	pass

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny

print (move(0, 0, 1))

x,y = move(0, 0, 1)
print ('x',x, 'y',y)


# 默认参数的函数的定义
'''
def power(x, n=2):
	return math.pow(x, n)

while True:
	print (power(int(input()), int(input())))
'''

# 默认参数，且不按顺序传入
def student_reg(name, age, sex='male', city="hangzhou"):
	print (name, age, sex, city)

student_reg("douzhk", 1, city='henan')

# 可变参数
# -- 不可变参数，传入 list 或 tuple
'''
def calc(n):
	sum = 0
	for i in n:
		sum += i ** 2
	return sum

while True:
	value = [int(input()), int(input())]
	print (calc(value))

'''

# -- 利用可变参数
'''
def calc(*n):
	sum = 0
	for i in n:
		sum += i ** 2
	return sum

while True:
	print (calc(int(input()), int(input())))

'''

# 关键词参数
'''
def stu_reg(name, age, **kw):
	print ('name :', name, 'age :', age, 'other :', kw)

stu_reg ('douzhk', 15, city='henan', sex='male')

other={'city':'henan', 'sex':'male'}
stu_reg ('douzhk', 16, **other)
'''

# 递归函数
'''
def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)

print (fact(int(input())))
'''
