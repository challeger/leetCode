"""
day: 2020-08-18
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvijdh/
题目名: 填充每个节点的下一个右侧子节点
题目描述: 给定一棵完美二叉树,其所有叶子节点都在同一层,每个父节点都有两个子节点
填充它的每个next指针,让这个指针指向其下一个右侧节点,如果找不到则设置为null

思路:
1. 层序遍历(BFS)
    一层一层遍历,在遍历每一层时,让出栈的节点指向下一个出栈的节点,若栈为空则指向None
2. 在一棵树中存在两种Next指针,一种是连接同一个父节点下的左右节点,我们要连接它们只需要
    node.left.next = node.right
    另一种是连接同一层节点中,该节点的右孩子与该节点的Next节点的左孩子
    也就是
    node.right.next = node.next.left
    也就是说,我们可以根据当前所在层的next节点,构造下一层的next节点,
    我们只需要不断的让节点往左移,然后通过该层的next节点,去构造下一层的Next节点即可.
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        # stack = [root]
        # while stack:
        #     level_list = []
        #     while stack:
        #         node = stack.pop(0)
        #         node.next = stack[0] if stack else None
        #         if node.left:
        #             level_list.append(node.left)
        #         if node.right:
        #             level_list.append(node.right)
        #     stack = level_list
        # return root

        leftmost = root
        while leftmost.left:
            # 当前层的第一个节点
            head = leftmost
            while head:
                # 让该节点的左孩子的next指向该节点的右孩子
                head.left.next = head.right
                # 若该节点存在next节点
                if head.next:
                    # 让该节点的右孩子的next节点指向该节点的next节点的左孩子
                    head.right.next = head.next.left
                # 在同一层中右移一个节点
                head = head.next
            # 移动到下一层
            leftmost = leftmost.left
        return root
