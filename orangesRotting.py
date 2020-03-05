# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   orangesRotting.py
@Contact :   9824373@qq.com
@Desc    :

            在给定的网格中，每个单元格可以有以下三个值之一：

            值 0 代表空单元格；
            值 1 代表新鲜橘子；
            值 2 代表腐烂的橘子。
            每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

            返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

            示例 1：
            输入：[[2,1,1],[1,1,0],[0,1,1]]
            输出：4
            示例 2：

            输入：[[2,1,1],[0,1,1],[1,0,1]]
            输出：-1
            解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
            示例 3：

            输入：[[0,2]]
            输出：0
            解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/rotting-oranges

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-05     zhan        1.0         None
'''

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        queue = deque()
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 2:
                    queue.append((i,j,0))


        def neighbors(iRow, iClo):
            for (nr,nc) in ((iRow-1,iClo),(iRow,iClo-1),(iRow+1,iClo),(iRow,iClo+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield (nr,nc)

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d + 1))

        if any(1 in row for row in grid):
            return -1
        return d

if __name__ == '__main__':
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    ans = Solution().orangesRotting(grid)
    print(ans)