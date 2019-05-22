#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   colorBorder.py
@Contact :   9824373@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/4 10:18   zhan      1.0         None
'''


class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        # visited = [[False for item in row] for row in grid]
        # 记录已访问节点原来的值
        visited = {}
        # oGrid = [[item for item in row] for row in grid]
        cnnColor = grid[r0][c0]
        if cnnColor != color:
            self.DFS(grid, visited, r0, c0, cnnColor, color)

        return grid

    def DFS(self, grid, visited, i, j, cnnColor, color):
        visited[(i, j)] = grid[i][j]
        if i == 0:
            grid[i][j] = color
        elif ((i - 1, j) in visited.keys() and visited[(i - 1, j)] != cnnColor) \
                or ((i - 1, j) not in visited.keys() and grid[i - 1][j] != cnnColor):
            grid[i][j] = color
        elif (i - 1, j) not in visited.keys() and grid[i - 1][j] == cnnColor:
            self.DFS(grid, visited, i - 1, j, cnnColor, color)

        if i + 1 == len(grid):
            grid[i][j] = color
        elif ((i + 1, j) in visited.keys() and visited[(i + 1, j)] != cnnColor) \
                or ((i + 1, j) not in visited.keys() and grid[i + 1][j] != cnnColor):
            grid[i][j] = color
        elif (i + 1, j) not in visited.keys() and grid[i + 1][j] == cnnColor:
            self.DFS(grid, visited, i + 1, j, cnnColor, color)

        if j == 0:
            grid[i][j] = color
        elif((i, j - 1) in visited.keys() and visited[(i, j - 1)] != cnnColor) \
                or ((i, j - 1) not in visited.keys() and grid[i][j - 1] != cnnColor):
            grid[i][j] = color
        elif (i, j - 1) not in visited.keys() and grid[i][j - 1] == cnnColor:
            self.DFS(grid, visited, i, j - 1, cnnColor, color)

        if j + 1 == len(grid[0]):
            grid[i][j] = color
        elif ((i, j + 1) in visited.keys() and visited[(i, j + 1)] != cnnColor) \
                or ((i, j + 1) not in visited.keys() and grid[i][j + 1] != cnnColor):
            grid[i][j] = color
        elif (i, j + 1) not in visited.keys() and grid[i][j + 1] == cnnColor:
            self.DFS(grid, visited, i, j + 1, cnnColor, color)


if __name__ == '__main__':
    grid = [[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]]
    r0, c0 = 1, 1
    color = 2
    print(Solution().colorBorder(grid, r0, c0, color))
