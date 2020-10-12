"""
day: 2020-10-12
url: https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
题目名: 二叉搜索树的最小绝对差
给你一棵所有节点为非负值的二叉搜索树,请你计算树中任意两节点的差的绝对值的最小值
思路:
    中序遍历二叉树, 用一个prev来记录上一个节点的值, 然后求与当前节点的值的绝对差
    取最小的即可
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = float('inf')
        prev = float('inf')
        def helper(node):
            nonlocal res, prev
            if not node:
                return None
            helper(node.left)
            res = min(abs(prev-node.val), res)
            prev = node.val
            helper(node.right)
        helper(root)
        return res
