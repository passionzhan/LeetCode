#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   longestPalindrome.py    
@Contact :   9824373@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :     
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