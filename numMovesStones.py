#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   numMovesStones.py
@Contact :   9824373@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/4 9:57   zhan      1.0         None
'''


class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """

        L = sorted([a, b, c])

        maxNum = L[2] - L[0] - 2
        minNum = 2

        if L[1] <= L[0] + 2 or L[2] <= L[1] + 2:
            minNum = 1
        else:
            minNum = 2

        if minNum > maxNum:
            minNum = maxNum

        return [minNum, maxNum]


if __name__ == '__main__':
    a, b, c = 99, 3, 1
    print(Solution().numMovesStones(a, b, c))
