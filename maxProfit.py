#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   maxProfit.py
@Contact :   9824373@qq.com
@License :   (C)Copyright 2017-2018, Zhan
@Desc    :
            给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

            如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

            注意你不能在买入股票前卖出股票。

            示例 1:

            输入: [7,1,5,3,6,4]
            输出: 5
            解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
                 注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
            示例 2:

            输入: [7,6,4,3,1]
            输出: 0
            解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
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

            # 处理 两段中间连续部分
            tmpSum1 = diff_prices[mIdx]
            tmpSum2 = diff_prices[mIdx + 1]
            maxV1 = diff_prices[mIdx]
            maxV2 = diff_prices[mIdx + 1]
            tmp1_bIdx = mIdx
            tmp2_eIdx = mIdx + 1
            # 只需要判断到左边最大段的起点 bIdx1(包含)
            for i in range(mIdx - 1, bIdx - 1, -1):
                tmpSum1 += diff_prices[i]
                if tmpSum1 > maxV1:
                    maxV1 = tmpSum1
                    tmp1_bIdx = i

            # 只需要判断到右边最大段的起点 eIdx2(包含)
            for j in range(mIdx + 2, eIdx2 + 1):
                tmpSum2 += diff_prices[j]
                if tmpSum2 > maxV2:
                    maxV2 = tmpSum2
                    tmp2_eIdx = j

            if v1 >= v2 and v1 >= (maxV1 + maxV2):
                return bIdx1, eIdx1, v1

            if v2 >= v1 and v2 >= (maxV1 + maxV2):
                return bIdx2, eIdx2, v2

            # 中间连续段大
            return tmp1_bIdx, tmp2_eIdx, (maxV1 + maxV2)

        bIdx, eIdx, maxV = maxSum(diff_prices, 0, len(diff_prices) - 1)
        # print('bIdx:%d' % bIdx)
        # print('eIdx:%d' % eIdx)
        # print('maxV:%d' % maxV)
        # for i in range(bIdx, eIdx + 2):
        #     print(prices[i])
        # print

        # if maxV < 0:
        #     return
        return max(0, maxV)


if __name__ == '__main__':
    a = [7, 1, 5, 3, 6, 4]
    a = [7, 6, 4, 3, 1]

    a = [1]
    print(Solution().maxProfit(a))
