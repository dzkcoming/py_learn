#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'这里是注释信息'

__author__ = 'Mat K'


with open("create", 'r') as f:
	print (f.read())

# 跟上面这句等效

try:
	f = open("create", 'r')
	print (f.read())
finally:
	if f:
		f.close()



# 默认 open 时，采用的是 utf-8, 可额外手动指定编码格式

f = open("create", 'r', encoding='gbk')
f.read()
