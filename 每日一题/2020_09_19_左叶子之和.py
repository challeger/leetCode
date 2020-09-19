"""
day: 2020-09-19
url: https://leetcode-cn.com/problems/sum-of-left-leaves/
题目名: 左叶子之和
计算给定二叉树的所有左叶子之和

思路:
    dfs树, 判断当前节点是否是左叶子,是则将其值加入结果中,否则继续向下遍历
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        node_sum = 0

        def dfs(node, flag):
            nonlocal node_sum

            if not node.left and not node.right and flag:
                node_sum += node.val
                return
            if node.left:
                dfs(node.left, True)
            if node.right:
                dfs(node.right, False)

        dfs(root, False)
        return node_sum
