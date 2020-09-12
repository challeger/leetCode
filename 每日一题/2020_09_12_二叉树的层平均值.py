"""
day: 2020-09-12
url: https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/
题目名: 二叉树的层平均值
给定一个非空二叉树,返回一个由每层节点平均值组成的数组.

思路:
    层序遍历.
"""
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return [0]

        res = []
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            tmp = 0
            for _ in range(size):
                node = queue.popleft()
                tmp += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp / size)
        return res
