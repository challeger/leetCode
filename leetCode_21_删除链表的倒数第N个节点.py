"""
day: 2020-08-13
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnarn7/
题目名: 删除链表中的倒数第N个节点
题目描述: 给定一个链表,删除链表的第n个节点, 并且返回链表的头结点

示例:
    输入: head = [4, 5, 1, 9], node = 5
    输出: [4, 1, 9]

    输入: head = [4, 5, 1, 9], node = 1
    输出: [4, 5, 9]

思路:
1. 遍历链表,将每个节点存储在列表foo中,foo[-n]表示要删除的节点,然后进行对应的操作
2. 使用双指针,快指针先走n步,然后慢指针与快指针一起走,当快指针走到尾部时,慢指针也指向
了要删除的节点.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # foo = []

        # while head:
        #     foo.append(head)
        #     head = head.next
        # if n == len(foo):
        #     return foo[0].next
        # foo[-n-1].next = foo[-n-1].next.next
        # return foo[0]

        node = ListNode(None)
        node.next = head
        fast, slow = node, node
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return node.next


if __name__ == "__main__":
    head = ListNode(1)
    mid = ListNode(2)
    head.next = mid
    Solution.removeNthFromEnd(head, 2)
