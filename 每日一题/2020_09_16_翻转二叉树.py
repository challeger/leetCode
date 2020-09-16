"""
day: 2020-09-16
url: https://leetcode-cn.com/problems/invert-binary-tree/
题目名: 翻转二叉树
翻转一棵二叉树

思路:
递归翻转
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        right = self.invertTree(root.left)
        left = self.invertTree(root.right)
        root.left, root.right = left, right
        return root
