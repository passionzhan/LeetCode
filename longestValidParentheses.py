# -*- encoding: utf-8 -*-
'''
@project :   LeetCode 
@File    :   longestValidParentheses.py
@Contact :   9824373@qq.com
@Desc    :
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-02-28   zhan      1.0         None
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1: return 0
        flag = False
        dp = [0 for i in s]

        ans = 0
        for i in range(1,len(s)):
            char = s[i]
            if i == 1:
                if char == ')' and s[0] == '(': dp[i] = 2
                else: dp[i] = 0
            elif char == ')' and s[i-1] == '(':
                dp[i] = dp[i-2] + 2
            elif char == ')' and s[i-1] == ')' and i-1-dp[i-1] >=0 and s[i-1-dp[i-1]]=='(': # (dp[i])
                dp[i] = dp[i-1] + 2 + dp[i-1-dp[i-1]-1]
            ans = max(dp[i],ans)

        return ans





        # # 深度优先搜索
#         # if len(s) <= 1: return 0
#         # flag = False
#         # dfs = {}
#         # for i in range(0, len(s) - 1):
#         #     if s[i] == '(' and s[i + 1] == ')':
#         #         dfs[i] = i + 1
#         #         flag = True
#         #         ans = 2
#         #
#         # if not flag:
#         #     return 0
#         #
#         #
#         # for k,v in dfs.items():
#         #     if v in dfs.keys():
#         #         dfs[k] = dfs[v]
#         #     else:
#         #         if k-1>=0 and v+1 < len(s) and s[k-1] == '(' and s[v+1] == ')':
#         #             if k-1 not in dfs:
#         #                 dfs[k-1] = v+1:
#         #             else:
#         #                 if


'''
dp算法
        # dp = [[False for char in s] for c in s]
        # if len(s) <= 1: return 0
        # flag = False
        # for i in range(0,len(s)-1):
        #     if s[i] == '(' and s[i+1] == ')':
        #         dp[i][i+1] = True
        #         flag = True
        #         ans = 2
        #
        # if not flag:
        #     return 0

        # for sub_len in range(4, len(s)+1, 2):
        #     for i in range(0,len(s)):
        #         if i + sub_len > len(s):break
        #
        #         for delta in range(2,sub_len+1,2):
        #             if dp[i][i+delta-1] and dp[i+delta][i+sub_len-1]:
        #                 dp[i][i+sub_len-1] = True
        #                 break
        #         if not dp[i][i+sub_len-1]:
        #             if dp[i+1][i+sub_len-2] and s[i] == '(' and s[i+sub_len-1] == ')':
        #                 dp[i][i + sub_len - 1] = True
        #
        #         if dp[i][i+sub_len-1]:
        #             ans = max(sub_len,ans)
        #
        # return ans
'''


        #
        # if len(dp) == 0: return 0
        # else: ans = 2
        #
        # while flag:
        #     flag = False
        #     for i, (bIdx,eIdx) in enumerate(dp):
        #         if bIdx-1 > 0 and eIdx+1 < len(dp) and s[bIdx-1] == '(' and s[eIdx+1] == ')':
        #             ans = max(ans, eIdx - bIdx + 3)
        #             dp[i] = (bIdx-1,eIdx+1)
        #             flag = True
        #
        # ans = {item for item in ans}
        #
        # return ans



if __name__ == '__main__':
    a = '(())()))))(())))()'
    # a = "(()"
    # a = ")()())"
    # a = "()()"
    # a = '('
    # a = "((())())(()))(()()(()(()))(()((((()))))))((()())()))()()(()(((((()()()())))()())(()()))((((((())))((()))()()))))(()))())))()))()())((()()))))(()(((((())))))()((()(()(())((((())(())((()()(()())))())(()(())()()))())(()()()))()(((()())(((()()())))(((()()()))(()()))()))()))))))())()()((()(())(()))()((()()()((())))()(((()())(()))())())))(((()))))())))()(())))()())))())()((()))((()))()))(((())((()()()(()((()((())))((()()))())(()()(()))))())((())))(()))()))))))()(()))())(()())))))(()))((())(()((())(((((()()()(()()())))(()())()((()(()()))(()(())((()((()))))))))(()(())()())()(()(()(()))()()()(()()())))(())(()((((()()))())))(())((()(())())))))())()()))(((())))())((()(()))(()()))((())(())))))(()(()((()((()()))))))(()()()(()()()(()(())()))()))(((()(())()())(()))())))(((()))())(()((()))(()((()()()(())()(()())()(())(()(()((((())()))(((()()(((()())(()()()(())()())())(()(()()((()))))()(()))))(((())))()()))(()))((()))))()()))))((((()(())()()()((()))((()))())())(()((()()())))))))()))(((()))))))(()())))(((()))((()))())))(((()(((())))())(()))))(((()(((((((((((((())(((()))((((())())()))())((((())(((())))())(((()))))()())()(())())(()))))()))()()()))(((((())()()((()))())(()))()()(()()))(())(()()))()))))(((())))))((()()(()()()()((())((((())())))))((((((()((()((())())(()((()))(()())())())(()(())(())(()((())((())))(())())))(()()())((((()))))((()(())(()(()())))))))))((()())()()))((()(((()((()))(((((()()()()()(()(()((()(()))(()(()((()()))))()(()()((((((()((()())()))((())()()(((((()(()))))()()((()())((()())()(())((()))()()(()))"
    a = "(()))())("
    ans = Solution().longestValidParentheses(a)
    print(ans)








