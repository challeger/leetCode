"""
day: 2020-08-14
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnldjj/
题目名: 二叉树的中序遍历
题目描述: 给定一个二叉树,返回按照中层序遍历得到的节点值
示例:
     2
    / \
   9   10
  / \ / \
 1  3 15  7
   输出: [1, 9, 3, 2, 15, 10, 7]
思路:
利用栈后进先出,将节点一直往左孩子移,直到为空,然后弹出栈,将值添加到结果中
然后再指向节点的右孩子,若右孩子有左孩子,继续移动直到空,以此循环.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 迭代写法
        # res = []
        # stack = []
        # if root:
        #     while stack or root:
        #         while root:
        #             stack.append(root)
        #             root = root.left
        #         root = stack.pop()
        #         res.append(root.val)
        #         root = root.right
        # return res

        # 递归写法
        res = []

        def helper(node):
            if node:
                if node.left:
                    helper(node.left)
                res.append(node.val)
                if node.right:
                    helper(node.right)
        helper(root)
        return res
