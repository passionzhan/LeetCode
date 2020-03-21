# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   minIncrementForUnique.py
@Contact :   9824373@qq.com
@Desc    :
            给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。

            返回使 A 中的每个值都是唯一的最少操作次数。

            示例 1:

            输入：[1,2,2]
            输出：1
            解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
            示例 2:

            输入：[3,2,1,2,1,7]
            输出：6
            解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
            可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
            提示：

            0 <= A.length <= 40000
            0 <= A[i] < 40000

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-22     zhan        1.0         None
'''
from typing import List

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if len(A) <= 1: return 0
        A.sort()

        num = 0
        for i in range(1, len(A)):
            num += max(0, A[i - 1] + 1 - A[i])
            A[i] = max(A[i], A[i - 1] + 1)

        return num


if __name__ == '__main__':
    A = [3,2,1,2,1,7]

    ans = Solution().minIncrementForUnique(A)
    print(ans)