#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/10/25 14:50
# @Author : yangyuanqiang
# @File : 4.py
#python v2.7

#猜数字游戏，使用random模块，随机生成数字

import sys
import random

num1 = random.randint(1,20)
for i in range (1,7):
    num2 = int(raw_input("Please input the number you guess: "))
    if num2 == num1:
        print "You win!"
        sys.exit()
    elif num2 > num1:
        print "Guess large,Please continue to guess: "
        print "You still have %s chance." % (6-i)
    elif num2 < num1:
        print "Guess small,Please continue to guess: "
        print "You still have %s chance." % (6-i)
else:
    print "The correct number is: %s" % num1
    print "You lost!"
    print "Game over."