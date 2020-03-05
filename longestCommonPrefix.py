# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   longestCommonPrefix.py
@Contact :   9824373@qq.com
@Desc    :

            编写一个函数来查找字符串数组中的最长公共前缀。

            如果不存在公共前缀，返回空字符串 ""。

            示例 1:

            输入: ["flower","flow","flight"]
            输出: "fl"
            示例 2:

            输入: ["dog","racecar","car"]
            输出: ""
            解释: 输入不存在公共前缀。
            说明:

            所有输入只包含小写字母 a-z 。

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-05     zhan        1.0         None
'''
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return  ''
        min_len = min(map(len,strs))

        idx = 0
        fStr = strs[0]
        while idx <= min_len-1:
            # idx += 1
            exit = False
            for i in range(1,len(strs)):
                if strs[i][idx] != fStr[idx]:
                    exit = True
                    break
            if exit:
                break
            idx += 1

        return '' if idx < 0 else fStr[:idx]



if __name__ == '__main__':
    strs = ["flower","flow","floight"]
    # strs = ["rog", "racecar", "rar"]
    # strs = []
    # strs = ["c", "c"]
    ans = Solution().longestCommonPrefix(strs)
    print(ans)