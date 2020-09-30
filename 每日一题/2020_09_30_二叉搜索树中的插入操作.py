"""
day: 2020-09-30
url: https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/
题目名: 二叉搜索树中的插入操作
给定一个BST的根节点和要插入树中的值,将值插入二叉搜索树.返回插入后的二叉搜索树的根节点
输入的数据保证和原始二叉搜索树中的任意节点值都不同
思路:
1. 递归
    一直递归到最深处,找到自己的位置,创建一个节点即可
    因为二叉搜索树的性质,且要插入的值与树中的节点都不相同,所以必然有一个空位是可以放
    要插入的值的
2, 迭代
    用一个节点来记录要插入的节点的父节点,然后一个节点p来遍历整棵树
    如果p.val < val,说明要插入的位置在p的右边
    否则说明要插入的位置在p的左边,这样一直遍历到p为空,那么p就是要插入的位置
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:  # 结束条件,表示找到了自己的位置
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

    def insertIntoBST_2(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        parent = p = root  # parent用来记录要插入的节点的父节点
        while p:
            parent = p
            p = p.right if p.val < val else p.left  # 找到要插入的节点的位置,为空表示此处就是要插入的节点
        if parent.val < val:  # 判断是插入左边还是右边
            parent.right = TreeNode(val)
        else:
            parent.left = TreeNode(val)
        return root
