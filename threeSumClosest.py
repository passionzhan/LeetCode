#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@project :   LeetCode 
@File    :   threeSumClosest
@Contact :   9824373@qq.com
@Desc    :
            给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

            例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

            与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/3sum-closest

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-02-21   zhan      1.0         None
'''

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        nums_len = len(sorted_nums)
        ans = sorted_nums[0] + sorted_nums[1] + sorted_nums[2]
        for i in range(nums_len-2):
            # 当前最小的三个数相加比 target 提前终止循环
            tmp_sum = sorted_nums[i] + sorted_nums[i+1] + sorted_nums[i+2]
            if abs(target - tmp_sum) < abs(target - ans):
                ans = tmp_sum
            if tmp_sum > target:
                return ans

            # 终止此轮循环
            tmp_sum = sorted_nums[i] + sorted_nums[nums_len - 2] + sorted_nums[nums_len - 1]
            if abs(target - tmp_sum) < abs(target - ans):
                ans = tmp_sum
            if tmp_sum < target:
                continue

            bIdx = i + 1
            eIdx = nums_len - 1
            while bIdx < eIdx:
                tmp_sum = sorted_nums[i] + sorted_nums[bIdx] + sorted_nums[eIdx]
                if abs(target - tmp_sum) < abs(target - ans):
                    ans = tmp_sum

                if target > tmp_sum:
                    bIdx += 1
                elif target < tmp_sum:
                    eIdx -= 1
                else:
                    return ans

        return ans

if __name__ == '__main__':

    a = [-2,-1,3,3]
    target = 2
    a       = [-1, 2, 1, -4]
    target  = 1

    ans = Solution().threeSumClosest(a,target)
    print(ans)
