#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : longestPalindrome.py
# @Author: Zhan
# @Date  : 5/22/2019
# @Desc  :
            '''
            给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

            示例 1：

            输入: "babad"
            输出: "bab"
            注意: "aba" 也是一个有效答案。
            示例 2：

            输入: "cbbd"
            输出: "bb"
            '''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) == 0:
            return ''


        dp = [[False for j in range(len(s))] for i in range(len(s))]
        rst = 1
        rst_str = s[0]

        for i in range(len(s)-1):
            dp[i][i] = True
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                rst = max(rst, 2)
                rst_str = s[i:i + 2]

        dp[len(s)-1][len(s)-1] = True

        for sub_len in range(3, len(s)+1):
            for i in range(len(s)-sub_len+1):
                # if i + sub_len - 1 < len(s):
                dp[i][i + sub_len - 1] = (s[i] == s[i + sub_len - 1] and dp[i + 1][i + sub_len - 2])
                if dp[i][i + sub_len - 1]:
                    if rst < sub_len:
                        rst = sub_len
                        rst_str = s[i:i + sub_len]
                        # rst = max(rst, sub_len)
                # if i - sub_len + 1 >= 0:
                #     dp[i + sub_len - 1][i] = (s[i] == s[i + sub_len - 1] and dp[i + 1][i + sub_len - 2])

        return rst_str


if __name__ == '__main__':
    # a, b, c = 99, 3, 1
    s = "abba"
    s = "cbbd"
    # s = "abcda"
    # s = "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
    print(Solution().longestPalindrome(s))
