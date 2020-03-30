# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   middleNode.py
@Contact :   9824373@qq.com
@Desc    :
            给定一个带有头结点 head 的非空单链表，返回链表的中间结点。

            如果有两个中间结点，则返回第二个中间结点。

             

            示例 1：

            输入：[1,2,3,4,5]
            输出：此列表中的结点 3 (序列化形式：[3,4,5])
            返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
            注意，我们返回了一个 ListNode 类型的对象 ans，这样：
            ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
            示例 2：

            输入：[1,2,3,4,5,6]
            输出：此列表中的结点 4 (序列化形式：[4,5,6])
            由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
             

            提示：

            给定链表的结点数介于 1 和 100 之间。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/middle-of-the-linked-list

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-23     zhan        1.0         None
'''
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        nodelst = []

        while head:
            nodelst.append(head)
            head = head.next

        return nodelst[len(nodelst)//2]

if __name__ == '__main__':
    print('test')