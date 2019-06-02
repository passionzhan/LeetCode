#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   trap.py
@Contact :   9824373@qq.com
@License :   (C)Copyright 2017-2018, Zhan
@Desc    :
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/7 20:14   zhan      1.0         None
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0
        nonZeroIdx = 0
        for i, hi in enumerate(height):
            if hi != 0:
                nonZeroIdx = i
                break

        height = height[nonZeroIdx:]
        startEnd = height[0]
        stopEnd = 0
        stopIdx = 1
        for i in range(1, len(height), ):
            hi = height[i]
            if hi >= startEnd:
                stopEnd = hi
                stopIdx = i
                break
            if hi >= stopEnd:
                stopEnd = hi
                stopIdx = i

        belowV = min(startEnd, stopEnd)
        curVol = 0
        for i in range(1, stopIdx):
            curVol += belowV - height[i]

        if stopIdx == len(height) - 1:
            return curVol
        else:
            return curVol + self.trap(height[stopIdx:])


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    height = []
    print(Solution().trap(height))
