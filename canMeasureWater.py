# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   canMeasureWater.py
@Contact :   9824373@qq.com
@Desc    :

            有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？

            如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

            你允许：

            装满任意一个水壶
            清空任意一个水壶
            从一个水壶向另外一个水壶倒水，直到装满或者倒空
            示例 1: (From the famous "Die Hard" example)

            输入: x = 3, y = 5, z = 4
            输出: True
            示例 2:

            输入: x = 2, y = 6, z = 5
            输出: False

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/water-and-jug-problem
@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-21     zhan        1.0         None
'''

'''
一、数学方法：每次操作只能是使水的总量 +x -x +一-y
所以最后谁的总量是 z = ax + by （a，b）是整数且 z <= a+b
另外 贝祖定理 表明 z = ax + by 要有解，z必须是x，y的最大公约数的倍数。
二、深度优先dfs(用栈)，或者宽度优先bsf(用队列)
    在任意一个时刻，我们可以且仅可以采取以下几种操作：
    
    把 X 壶的水灌进 Y 壶，直至灌满或倒空；
    把 Y 壶的水灌进 X 壶，直至灌满或倒空；
    把 X 壶灌满；
    把 Y 壶灌满；
    把 X 壶倒空；
    把 Y 壶倒空。

'''
import math
from collections import deque
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # return self.canMeasureWater_math(x,y,z)
        # return self.canMeasureWater_bfs(x,y,z)
        return self.canMeasureWater_dfs(x,y,z)


    def canMeasureWater_math(self, x: int, y: int, z: int) -> bool:
        if x + y < z: return False
        if x==0 or y == 0: return z == 0 or z == x+y

        return z % math.gcd(x,y) == 0

    def neighbors(self,rx,ry,x,y):
        return [(0,ry),
                (x,ry),
                (rx,0),
                (rx,y),
                (rx - min(rx, y - ry), ry + min(rx, y - ry)),  #x往y中倒水
                (rx + min(ry, x - rx), ry - min(ry, x - rx)),  #y往x中倒水
                ]

    def canMeasureWater_bfs(self, x: int, y: int, z: int) -> bool:
        myque = deque()
        # deque 是双向队列,bfs保证先进先出
        myque.append((0,0))
        seen = {(0,0)}
        while myque:
            rx, ry = myque.popleft()
            if rx + ry == z or rx == z or ry == z: return True

            for nei in self.neighbors(rx, ry,x,y):
                if nei not in seen:
                    seen.add(nei)
                    myque.append(nei)
        return False

    def canMeasureWater_dfs(self, x: int, y: int, z: int) -> bool:
        # stack = [(0,0)]
        # seen = {(0,0)}
        # while stack:
        #     rx, ry = stack.pop()
        #     if rx + ry == z or rx == z or ry == z: return True
        #
        #     for nei in self.neighbors(rx, ry,x,y):
        #         if nei not in seen:
        #             seen.add(nei)
        #             stack.append(nei)
        # return False
        myque = deque()
        # deque 是双向队列,dfs保证先进后出
        myque.append((0,0))
        seen = {(0,0)}
        while myque:
            rx, ry = myque.pop() # 从右边弹出元素
            if rx + ry == z or rx == z or ry == z: return True

            for nei in self.neighbors(rx, ry,x,y):
                if nei not in seen:
                    seen.add(nei)
                    myque.append(nei)# 右边加入元素
        return False


if __name__ == '__main__':
    x = 2
    y = 6
    z = 5

    ans = Solution().canMeasureWater(x,y,z)
    print(ans)