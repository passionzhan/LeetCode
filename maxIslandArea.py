#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : maxIslandArea.py
# @Author: Zhan
# @Date  : 4/30/2019
# @Desc  :


class Solution(object):
    # 宽度优先搜索
    # def maxAreaOfIsland(self, grid):
    #     """
    #     :type grid: List[List[int]]
    #     :rtype: int
    #     """
    #     ### 1、扫描本行存在的岛屿、记录岛屿位置、大小
    #     ### 2、和上一行岛屿合并，丢弃已确定的非最大的岛屿，
    #     ### 3、返回最大岛屿
    #
    #     IslandsArea = []
    #     # 初始化hash表，-1表示该节点没有岛和他对应。
    #     node2Island_hash = { i:-1 for i in range(len(grid[0]))}
    #
    #     for j, row in enumerate(grid):
    #         newIsland = False
    #         preIsOne = False
    #         curIslandArea = 0
    #         curIslandNodes = []
    #         curLayerNodes2Island_hash = {}
    #         curLayerNodes2Island_hash ={ i:-1 for i in range(len(row))}
    #         curIslandIdx = 0
    #         for i,v in enumerate(row):
    #             if v == 1:
    #                 if node2Island_hash[i] == -1 and preIsOne == False:
    #                     curIslandArea += 1
    #                     curIslandNodes.append(i)  # 岛屿对应的节点
    #                     newIsland = True
    #                 elif node2Island_hash[i] == -1 and preIsOne == True:
    #                     if newIsland:
    #                         # 0 0
    #                         # 1 1
    #                         curIslandArea += 1
    #                         curIslandNodes.append(i)  # 岛屿对应的节点
    #                         newIsland = True
    #                     else:
    #                         ## 1  0
    #                         ## 1  1
    #                         IslandsArea[curIslandIdx] += 1  # 岛屿面积数量+1
    #                         curLayerNodes2Island_hash[i] = curIslandIdx
    #                 elif node2Island_hash[i] != -1 and preIsOne == True:# 和之前岛屿有联通,且前一个元素为1，
    #                     if newIsland:# curIslandIdx为新建的岛屿
    #                         # 0 0 1
    #                         # 0 1 1
    #                         IslandsArea[node2Island_hash[i]] += curIslandArea
    #                         curIslandIdx = node2Island_hash[i] #将连通岛屿设为当前岛屿
    #                         for idx in curIslandNodes:
    #                             curLayerNodes2Island_hash[idx] = curIslandIdx
    #                         newIsland = False
    #                         curIslandNodes = []
    #                         curIslandArea = 0
    #                         IslandsArea[curIslandIdx] += 1 #岛屿面积数量+1
    #                         curLayerNodes2Island_hash[i] = curIslandIdx
    #                     else:
    #                         #1 0 0 1
    #                         #1 1 1 1
    #                         IslandsArea[curIslandIdx] += 1 #岛屿面积数量+1
    #                         if node2Island_hash[i] != curIslandIdx:
    #                             preIsland_Idx = node2Island_hash[i]
    #                             IslandsArea[curIslandIdx] += IslandsArea[preIsland_Idx]
    #                             IslandsArea.pop(preIsland_Idx) # 合并岛屿后将其从岛屿集合中删除
    #                             if preIsland_Idx < curIslandIdx: # 岛屿集合中删除岛屿后会影响当前岛屿索引
    #                                 curIslandIdx -= 1
    #                             for k,v in node2Island_hash.items():
    #                                 if v == preIsland_Idx:
    #                                     node2Island_hash[k] = curIslandIdx
    #                                 elif v > preIsland_Idx: #索引-1
    #                                     node2Island_hash[k] -= 1
    #                             for k,v in curLayerNodes2Island_hash.items():
    #                                 if v > preIsland_Idx:
    #                                     curLayerNodes2Island_hash[k] -= 1
    #
    #                         curLayerNodes2Island_hash[i] = curIslandIdx
    #
    #                 else: # 和之前岛屿有联通,且前一个元素为0，
    #                     curIslandIdx = node2Island_hash[i]
    #                     IslandsArea[curIslandIdx] += 1  # 岛屿面积数量+1
    #                     curLayerNodes2Island_hash[i] = curIslandIdx
    #
    #                 preIsOne = True
    #             else: # 当前位置元素为 0
    #                 if newIsland:
    #                     IslandsArea.append(curIslandArea)
    #                     for idx in curIslandNodes:
    #                         curLayerNodes2Island_hash[idx] = len(IslandsArea) - 1
    #                     newIsland = False
    #                     curIslandNodes = []
    #                     curIslandArea = 0
    #                 preIsOne = False
    #                 curLayerNodes2Island_hash[i] = -1
    #
    #         if newIsland:
    #             IslandsArea.append(curIslandArea)
    #             for idx in curIslandNodes:
    #                 curLayerNodes2Island_hash[idx] = len(IslandsArea) - 1
    #             newIsland = False
    #             curIslandNodes = []
    #             curIslandArea = 0
    #
    #         node2Island_hash  = curLayerNodes2Island_hash
    #
    #     maxArea = 0
    #     for v in IslandsArea:
    #         if v > maxArea:
    #             maxArea = v
    #
    #     return maxArea

    #  深度优先搜索
    def maxAreaOfIsland(self, grid):
        visited = [[False for i in row] for row in grid]
        maxArea = 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1:
                    maxArea = max(maxArea, self.DFS(grid, visited, i, j))
        return maxArea

    def DFS(self, grid, visited, i, j):
        area = 0
        if not visited[i][j]:
            visited[i][j] = True
            area = 1
            if i - 1 >= 0 and grid[i -
                                   1][j] != 0 and visited[i - 1][j] == False:
                area += self.DFS(grid, visited, i - 1, j)  # up
            if j + 1 < len(grid[0]) and grid[i][j +
                                                1] != 0 and visited[i][j + 1] == False:
                area += self.DFS(grid, visited, i, j + 1)  # right
            if i + 1 < len(grid) and grid[i +
                                          1][j] != 0 and visited[i + 1][j] == False:
                area += self.DFS(grid, visited, i + 1, j)  # down
            if j - 1 >= 0 and grid[i][j -
                                      1] != 0 and visited[i][j - 1] == False:
                area += self.DFS(grid, visited, i, j - 1)  # left
        return area


if __name__ == '__main__':
    grid = [[1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]]
    grid = [[1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
            [0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
            [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
            [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1],
            [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0],
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1],
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1],
            [0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
            [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
            [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0],
            [1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
            [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1],
            [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
            [0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
            [1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0]]
    maxIslandArea = Solution().maxAreaOfIsland(grid)
    print(maxIslandArea)
