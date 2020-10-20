"""
day: 2020-10-20
url: https://leetcode-cn.com/problems/reorder-list/
题目名: 重排链表
给定一个单链表L:L0->L1->L2->..->Ln-1->Ln
将其重新排列后变为:L0->Ln->L1->Ln-1->...

思路:
1. 队列
    先遍历链表,把所有节点存储到一个队列中,然后用两个指针left和right
    分别指向队列头部与尾部,首先让left的节点指向right,然后让left指针后移
    一位,这里必须先判断left是否与right相等,防止出现环.
    如果不相等,则让right的节点再指向现在的left节点.

    在left < right为false之后,就退出循环,在退出循环后必须再将当前left指向的节点
    的next指向空
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next
        left = 0
        right = len(stack) - 1
        while left < right:
            stack[left].next = stack[right]
            left += 1
            if left == right:
                break
            stack[right].next = stack[left]
            right -= 1
        stack[left].next = None
