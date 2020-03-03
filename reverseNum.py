# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   reverseNum.py
@Contact :   9824373@qq.com
@Desc    :
            将输入的整数(正数或者负数)，反转顺序后输出。
@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-03     zhan        1.0         None
'''


def reverseNum_str(a):

    a_str = str(abs(a))
    a_str = ''.join(reversed(a_str))

    ans = int(a_str)

    return ans if a>0 else -ans


def reverseNum_mod(a):

    a_abs = abs(a)

    intList = []
    while a_abs > 0:
        intList.append(a_abs % 10)
        a_abs = a_abs // 10

    ans = 0
    for num in intList:
        ans *= 10
        ans += num

    return ans if a > 0 else -ans


if __name__ == '__main__':
    a = 120
    a = -120

    a = -130211

    a = -1980200

    a = 0

    a =  3246798976543


    ans_str = reverseNum_str(a)
    print(ans_str)

    ans_mod = reverseNum_mod(a)
    print(ans_mod)
