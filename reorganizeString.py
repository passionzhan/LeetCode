# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   reorganizeString.py
@Contact :   9824373@qq.com
@Desc    :
@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-01     zhan        1.0         None
'''

class Solution:
    def reorganizeString(self, S: str) -> str:
        charSet = {}
        if len(S) <= 1: return S

        maxCount = 0
        maxCount_char = ''
        for char in S:
            charSet.setdefault(char,0)
            charSet[char] += 1
            if charSet[char] > (len(S)-1)// 2 + 1: return ''
            if maxCount < charSet[char]:
                maxCount = charSet[char]
                maxCount_char = char

        s_s = maxCount_char * charSet[maxCount_char]

        for char in charSet:
            if char != maxCount_char:
                s_s += char * charSet[char]

        ans = [' ']* len(s_s)
        ans[::2], ans[1::2] = s_s[:(len(ans)+1)//2], s_s[(len(ans)+1)//2:],
        ans = ''.join(ans)

        return ans

        # gap = (len(S)+1) // maxCount
        #
        # ans = [maxCount_char if i%gap==0 else ' ' for i in range(len(S))]

        # ans = ''
        # # while len(ans) < len(S):
        # for char in charSet:
        #     ans += [char] * charSet[char] * 2
        #     i = 1
        # 
        #     if charSet[char] > 0:
        #         ans += char
        #         charSet[char] -= 1

        return ans


if __name__ == '__main__':
    S = "aab"
    # S = "aaab"
    # S = 'aaabc'
    # SS = { char:1  for char in S}

    ans = Solution().reorganizeString(S)

    print(ans)
