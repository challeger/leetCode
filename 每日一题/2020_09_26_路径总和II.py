"""
day: 2020-09-26
url: https://leetcode-cn.com/problems/path-sum-ii/
题目名: 路径总和II
给定一个二叉树和一个目标和,找到所有从根节点到叶子节点路径总和等于给定目标和的路径
思路:
    依次深度遍历即可.
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        
        def dfs(track, node, remain):
            if not node:
                return
            # 如果是叶子节点并且值正好相等,就将列表加入结果中,并结束本次dfs
            if not node.left and not node.right and node.val == remain:
                track.append(node.val)
                res.append(track)
                return
            # 否则依次遍历左子树与右子树
            track.append(node.val)
            dfs(track[:], node.left, remain - node.val)
            dfs(track[:], node.right, remain - node.val)
        
        dfs([], root, sum)
        return res
