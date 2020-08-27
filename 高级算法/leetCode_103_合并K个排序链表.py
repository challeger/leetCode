"""
day: 2020-08-27
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xwylvd/
题目名: 合并K个排序链表
给你一个链表数组,每个链表都已经按升序排列.请你将所有链表合并到一个升序链表中,返回合并后
的链表
示例:
    输入: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    输出: [1, 1, 2, 3, 4, 4, 5, 6]
    输入: list = [[]]
    输出: []
思路:
1. 分治法
    首先,K个链表合并,可以分解为多次两个链表合并,我们用分治的思想,
    8->4->2->1,然后进行两个链表合并操作,递归执行,最终得到答案
2. 优先队列
    我们维护一个最小堆,里面存储着lists中的每个链表的头结点的值与它的索引.
    每次我们弹出最小堆的堆顶将其加入结果的链表中,然后在将堆顶对应的链表的当前结点
    加入堆中
"""
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # def mergeTwoKLists(a: ListNode, b: ListNode) -> ListNode:
        #     if not a or not b:
        #         return a if a else b
        #     head = ListNode()
        #     current = head
        #     a_ptr = a
        #     b_ptr = b
        #     while a_ptr and b_ptr:
        #         if a_ptr.val < b_ptr.val:
        #             current.next = a_ptr
        #             a_ptr = a_ptr.next
        #         else:
        #             current.next = b_ptr
        #             b_ptr = b_ptr.next
        #         current = current.next
        #     current.next = a_ptr if a_ptr else b_ptr
        #     return head.next

        # def merge(left, right):
        #     if left == right:
        #         return lists[left]
        #     if left > right:
        #         return None
        #     mid = (left + right) >> 1
        #     return mergeTwoKLists(merge(left, mid), merge(mid+1, right))

        # return merge(0, len(lists)-1)

        import heapq
        head = ListNode()
        current = head
        lists_head = []
        for i in range(len(lists)):
            if lists[i]:
                # 建立一个最小堆
                heapq.heappush(lists_head, (lists[i].val, i))
                lists[i] = lists[i].next

        while lists_head:
            # 每次弹出堆顶
            val, idx = heapq.heappop(lists_head)
            current.next = ListNode(val)
            current = current.next
            if lists[idx]:
                # 将弹出堆顶的链表的下一个节点加入堆中
                heapq.heappush(lists_head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return head.next
