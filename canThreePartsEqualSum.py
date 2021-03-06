# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   canThreePartsEqualSum.py
@Contact :   9824373@qq.com
@Desc    :
            给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。

            形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。

             

            示例 1：

            输出：[0,2,1,-6,6,-7,9,1,2,0,1]
            输出：true
            解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
            示例 2：

            输入：[0,2,1,-6,6,7,9,-1,2,0,1]
            输出：false
            示例 3：

            输入：[3,3,6,5,-2,2,5,1,-9,4]
            输出：true
            解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
             

            提示：

            3 <= A.length <= 50000
            -10^4 <= A[i] <= 10^4

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-11     zhan        1.0         None
'''
from typing import List

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if len(A) <= 2: return False
        total = sum(A)
        if total % 3 != 0: return False

        tmpSum = 0
        iflag = 0

        for i, val in enumerate(A):
            tmpSum += val
            if tmpSum == total/3:
                tmpSum = 0
                iflag += 1

            if iflag == 3:
                break

        if iflag == 3: return True
        else: return False


if __name__ == '__main__':
    A = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
    A = [0,2,1,-6,6,7,9,-1,2,0,1]
    A = [3,3,6,5,-2,2,5,1,-9,4]
    ans = Solution().canThreePartsEqualSum(A)
    print(ans)
