# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   fourSum.py
@Contact :   9824373@qq.com
@Desc    :
            给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

            注意：

            答案中不可以包含重复的四元组。

            示例：

            给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

            满足要求的四元组集合为：
            [
              [-1,  0, 0, 1],
              [-2, -1, 1, 2],
              [-2,  0, 0, 2]
            ]

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-18     zhan        1.0         None
'''
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) <4: return []
        nums.sort()
        ans = self.dfs(nums,target,depth=1,prefix=[])


        return ans

    def dfs(self,nums,target,depth,prefix):
        ans = []
        if depth == 4:
            for num in nums:
                if num == target:
                    tmp = prefix[:]
                    tmp.append(num)
                    ans.append(tmp)
                    # 保证不重复，最后一层只返回一个即可
                    return ans
            return ans

        else:
            curNums = nums[:]
            for i, num in enumerate(nums):
                curNums.remove(num)
                if i>=1 and num == nums[i-1]:
                    continue

                curTarget = target - num
                curPrefix = prefix[:]
                curPrefix.append(num)
                ans += self.dfs(curNums,curTarget,depth+1,curPrefix)
            return ans

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    nums = [-3, -2, -1, 0, 0, 1, 2, 3]
    target = 0
    nums = [5, 5, 3, 5, 1, -5, 1, -2]
    target = 4

    ans = Solution().fourSum(nums,target)
    print(ans)






