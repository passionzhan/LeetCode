# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   numWays.py
@Contact :   9824373@qq.com
@Desc    :
            一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

            答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

            示例 1：

            输入：n = 2
            输出：2
            示例 2：

            输入：n = 7
            输出：21
            提示：

            0 <= n <= 100
            注意：本题与主站 70 题相同：https://leetcode-cn.com/problems/climbing-stairs/

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-20     zhan        1.0         None
'''

class Solution:
    def numWays(self, n: int) -> int:
        tmpArr = []
        tmpArr.append(1)
        tmpArr.append(1)

        if n == 0: return tmpArr[0]
        if n == 1: return tmpArr[1]
        for i in range(2,n+1):
            tmpArr.append(tmpArr[i-1]+tmpArr[i-2])

        return tmpArr[n] % (int)(1e9+7)

if __name__ == '__main__':
    n = 54

    ans = Solution().numWays(n)
    print(ans)


