"""
day: 2020-10-23
url: https://leetcode-cn.com/problems/palindrome-linked-list/
题目名: 回文链表
请判断一个链表是否是回文链表

示例:

    输入: 1->2
    输出: False

    输入: 1->2->2->1
    输出: True
思路:
1.将链表的所有值存入列表中,然后双指针比较

2.找到链表的中点,然后把后半部分翻转,然后逐个对比
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 找到链表的中点
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 反转后半部分链表
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
