#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   maxSubArray.py    
@Contact :   9824373@qq.com
@License :   (C)Copyright 2017-2018, Zhan
@Desc    :     
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/7/9 16:44   zhan      1.0         None
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return 0

        # if len()
        # nums = [nums[i] - nums[i - 1]
        #                for i in range(1, len(nums))]

        def maxSum(numsList, bIdx, eIdx):
            if bIdx == eIdx:
                return bIdx, bIdx, numsList[bIdx]

            mIdx = (bIdx + eIdx) // 2
            bIdx1, eIdx1, v1 = maxSum(numsList, bIdx, mIdx)
            bIdx2, eIdx2, v2 = maxSum(numsList, mIdx + 1, eIdx)

            tmpSum1 = numsList[mIdx]
            tmpSum2 = numsList[mIdx + 1]
            tmpV1 = numsList[mIdx]
            tmpV2 = numsList[mIdx + 1]
            tmp1_bIdx = mIdx
            tmp2_eIdx = mIdx + 1
            for i in range(mIdx - 1, bIdx - 1, -1):
                tmpSum1 += numsList[i]
                if tmpSum1 > tmpV1:
                    tmpV1 = tmpSum1
                    tmp1_bIdx = i

            for j in range(mIdx + 2, eIdx + 1):
                tmpSum2 += numsList[j]
                if tmpSum2 > tmpV2:
                    tmpV2 = tmpSum2
                    tmp2_eIdx = j

            if v1 >= v2 and v1 >= (tmpV1 + tmpV2):
                return bIdx1, eIdx1, v1

            if v2 >= v1 and v2 >= (tmpV1 + tmpV2):
                return bIdx2, eIdx2, v2

            return tmp1_bIdx, tmp2_eIdx, (tmpV1 + tmpV2)

        bIdx, eIdx, maxV = maxSum(nums, 0, len(nums) - 1)
        print('bIdx:%d' % bIdx)
        print('eIdx:%d' % eIdx)
        print('maxV:%d' % maxV)
        for i in range(bIdx, eIdx + 1):
            print(nums[i])
        # print

        # if maxV < 0:
        #     return
        return maxV

if __name__ == '__main__':
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # a = [7, 6, 4, 3, 1]

    # a = [-1]
    print(Solution().maxSubArray(a))