"""
day: 2020-09-06
url: https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/
题目名: 二叉树的层序遍历II
给定一个二叉树,返回其节点值自底向上的层次遍历.
即按从叶子节点所在层到根节点所在的层,逐层从左向右遍历
思路:
正序遍历,反向输出.
"""
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            tmp = []
            for _ in range(size):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)

        return res[::-1]
