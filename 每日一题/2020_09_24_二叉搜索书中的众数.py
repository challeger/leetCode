"""
day: 2020-09-24
url: https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/
题目名: 二叉搜索树中的众数
给定一个有相同值的二叉搜索树(BST),找出 BST 中的所有众数(出现频率最高的元素)
思路:
    中序遍历BST,是一个递增的有序数组,那么问题就可以转换为在一个递增数组中求众数.
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ans = []
        most = 0
        last = None
        cnt = 0

        def inorder(node):
            if not node:
                return
            nonlocal ans, most, last, cnt
            # 中序遍历
            inorder(node.left)
            # 如果与上一个相等,那么现在的cnt+1
            if node.val == last:
                cnt += 1
            # 不相等就置为1
            else:
                cnt = 1
            # 如果与目前的众数的数量相等,那么就加入ans数组中
            if cnt == most:
                ans.append(node.val)
            # 如果比它大,那就重置ans数组
            elif cnt > most:
                most = cnt
                ans = [node.val]
            last = node.val
            inorder(node.right)

        inorder(root)
        return ans
