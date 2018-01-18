#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# generator 生成器

#  --- 1 ---
a = (i for i in range(10))

for i in a:
	print (i)

#  --- 2 --- , 通过 yield ，只能放到函数里用

def odd():
	yield(1)
	yield(3)
	yield(5)

a = odd()
for i in a:
	print (i)
