"""
day: 2020-08-20
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvsehe/
题目名: 数组中的第K个最大元素
题目描述: 在未排序的数组中找到第K个最大的元素,请注意,你需要找的是数组排序后的第K个最大
的元素,而不是第K个不同的元素
示例:
    输入: [3,2,1,5,6,4] 和 k = 2
    输出: 5
    输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
    输出: 4
思路:
1. 快速排序
    选择一个元素作为边界,将所有比这个元素小的排在该元素左边,否则排在右边,
    那么这个元素的索引,就是他在数组中的大小的排序,我们将其与我们的目标进行对比
    如果小了,说明在左边,否则在右边,那么下一次就从对应的区间中再选择一个元素,以此类推,
    直到找到了想要的元素.
2. 堆排序
    建立一个大顶堆,然后进行k-1次pop操作,那么堆顶就是第K大的元素
"""
from typing import List
import random


class MaxHeap:
    def __init__(self):
        super().__init__()
        self.count = 0
        self.data = []

    def _shift_up(self, index):
        parent = (index-1) >> 1
        while index > 0 and self.data[index] > self.data[parent]:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent
            parent = (index-1) >> 1

    def _shift_down(self, index):
        max_child = (index << 1) + 1
        while max_child < self.count:
            if max_child + 1 < self.count and self.data[max_child + 1] > self.data[max_child]:
                max_child += 1
            if self.data[index] >= self.data[max_child]:
                break
            self.data[index], self.data[max_child] = self.data[max_child], self.data[index]
            index = max_child
            max_child = (index << 1) + 1

    def add(self, x):
        self.data.append(x)
        self._shift_up(self.count)
        self.count += 1

    def pop(self):
        if self.count:
            ret = self.data[0]
            self.data[0] = self.data[-1]
            self.data.pop()
            self.count -= 1
            self._shift_down(0)
            return ret


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[len(nums)-k]

        # def partition(idx_left, idx_right):
        #     # 随机选择一个边界元素
        #     random_idx = random.randint(idx_left, idx_right)
        #     # 将边界元素调到第一个元素
        #     nums[random_idx], nums[idx_left] = nums[idx_left], nums[random_idx]
        #     pivot = nums[idx_left]
        #     # 左边界的边界
        #     j = idx_left
        #     for i in range(idx_left+1, idx_right+1):
        #         # 如果比边界元素小
        #         if nums[i] < pivot:
        #             j += 1
        #             # 将该元素与边界元素交换位置
        #             nums[i], nums[j] = nums[j], nums[i]
        #     # 最后将边界元素放到边界上.
        #     nums[idx_left], nums[j] = nums[j], nums[idx_left]
        #     # 返回边界元素的索引,代表他在数组中的地位.
        #     return j
        heap = MaxHeap()
        for num in nums:
            heap.add(num)
        for _ in range(k-1):
            heap.pop()
        return heap.data[0]
        # size = len(nums)
        # # 第k个最大的元素,也就是第size-k个最小的元素
        # target = size - k
        # left = 0
        # right = size - 1
        # while True:
        #     index = partition(left, right)
        #     if index == target:
        #         return nums[index]
        #     # 若小于,说明要找的元素在右边界
        #     elif index < target:
        #         left = index + 1
        #     # 若大于,说明要找的元素在左边界
        #     else:
        #         right = index - 1


if __name__ == "__main__":
    test = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    count = 4
    s = Solution()
    print(s.findKthLargest(test, count))
