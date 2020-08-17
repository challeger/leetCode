"""
day: 2020-08-17
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvw73v/
题目名: 两数相加
题目描述: 给出两个非空的链表用来表示两个非负的整数.其中,它们各自的位数是按照逆序的方式存储的,
并且它们的每个节点只能存储一位数字.
如果我们将这两个数相加起来,则会返回一个新的链表来表示它们的和.
除了数字0以外,这两个数都不会以0开头
示例:
    输入: (2->4->3)+(5->6->4)
    输出: 7->0->8
思路:
    在长度较短的链表前位补0,添加一个进位carry来表示是否需要+1,依次相加
    在循环结束后需要根据carry判断是否需要额外添加一个1
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        head = res
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            foo = carry + x + y
            # 判断是否需要进位
            carry = foo // 10
            # 得到的余数就是该位的结果
            res.next = ListNode(foo % 10)
            res = res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            res.next = ListNode(carry)
        return head.next
