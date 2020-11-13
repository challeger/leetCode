"""
day: 2020-11-13
url: https://leetcode-cn.com/problems/odd-even-linked-list/
题目名: 奇偶链表
给定一个单链表,把所有的奇数节点和偶数节点分别排在一起.
请注意,这里的奇数节点和偶数节点指的是节点编号的奇偶性,而不是节点的值的奇偶性

思路:
双指针,一个指向奇数位,一个指向偶数位

每次先让奇数位的节点的next指向偶数位的next
然后把奇数节点后移
再让偶数位的next指向奇数位的next
再把偶数位后移

当偶数位或者偶数位的next为空,说明已经全部接好了,就让偶数位的头部接到奇数位的尾部的next上
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd = head
        even = head.next
        evenHead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
