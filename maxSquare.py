#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : maxSquare.py
# @Author: Zhan
# @Date  : 7/11/2019
# @Desc  : 最大正方形
#     在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
#
#     示例:
#
#     输入:
#
#     1 0 1 0 0
#     1 0 1 1 1
#     1 1 1 1 1
#     1 0 0 1 0
#
#     输出: 4

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        nrow = len(matrix)
        if nrow <= 0:
            return 0

        ncol = len(matrix[0])

        if ncol <= 0:
            return 0

        pre = 0
        dp = [0 for item in matrix[0]]
        rst = 0

        for i in range(0, nrow):
            for j in range(0, ncol):
                if j == 0:
                    pre = dp[j]
                    dp[j] = int(matrix[i][j])
                elif matrix[i][j] == "1":
                    tmp = dp[j]
                    dp[j] = min(pre, dp[j - 1], dp[j]) + 1
                    pre = tmp
                else:
                    pre = dp[j]
                    dp[j] = 0
                rst = max(rst, dp[j])

        return rst * rst


if __name__ == '__main__':
    a = [["1","0","1","0","0"],
         ["1","0","1","1","1"],
         ["1","1","1","1","1"],
         ["1","0","1","1","1"]
         ]
    # a = [7, 6, 4, 3, 1]

    # a = [-1]
    print(Solution().maximalSquare(a))