# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   merge.py
@Contact :   9824373@qq.com
@Desc    :
            给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。

            初始化 A 和 B 的元素数量分别为 m 和 n。

            示例:

            输入:
            A = [1,2,3,0,0,0], m = 3
            B = [2,5,6],       n = 3

            输出: [1,2,2,3,5,6]

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/sorted-merge-lcci

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-03     zhan        1.0         None
'''
from typing import List

class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """

        idx = m + n -1
        Aidx = m - 1
        Bidx = n - 1
        while idx >= 0:
            if Aidx < 0:
                A[idx] = B[Bidx]
                Bidx -= 1
            elif Bidx < 0:
                A[idx] = A[Aidx]
                Aidx -= 1
            elif A[Aidx] > B[Bidx]:
                A[idx] = A[Aidx]
                Aidx -= 1
            else:
                A[idx] = B[Bidx]
                Bidx -= 1

            idx -= 1


if __name__ == '__main__':
    A = [1,2,3,0,0,0]
    m = 3
    B = [2,5,6]
    n = 3

    Solution().merge(A,m,B,n)
    print(A)
