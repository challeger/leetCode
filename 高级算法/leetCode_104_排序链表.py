"""
day: 2020-08-27
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xwcdnh/
题目名: 排序链表
在O(nlogn)时间复杂度和常数级空间复杂度下,对链表进行排序
示例:
    输入: -1->5->3->4->0
    输出: -1->0->3->4->5
思路:
1. 归并排序(递归)
    快慢指针找中点,然后从中间切断链表,分别对两边链表进行排序,最后再合并.
    但因为链表会使用log(n)的堆栈空间,所以不符合题目要求
2. 归并排序(迭代)
    自底向上来进行归并排序..
    第一次迭代将节点 1对1排序组合
    第二次迭代将节点 2对2排序组合
    第三次迭代将节点 4对4排序组合
    ....
    第n次迭代将节点  2^(n-1)排序组合
    直到要排序的半边节点的长度已经大于或等于链表的长度了,这时说明排序完成了.

    定义一个变量intv来表示当前循环单次合并的节点数,,然后根据这个intv,遍历链表
    每次先找到intv个左链表,然后找到intv个右链表,将它们合并排序后,将剩余待排序的链表
    接到排好序的链表的后面,然后继续遍历链表..直到全部排好序,将intv*2,继续下一次循环.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # if not head or not head.next:
        #     return head
        # slow, fast = head, head.next
        # # 快慢指针找中点
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # # 从中点切断链表
        # mid, slow.next = slow.next, None
        # left, right = self.sortList(head), self.sortList(mid)
        # h = res = ListNode(0)
        # while left and right:
        #     if left.val < right.val:
        #         h.next, left = left, left.next
        #     else:
        #         h.next, right = right, right.next
        #     h = h.next
        # h.next = left if left else right
        # return res.next
        h, length, intv = head, 0, 1
        while h:
            h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        # intv表示左边链表与右边链表的长度,第一次是1,1合并,第二次是2,2合并..以此类推
        # 直到intv>=length,这时已经不存在右边链表来合并了,所以已经排序完成
        while intv < length:
            # 从头开始遍历链表
            pre, h = res, res.next
            while h:
                # 找到长度为intv的左边链表
                left_node, i = h, intv
                while i and h:
                    h, i = h.next, i - 1
                # 如果左边走完了,i还大于0,说明左边的元素不超过intv,那么就不存在右边链表了,直接退出
                if i:
                    break
                # 找到长度在intv内的右边链表
                right_node, i = h, intv
                while i and h:
                    h, i = h.next, i - 1
                # 左边链表的长度与右边链表的长度,右边链表的长度可以小于Intv
                left_len, right_len = intv, intv - i
                # 将左边链表与右边链表排序合并
                while left_len and right_len:
                    if left_node.val < right_node.val:
                        pre.next, left_node = left_node, left_node.next
                        left_len -= 1
                    else:
                        pre.next, right_node = right_node, right_node.next
                        right_len -= 1
                    pre = pre.next
                pre.next = left_node if left_len else right_node
                # 让pre指向排好序的链表的尾节点
                while left_len > 0 or right_len > 0:
                    pre = pre.next
                    left_len -= 1
                    right_len -= 1
                # 将剩余待排序的链表接在排好序的尾节点后面
                pre.next = h
            # 向上一层
            intv *= 2
        return res.next


if __name__ == "__main__":
    t1 = ListNode(4)
    t1.next = ListNode(2)
    t1.next.next = ListNode(1)
    t1.next.next.next = ListNode(3)
    s = Solution()
    print(s.sortList(t1).val)
