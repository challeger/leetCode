"""
day: 2020-08-13
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnnhm6/
题目名: 反转链表
题目描述: 反转一个单链表

示例:
    输入: 1->2->3->4->5->null
    输出: 5->4->3->2->1->null
思路:
1. 将链表存储在列表中,然后反向遍历,依次更改
2. 迭代
    定义一个指针从None开始,指向上一个经过的节点
    遍历链表,将每个节点的next指向上一个经过的节点
3. 递归
    若当前节点或当前节点的下一个节点为None,则返回当前节点
    否则让当前节点的下一个节点指向的下一个节点指向当前节点
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def reverseList(head: ListNode) -> ListNode:
        # foo = []
        # if not head:
        #     return None
        # while head:
        #     foo.append(head)
        #     head = head.next
        # for i in range(-1, -len(foo), -1):
        #     foo[i].next = foo[i-1]
        # else:
        #     foo[0].next = None
        # return foo[-1]

        # 指向反转后的链表的首部
        # prev = None
        # 遍历链表的指针
        # while head:
        #     head.next, prev, head = prev, head, head.next
        # return prev

        if not head or not head.next:
            return head
        node = Solution.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node
