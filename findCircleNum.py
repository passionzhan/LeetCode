#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : findCircleNum.py
# @Author: Zhan
# @Date  : 4/30/2019
# @Desc  :


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        hasVisited = set()
        rtnCircleNum = 0
        for i in range(len(M)):
            if i not in hasVisited:
                self.DFS(M, i, hasVisited)
                rtnCircleNum += 1

        return rtnCircleNum

    def DFS(self, M, i, hasVisited):
        hasVisited.add(i)
        for j in range(len(M[i])):
            if j != i and j not in hasVisited and M[i][j] == 1:
                self.DFS(M, j, hasVisited)
        return


if __name__ == '__main__':
    M = [[1,1,0],
         [1,1,0],
         [0,0,1]]
    rtnCircleNum = Solution().findCircleNum(M)
    print(rtnCircleNum)
