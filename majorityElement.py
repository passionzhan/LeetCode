# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   majorityElement.py
@Contact :   9824373@qq.com
@Desc    :
            给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

            你可以假设数组是非空的，并且给定的数组总是存在多数元素。

            示例 1:

            输入: [3,2,3]
            输出: 3
            示例 2:

            输入: [2,2,1,1,1,2,2]
            输出: 2

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/majority-element

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-13     zhan        1.0         None
'''
from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = defaultdict(int)
        bound = len(nums) // 2
        for val in nums:
            my_dict[val] += 1
            if my_dict[val] > bound:
                return val

        return None

if __name__ == '__main__':
    nums = [2,2,1,1,1,2,2]
    nums = [3,2,3]

    ans = Solution().majorityElement(nums)
    print(ans)