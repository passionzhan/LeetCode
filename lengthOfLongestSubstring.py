'''
@project :   LeetCode
@File    :   lengthOfLongestSubstring
@Contact :   9824373@qq.com
@Desc    :
            给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

            示例 1:

            输入: "abcabcbb"
            输出: 3
            解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
            示例 2:

            输入: "bbbbb"
            输出: 1
            解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
            示例 3:

            输入: "pwwkew"
            输出: 3
            解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
                 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-02-24   zhan      1.0         None
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        bIdx, eIdx, ans = 0, 0, 0
        curDict = {}
        while eIdx < len(s):
            if s[eIdx] not in curDict:
                curDict[s[eIdx]] = eIdx
            else:
                for char in s[bIdx:curDict[s[eIdx]]]:
                    curDict.pop(char)
                bIdx = curDict[s[eIdx]] + 1
                curDict[s[eIdx]] = eIdx
            ans = max(len(curDict), ans)
            eIdx += 1
        return ans


if __name__ == '__main__':
    a = "abcabcbb"
    # a = "pwwkew"
    a = "因为DFDAF无重DF复DF字F为符"
    ans = Solution().lengthOfLongestSubstring(a)
    print(ans)