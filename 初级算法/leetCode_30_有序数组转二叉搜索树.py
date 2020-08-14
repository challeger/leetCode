"""
day: 2020-08-14
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xninbt/
题目名: 有序数组转二叉搜索树
题目描述: 给定一个升序数组,转换为一棵高度平衡二叉搜索树
本题中的高度平衡二叉树是指一个二叉树每个节点的左右两个子树的高度差的绝对值不超过1
示例:
    输入: [-10, -3, 0, 5, 9]
     0
    / \
   -3  9
  /   / 
-10  5  
思路:
    将数组二分,每次二分取中间位置的左边的数组作为根节点,根节点的下标为mid = (left + right) // 2
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        def helper(left, right):
            if left > right:
                return
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)
            return root
        return helper(0, len(nums)-1)
        # if nums:
        #     if len(nums) == 1:
        #         return TreeNode(nums[0])
        #     mid = len(nums) // 2
        #     root = TreeNode(mid)
        #     root.left = self.sortedArrayToBST(nums[:mid])
        #     root.right = self.sortedArrayToBST(nums[mid+1:])
        #     return root
