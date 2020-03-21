# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   getLeastNumbers.py
@Contact :   9824373@qq.com
@Desc    :
            输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。



            示例 1：

            输入：arr = [3,2,1], k = 2
            输出：[1,2] 或者 [2,1]
            示例 2：

            输入：arr = [0,1,2,1], k = 1
            输出：[0]


            限制：

            0 <= k <= arr.length <= 10000
            0 <= arr[i] <= 10000
@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-20     zhan        1.0         None
'''
from typing import List
import heapq

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0: return []
        if len(arr) <= k: return arr

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)

        for x in arr[k:]:
            if -x > hp[0]:
                heapq.heappushpop(hp,-x)

        ans = [-x for x in hp[:k]]

        # ans = heapq.nsmallest(k,arr)

        return  ans

if __name__ == '__main__':
    arr = [0, 1, 2, 1]
    k = 2
    # arr = [0, 0, 0, 2, 0, 5]
    # k = 3
    ans = Solution().getLeastNumbers(arr,k)
    print(ans)
