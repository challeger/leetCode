"""
day: 2020-10-10
url: https://leetcode-cn.com/problems/linked-list-cycle-ii/
题目名: 环形链表II
如果链表中有某个节点,可以通过连续跟踪 next 指针再次到达,则链表中存在环,返回入环的第一个节点
没有则返回null
思路:
    先用快慢指针判断是否有环
    如果有环,那么用一个从头结点出发的指针,与当前相遇的指针
    同时出发,再次相遇就是环的入口

    没有环就返回null

    我们假设起点到环入口的距离是a,相遇时slow指针在环内走了距离b,环剩下的长度为c
    那么fast指针,在与slow指针相遇时,走的总长度为 a + n(b+c) + b,n为fast指针走完的环的n圈

    因为fast指针的速度是slow的两倍,所以有
    2(a+b) = a + n(b+c) + b
    => a = (n-1)(b+c) + c
    那么slow在走了 (n-1)(b+c) + c步后,会回到环的入口, 因为环剩下的长度是c
    所以只需要让一个指针从head出发,与slow同步走,那么当他们走了a步后,会在环的入口
    相遇.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
