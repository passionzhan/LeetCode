# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   diameterOfBinaryTree.py
@Contact :   9824373@qq.com
@Desc    :
@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-10     zhan        1.0         None
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None: return 0
        ans = self.divideConquer(root)

        return ans[0]

    def divideConquer(self,root):
        if root.left == None and root.right == None: return 0,1

        if root.left:
            leftDiameter, leftDepth = self.divideConquer(root.left)
        else:
            leftDiameter, leftDepth = -1, 0
        if root.right:
            rightDiameter, rightDepth = self.divideConquer(root.right)
        else:
            rightDiameter, rightDepth = -1, 0

        diameter = max(leftDiameter,rightDiameter,leftDepth+rightDepth)

        return diameter, max(leftDepth,rightDepth) + 1



if __name__ == '__main__':
    [1, 2, 3, 4, 5]
    leftChild = TreeNode(2)
    leftChild.left = TreeNode(4)
    leftChild.right = TreeNode(5)
    root = TreeNode(1)
    root.left = leftChild
    root.right =  TreeNode(3)

    ans = Solution().diameterOfBinaryTree(root)
    print(ans)





