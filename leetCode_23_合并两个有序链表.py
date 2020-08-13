"""
day: 2020-08-13
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnnbp2/
题目名: 合并两个有序链表
题目描述: 将两个升序链表合并为一个新的升序链表并返回.

示例:
    输入: 1->2->4, 1->3->4
    输出: 1->1->2->3->4->4
思路:
1.迭代
    每次循环比较链表1与链表2当前的值,将较小的节点添加到新链表中,直到
    有一个链表遍历完成,然后将另一个链表未遍历完的节点添加到新链表后
2.递归
    若l1或l2一开始就是空链表,则不需要合并,返回非空链表即可,否则判断
    哪个链表的头结点值更小,然后递归地决定下一个节点,如果有一个链表节点为空,
    递归结束
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        result = head

        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 if l1 else l2
        return result.next

        # if not l1:
        #     return l2
        # elif not l2:
        #     return l1
        # elif l1.val < l2.val:
        #     l1.next = Solution.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = Solution.mergeTwoLists(l2.next, l1)
        #     return l2


if __name__ == "__main__":
    head_1 = ListNode(1)
    head_2 = ListNode(1)

    foo = ListNode(2)
    head_1.next = foo
    foo = ListNode(4)
    head_1.next.next = foo

    foo = ListNode(3)
    head_2.next = foo
    foo = ListNode(4)
    head_2.next.next = foo
    h1 = Solution.mergeTwoLists(head_1, head_2)
    while h1:
        print(h1.val)
        h1 = h1.next
