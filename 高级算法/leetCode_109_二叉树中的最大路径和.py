"""
day: 2020-08-28
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdhfe5/
题目名: 二叉树中的最大路径和
给定一个非空二叉树,返回其最大路径和.
本题中,路径被定义为一条从树中任意节点出发,到达任意节点的序列.该路径至少包含一个节点,且不一定经过
根节点.
示例:
    输入:
        1
       / \
      2   3
    输出: 6
思路:
我们定义一个节点的最大贡献值,意为:
    以该节点为根节点的子树中,以该节点为起点的一条路径的最大路径和
    1. 当节点为空时,贡献值为0
    2. 非空节点的最大贡献值,应该是该节点的值与其子节点中的最大贡献值的和,对于叶节点来说,
    它的最大贡献值就是它自己的节点值..
我们定义一个函数递归的计算树中所有节点的左右子树的最大贡献值,那么以该节点为根节点的子树中,
包含该节点的最大路径和就是 left + node.val + right,所有节点的这个值的最大值,就是我们要求的结果.
每次递归,我们应该计算包含该节点的最大路径和,然后返回该节点的最大贡献值
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.maxSum = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0
            # 左子树的最大贡献
            leftGain = max(maxGain(node.left), 0)
            # 右子树的最大贡献
            rightGain = max(maxGain(node.right), 0)
            # 以当前节点为根节点的最大路径和
            priceNewPath = node.val + leftGain + rightGain
            self.maxSum = max(self.maxSum, priceNewPath)
            # 节点的最大贡献值
            return node.val + max(leftGain, rightGain)
        maxGain(root)
        return self.maxSum
