"""
day: 2020-10-18
url: https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
题目名: 删除链表的倒数第N个节点
给定一个链表,删除链表的倒数第 n 个节点,并且返回链表的头结点

思路:
1.
    遍历链表,把链表的每个节点都存储到一个列表中
    根据n删除对应的节点
2. 快慢指针
    让快指针先走n步,此时快指针与慢指针之间的距离就是n,然后
    让快慢指针同时走,那么当快指针走到尾节点时,慢指针正好指向
    倒数第n个节点.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        foo_head = ListNode(0, head)
        fast = head
        slow = foo_head
        for _ in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return foo_head.next

    def removeNthFromEnd_1(self, head: ListNode, n: int) -> ListNode:
        stack = []
        while head:
            stack.append(head)
            head = head.next
        if n == len(stack):
            return stack[0].next
        stack[-n-1].next = stack[-n].next
        return stack[0]
