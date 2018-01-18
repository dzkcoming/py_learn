#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#迭代的用法

d={'a':1, 'b':2, 'c':3}

for i in d.values():
	print (i)

for i in d:
	print (i)

for i in d.items():
	print (i)

# 判断是否能迭代的语法

from collections import Iterable
print ('dict 可以迭代 ? ', isinstance(d, Iterable))
print ('list/tuple 可以迭代 ? ', isinstance([1,2,3], Iterable))

# isinstance 用于判断
print ('1 是 int ? ', isinstance(1, int))


#取两个值
for key,value in d.items():
	print (key, value)

# 获得索引
for i, c in enumerate("abcde"):
	print (i, c)


# list 生成

a=list(range(5))
print (a)

a=[i ** 2 for i in range(5)]
print (a)

a=[i ** 2 for i in range(5) if (i % 2 == 0)]
print (a)

a=[m + n for m in 'abc' if (m != 'a') for n in 'ABC' if (n != 'A')]
print (a)


