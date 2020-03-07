# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   findContinuousSequence.py
@Contact :   9824373@qq.com
@Desc    :
        输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

        序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

         

        示例 1：

        输入：target = 9
        输出：[[2,3,4],[4,5]]
        示例 2：

        输入：target = 15
        输出：[[1,2,3,4,5],[4,5,6],[7,8]]
         

        限制：

        1 <= target <= 10^5

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-06     zhan        1.0         None
'''
from typing import List

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        curList= []
        curSum = 0
        ans = []
        i = 0
        while i <= (target+1)//2:
            i += 1
            curList.append(i)
            curSum += i
            if curSum == target:
                ans.append(curList[:])
            elif curSum > target:
                while curList:
                    curEle = curList[0]
                    curSum -= curEle
                    curList.remove(curEle)
                    if curSum < target:
                        break
                    elif curSum == target:
                        ans.append(curList[:])
                        break

        return ans

if __name__ == '__main__':
    target = 9
    # target = 15

    ans = Solution().findContinuousSequence(target)
    print(ans)
