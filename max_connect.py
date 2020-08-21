# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# PROJECT_NAME:         design_pattern
# Name:                 max_connect.py
# Author:               9824373
# Date:                 2020-08-19  21:03
# Contact:              9824373@qq.com
# Version:              V1.0
# Description:  
#-------------------------------------------------------------------------------       

'''
0 1 1 1 0 1 1 1
1 1 1 0 1 0 1 1
1 1 0 1 1 0 1 1
int getMaxLinked(int[][] matrix,int n,int m)
{
}
我给定任意一个矩阵n*m,其中只有 0 1 两个数字,1表示可以走通,0表示不能走通,只能上下左右,求矩阵的最长联通长度

假如说
m和n如果是无限大情况,应该怎么处理?
'''
# from queue import Queue
from collections import deque
import copy

def neighbors(matrix, iRow, iClo):
    for (nr, nc) in ((iRow - 1, iClo), (iRow + 1, iClo), (iRow, iClo - 1), (iRow, iClo + 1)):
        if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
            yield (nr, nc)

# 深度优先搜索
def dfs(matrix, seen, i, j):
    res_len = 1
    rst_lst = [0, ]
    for nei_i, nei_j in neighbors(matrix,i,j,):
        if matrix[nei_i][nei_j]==1 and (nei_i,nei_j) not in seen:
            next_seen = copy.deepcopy(seen)
            next_seen.add((nei_i,nei_j))
            rst_lst.append(dfs(matrix, next_seen, nei_i, nei_j))
    res_len += max(rst_lst)
    return res_len

def max_linked(matrix):
    n = len(matrix)
    m = len(matrix[0])

    untraveled = set([(i,j) for i in range(n) for j in range(m) if matrix[i][j]==1])

    max_len = 0
    for i,j in untraveled:
    # for i, j in ((0,5),(1,0),):
        cur_seen = set()
        cur_seen.add((i,j))
        cur_len = dfs(matrix, cur_seen, i, j)

        # for n_i, n_j in neighbors(matrix, i, j):
        #     if matrix[n_i][n_j] == 1 and (n_i, n_j) not in cur_seen:
        #
        #         cur_len += dfs(matrix, next_cur_seen, i, j)
        #
        max_len = max(max_len, cur_len)

    return max_len - 1

# def max_linked(matrix):
#     n = len(matrix)
#     m = len(matrix[0])
#
#     for i in range(n):
#         for j in range(j):
#             if matrix[i][j]:
#                 cur_deque = deque()
#                 cur_deque.append(matrix[i][j])
#                 seen = set([matrix[i][j]],)
#                 for ii,jj in neighbors(matrix,i,j):
#                     if matrix[ii][jj] and matrix[ii][jj] not in seen:
#                         cur_deque.append(matrix[ii][jj])
#

if __name__ == '__main__':
    a = [
            [0, 1, 1, 0, 1, 1, 1, 1,],
            [1, 0, 1, 0, 1, 0, 1, 0,],
            [1, 1, 1, 0, 1, 0, 1, 1,],
         ]

    rst = max_linked(a)
    print(rst)


