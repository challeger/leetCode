"""
day: 2020-08-27
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xwbna3/
题目名: 复制带随机指针的链表
给定一个链表,每个节点包含一个额外增加的随机指针,该指针可以指向链表中的任何节点或空节点
要求返回这个链表的深拷贝
我们用一个由n个节点组成的链表来表示输入/输出中的链表.每个节点用一个[val, random_index]表示
    val: 一个表示node.val的整数
    random_index: 随机指针指向的节点索引
示例:
    输入: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    输出: [[7,null],[13,0],[11,4],[10,2],[1,0]]
思路:
1. 递归回溯
    当我们遍历到某个节点时,如果我们已经有这个节点的拷贝,那么就返回它的拷贝,否则
    创造一个新节点,并加入到已访问的字典中..
    然后我们继续拷贝node的next与random节点
2. O(1)额外空间复制
    我们将拷贝的新节点放在原节点的右侧,那么新节点的random,应该指向原节点的random节点
    的右侧节点..我们第一次遍历,创建新的节点,第二次遍历,将random指向正确的节点,第三次遍历
    将原链表与新链表分开,最终返回新链表的head
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visitedHash = {}

    def copyNode(self, node):
        if node:
            if node in self.visitedHash:
                return self.visitedHash[node]
            else:
                self.visitedHash[node] = Node(node.val, None, None)
                return self.visitedHash[node]
        return None

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        # if head in self.visitedHash:
        #     return self.visitedHash[head]

        # 哈希递归
        # node = Node(head.val, None, None)
        # self.visitedHash[head] = node
        # node.next = self.copyRandomList(head.next)
        # node.random = self.copyRandomList(head.random)
        # return node

        # 哈希迭代
        # old_node = head
        # new_node = Node(old_node.val, None, None)
        # self.visitedHash[old_node] = new_node
        # while old_node:
        #     new_node.random = self.copyNode(old_node.random)
        #     new_node.next = self.copyNode(old_node.next)
        #     old_node = old_node.next
        #     new_node = new_node.next
        # return self.visitedHash[head]

        ptr = head
        # 将每个节点的复制节点放在节点的右侧
        while ptr:
            new_node = Node(ptr.val, None, None)
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next
        # 将每个节点的random复制给它的复制节点
        ptr = head
        while ptr:
            # 复制节点的random,应该指向原节点的random的右侧节点
            # 也就是它的复制节点
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next
        # 遍历原来的链表
        ptr_old_node = head
        # 遍历复制的链表
        ptr_new_node = head.next
        head_new = head.next
        # 将原来的链表与复制的链表分开
        while ptr_old_node:
            ptr_old_node.next = ptr_old_node.next.next
            ptr_new_node.next = ptr_new_node.next.next if ptr_new_node.next else None
            ptr_old_node = ptr_old_node.next
            ptr_new_node = ptr_new_node.next
        return head_new
