#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/10/25 16:01
# @Author : yangyuanqiang
# @File : 7.py
#python v2.7

#while循环遍历文件内容

fd = open("test.txt")
while True:
    line = fd.readline()
    if not line:    #not line如果为空，为True，条件成立，break退出
        break
    print line,

fd.close()