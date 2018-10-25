#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/10/25 17:10
# @Author : yangyuanqiang
# @File : 8.py
#python v2.7

#统计系统剩余的内存

with open('/proc/meminfo') as fd:
    for line in fd:
        if line.startswith('MemTotal'):
            total = line.split()[1]
            continue
        if line.startswith('MemFree'):
            free = line.split()[1]
            continue
        if line.startswith('Buffers'):
            buffers = line.split()[1]
            continue
        if line.startswith('Cached'):
            cached = line.split()[1]
            break

free = int(free) + int(buffers) + int(cached)
print "Total Memory: %0.2f" % (int(total) / 1024.0) + 'M'
print "Free Memory: %0.2f" % (int(free) / 1024.0) + 'M'
print "Free Memory in precent: %0.2f" % ((int(free) /1024.0) / (int(total) / 1024.0) * 100) + '%'