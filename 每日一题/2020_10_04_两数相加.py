"""
day: 2020-10-04
url: https://leetcode-cn.com/problems/add-two-numbers/
题目名: 两数相加
给出两个 非空 的链表用来表示两个非负的整数.
其中,它们各自的位数是按照 逆序 的方式存储的,并且它们的每个节点只能存储 一位 数字.
如果,我们将这两个数相加起来,则会返回一个新的链表来表示它们的和.

您可以假设除了数字 0 之外,这两个数都不会以 0 开头.
思路:
    同时遍历两个链表,定义一个进位carry来判断下一次相加是否需要进位即可
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode(0)  # 用来建立新链表的节点
        head = node  # 最终返回的结果
        carry = 0  # 进位

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            foo = x + y + carry
            carry = foo // 10
            node.next = ListNode(foo % 10)
            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            node.next = ListNode(carry)
        return head.next
