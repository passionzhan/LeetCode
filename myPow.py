# -*- encoding: utf-8 -*-
'''
@project :   LeetCode 
@File    :   myPow
@Contact :   9824373@qq.com
@Desc    :
            实现 pow(x, n) ，即计算 x 的 n 次幂函数。

            示例 1:

            输入: 2.00000, 10
            输出: 1024.00000
            示例 2:

            输入: 2.10000, 3
            输出: 9.26100
            示例 3:

            输入: 2.00000, -2
            输出: 0.25000
            解释: 2-2 = 1/22 = 1/4 = 0.25
            说明:

            -100.0 < x < 100.0
            n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/powx-n

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-02-26   zhan      1.0         None
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        pos_n = abs(n)
        tmp = x
        ans = 1
        while pos_n > 0:
            if pos_n % 2 == 1:
                ans *= tmp
            tmp *= tmp
            pos_n = pos_n >> 1

        if n < 0:
            ans = 1/ans
        return ans


if __name__ == '__main__':
    x = 3
    n = -7
    # n = 7
    # n = 8
    # n = -16
    # n = 16
    ans = Solution().myPow(x,n)

    print(ans)

    print(pow(x,n))
