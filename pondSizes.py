# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   pondSizes.py
@Contact :   9824373@qq.com
@Desc    :
@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-07     zhan        1.0         None
'''
from typing import List
from collections import deque

class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        def neighbors(iR,iC,flag):
            ans = []
            if (iR-1,iC-1) in flag:
                ans.append((iR-1,iC-1))
            if (iR-1,iC) in flag:
                ans.append((iR-1,iC))
            if (iR-1,iC+1) in flag:
                ans.append((iR-1,iC+1))
            if (iR,iC-1) in flag:
                ans.append((iR,iC-1))
            if (iR, iC + 1) in flag:
                ans.append((iR, iC + 1))
            if (iR + 1, iC-1) in flag:
                ans.append((iR + 1, iC-1))
            if (iR + 1, iC) in flag:
                ans.append((iR + 1, iC))
            if (iR+1, iC + 1) in flag:
                ans.append((iR+1, iC + 1))
            return ans

        flag = {(i,j) for j in range(len(land[0])) for i in range(len(land)) if land[i][j] == 0}

        ans = []
        while flag:
            tmpArea = 0
            mydueque = deque()
            mydueque.append(flag.pop())

            while mydueque:
                curEle = mydueque.popleft()
                tmpArea +=1
                for neighbor in neighbors(curEle[0], curEle[1], flag):
                    mydueque.append(neighbor)
                    flag.remove(neighbor)

            ans.append(tmpArea)

        ans.sort()

        return ans

if __name__ == '__main__':
    a = [
          [0,2,1,0],
          [0,1,0,1],
          [1,1,0,1],
          [0,1,0,1]
        ]

    ans = Solution().pondSizes(a)

    print(ans)

