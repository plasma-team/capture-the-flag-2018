#! /usr/bin/env python

import string
import random
import math

flag = open('flag.txt','rb').read()
out = open('encrypted', 'wb')

LEN_KEY = 32
ASCII_LETTERS = string.ascii_letters

size = int(math.ceil(math.sqrt(len(flag))))

def pad(s):
    return s + (size - (len(s) % size)) * chr(size - len(s) % size)

def encrypt(flag):

    flag = pad(flag)
    arr = [flag[size*x:size*(x+1)] for x in range(len(flag)/size)]

    num = []
    for z in range(size):
        while(True):
            ch = random.choice(string.digits)
            if ch != '0':
                break
        num.append(z * '0' + ch + (size-1-z)*'0')

    res = []
    for p in range(size):
        temp = []
        for q in range(size):
            cnt = 0
            for r in range(size):
                cnt += ord(arr[p][r]) * ord(num[r][q])
            temp.append(cnt)
        res.append(temp)

    return res

encrypted = encrypt(flag)
out.write(str(encrypted))

out.close()
