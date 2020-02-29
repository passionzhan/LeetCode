# -*- encoding: utf-8 -*-
'''
@project :   LeetCode 
@File    :   letterCombinations.py
@Contact :   9824373@qq.com
@Desc    :

        给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

        给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
        输入："23"
        输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-02-28   zhan      1.0         None
'''
from typing  import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        i2char = {}
        i2char['2'] = ['a', 'b', 'c']
        i2char['3'] = ['d', 'e', 'f']
        i2char['4'] = ['g', 'h', 'i']
        i2char['5'] = ['j', 'k', 'l']
        i2char['6'] = ['m', 'n', 'o']
        i2char['7'] = ['p', 'q', 'r', 's']
        i2char['8'] = ['t', 'u', 'v']
        i2char['9'] = ['w', 'x', 'y', 'z']

        if len(digits) == 0: return []
        pre_ans = []
        # pre_ans += map[digits[0]]

        for i in range(0, len(digits)):
            cur_ans = []
            if len(pre_ans) == 0:
                pre_ans = i2char[digits[i]]
                continue
            for s in pre_ans:
                for char in i2char[digits[i]]:
                    tmp = s[:]
                    tmp += char
                    cur_ans.append(tmp)
            pre_ans = cur_ans

        return pre_ans


if __name__ == '__main__':
    a = '347'

    ans = Solution().letterCombinations(a)
    print(ans)