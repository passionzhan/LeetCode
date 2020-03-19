#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   longestPalindrome.py    
@Contact :   9824373@qq.com
@License :   (C)Copyright 2017-2018, Zhan
@Desc    :
            给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

            在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

            注意:
            假设字符串的长度不会超过 1010。

            示例 1:

            输入:
            "abccccdd"

            输出:
            7

            解释:
            我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/15 8:54   zhan      1.0         None
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        rst = 0
        for char in s:
            dict[char] = dict.setdefault(char, 0) + 1

        odd = False
        for k, v in dict.items():
            rst += v
            if v % 2 == 1:
                odd = True
                rst -= 1

        if odd:
            rst += 1

        return rst

if __name__ == '__main__':
    s = "dvdf"
    s = "abccccdd"
    # s = "aabaab!bb"
    print(Solution().longestPalindrome(s))