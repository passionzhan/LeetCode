# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   pondSizes.py
@Contact :   9824373@qq.com
@Desc    :
    你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。

    示例：

    输入：
    [
      [0,2,1,0],
      [0,1,0,1],
      [1,1,0,1],
      [0,1,0,1]
    ]
    输出： [1,2,4]
    提示：

    0 < len(land) <= 1000
    0 < len(land[i]) <= 1000

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/pond-sizes-lcci

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-07     zhan        1.0         None
'''
from typing import List
from collections import deque

class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        def neighbors(iR,iC,flag):
            ans = set()
            if (iR-1,iC-1) in flag:
                ans.add((iR-1,iC-1))
            if (iR-1,iC) in flag:
                ans.add((iR-1,iC))
            if (iR-1,iC+1) in flag:
                ans.add((iR-1,iC+1))
            if (iR,iC-1) in flag:
                ans.add((iR,iC-1))
            if (iR, iC + 1) in flag:
                ans.add((iR, iC + 1))
            if (iR + 1, iC-1) in flag:
                ans.add((iR + 1, iC-1))
            if (iR + 1, iC) in flag:
                ans.add((iR + 1, iC))
            if (iR+1, iC + 1) in flag:
                ans.add((iR+1, iC + 1))
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

