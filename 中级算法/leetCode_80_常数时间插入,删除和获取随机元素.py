"""
day: 2020-08-22
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xw5rt1/
题目名: 常数时间插入,删除和获取随机元素
题目描述: 设计一个支持在平均时间复杂度O(1)下,执行以下操作的数据结构
    1.insert(val):当元素val不存在时,向集合中插入此项
    2.remove(val):当元素val存在时,从集合中删除此项
    3.getRandom:随机返回现有集合中的一项,每个元素应该有相同的概率被返回
示例:
// 初始化一个空的集合。
RandomizedSet randomSet = new RandomizedSet();

// 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomSet.insert(1);

// 返回 false ，表示集合中不存在 2 。
randomSet.remove(2);

// 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomSet.insert(2);

// getRandom 应随机返回 1 或 2 。
randomSet.getRandom();

// 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomSet.remove(1);

// 2 已在集合中，所以返回 false 。
randomSet.insert(2);

// 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
randomSet.getRandom();
思路:
    insert直接利用列表的append
    remove每次将要删除的元素与尾部元素对调,然后删除尾部元素
    random利用random模块中的choice即可

    所以需要一个list来记录数据,以及一个dict来记录数值对应的索引.
    在insert时,self.dict[value] = len(self.list)
    self.list.append(value)
    在remove时,取出要删除的值的索引,以及最后一个数的值
    然后将最后一个数的值放到要删除的值上,并设置dict中的索引
    然后pop(), del self.dict[value]
"""


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self._hashmap = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self._hashmap:
            self._hashmap[val] = len(self.data)
            self.data.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self._hashmap:
            idx, last_element = self._hashmap[val], self.data[-1]
            self.data[-1], self._hashmap[last_element] = self.data[idx], idx
            self.data.pop()
            del self._hashmap[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        from random import choice
        return choice(self.data)
