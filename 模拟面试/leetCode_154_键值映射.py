"""
day: 2020-09-09
url: https://leetcode-cn.com/problems/map-sum-pairs/
题目名: 键值映射
实现一个 MapSum 类里的两个方法，insert 和 sum。
对于方法 insert，你将得到一对（字符串，整数）的键值对。字符串表示键，整数表示值
如果键已经存在，那么原来的键值对将被替代成新的键值对
对于方法 sum，你将得到一个表示前缀的字符串，你需要返回所有以该前缀开头的键的值的总和。

思路:

    前缀树.

"""


class MapSum(object):
    def __init__(self):
        self.root = {}

    def insert(self, key, val):
        node = self.root
        for char in key:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['val'] = val

    def dfs(self, node, sum):
        for child in node:
            if child == 'val':
                sum += node[child]
            else:
                sum = self.dfs(node[child], sum)
        return sum

    def sum(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return 0
            node = node[char]
        return self.dfs(node, 0)
