#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   maxProfit.py
@Contact :   9824373@qq.com
@License :   (C)Copyright 2017-2018, Zhan
@Desc    :
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/6/2 15:01   zhan      1.0         None
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        # if len()
        diff_prices = [prices[i] - prices[i - 1]
                       for i in range(1, len(prices))]

        def maxSum(diff_prices, bIdx, eIdx):
            if bIdx == eIdx:
                return bIdx, bIdx, diff_prices[bIdx]

            mIdx = (bIdx + eIdx) // 2
            bIdx1, eIdx1, v1 = maxSum(diff_prices, bIdx, mIdx)
            bIdx2, eIdx2, v2 = maxSum(diff_prices, mIdx + 1, eIdx)

            tmpSum1 = diff_prices[mIdx]
            tmpSum2 = diff_prices[mIdx + 1]
            tmpV1 = diff_prices[mIdx]
            tmpV2 = diff_prices[mIdx + 1]
            tmp1_bIdx = mIdx
            tmp2_eIdx = mIdx + 1
            for i in range(mIdx - 1, bIdx - 1, -1):
                tmpSum1 += diff_prices[i]
                if tmpSum1 > tmpV1:
                    tmpV1 = tmpSum1
                    tmp1_bIdx = i

            for j in range(mIdx + 2, eIdx + 1):
                tmpSum2 += diff_prices[j]
                if tmpSum2 > tmpV2:
                    tmpV2 = tmpSum2
                    tmp2_eIdx = j

            if v1 >= v2 and v1 >= (tmpV1 + tmpV2):
                return bIdx1, eIdx1, v1

            if v2 >= v1 and v2 >= (tmpV1 + tmpV2):
                return bIdx2, eIdx2, v2

            return tmp1_bIdx, tmp2_eIdx, (tmpV1 + tmpV2)

        bIdx, eIdx, maxV = maxSum(diff_prices, 0, len(diff_prices) - 1)
        print('bIdx:%d' % bIdx)
        print('eIdx:%d' % eIdx)
        print('maxV:%d' % maxV)
        for i in range(bIdx, eIdx + 2):
            print(prices[i])
        # print

        # if maxV < 0:
        #     return
        return max(0, maxV)


if __name__ == '__main__':
    a = [7, 1, 5, 3, 6, 4]
    a = [7, 6, 4, 3, 1]

    a = [1]
    print(Solution().maxProfit(a))
