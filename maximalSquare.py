#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : maximalSquare.py
# @Author: Zhan
# @Date  : 7/9/2019
# @Desc  :

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


        maxLen = min(nrow,ncol)

        rstMatrix = [[list(range(0,maxLen)) for item in row] for row in matrix]

        rst = [0,0,0]
        # initial
        for i in range(0,nrow):
            for j in range(0,ncol):
                rstMatrix[i][j][0] = (matrix[i][j] == '1')
                if rstMatrix[i][j][0] == True:
                    rst = [i,j,1]

        for s_len in range(2, maxLen + 1):
            for i in range(0, nrow - s_len + 1):
                for j in range(0, ncol - s_len + 1):
                    if rstMatrix[i][j][s_len - 2] and rstMatrix[i+1][j][s_len - 2] \
                            and rstMatrix[i][j+1][s_len - 2] and rstMatrix[i+1][j+1][s_len - 2]:
                        rstMatrix[i][j][s_len - 1] = True
                        rst = [i, j, s_len]
                    else:
                        rstMatrix[i][j][s_len - 1] = False


        return rst[2]*rst[2]

if __name__ == '__main__':
    a = [["1","0","1","0","0"],
         ["1","0","1","1","1"],
         ["1","1","1","1","1"],
         ["1","0","0","1","0"]
         ]
    # a = [7, 6, 4, 3, 1]

    # a = [-1]
    print(Solution().maximalSquare(a))



