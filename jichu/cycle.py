#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# cycyle

classmate = ['douzhk', 'libang', 'zhengli']

for name in classmate:
    print (name)

sum = 0



for i in range(101):
    sum += i

print ("sum : ", sum)


# while cycle
sum = 0
i = 0
while True:
	sum += i
	i   += 1
	if (i == 101):
		break

print ("sum : ", sum)
