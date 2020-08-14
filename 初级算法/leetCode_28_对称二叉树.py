"""
day: 2020-08-14
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn7ihv/
题目名: 对称二叉树
题目描述: 给定一个二叉树,检查它是否是镜像对称的
示例:
     2
    / \
   1   1
  / \ / \
 2  3 3  2
   输出: true
     2
    / \
   1   1
    \   \
     3   3
   输出: false
思路:
1.层次遍历
    将每一层的值存在一个列表中,若节点为空则值为-1,每次遍历完一层将列表与反转列表进行对比,
    若不相等则返回false,遍历完则返回true
2.同步指针
    使两个指针同步移动,left与right一开始都指向root,当left左移时,right右移
    left右移时,right左移,每次检查left与right的值是否相等,如果相等,再判断left与right的节点
    的值是否相等.可以用迭代和递归两种方式实现
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # if root:
        #     nodes = [root]
        #     while nodes:
        #         node_vals = []
        #         next_nodes = []
        #         for node in nodes:
        #             if node:
        #                 next_nodes.extend([node.left, node.right])
        #             node_vals.append(node.val if node else -1)
        #         if node_vals != node_vals[::-1]:
        #             return False
        #         nodes = next_nodes
        # return True

        # def check(left, right):
        #     if not left and not right:
        #         return True
        #     if not left or not right:
        #         return False
        #     return left.val == right.val and check(left.left, right.right) and check(left.right, right.left)
        # return check(root, root)

        if root:
            queue = [root.left, root.right]
            while queue:
                left = queue.pop()
                right = queue.pop()
                if not left and not right:
                    continue
                elif (not left or not right) or (left.val != right.val):
                    return False
                # 左节点的左孩子与右节点的右孩子
                queue.append(left.left)
                queue.append(right.right)
                # 左节点的右孩子与右节点的左孩子
                queue.append(left.right)
                queue.append(right.left)
            return True
        return True
