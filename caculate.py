# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   caculate.py
@Contact :   9824373@qq.com
@Desc    :
            请实现如下接口

                /* 功能：四则运算

                 * 输入：strExpression：字符串格式的算术表达式，如: "3+2*{1+2*[-4/(8-6)+7]}"

                     * 返回：算术表达式的计算结果

                 */

                public static int calculate(String strExpression)

                {

                    /* 请实现*/

                    return 0;

                }

            约束：

            pucExpression字符串中的有效字符包括[‘0’-‘9’],‘+’,‘-’, ‘*’,‘/’ ,‘(’， ‘)’,‘[’, ‘]’,‘{’ ,‘}’。

            pucExpression算术表达式的有效性由调用者保证;

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-24     zhan        1.0         None
'''
from typing import List

class Solution:
    def calculate(self, strExpression: str):
        stack = []


        first_op = {'*','/'}
        second_op = {'+','-'}
        left_brakects = {'(','[','{'}
        right_brakects = {')',']','}'}
        digits = {'0','1','2','3', '4','5','6','7', '8','9'}


        def getEle(strExp):
            ans = ''
            i = 0
            while i < len(strExp):
                if strExp[i] not in digits:
                    if len(ans) == 0:
                        yield strExp[i]
                        i += 1
                    else:
                        yield int(ans)
                        ans = ''
                        # i -= 1
                else:
                    ans += strExp[i]
                    i += 1
                    if i == len(strExp):
                        yield int(ans)

        # for ele in getEle(strExpression):
        eleLst = []
        for ele in getEle(strExpression):
            eleLst.append(ele)

        while eleLst:
            curEle = eleLst.pop(0)
            if not stack:
                stack.append(curEle)
                continue
            if curEle not in first_op and curEle not in second_op and curEle not in left_brakects and curEle not in right_brakects:
                op = stack.pop()
                if op in left_brakects:
                    stack.append(op)
                    stack.append(curEle)
                elif op in first_op:
                    firstNum = stack.pop()
                    if op == '*': rst = firstNum * curEle
                    elif op == '/': rst = firstNum / curEle
                    eleLst.insert(0, rst)
                elif op in second_op:
                    firstNum = stack.pop()
                    if (eleLst and eleLst[0] not in first_op) or (not eleLst):
                        if op == '+': rst = firstNum + curEle
                        elif op == '-':
                            # 处理负数情况
                            if firstNum in first_op or firstNum in second_op or firstNum in left_brakects or firstNum in right_brakects:
                                rst = -curEle
                                stack.append(firstNum)
                            else:
                                rst = firstNum - curEle
                        eleLst.insert(0, rst)
                    else:
                        stack.append(firstNum)
                        stack.append(op)
                        stack.append(curEle)
                # i += 1
            elif curEle in right_brakects:
                firstNum = stack.pop()
                l_brakect = stack.pop()
                eleLst.insert(0, firstNum)
                # i += 1
            else:
                stack.append(curEle)
                # i += 1
        ans = stack.pop()
        return ans

if __name__ == '__main__':
    test  = '3+34*4*[(956+31)-4/3]+9876/67'
    test = '3+2*{1+2*[-4/(8-6)+7]}'
    # test  = '3+34*4'

    ans = Solution().calculate(test)
    print(ans)
    print(eval(r'3+2*(1+2*(-4/(8-6)+7))'))
    # a = 3+34*4*((956+31)-4/3)+9876/67
    # print(a)
    # '3+34*4*[(956+31)-4/3]+9876/67'


