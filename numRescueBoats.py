# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   numRescueBoats.py
@Contact :   9824373@qq.com
@Desc    :
            第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。

            每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

            返回载到每一个人所需的最小船数。(保证每个人都能被船载)。



            示例 1：

            输入：people = [1,2], limit = 3
            输出：1
            解释：1 艘船载 (1, 2)
            示例 2：

            输入：people = [3,2,2,1], limit = 3
            输出：3
            解释：3 艘船分别载 (1, 2), (2) 和 (3)
            示例 3：

            输入：people = [3,5,3,4], limit = 5
            输出：4
            解释：4 艘船分别载 (3), (3), (4), (5)
            提示：

            1 <= people.length <= 50000
            1 <= people[i] <= limit <= 30000

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-19     zhan        1.0         None
'''
from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        ans = 0
        i, j = 0, len(people)-1
        while i <= j:
            ans += 1
            # 最重和最轻能坐一条船
            if people[i] + people[j] <= limit:
                i += 1
                # i向前移一位
            #否则最重的自己做一条船， j 要 -1
            # 最重的和最轻的和坐一条船， j 也要 -1
            j -= 1

        return ans


if __name__ == '__main__':
    people = [3,5,3,4]
    limit = 5

    people = [3, 2, 2, 1]
    limit = 3
    ans = Solution().numRescueBoats(people,limit)
    print(ans)