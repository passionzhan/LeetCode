#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   maxUncrossLines_dp.py    
@Contact :   9824373@qq.com
@License :   (C)Copyright 2017-2018, Zhan
@Desc    :     
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/7 22:25   zhan      1.0         None
'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   maxUncrossedLines.py
@Contact :   9824373@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/5 1:10   zhan      1.0         None
'''

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   maxUncrossedLines_backup.py
@Contact :   9824373@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/5/4 21:40   zhan      1.0         None
'''


class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        rst = [[0 for j in range(len(B)+1)] for i in range(len(A)+1)]

        for i in range(1,len(rst)):
            for j in range(1,len(rst[0])):
                if A[i-1] == B[j-1]:
                    rst[i][j] = 1 + rst[i-1][j-1]
                else:
                    rst[i][j] = max(rst[i-1][j], rst[i][j-1])

        return rst[-1][-1]

        # a_idx, a_idx_b, b_idx, b_idx_a = 0, 0, 0, 0
        # found = False
        # for i, ai in enumerate(A):
        #     for j, bj in enumerate(B):
        #         if ai == bj:
        #             a_idx_b = j
        #             found = True
        #             break
        #     if found:
        #         a_idx = i
        #         break
        #
        # if not found:
        #     return 0
        #
        # found = False
        # for j in range(a_idx_b + 1):
        #     bj = B[j]
        #     for i, ai in enumerate(A[a_idx:]):
        #         if bj == ai:
        #             b_idx_a = i + a_idx
        #             found = True
        #             break
        #     if found:
        #         b_idx = j
        #         break
        #
        # if len(A) == 1 or len(B) == 1:
        #     return 1
        #
        # if a_idx_b + 1 < len(B) \
        #         and b_idx + 1 < len(B) \
        #         and a_idx + 1 < len(A) \
        #         and b_idx_a + 1 < len(A):
        #     if a_idx_b == b_idx:
        #         return 1 + self.maxUncrossedLines(A[a_idx + 1:], B[a_idx_b + 1:])
        #     else:
        #         a = max(1 + self.maxUncrossedLines(A[a_idx + 1:], B[a_idx_b + 1:]),
        #             self.maxUncrossedLines(A[1:], B))
        #         b = max(1 + self.maxUncrossedLines(A[b_idx_a + 1:], B[b_idx + 1:]),
        #             self.maxUncrossedLines(A, B[1:]))
        #         return max(a, b)
        # else:
        #     if a_idx_b == b_idx:
        #         return 1
        #     elif a_idx_b + 1 == len(B) or a_idx + 1 == len(A):
        #         a = max(1, self.maxUncrossedLines(A[1:], B))
        #         b = max(1 + self.maxUncrossedLines(A[b_idx_a + 1:], B[b_idx + 1:]),
        #                 self.maxUncrossedLines(A, B[1:]))
        #         return max(a, b)
        #     elif b_idx + 1 == len(B) or b_idx_a + 1 == len(A):
        #         b = max(1, self.maxUncrossedLines(A, B[1:]))
        #         a = max(1 + self.maxUncrossedLines(A[a_idx + 1:], B[a_idx_b + 1:]),
        #                 self.maxUncrossedLines(A[1:], B))
        #         return max(a, b)
        #


if __name__ == '__main__':
    A = [1, 4, 2]
    B = [1, 2, 4]
    A = [4, 2, 1, 4, 2, 2, 5, 1, 4, 4, 1, 2, 4, 2, 1, 4, 1, 4, 1, 5]
    B = [4, 3, 4, 4, 3, 3, 1, 1, 4, 2, 3, 2, 5, 1, 2]
    A = [3, 1, 4, 1, 1, 3, 5, 1, 2, 2]
    B = [4, 1, 5, 2, 1, 1, 1, 5, 3, 1, 1, 1, 2, 3, 1, 4, 3, 5, 5, 3, 1, 2, 3, 2, 4, 1, 1, 1, 5, 3]
    A = [3, 3, 2]
    B = [3, 3, 1, 2]
    A = [2, 5, 1, 2, 5]
    B = [10, 5, 2, 1, 5, 2]
    A = [5, 1, 2, 5, 1, 2, 2, 3, 1, 1, 1, 1, 1, 3, 1]
    B = [2, 5, 1, 3, 4, 5, 5, 2, 2, 4, 5, 2, 2, 3, 1, 4, 5, 3, 2, 4, 5, 2, 4, 4, 2, 2, 2, 1, 3, 1]
    A = [1, 2, 4, 1, 4, 4, 3, 5, 5, 1, 4, 4, 4, 1, 4, 3, 4, 2, 4, 2]
    B = [2, 4, 1, 1, 3, 5, 2, 1, 5, 1, 2, 3, 3, 2, 1, 4, 1, 2, 5, 5]
    # 7
    # +1
    # +1
    # +1
    # +1
    # +3
    # +1
    # A = [4, 2, 2, 5, 1, 4, 4, 1, 2, 4, 2, 1, 4, 1, 4, 1, 5]
    # B = [4, 4, 3, 3, 1, 1, 4, 2, 3, 2, 5, 1, 2]
    # # +1
    # A = [4, 2, 1, 4, 1, 4, 1, 5]
    # B = [3, 2, 5, 1, 2]
    # +1
    # +1
    # +1

    # A = [2, 1, 4, 2, 2, 5, 1, 4, 4, 1, 2, 4, 2, 1, 4, 1, 4, 1, 5]
    # B = [4, 4, 3, 3, 1, 1, 4, 2, 3, 2, 5, 1, 2]
    # A = [2, 2, 5, 1, 4, 4, 1, 2, 4, 2, 1, 4, 1, 4, 1, 5]
    # B = [4, 3, 3, 1, 1, 4, 2, 3, 2, 5, 1, 2]
    print(Solution().maxUncrossedLines(A, B))
