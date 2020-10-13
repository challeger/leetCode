"""
day: 2020-10-13
url: https://leetcode-cn.com/problems/swap-nodes-in-pairs/
题目名: 两两交换链表中的节点
给定一个链表,两两交换其中相邻的节点,并返回交换后的链表.
你不能只是单纯的改变节点内部的值,而是需要实际的进行节点交换
思路:
    用递归,首先拿出head原本指向的next节点,定义为newHead
    然后再让next指向newHead的next节点(这里需要递归调用)
    最后让newHead.next指向head
    结束条件:
        当前节点为空,或者当前节点的下一个节点为空,这样都不能进行交换所以直接返回
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = head.next  # 先拿到head.next节点
        head.next = self.swapPairs(newHead.next)  # 让head指向head.next.next,此处应该是已经交换好的链表
        newHead.next = head  # 让head原本的next节点指向head
        return newHead
