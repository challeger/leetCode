"""
day: 2020-09-14
url: https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
题目名: 二叉树的中序遍历
给定一个二叉树,返回其中序遍历
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        tree = [root]
        while tree:
            # 利用栈后进先出的特性
            # 每次访问到一个节点,就将它以[右孩子,根节点的值,左孩子]添加到栈中
            # 这样就会先访问左孩子,然后访问根节点的值,最后访问右孩子.
            node = tree.pop()
            if isinstance(node, TreeNode):
                tree.extend([node.right, node.val, node.left])
            # 如果访问到的是值,那么就添加到结果中
            elif isinstance(node, int):
                res.append(node)
        return res

    def inorderTraversal_2(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res
