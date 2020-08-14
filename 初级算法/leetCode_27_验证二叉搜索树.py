"""
day: 2020-08-14
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn08xg/
题目名: 验证二叉搜索树
题目描述: 给定一个二叉树,判断其是否是一个有效的二叉搜索树
二叉搜索树具有以下特征:
    节点的左子树只包含小于当前节点的数
    节点的右子树只包含大于当前节点的数
    所有左子树和右子树自身也必须是二叉搜索树
示例:
     2
    / \
   1   3
   输出: true
     5
    / \
   1   4
   输出: false
思路:
节点的左树的所有子节点的值都必须小于该节点的值,右树则必须大于,它的节点也必须是二叉搜索树
1. 设计一个递归函数
    helper(lower, upper, root),这个函数会判断节点的子树节点的值是否都在(lower, upper)范围内
    若不满足则返回false,否则继续递归检查,如果都满足说明是一棵二叉搜索树
    在检索左子树时,我们要将upper设置为root.val,因为左子树中的节点必须都小于节点
    同理,检索右子树时,需要将lower设置为root,val,因为右子树中的节点必须都大于节点
2. 中序遍历
    中序遍历是先输出左孩子,然后是该节点,最后是右孩子
    二叉搜索树中序遍历输出的是一个有序数组,所以我们在中序遍历时,定义一个变量记录上一个
    输出的值,然后将当前节点的值与上一个输出的值进行对比,若不小于,则输出false,遍历完成则输出
    true
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # float('-inf') -> 负无穷大 float('inf') -> 正无穷大
        # def helper(lower, upper, root):
        #     if not root:
        #         return True
        #     if not lower < root.val < upper:
        #         return False
        #     return helper(lower, root.val, root.left) and helper(root.val, upper, root.right)
        # return helper(float('-inf'), float('inf'), root)
        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True
