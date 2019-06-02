#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   isMatch.py
@Contact :   9824373@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/31 22:19   zhan      1.0         None
'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        dp = [{} for i in range(len(s) + 1)]
        dp[0]['0'] = True
        for i in range(1, len(s)+1):
            dp[i]['0'] = False

        for j in range(1, len(p)+1):
            if j % 2 == 0:
                dp[0][str(j)] = dp[0][str(j-2)] and p[j-1] == '*'
            else:
                dp[0][str(j)] = False

        for i in range(1,len(s) + 1):
            for j in range(1,len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][str(j)] = (dp[i].setdefault(str(j - 2),False) or (dp[i - 1].setdefault(str(j),False) and ((s[i - 1] == p[j - 2]) or p[j-2] == '.')))
                elif p[j - 1] == '.':
                    dp[i][str(j)] = dp[i - 1].setdefault(str(j - 1), False)
                else:
                    dp[i][str(j)] = (s[i - 1] == p[j - 1]
                                     and dp[i - 1].setdefault(str(j - 1), False))
        return dp[len(s)].setdefault(str(len(p)),False)

if __name__ == '__main__':
    s = "ab"
    p = ".*c"
    # s = "aa"
    # p = "a"

    s = ""
    p = ".*"
    s = "aa"
    p = "a*"
    # s = "ab"
    # p = ".*"
    # s = "aab"
    # p = "c*a*b"
    s = "aab"
    p = "b.*"
    print(Solution().isMatch(s, p))
