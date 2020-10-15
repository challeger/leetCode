"""
day: 2020-10-15
url: https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
题目名: 填充每个节点的下一个右侧节点指针
给定一个完美二叉树,其所有叶子节点都在同一层,每个父节点都有两个子节点.二叉树定义如下
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个next指针,让这个指针指向其下一个右侧节点.如果找不到下一个右侧节点,
则将next指针设置为NULL.

注意:
    只能使用O(1)的额外空间
    递归占用的栈空间不算额外的空间复杂度
思路:
1. 迭代:
    用当前的节点去连接下一层节点,让当前节点的left指向当前节点的right
    然后让当前节点的right指向当前节点的next的left,以此类推..
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        node = root

        while node.left:  # 有子节点才继续遍历,因为是完美二叉树,有左节点那么下一层必然都是节点
            next_node = node.left
            while node.next:  # 判断当前节点右侧是否还有节点
                node.left.next = node.right
                node.right.next = node.next.left
                node = node.next
            node.left.next = node.right  # 虽然右侧没有节点,但是左子节点还得指向右子节点
            node = next_node  # 遍历下一层
        return root

    def connect_2(self, root: 'Node') -> 'Node':
        if not root or not root.left:
            return root
        root.left.next = root.right
        if root.next:
            root.right = root.next.left
        self.connect_2(root.left)
        self.connect_2(root.right)
