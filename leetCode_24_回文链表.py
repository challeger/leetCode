"""
day: 2020-08-13
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnv1oc/
题目名: 回文链表
题目描述: 判断一个链表是否为回文链表

示例:
    输入: 1->2
    输出: false
    输入: 1->2->2->1
    输出: true
思路:
1. 递归
    在对象中定义一个首节点开始的指针,然后在递归函数中递归到链表尾节点,将尾节点与首节点
    的值对比,若相等则外部指针右移一位,继续递归..
    若某次递归时两边的值不相等,则递归返回False,一路递归出去的结果都应该是False.
2. 找中心点,反转后半部分
    利用一个快慢指针,快指针遍历的速度是慢指针的两倍,所以快指针遍历完成时慢指针正好指向
    链表的中心点.然后将中心点之后的链表反转,接着从链表头部与链表中心点(反转后的链表的头部)
    进行对比,直到遍历完成或者不相等.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # vals = []
        # current_head = head
        # while current_head:
        #     vals.append(current_head.val)
        #     current_head = current_head.next
        # return vals == vals[::-1]

        # def reverse(node):
        #     prev = None
        #     # 遍历链表的指针
        #     while node:
        #         node.next, prev, node = prev, node, node.next
        #     return prev
        # fast, slow = head, head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next

        # reverse_head = reverse(slow)
        # order_head = head
        # while order_head and reverse_head:
        #     if order_head.val != reverse_head.val:
        #         return False
        #     order_head = order_head.next
        #     reverse_head = reverse_head.next
        # return True

        self.front_pointer = head

        def reverse_check(current_node=head):
            if current_node:
                if not reverse_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True
        return reverse_check()
