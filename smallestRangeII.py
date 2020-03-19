# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   smallestRangeII.py
@Contact :   9824373@qq.com
@Desc    :
            给定一个整数数组 A，对于每个整数 A[i]，我们可以选择 x = -K 或是 x = K，并将 x 加到 A[i] 中。

            在此过程之后，我们得到一些数组 B。

            返回 B 的最大值和 B 的最小值之间可能存在的最小差值。



            示例 1：

            输入：A = [1], K = 0
            输出：0
            解释：B = [1]
            示例 2：

            输入：A = [0,10], K = 2
            输出：6
            解释：B = [2,8]
            示例 3：

            输入：A = [1,3,6], K = 3
            输出：3
            解释：B = [4,6,3]


            提示：

            1 <= A.length <= 10000
            0 <= A[i] <= 10000
            0 <= K <= 10000

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-20     zhan        1.0         None
'''

'''
对于有序的 A，只需要对每个 i，比较 A[0] + K, A[i] + K, A[i+1] - K, A[A.length - 1] - K 。
'''
from typing import List

class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        min_v, max_v = A[0], A[len(A)-1]
        ans = max_v - min_v

        for i in range(len(A)-1):
            a, b = A[i], A[i+1]
            ans = min(ans, max(max_v-K,a+K)-min(min_v+K,b-K))

        return ans

if __name__ == '__main__':
    A = [1,3,6]
    K = 3

    ans = Solution().smallestRangeII(A, K)
    print(ans)



