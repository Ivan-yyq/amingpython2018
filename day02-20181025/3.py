#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/10/25 14:49
# @Author : yangyuanqiang
# @File : 3.py
#python v2.7

import time
import sys

for i in range(10):
    if i == 3:
        continue
#    time.sleep(1)
    elif i == 5:
        continue
    elif i == 6:
        pass
    elif i == 7:
        sys.exit()
    print i
else:
    print "main end"
print "hahaha"