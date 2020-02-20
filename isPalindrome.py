#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@project :   LeetCode 
@File    :   isPalindrome
@Contact :   9824373@qq.com
@Desc    :
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

    示例 1:

    输入: 121
    输出: true
    示例 2:

    输入: -121
    输出: false
    解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
    示例 3:

    输入: 10
    输出: false
    解释: 从右向左读, 为 01 。因此它不是一个回文数。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/palindrome-number

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-02-20   zhan      1.0         None
'''


class Solution:
    def isPalindrome_str(self, x: int) -> bool:
        if x < 0: return False

        x_str = str(x)
        bIdx = 0
        eIdx = len(x_str)- 1
        if eIdx == bIdx: return True
        else:
            while eIdx - bIdx >= 1:
                if x_str[bIdx] != x_str[eIdx]:
                    return False

                bIdx += 1
                eIdx -= 1
            return True

    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == 0: return True

        nums = []
        while x != 0:
            nums.append(x%10)
            x = x // 10

        bIdx = 0
        eIdx = len(nums)- 1
        if eIdx == bIdx: return True
        else:
            while eIdx - bIdx >= 1:
                if nums[bIdx] != nums[eIdx]:
                    return False

                bIdx += 1
                eIdx -= 1
            return True

    def numsofInt(self,x: int)->int:
        c = 0
        while x != 0:
            x = x // 10
            c += 1
        return c



if __name__ == '__main__':



    a = 10201
    a = -10
    a = 110
    a = 11011

    ans = Solution().isPalindrome(a)
    print(ans)
