"""
day: 2020-09-23
url: https://leetcode-cn.com/problems/merge-two-binary-trees/
题目名: 合并二叉树
给定两个二叉树,想象当你将它们中的一个覆盖到另一个上时,两个二叉树的一些节点便会重叠.
你需要将他们合并为一个新的二叉树.
合并的规则是如果两个节点重叠,那么将他们的值相加作为节点合并后的新值,否则不为 NULL 的节点将直接作为新二叉树的节点.
思路:
    自顶向下遍历两棵树,如果两棵树的节点都不为空
    那么就将t2的值加到t1的节点上,否则返回两个节点中
    不为空的节点,如果都为空,那么就返回空
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            # 合并两个节点
            t1.val += t2.val
            # 将节点的左子树合并
            t1.left = self.mergeTrees(t1.left, t2.left)
            # 将节点的右子树合并
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
        # 会返回两个节点中不为空的那个节点,如果都为空,那返回的就是None
        return t1 or t2
