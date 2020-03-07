# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   MaxQueue.py
@Contact :   9824373@qq.com
@Desc    :
            请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

            若队列为空，pop_front 和 max_value 需要返回 -1

            示例 1：

            输入:
            ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
            [[],[1],[2],[],[],[]]
            输出: [null,null,null,2,1,2]
            示例 2：

            输入:
            ["MaxQueue","pop_front","max_value"]
            [[],[],[]]
            输出: [null,-1,-1]
             

            限制：

            1 <= push_back,pop_front,max_value的总操作数 <= 10000
            1 <= value <= 10^5

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-07     zhan        1.0         None
'''


class MaxQueue:

    def __init__(self):
        self.__max_value = -1
        self.data = []


    def max_value(self) -> int:
        return self.__max_value


    def push_back(self, value: int) -> None:
        self.data.append(value)
        self.__max_value = max(value,self.__max_value)

    def pop_front(self) -> int:
        if len(self.data) == 0:
            return -1
        else:
            popVal = self.data.pop(0)
            if self.__max_value == popVal:
                self.__max_value = -1
                for val in self.data:
                    self.__max_value = max(self.__max_value,val)

            return popVal

if __name__ == '__main__':

# Your MaxQueue object will be instantiated and called as such:
    obj = MaxQueue()
    param_1 = obj.max_value()
    obj.push_back(23)
    param_3 = obj.pop_front()