"""
day: 2020-10-31
url: https://leetcode-cn.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
题目名: O(1)时间插入、删除和获取随机元素，允许重复

设计一个支持在平均 时间复杂度 O(1) 下， 执行以下操作的数据结构。

注意: 允许出现重复元素。

insert(val)：向集合中插入元素 val。
remove(val)：当 val 存在时，从集合中移除一个 val。
getRandom：从现有集合中随机获取一个元素。每个元素被返回的概率应该与其在集合中的数量呈线性相关。


思路:
    列表存值, 字典存索引集合
    插入的时候,就判断val是否已经在字典中,然后来进行操作

    删除的时候,先判断删除的val是否是列表的最后一个,是的话就pop和删除字典中索引集合的值即可
    否则,需要将要删除的值的索引,换为结尾的值,并且索引也要进行修改.
"""
from typing import List
import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.indexs = {}
        self.length = -1

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.data.append(val)
        self.length += 1

        if val in self.indexs:
            self.indexs[val].add(self.length)
            return False
        else:
            self.indexs[val] = {self.length}
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.indexs:
            if val == self.data[-1]:  # 如果是最后一个元素
                self.indexs[val].remove(self.length)
            else:  # 如果不是最后一个元素
                index = self.indexs[val].pop()  # 拿到要删除的索引
                self.indexs[self.data[-1]].remove(self.length)  # 把尾部的元素索引进行交换
                self.indexs[self.data[-1]].add(index)
                self.data[index] = self.data[-1]
            self.data.pop()

            if not self.indexs[val]:  # 删掉后如果没有值了,那么就删掉该键
                del self.indexs[val]
            self.length -= 1
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        if self.length >= 0:
            return self.data[random.randint(0, self.length)]
