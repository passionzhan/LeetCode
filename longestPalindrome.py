#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : longestPalindrome.py
# @Author: Zhan
# @Date  : 5/22/2019
# @Desc  :

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

        for i in range(len(s)):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = True
                elif j - i <= 1 and s[i] == s[j]:
                    dp[i][j] = True
                    rst = max(rst, 2)
                    rst_str = s[i:j+1]
                    # dp[j][i] = True
                else:
                    dp[i][j] = False

        for sub_len in range(3, len(s)+1):
            for i in range(len(s)):
                if i + sub_len - 1 < len(s):
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
    s = "abcda"
    print(Solution().longestPalindrome(s))
