# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   MyStack.py
@Contact :   9824373@qq.com
@Desc    :
            使用队列实现栈的下列操作：

            push(x) -- 元素 x 入栈
            pop() -- 移除栈顶元素
            top() -- 获取栈顶元素
            empty() -- 返回栈是否为空
            注意:

            你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
            你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
            你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/implement-stack-using-queues

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-01     zhan        1.0         None
'''

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.data) > 0:
            return self.data.pop()
        else:
            return None

    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.data) > 0:
            return self.data[len(self.data)-1]
        else:
            return None

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.data) > 0:
            return False
        else:
            return True

if __name__ == '__main__':

    # Your MyStack object will be instantiated and called as such:
    x = 23
    y = 33

    obj = MyStack()
    obj.push(x)
    obj.push(y)

    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()

    print(param_2)
    print(param_3)
    print(param_4)