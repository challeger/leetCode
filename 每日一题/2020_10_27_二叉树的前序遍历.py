"""
day: 2020-10-27
url: https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
题目名: 二叉树的前序遍历
给定一个二叉树,返回它的前序遍历

思路:

1. 递归
    朴实无华.
2. 迭代
    用一个栈来记录节点,每次将栈顶元素推出栈,并将数字添加到res中,
    然后将右子树与左子树推入栈中,一直循环直到栈为空.
3. morris遍历
    让节点一直往右走,直到right指针为空,那么则让其指向当前节点.
    这样在左子树遍历完之后,它又会重新回到当前节点.具体参考这个博客
    https://blog.csdn.net/wdq347/article/details/8853371
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal_1(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []

        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res

    def preorderTraversal_2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    def preorderTraversal_3(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        p1 = root
        while p1:
            p2 = p1.left
            if p2:
                while p2.right and p2.right != p1:
                    p2 = p2.right
                if not p2.right:
                    res.append(p1.val)
                    p2.right = p1
                    p1 = p1.left
                    continue
                else:
                    p2.right = None  # 有右子节点,说明是遇到了p1,也就是全部遍历完了
            else:
                res.append(p1.val)
            p1 = p1.right

        return res
