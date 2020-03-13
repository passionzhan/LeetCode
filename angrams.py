# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   angrams.py
@Contact :   9824373@qq.com
@Desc    :
            编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。

            注意：本题相对原题稍作修改

            示例:

            输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
            输出:
            [
              ["ate","eat","tea"],
              ["nat","tan"],
              ["bat"]
            ]
            说明：

            所有输入均为小写字母。
            不考虑答案输出的顺序。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/group-anagrams-lcci

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-13     zhan        1.0         None
'''


from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        以排序后的字符串为key键hash表。
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        sort_strs = defaultdict(list)


        for s in strs:
            tmps = ''.join(sorted(s))
            sort_strs[tmps].append(s)

        return list(sort_strs.values())

if __name__ == '__main__':

    a = ["eat","tea","tan","ate","nat","bat"]
    rst = Solution().groupAnagrams(a)
    print(rst)