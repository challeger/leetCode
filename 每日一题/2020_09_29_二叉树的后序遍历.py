"""
day: 2020-09-29
url: https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
题目名: 二叉树的后序遍历
给定一个二叉树.返回它的后序遍历
思路:
1. 递归
    简单
2, 迭代
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        def dfs(node):
            if not node:
                return
            dfs(node.left)  # 先访问左节点
            dfs(node.right)  # 然后右节点
            res.append(node.val)  # 最后是根节点

        # 迭代
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if isinstance(node, TreeNode):
                # 将节点以 [根节点值, 右节点, 左节点]推入栈中
                # 因为是先进后出,所以访问顺序是左节点->右节点->根节点
                stack.extend([node.val, node.right, node.left])
            if isinstance(node, int):
                res.append(node)
        return res
