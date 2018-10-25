#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/10/25 14:56
# @Author : yangyuanqiang
# @File : 5.py
#python v2.7

#写，w重新打开文件，原文件内容被清空，a打开文件，追加内容
# file = open('test.txt', 'a')
# fw = file.write('456\n')

#读
file = open('test.txt')
#read()返回的是字符串
# print(file.read())
# print(type(file.read()))
#readline()返回的是字符串
# print(file.readline())
#readlines()返回的是列表
print(file.readlines())

#关闭文件
file.close()