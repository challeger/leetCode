"""
day: 2020-09-02
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdu2v2/
题目名: LRU缓存机制
运用你掌握的数据结构,设计和实现一个LRU(最近最少使用)缓存机制.他应该支持以下操作:获取数据get和写入数据put
获取数据get(key): 如果关键字(key)存在于缓存中,则获取关键字的值(总为正数),否则返回-1
写入数据put(key, value): 如果关键字已经存在,则变更其数据值,如果关键字不存在,则chauffeur该组.当缓存容量达到上限时,
它应该在写入新数据之前删除最久未使用的数据值,从而为新的数据值留出空间..
示例:
    LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // 返回  1
    cache.put(3, 3);    // 该操作会使得关键字 2 作废
    cache.get(2);       // 返回 -1 (未找到)
    cache.put(4, 4);    // 该操作会使得关键字 1 作废
    cache.get(1);       // 返回 -1 (未找到)
    cache.get(3);       // 返回  3
    cache.get(4);       // 返回  4
思路:
"""


class DLinkNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        # 定义伪头结点与伪尾节点,这样在整个链表中,首部与尾部节点不会变化.
        # 对于我们的缓存,头结点的下一个节点表示最近使用的节点
        # 尾节点的前一个节点表示最久未使用的节点
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.max_len = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 获取节点
        node = self.cache.get(key)
        # 如果该节点在首部之后,在使用它之后,需要将它放到首部,表示他是最近使用的一个元素
        if node != self.head.next:
            # 从链表中删除节点
            self.delete_node(node)
            # 并插入到链表首部
            self.insert_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # 判断是否已经在缓存中了
        if key in self.cache:
            # 在的话就直接修改值
            node = self.cache[key]
            node.value = value
            # 然后判断该节点是否在首部之后,不在则将其放到首部,表示是最近使用的元素
            if node != self.head.next:
                self.delete_node(node)
                self.insert_to_head(node)
        else:
            # 否则创建一个新节点
            node = DLinkNode(key, value)
            # 判断缓存是否已经满了
            if self.max_len == len(self.cache):
                # 满了的话需要将链表尾节点的前一个节点(最久未使用节点)删除
                self.cache.pop(self.tail.prev.key)
                self.delete_node(self.tail.prev)
            # 将节点放入缓存中
            self.cache[key] = node
            # 并将节点记录为最近使用节点
            self.insert_to_head(node)

    def insert_to_head(self, node: DLinkNode):
        # 将节点插入到链表的首部之后
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def delete_node(self, node):
        # 将节点从链表中删除
        node.prev.next = node.next
        node.next.prev = node.prev


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(2, 1)
    lru.put(2, 2)
    print(lru.get(2))
    print(lru.get(1))
