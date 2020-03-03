# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   reverseList.py
@Contact :   9824373@qq.com
@Desc    :
用递归和迭代两种方法实现将一个链表反转
@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-02     zhan        1.0         None
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
    '''
    基于递归
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None: return None
        if head.next == None:
            return head
        else:
            subList = self.reverseList(head.next)
            nextNode = subList

            while nextNode.next:
                nextNode = nextNode.next

            nextNode.next = head
            head.next = None
            return subList
    '''
    # 基于迭代
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None: return None
        if head.next == None:
            return head

        preNode, curNode = None, head
        while curNode.next:
            curNode.next, tmpNode = preNode, curNode.next
            preNode, curNode = curNode, tmpNode

        curNode.next = preNode
        return curNode

if __name__ == '__main__':
    a = [1, 3, 5, 7, 8]
    b = [5, 4, 2, 1, 8,7,2]

    l1 = ListNodefromList(a)
    l2 = ListNodefromList(b)

    rst = Solution().reverseList(l2)
    while rst:
        print(rst.val)
        rst = rst.next