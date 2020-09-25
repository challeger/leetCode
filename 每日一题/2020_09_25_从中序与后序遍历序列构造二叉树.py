"""
day: 2020-09-25
url: https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
题目名: 从中序与后序遍历序列构造二叉树
根据一棵树的中序遍历与后序遍历构造二叉树

注意:
    你可以假设树中没有重复的元素
思路:
    中序遍历: [左子树遍历结果, 根节点, 右子树遍历结果]
    后序遍历: [左子树遍历结果, 右子树遍历结果, 根节点]
    对于后序遍历,尾部节点就是我们的根节点,所以每次遍历,以
    当前postorder的尾部节点作为根节点,找到在inorder中对应的索引idx
    以此去构造左子树与右子树,左子树就是 [left, idx-1]
    右子树就是[idx+1, right]
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            # 如果这里没有节点构造二叉树了，就结束
            if in_left > in_right:
                return None

            # 选择 post_idx 位置的元素作为当前子树根节点
            val = postorder.pop()
            root = TreeNode(val)

            # 根据 root 所在位置分成左右两棵子树
            index = idx_map[val]

            # 构造右子树
            root.right = helper(index + 1, in_right)
            # 构造左子树
            root.left = helper(in_left, index - 1)
            return root

        # 建立（元素，下标）键值对的哈希表
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)
