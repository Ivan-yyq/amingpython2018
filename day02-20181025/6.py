#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/10/25 15:52
# @Author : yangyuanqiang
# @File : 6.py
#python v2.7

#for循环遍历文件内容

fd = open('test.txt')
for line in fd:
    print line,

fd.close()