"""
day: 2020-10-29
url: https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/
题目名: 求根到叶子节点数字之和
给定一个二叉树,它的每个节点都存放一个0-9的数字,每条从根到叶子节点的路径都代表一个数字.
例如,从根到叶子节点路径 1->2->3代表数字123
计算从根到叶子节点生成的所有数字之和

示例:
    输入: 1
         /\
        2  3
    输出: 25

思路:
深度遍历:
    深度遍历,直到遍历到叶子节点,就将答案累加到结果中
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0

        def helper(path, node):
            nonlocal res
            if not node:
                return
            tmp = path * 10 + node.val
            if not node.left and not node.right:
                res += tmp
                return
            helper(tmp, node.left)
            helper(tmp, node.right)
        if root:
            helper(0, root)
        return res
