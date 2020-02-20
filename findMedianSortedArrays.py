#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   findMedianSortedArrays
@Contact :   9824373@qq.com
@Desc    :
                给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

                请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

                你可以假设 nums1 和 nums2 不会同时为空。

                示例 1:

                nums1 = [1, 3]
                nums2 = [2]

                则中位数是 2.0
                示例 2:

                nums1 = [1, 2]
                nums2 = [3, 4]

                则中位数是 (2 + 3)/2 = 2.5

                来源：力扣（LeetCode）
                链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-02-19   zhan      1.0         None
'''

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if n < m:
            nums1, nums2, m, n = nums2, nums1, n, m

        if n == 0:
            raise ValueError
        if m == 0:
            return (nums2[n//2] + nums2[n//2 -1])/2  if n % 2 == 0 else nums2[n//2]

        bIdx, eIdx = 0, m
        half_len = (m+n) // 2

        while bIdx <= eIdx:
            mid_i = (bIdx + eIdx) // 2
            mid_j = half_len - mid_i

            if mid_i < m and nums2[mid_j-1] > nums1[mid_i]:
                # 右移
                bIdx = mid_i + 1
            elif mid_i > 0 and nums1[mid_i-1] > nums2[mid_j]:
                # 左移
                eIdx = mid_i - 1
            else:
                # mid_i 分割正好
                # 1 、nums2[mid_j-1] <= nums1[mid_i] and nums1[mid_i-1] <= nums2[mid_j]:
                # 2、 边界  mid_i <= 0 或者 mid_i >= m
                if mid_i == 0: max_left = nums2[mid_j-1]
                elif mid_j == 0: max_left = nums1[mid_i-1]
                else: max_left = max(nums2[mid_j-1],nums1[mid_i-1])

                if mid_i == m: min_right = nums2[mid_j]
                elif mid_j == n: min_right = nums1[mid_i]
                else: min_right = min(nums2[mid_j],nums1[mid_i])

                if (m + n) % 2 == 0:
                    return (max_left + min_right) / 2
                else:
                    return min_right





if __name__ == '__main__':
    # nums1 = [1, 3]
    nums1 = [2,3]
    # nums1 = [1, 2]
    # nums2 = [3, 4]
    # nums1 = []
    # nums2 = [1]
    # nums1 = [3]
    nums2 = [-2, -1, 0, 1]
    nums1 = [0, 0]
    nums2 = [0, 0]
    nums1 = [-3,-2,-1,1, 2, 3]
    nums2 = [ 4, 5,7]

    nums1 = [1, 2]
    nums2 = [-1, 3]
    nums1 = [3, 4]
    nums2 = [1, 2, 5]
    nums1 = [1, 2, 4]
    nums1 = [1, 2]
    nums2 = [3, 4]
    # nums2 = [3, 5, 6]
    # nums1 = [1, 3]
    # nums2 = [2, 4, 5, 6, 7]
    # nums1 = [1, 2, 4]
    # nums2 = [3, 5, 6, 7]
    ans = Solution().findMedianSortedArrays(nums1,nums2)
    print(ans)