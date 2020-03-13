# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   gcdOfStrings.py
@Contact :   9824373@qq.com
@Desc    :
            对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。

            返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

             

            示例 1：

            输入：str1 = "ABCABC", str2 = "ABC"
            输出："ABC"
            示例 2：

            输入：str1 = "ABABAB", str2 = "ABAB"
            输出："AB"
            示例 3：

            输入：str1 = "LEET", str2 = "CODE"
            输出：""
             

            提示：

            1 <= str1.length <= 1000
            1 <= str2.length <= 1000
            str1[i] 和 str2[i] 为大写英文字母

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/greatest-common-divisor-of-strings

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-12     zhan        1.0         None
'''


'''
需要知道一个性质：如果 str1 和 str2 拼接后等于 str2和 str1 拼接起来的字符串（注意拼接顺序不同），那么一定存在符合条件的字符串 X。

先证必要性，即如果存在符合条件的字符串 X ，则 str1 和 str2 拼接后等于 str2和 str1 拼接起来的字符串。

再看充分性，简单来说，我们可以如下图一样先将两个拼接后的字符串放在一起。不失一般性，我们假定 str1 的长度大于 str2，
我们等间隔取 gcd(len1,len2)长度的字符串。则可以证明每个将的字符串都相等。
'''
import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2: return  ''
        tmpStr1 = str1 + str2
        tmpStr2 = str2 + str1

        gcd = math.gcd(len(str1),len(str2))
        if tmpStr1 == tmpStr2: return str1[:gcd]
        else: return ''
