"""
day: 2020-08-28
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdh5o7/
题目名: 二叉树的最近公共祖先
给定一个二叉树,找到该树中两个指定节点的最近公共祖先.
最近公共祖先的定义为: '对于有根数T的两个节点p, q,最近公共祖先表示为一个节点x,满足x是p,q的祖先且x的深度尽可能
的大(一个节点也可以是它自己的祖先)'
示例:
    输入:
        3
       / \
      5   1
     / \ / \
    6  2 0  8
    p=5, q=1
    输出:
    3
思路:
对于p,q的最近公共祖先root,只会有以下几种情况:
    1. p和q在root的子树中,且分列在root的异侧
    2. p=root, 且q在root的子树中
    3. q=root, 且p在root的子树总
采用后序遍历,自底向上遍历,当当前节点为空,或者是p或q节点时,直接返回该节点.

递归左子节点left与右子节点right

1. 当left和right都为空时,说明root的子树中都不包含p,q,所以返回Null
2. 当left和right都不为空时,说明root的p,q分别在root的翼侧,那么返回root
3. 当left为空,right不为空时,说明right是p,q中的一个节点,或者是他们的最近公共祖先,所以返回right
4. 当left不为空,right为空时,同3.返回left.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        leftNode = self.lowestCommonAncestor(root.left, p, q)
        rightNode = self.lowestCommonAncestor(root.right, p, q)
        if not leftNode:
            return rightNode
        if not rightNode:
            return leftNode
        return root
