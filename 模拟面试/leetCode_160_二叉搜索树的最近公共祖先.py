"""
day: 2020-09-11
url: https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/
题目名: 二叉搜索树的最近公共祖先
给定一个二叉搜索树,找到该树中两个指定节点p,q的最近公共祖先

思路:

    二叉搜索树的性质: 左子节点 < 根节点 < 右子节点

如果p,q都大于根节点,说明最近公共祖先在右子节点的子树上,就向右搜索
如果都小于根节点,就向左搜索
否则,当前的根节点就是最近公共祖先.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 保证p的值一直小于q,可以减少判断次数
        if p.val > q.val:
            p, q = q, p
        while root:
            if root.val < p.val:
                root = root.right
            elif root.val > q.val:
                root = root.left
            else:
                break
        return root
