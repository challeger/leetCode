"""
day: 2020-08-18
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvuyv3/
题目名: 二叉搜索树中第k小的元素
题目描述: 给定一棵二叉搜索树,查找其中第k个最小的元素

思路:
1. 中序遍历
    查找第k个元素就移动k次,当k=0时,就返回当前节点的值
2. 记忆BST树
    在节点中新增两个变量,leftnodes与rightnodes,分别记录
    当前节点的左子树节点数与右子树节点数,当前节点在二叉搜索树
    中就是第leftnodes+1小的元素,当k小于leftnodes+1时,说明
    要找的节点在当前节点的左子树中,否则在右子树中,一直这样移动直到
    k == leftnodes+1
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
