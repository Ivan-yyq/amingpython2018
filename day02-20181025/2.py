#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/10/25 14:48
# @Author : yangyuanqiang
# @File : 2.py
#python v2.7

#99乘法口诀表

for i in xrange(1,10):
    for j in xrange(1,i+1):
        print "%s x %s = %s" % (j, i, j*i) ,
    print