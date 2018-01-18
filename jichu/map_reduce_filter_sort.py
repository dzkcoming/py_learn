#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# map 
print ('--------------------  map  ----------------------')

def my_power(x):
	return x ** 2

r=map(my_power, list(range(10)))

from collections import Iterable
print ('type : ', type(r), ' can iter ? ', isinstance(r, Iterable))

for i in r:
	print (i)


# reduce
from functools import reduce

print ('--------------------  reduce  ----------------------')

# 初级用法
def my_add(x, y):
	return x+y

print (reduce(my_add, (1,2,3,4)))

# 高级用法
def fn(x, y):
	return x * 10 + y

def char2num(c):
	return {'0':0, '1':1, '2':2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]

print (reduce (fn, map(char2num, '12345')))

# 将以上整理成函数就是

def str2int(s):
	def fn(x, y):
		return x * 10 + y

	def char2num(c):
		return {'0':0, '1':1, '2':2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]

	return reduce (fn, map(char2num, s))

print ('3123123')


# 利用临时函数再简化

def str2int(s):
	def char2num(c):
		return {'0':0, '1':1, '2':2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]

	return reduce (lambda x, y: x * 10 + y, map(char2num, s))

print (str2int('222'))

# 测试用例
def jiuzheng(s):
	a = []
	a.append(s[0].upper())
	a.append(s[1:].lower())
	print ('debug : ', a)
	return a

classmate=['sssDd', 'aAAaa', 'bBBb']

print (tuple(map(jiuzheng, classmate)))

def prod(s):
	return reduce (lambda x,y: x * y, s)

print (prod((1,2,4,5)))

# filter 
def is_odd(n):
	return n % 2 == 0

print (list(filter(is_odd, (1,2,3,4,5,6))))

def is_none(n):
	return n

def is_none(n):
	return n and n.strip()

print (list(filter(is_none, ('', 'a', 'b', None, 'c', ' ', 'd'))))


# 排序 sort
print (sorted((2,1,3)))

classmate={'dzouhk':10, 'zhengli':100, 'bi':20, 'lishoujian':90}
print (sorted(classmate))

# 按照分数排序
print (sorted(classmate, key=lambda d:d[1]))
