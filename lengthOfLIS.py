# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   lengthOfLIS.py
@Contact :   9824373@qq.com
@Desc    :
            给定一个无序的整数数组，找到其中最长上升子序列的长度。

            示例:

            输入: [10,9,2,5,3,7,101,18]
            输出: 4
            解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
            说明:

            可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
            你算法的时间复杂度应该为 O(n2) 。
            进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/longest-increasing-subsequence

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-14     zhan        1.0         None
'''
from typing import List
from collections import defaultdict

class TriNode:
    def __init__(self):
        self.sequence = []
        self.children = defaultdict(TriNode)
        # self.parent = None

class Trie:
    def __init__(self):
        self.root = TriNode()
        self.ans = []

    def insert(self, node, num):
        '''
        往字典树中插入数字num
        :param num: int 类型
        :return:
        '''
        curNode = node
        inserted = False
        for k,v in curNode.children.items():
            if k < num:
                inserted = True
                self.insert(v, num)

        if not inserted:
            curNode.children[num].sequence = curNode.sequence[:]
            curNode.children[num].sequence.append(num)
            if len(curNode.children[num].sequence) > len(self.ans):
                self.ans = curNode.children[num].sequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            trie.insert(trie.root,num)

        return len(trie.ans)

if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]

    ans = Solution().lengthOfLIS(nums)
    print(ans)
