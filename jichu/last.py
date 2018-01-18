#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'这里是注释信息'

__author__ = 'Dou Zhongkang'

print ('hello, this is test.py')

import sys

def test():
	args = sys.argv
	print ("argc : ", len(args), 'argv : ', args)

if __name__ == '__main__':
	test()
