# -*- encoding: utf-8 -*-
'''
@project :   LeetCode 
@File    :   combinationSum
@Contact :   9824373@qq.com
@Desc    :
        给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

        candidates 中的数字可以无限制重复被选取。

        说明：

        所有数字（包括 target）都是正整数。
        解集不能包含重复的组合。 
        示例 1:

        输入: candidates = [2,3,6,7], target = 7,
        所求解集为:
        [
          [7],
          [2,2,3]
        ]
        示例 2:

        输入: candidates = [2,3,5], target = 8,
        所求解集为:
        [
          [2,2,2,2],
          [2,3,3],
          [3,5]
        ]


@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-02-24   zhan      1.0         None
'''

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []

        if target <=0:
            return []

        path = []
        ans = []
        candidates = sorted(candidates)
        # self.dfs(target,candidates,0,len(candidates),path,ans)
        ans = self.dp(candidates,target)
        return ans

    def dfs(self,target,cand,bIdx,eIdx,path,ans):
        for i in range(bIdx,eIdx):
            delta = target - cand[i]
            if delta == 0:
                cur_path = path[:]
                cur_path.append(cand[i])
                ans.append(cur_path[:])
            elif delta > 0:
                cur_path = path[:]
                cur_path.append(cand[i])
                self.dfs(delta,cand,i,eIdx,cur_path,ans)
            else:
                break

        return ans

    def dp(self,candidates,target):
        t_dict  = {}
        for i in range(1,target+1):
            t_dict[i] = []

        for i in range(1,target+1):
            for j in candidates:
                if j == i:
                    t_dict[i].append([j])
                elif j < i:
                    for item in t_dict[i-j]:
                        x = item[:]
                        x.append(j)
                        x = sorted(x)
                        if x not in t_dict[i]:
                            t_dict[i].append(x)
                else:
                    break
        return t_dict[target]


if __name__ == '__main__':
    candidates = [2, 3, 6, 7,1,]
    # candidates = [7,2,3,]
    target = 7
    candidates = [2, 5, 3, 6]
    target = 8
    ans = Solution().combinationSum(candidates,target)
    print(ans)
