"""
day: 2020-09-21
url: https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
题目名: 把二叉搜索树转换为累加树
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)
使得每个节点的值是原来的节点值加上所有大于它的节点值之和
思路:
    二叉搜索树右节点 > 根节点 > 左节点,先递归访问右节点,把最大的数的累加值求出来
    然后求根节点的累加值,最后求左节点的累计值.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    num = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            # 先求出右子树的累加和
            self.convertBST(root.right)
            # 根据右子树的累加和求出根节点的累加和
            root.val += self.num
            # 记录根节点的累加和
            self.num = root.val
            # 用根节点的累加和求左子树的各节点的累加和
            self.convertBST(root.left)
        return root
