"""
day: 2020-08-13
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnwzei/
题目名: 环形链表
题目描述: 判断链表中是否有环,使用整数pos来表示链尾连接到链表中的位置,如果pos是-1,则在链表中
没有环
思路:
1. 快慢指针:
    一个快指针一个慢指针,如果是闭环必然会有一次循环会遇到,否则就结束
2. 集合:
    判断节点是否在一个集合中,在则说明重复访问了同一个节点,否则将节点添加到集合中
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # fast, slow = head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        #     if fast == slow:
        #         return True
        # return False

        nodes = set()
        currlent = head
        while currlent:
            if currlent in nodes:
                return True
            nodes.add(currlent)
            currlent = currlent.next
        return False


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    sl = Solution()
    sl.hasCycle(node1)
