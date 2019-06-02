#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   isMatch2.py
@Contact :   9824373@qq.com
@License :   (C)Copyright 2017-2018, Zhan
@Desc    :
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/6/2 21:02   zhan      1.0         None
@desc:
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        rst = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]

        rst[0][0] = True
        for j in range(1, len(p) + 1):
            rst[0][j] = rst[0][j - 1] and p[j-1] == '*'

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if (p[j - 1] == '*'):
                    rst[i][j] = rst[i][j - 1] or rst[i - 1][j]
                else:
                    rst[i][j] = (s[i - 1] == p[j - 1] or p[j - 1]
                                 == '?') and rst[i - 1][j - 1]

                # rst[i][j] =

        return rst[len(s)][len(p)]

if __name__ == '__main__':
    s = "ab"
    p = ".*c"
    # s = "aa"
    # p = "a"

    s = ""
    p = ".*"
    s = "aa"
    p = "a*"
    # s = "aa"
    # p = "a"
    # s = "ab"
    # p = ".*"
    # s = "aab"
    # p = "c*a*b"
    # s = "aab"
    # p = "b.*"
    print(Solution().isMatch(s, p))
