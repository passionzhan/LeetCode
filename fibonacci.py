#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   fibonacci.py
@Contact :   9824373@qq.com
@License :   (C)Copyright 2017-2018, Zhan
@Desc    :
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/6/1 23:06   zhan      1.0         None
'''

import time

import numpy as np


def DP_Fibonacci(n):
    rst = [0 for i in range(n + 1)]
    rst[0] = 0
    rst[1] = 1

    for i in range(2, n + 1):
        rst[i] = rst[i - 2] + rst[i - 1]
    return rst[n]


def DIV_Fibonacci(n):
    def matrix_multiply(A, n):
        rst = np.eye(2,dtype=np.int64)
        tmp = A
        while n > 0:
            if n & 1:
                rst = np.dot(rst, tmp)
            tmp = np.dot(tmp, tmp)
            n = (n >> 1)
        return rst

    A = np.array([[1, 1], [1, 0]],dtype=np.int64)
    B = matrix_multiply(A, n - 1)
    return B[0, 0]


if __name__ == '__main__':
    start = time.clock()
    rst = DP_Fibonacci(100000)
    end = time.clock()
    print(
        'DP_Fibonacci Running time: %s Seconds  and result is %d ' %
        ((end - start), rst))

    start = time.clock()
    rst = DIV_Fibonacci(100000)
    end = time.clock()
    print(
        'DIV_Fibonacci Running time: %s Seconds and result is %d ' %
        ((end - start), rst))
