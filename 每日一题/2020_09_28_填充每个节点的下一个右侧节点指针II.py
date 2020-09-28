"""
day: 2020-09-28
url: https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/
题目名: 填充每个节点的下一个右侧节点指针II
给定一个二叉树,填充它的每个next指针,让这个指针指向其下一个右侧节点.如果找不到下一个右侧节点,则将
next指针设置为NULL

    只能使用常量级额外空间
    使用递归解题也可
思路:
    用当前层已建立的关系,去遍历下一层的所有节点,并将它们连接起来
    首先root节点所在的第一层是已经建立好连接关系了的.
    我们给下一层定义一个虚拟的head节点,然后使用next来遍历当前的层的每一个节点curr,
    使用curr.left与curr.right来遍历下一层节点,并将其连接到head上,然后遍历完整棵树,
    关系也就建立完成了
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        left_first = root  # 当前层的最左边的节点
        while left_first:
            head = tail = Node(0)  # head代表下一层的节点的虚拟头部
            curr = left_first
            while curr:  # tail表示现在待连接的节点
                if curr.left:  # 用当前层的节点去遍历下一层的节点
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next
            left_first = head.next
        return root
