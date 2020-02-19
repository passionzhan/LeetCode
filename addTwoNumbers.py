'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def ListNodefromList(l:list)->ListNode:
    preNode = None
    for i in range(len(l)-1,-1,-1):
        curNode = ListNode(l[i])
        curNode.next = preNode
        preNode = curNode
    return curNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode)->ListNode:

        carry = 0
        rootNode = ListNode(0)
        preListNode = rootNode

        while (l1 or l2):
            if l1 == None: v1 = 0
            else: v1 = l1.val
            if l2 == None: v2 = 0
            else: v2 = l2.val

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur_Node = ListNode(val)
            preListNode.next = cur_Node
            preListNode = cur_Node

            if l1 is not None: l1  = l1.next
            if l2 is not None: l2  = l2.next

        if carry == 1:
            cur_Node = ListNode(1)
            preListNode.next = cur_Node


        return rootNode.next


if __name__ == '__main__':
    a = [1, 3, 5, 7, 8]
    b = [5, 4, 2, 1, 8,7,2]

    l1 = ListNodefromList(a)
    l2 = ListNodefromList(b)

    rst = Solution().addTwoNumbers(l1,l2)
    while rst:
        print(rst.val)
        rst = rst.next

