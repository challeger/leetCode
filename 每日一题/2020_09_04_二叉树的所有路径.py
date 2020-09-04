"""
day: 2020-09-04
url: https://leetcode-cn.com/problems/binary-tree-paths/
题目名: 二叉树的所有路径
给定一个二叉树,返回所有从根节点到叶子节点的路径.

思路:
    深度优先遍历.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []

        def dfs(node: TreeNode, string):
            if not node.left and not node.right:
                res.append(string)
                return
            if node.left:
                dfs(node.left, string + f'->{node.left.val}')
            if node.right:
                dfs(node.right, string + f'->{node.right.val}')
        if root:
            dfs(root, f'{root.val}')
        return res
