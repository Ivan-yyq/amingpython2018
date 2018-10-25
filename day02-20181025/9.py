#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/10/25 17:31
# @Author : yangyuanqiang
# @File : 9.py
#python v2.7

#数据类型转换(计算mac地址)

macaddr = "9C-5C-8E-70-31-46"
prefix_mac = macaddr[:-3]
last_two = macaddr[-2:]
plus_one = int(last_two, 16) + 1

if plus_one in range(10):
    new_last_tow = hex(plus_one)[2:]
    new_last_tow = '0' + new_last_tow
else:
    new_last_tow = hex(plus_one)[2:]
    if len(new_last_tow) == 1:
        new_last_tow = '0' + new_last_tow

new_mac = prefix_mac + '-' + new_last_tow
print("新生成的MAC地址：%s" % new_mac)
