#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   maxProfit2.py
@Contact :   9824373@qq.com
@License :   (C)Copyright 2017-2018, Zhan
@Desc    :
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/6/2 20:29   zhan      1.0         None
@desc:
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''

# 贪心发求解

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) <= 1:
            return 0

        diff_prices = [prices[i] - prices[i - 1]
                       for i in range(1, len(prices))]
        rst = 0
        i = 0
        idxList = [-1]
        while i < len(diff_prices):
            if diff_prices[i] > 0:
                if idxList[-1] == -1:
                    idxList[-1] = i
                rst += diff_prices[i]
            else:
                if idxList[-1] != -1:
                    idxList.append(i - 1)
                    idxList.append(-1)
            i += 1
        for i in range(len(idxList)):
            if (i + 1) % 2 == 1:
                print('买入时机:%d' % idxList[i])
            else:
                print('卖出时机:%d' % (idxList[i] + 1))

        return max(0, rst)


if __name__ == '__main__':
    a = [7, 1, 5, 3, 6, 4]
    # a = [7, 6, 4, 3, 1]

    # a = [1]
    print(Solution().maxProfit(a))
