#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'这里是注释信息'

__author__ = 'Mat K'

import os
import sys

#fd=open(filename, 'r')
#
#str=fd.read()
#print(str)
#
#fd.close()

if len(sys.argv) == 1:
    filename="./file_io.py"
else:
    filename=sys.argv[1]

OFFSET=44
CHANNEL_NUMBER=2
MAXVALUE=0x7ffe

start_value = 0
cur_len = 0
read_len = 1024

def combine2short(low, high):
    return (high << 8) + low

with open(filename, 'rb') as f:
    file_len = os.path.getsize(filename)
    print("filelen : %d" % (file_len))
    if file_len < OFFSET:
        print("file len is too small")
        exit()

    ret = f.read(OFFSET)
    if (len(ret) != OFFSET):
        print("read failed, want : %d, actual : %d" % (OFFSET, len(ret)))
        exit()

    cur_len += OFFSET

    while True:
        ret = f.read(read_len)
        #print("data:", ret)
        #print(len(ret))
        read_size = len(ret)

        i = 0
        while i < read_size:
            # check data

            j = 0
            while (j < 2*CHANNEL_NUMBER):
                cur_value = combine2short(ret[i + j], ret[i+1 + j])
                if start_value != cur_value :
                    print("addr : %x expect : %x actual : %x" % (cur_len + i + j, start_value, cur_value))
                    start_value = cur_value
                j += 2

            i += 2*CHANNEL_NUMBER
            start_value += 1
            if start_value > MAXVALUE:
                start_value = 0

        cur_len += len(ret)
        if (len(ret) != read_len):
            print("read fin\n")
            break

    print("actual read len : ", cur_len)

