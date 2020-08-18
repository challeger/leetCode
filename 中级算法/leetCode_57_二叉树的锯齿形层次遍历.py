"""
day: 2020-08-18
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvle7s/
题目名: 二叉树的锯齿形层次遍历
题目描述: 给定一个二叉树,返回其锯齿形层次遍历(即先从左往右,再从右往左,以此类推)
示例:
     2
    / \
   9   10
  / \ / \
 1  3 15  7
   输出: [[3], [10, 9], [1, 3, 15, 7]]
思路:
1. 广度优先
    设置一个信号位判断是否需要反转,正常广度遍历树,按照信号位来将该层的数反转插入结果中
2. 深度优先
    设置一个变量level来记录当前节点所在的层数,根据level来决定是从尾部追加还是从头插入节点.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list:
        # stack = []
        # if root:
        #     queue = [root]
        #     is_left = True
        #     while queue:
        #         level_list = []
        #         size = len(queue)
        #         for _ in range(size):
        #             curr = queue.pop(0)
        #             if curr:
        #                 level_list.append(curr.val)
        #                 if curr.left:
        #                     queue.append(curr.left)
        #                 if curr.right:
        #                     queue.append(curr.right)
        #         # 判断是否需要将该层反转
        #         stack.append(level_list if is_left else level_list[::-1])
        #         is_left = not is_left
        if not root:
            return []
        stack = []

        def dfs(node, level):
            if level >= len(stack):
                stack.append([node.val])
            else:
                if level % 2:
                    stack[level].insert(0, node.val)
                else:
                    stack[level].append(node.val)
            for next_node in [node.left, node.right]:
                if next_node:
                    dfs(next_node, level+1)
        dfs(root, 0)
        return stack
