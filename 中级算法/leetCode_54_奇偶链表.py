"""
day: 2020-08-17
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvdwtj/
题目名: 奇偶链表
题目描述: 给定一个单链表,将所有的奇数节点和偶数节点分别排在一起,奇偶数是值节点索引的奇偶数
    需要保持奇偶节点的相对顺序
    第一个节点为奇数节点,第二个为偶数节点
示例:
    输入: 1->2->3->4->5->NULL
    输出: 1->3->5->2->4->NULL
思路:
    双指针odd, even分别指向链表的第一位与第二位,
    每次循环先将odd的下一个节点指向even的下一个节点
    然后将odd后移一位,
    再将even的下一个节点指向odd的下一个节点
    然后even后移一位,直到even为空或者even.next为空
    最后让odd.next指向even的头部
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
