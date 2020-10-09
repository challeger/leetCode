"""
day: 2020-10-09
url: https://leetcode-cn.com/problems/linked-list-cycle/
题目名: 环形链表
如果链表中有某个节点,可以通过连续跟踪 next 指针再次到达,则链表中存在环
思路:
    快慢指针,一直循环直到 快指针为空
    或者 快指针与慢指针相遇
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
