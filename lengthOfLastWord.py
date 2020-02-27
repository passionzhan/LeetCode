# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   lengthOfLastWord
@Contact :   9824373@qq.com
@Desc    :
            给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。

            如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

            如果不存在最后一个单词，请返回 0 。

            说明：一个单词是指仅由字母组成、不包含任何空格的 最大子字符串。

             

            示例:

            输入: "Hello World"
            输出: 5

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/length-of-last-word

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-02-20   zhan      1.0         None
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # "a "
        s = s.strip()
        ans = None
        for char in s:
            if char == " ":
                ans = None
            elif ans is None:
                ans = char
            else:
                ans +=char

        ans = 0 if ans == None else len(ans)
        return ans


if __name__ == '__main__':
    s = "ww ad "
    ans = Solution().lengthOfLastWord(s)
    print(ans)
