#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def my_abs(x):
	if not isinstance (x, (int, float)):
		raise TypeError('bad operand type.')
	if x > 0:
		return x
	else:
		return -x

my_abs("123")

while True:
	print (my_abs(int(input())))
