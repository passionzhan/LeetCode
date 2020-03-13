# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   numIslands.py
@Contact :   9824373@qq.com
@Desc    :
            给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

            示例 1:

            输入:
            11110
            11010
            11000
            00000

            输出: 1
            示例 2:

            输入:
            11000
            11000
            00100
            00011

            输出: 3

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/number-of-islands

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-12     zhan        1.0         None
'''
from typing import List

class Solution:
    def dfs(self,grid,i,j,seen):
        seen.add((i,j))
        for m,n in self.neighbors(grid,i,j,seen):
            if grid[m][n]=='1':
                self.dfs(grid,m,n,seen)

    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()

        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in seen:
                    num += 1
                    self.dfs(grid,i,j,seen)

        return num


    def neighbors(self,grid,i,j,seen):
        for (m,n) in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
            if (m,n) not in seen and 0<= m < len(grid) and 0<= n < len(grid[0]):
                yield (m,n)


if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']
    ]

    # grid =[ ['1', '1', '0', '0', '0'],
    #         ['1', '1', '0', '0', '0'],
    #         ['0', '0', '1', '0', '0'],
    #         ['0', '0', '0', '1', '1'],
    # ]

    ans = Solution().numIslands(grid)
    print(ans)

