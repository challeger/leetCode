"""
day: 2020-08-17
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xv02ut/
题目名: 相交链表
题目描述: 编写一个程序,找到两个单链表相交的起始节点
示例:
    输入: A: [5, 4, 3, 2, 1] B: [9, 2, 4, 3, 2, 1]
    输出: 4
思路:
    定义两个指针p_a,p_b,分别从headA与headB开始遍历,
    当p_a指向A链表的尾部时,将它定位到B链表的头部,类似的
    将p_b定位到A链表的头部,
    若两者相交,则在第二次遍历时必然在一个节点会相遇,否则两者都会指向
    None节点.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p_a = headA
        p_b = headB
        while p_a != p_b:
            p_a = p_a.next if p_a else headB
            p_b = p_b.next if p_b else headA
        return p_a
