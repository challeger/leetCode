"""
day: 2020-08-14
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnd69e/
题目名: 二叉树的最大深度
题目描述: 给定一个二叉树,找出其最大深度,二叉树的深度为根节点到最远叶子节点的最长路径上的节点数
思路:
1. 深度优先
    递归判断左子树与右子树的最大深度,在遇到空节点时返回0
2. 广度优先
    每一次将每一层的节点添加到列表中,直到列表为空,说明遍历完成
    循环了n次深度就是n-1(因为在节点都为空的一层也会执行一次循环)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0
        if root:
            nodes = [root]
            depth = 0
            while nodes:
                new_nodes = []
                for node in nodes:
                    if node:
                        new_nodes.extend([node.left, node.right])
                nodes = new_nodes
                depth += 1
            return depth - 1
        return 0
