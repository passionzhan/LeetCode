# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   isValidBrackets.py
@Contact :   9824373@qq.com
@Desc    :
@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-02-29     zhan        1.0         None
'''


class Solution:
    def isValid(self, s: str) -> bool:
        s_stack = []
        for bracket in s:
            if len(s_stack) == 0 and (bracket == ')' or bracket == ']' or bracket == '}'):
                return False
            if bracket == '(' or bracket == '[' or bracket == '{':
                s_stack.append(bracket)
            elif bracket == ')':
                if s_stack.pop() != '(': return False
            elif bracket == ']':
                if s_stack.pop() != '[': return False
            elif bracket == '}':
                if s_stack.pop() != '{': return False

        if len(s_stack) > 0:
            return False
        else:
            return True


if __name__ == '__main__':
    a = "()[]{}"

    ans = Solution().isValid(a)
    print(ans)



