# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   shortestBridge.py
@Contact :   9824373@qq.com
@Desc    :
@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-08     zhan        1.0         None
'''
from typing import List
from collections import deque

class Solution:
    def neighbors(self, A, iR, iC, flag):
        # ans = set()
        if (iR - 1, iC) in flag:
            yield (iR - 1, iC)
            # if inland:
            #     if A[iR - 1][iC]: ans.add((iR - 1, iC))
            # else:
            #     ans.add((iR - 1, iC))

        if (iR + 1, iC) in flag:
            yield (iR + 1, iC)
            # if inland:
            #     if A[iR + 1][iC]: ans.add((iR + 1, iC))
            # else:
            #     ans.add((iR + 1, iC))

        if (iR, iC + 1) in flag:
            yield (iR, iC + 1)
            # if inland:
            #     if A[iR][iC + 1]: ans.add((iR, iC + 1))
            # else:
            #     ans.add((iR, iC + 1))

        if (iR, iC - 1) in flag:
            yield (iR, iC - 1)
            # if inland:
            #     if A[iR][iC - 1]: ans.add((iR, iC - 1))
            # else:
            #     ans.add((iR, iC - 1))

        # return ans

    def shortestBridge(self, A: List[List[int]]) -> int:
        flag = {(i,j) for i in range(len(A)) for j in range(len(A[0]))}
        for i,j in flag:
            if A[i][j]:
                borders = self.findBorders_dfs(A,i,j,flag)
                break

        mydeque = deque()
        for border in borders:
            mydeque.append((border,0))

        while mydeque and flag:
            curEle, d= mydeque.popleft()
            for i,j in self.neighbors(A,curEle[0],curEle[1],flag):
                if A[i][j] == 1:
                    return d
                else:
                    mydeque.append(((i,j),d+1))
                    flag.remove((i,j))

        return -1


    def findBorders_dfs(self,A,i,j,flag):
        ans = set()
        flag.remove((i,j))
        for (n_i,n_j) in self.neighbors(A,i,j,flag):
            if A[n_i][n_j] == 0:
                ans.add((i,j))
            else:
                ans = ans.union(self.findBorders_dfs(A,n_i,n_j,flag))
        return ans


if __name__ == '__main__':
    A = [[0,1],[1,0]]
    A = [[1,1,1,1,1],
         [1,0,0,0,1],
         [1,0,1,0,1],
         [1,0,0,0,1],
         [1,1,1,1,1]]
    # A =  [[0, 1, 0],
    #       [0, 0, 0],
    #       [0, 0, 1]]
    ans = Solution().shortestBridge(A)
    print(ans)










