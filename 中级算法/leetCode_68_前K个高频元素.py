"""
day: 2020-08-20
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvzpxi/
题目名: 前K个高频元素
题目描述: 给定一个非空的整数数组,返回其中出现频率前K高的元素
示例:
    输入: nums=[1, 1, 1, 2, 2, 3], k=2
    输出: [1, 2]
思路:
1.桶排序
    先将各个数字出现的次数记录到字典中,然后根据nums的长度建立一个List[List[int]],
    第一个list的索引代表出现的次数,第二个list存放出现次数为该索引的数字,然后从末尾开始
    遍历,如果桶内有元素就将其返回,直到返回了足够的结果
2.小顶堆
    先将各个数字出现的次数记录到字典num_count中,然后取num_count的前k个item,
    建立一个大小为k的最小堆,之后遍历num_count[k:],如果遇到比堆顶大的节点,就弹出堆顶
    并将当前节点加入堆中

小顶堆的建立

小顶堆本质上是一棵完全二叉树,但除叶子节点外,小顶堆的每个父节点的value都要
比其左右两个子节点的value小,其根节点一定是整个数组中最小的元素.
堆的建立,核心操作是上浮shift_up与下沉shift_down
上浮:
    若当前节点不是根节点,且当前节点的value小于其父节点,则将其与其父节点交换,
    我们会循环进行上浮操作,直到当前节点不满足上浮条件.
    节点的索引是index,那么它的父节点的索引是(index-1)>>1
下沉:
    将当前节点与左子节点和右子节点进行对比,与值较小的一个节点交换位置,直到当前节点
    是三个节点中最小的,或者已经没有子节点了.
添加:
    在堆中append一个元素,并对其进行上浮操作.
弹出堆顶:
    将堆的最后一个元素移动到堆顶,然后对其进行下沉操作.
"""
from typing import List


class MinHeap:
    def __init__(self):
        super().__init__()
        self._data = []
        self._count = 0

    @property
    def size(self):
        return self._count

    @property
    def isEmpty(self):
        return not self._count

    @property
    def top(self):
        if self._count:
            return self._data[0]
        else:
            return None

    def add(self, x):
        self._data.append(x)
        self._shift_up(self._count)
        self._count += 1

    def pop(self):
        if self._count:
            ret = self._data[0]
            self._data[0] = self._data[-1]
            self._data.pop()
            self._count -= 1
            self._shift_down(0)
            return ret

    def _shift_up(self, index):
        parent = (index-1) >> 1
        while index > 0 and self._data[index][1] < self._data[parent][1]:
            self._data[index], self._data[parent] = self._data[parent], self._data[index]
            index = parent
            parent = (index-1) >> 1

    def _shift_down(self, index):
        min_child = (index << 1) + 1
        while min_child < self.size:
            if min_child + 1 < self.size and self._data[min_child+1][1] < self._data[min_child][1]:
                min_child = min_child + 1
            if self._data[index][1] <= self._data[min_child][1]:
                break
            self._data[index], self._data[min_child] = self._data[min_child], self._data[index]
            index = min_child
            min_child = (index << 1) + 1


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        # num_count = Counter(nums)
        # return [foo[0] for foo in num_count.most_common(k)]

        # from collections import defaultdict
        # num_count = defaultdict(int)
        # for num in nums:
        #     num_count[num] += 1
        # res = []
        # foo = [[] for _ in range(len(nums) + 1)]
        # for key, value in num_count.items():
        #     foo[value].append(key)
        # idx = len(foo) - 1
        # while len(res) < k and idx > 0:
        #     if foo[idx]:
        #         res.extend(foo[idx])
        #     idx -= 1
        # return res[:k]
        num_count = Counter(nums)
        num_count = list(num_count.items())
        heap = MinHeap()
        for i in range(k):
            heap.add(num_count[i])
        for i in range(k, len(num_count)):
            if num_count[i][1] > heap.top[1]:
                heap.pop()
                heap.add(num_count[i])
        return [item[0] for item in heap._data]


if __name__ == "__main__":
    test = [5,-3,9,1,7,7,9,10,2,2,10,10,3,-1,3,7,-9,-1,3,3]
    count = 3
    s = Solution()
    print(s.topKFrequent(test, count))
