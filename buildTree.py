# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   buildTree.py
@Contact :   9824373@qq.com
@Desc    :
            根据一棵树的前序遍历与中序遍历构造二叉树。

            注意:
            你可以假设树中没有重复的元素。

            例如，给出

            前序遍历 preorder = [3,9,20,15,7]
            中序遍历 inorder = [9,3,15,20,7]
            返回如下的二叉树：

                3
               / \
              9  20
                /  \
               15   7

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-09     zhan        1.0         None
'''
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0: return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root

        rootIdx = inorder.index(preorder[0])
        if rootIdx > 0:
            root.left  = self.buildTree(preorder[1:rootIdx+1], inorder[0:rootIdx])
        if rootIdx <  len(preorder) - 1:
            root.right = self.buildTree(preorder[rootIdx+1:],inorder[rootIdx+1:],)

        return root


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    Solution().buildTree(preorder,inorder)