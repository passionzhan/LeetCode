#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : maxSubArray_oneTravel.py
# @Author: Zhan
# @Date  : 7/9/2019
# @Desc  :

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 0:
            return 0

        curNum = nums[0]
        curSum = nums[0]
        rst = nums[0]

        for i in range(1,len(nums)):
            curNum = nums[i]
            if curSum > 0:
                curSum += nums[i]
                rst = max(curSum, rst)
            else:
                curSum = nums[i]
                rst = max(curSum, rst)

        return rst

if __name__ == '__main__':
    a = [-2,1,-3,4,-1,2,1,-5,4]
    # a = [7, 6, 4, 3, 1]

    # a = [-1]
    print(Solution().maxSubArray(a))