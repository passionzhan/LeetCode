#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   findLengthOfLCIS.py    
@Contact :   9824373@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :     
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/19 21:53   zhan      1.0         None
'''


class Solution(object):
    def findLengthOfLCIS_iter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1

        rst = 0
        preNum = float('-inf')
        for i, num in enumerate(nums):
            if num <= preNum:
                return max(rst, self.findLengthOfLCIS_iter(nums[i:]))
            else:
                preNum = num
                rst += 1

        return rst

    def findLengthOfLCIS(self, nums):
        if len(nums) == 0:
            return 0
        rst = 0
        bIdx, i = 0, 0
        preNum = float('-inf')
        for i in range(len(nums)):
            num = nums[i]
            if num <= preNum:
                rst = max(rst, i - bIdx)
                bIdx = i
            preNum = num
        return max(rst, i - bIdx + 1)


if __name__ == '__main__':
    s = [1,3,5,4,7]
    s = [2,2]
    print(Solution().findLengthOfLCIS(s))