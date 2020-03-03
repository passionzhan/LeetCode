# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   largestNumber.py
@Contact :   9824373@qq.com
@Desc    :
            给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

            示例 1:

            输入: [10,2]
            输出: 210
            示例 2:

            输入: [3,30,34,5,9]
            输出: 9534330
            说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/largest-number
@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-03     zhan        1.0         None
'''
from typing import List
import functools

class Solution:
    def cmp(self,a,b):
        if str(a) + str(b) >str(b) + str(a):
            return -1
        else:
            return 1

    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 0: return  '0'
        if len(nums) == 1: return  str(nums[0])

        for i, num in enumerate(nums):
            nums[i] = str(num)

        nums.sort(key = functools.cmp_to_key(self.cmp))
        ans = ''.join(nums) +  '1'
        ans.strip('0')
        if len(ans) == 1:
            ans = '0'
        else:
            ans = ans[0:-1]
        return ans


if __name__ == '__main__':
    a = [3, 30, 34, 5, 9]

    ans = Solution().largestNumber(a)
    print(ans)