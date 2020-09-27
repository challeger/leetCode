"""
day: 2020-09-27
url: https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
题目名: 二叉搜索树的最近公共祖先
给定一个二叉搜索树,找到该数中两个指定节点的最近公共祖先
思路:
    对于指定节点p,q,以及当前节点node,会有三种情况
    1.p,q的值均大于node的值,那么p,q的最近祖先应该在node的右子树
    2.p,q的值均小于node的值,那么p,q的最近祖先应该在node的左子树
    3.否则,p,q分别在node的左子树与右子树,那么node就是p,q的最近祖先.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 三种情况
        # p,q都比当前节点小 -> 在左边
        # p,q都比当前节点大 -> 在右边
        # p,q分别在两边 -> 当前节点就是最近公共祖先
        def dfs(node):
            if not node:
                return None
            if node.val < p.val and node.val < q.val:
                return dfs(node.right)
            elif node.val > p.val and node.val > q.val:
                return dfs(node.left)
            else:
                return node

        return dfs(root)
