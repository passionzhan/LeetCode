# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   coinChange.py
@Contact :   9824373@qq.com
@Desc    :
            给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

            示例 1:

            输入: coins = [1, 2, 5], amount = 11
            输出: 3
            解释: 11 = 5 + 5 + 1
            示例 2:

            输入: coins = [2], amount = 3
            输出: -1
            说明:
            你可以认为每种硬币的数量是无限的。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/coin-change

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-08     zhan        1.0         None
'''
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        动态规划算法
        :param coins:
        :param amount:
        :return:
        '''
        if amount == 0: return 0
        all_ans = {val:1 for val in coins}
        if amount in all_ans: return 1
        basic_eles = coins
        basci_minVal = min(coins)
        pre_eles = coins
        pre_minVal = basci_minVal

        while pre_minVal + basci_minVal <= amount:
            cur_eles = []
            cur_minVal = float('inf')
            for val_i in basic_eles:
                for val_j in pre_eles:
                    curVal = val_i + val_j
                    if curVal not in all_ans:
                        cur_minVal = min(curVal, cur_minVal)
                        cur_eles.append(curVal)
                        all_ans[curVal] = 1 + all_ans[val_j]
                        if curVal == amount:
                            return all_ans[curVal]
                        # else:
                        #     cur_eles.append(curVal)
            pre_minVal = cur_minVal
            pre_eles = cur_eles

        return -1

if __name__ == '__main__':
    coins = [4,1]
    amount = 3
    coins = [1, 2, 5]
    amount = 11

    ans = Solution().coinChange(coins,amount)
    print(ans)

