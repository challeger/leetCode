"""
day: 2020-09-02
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xd3xme/
题目名: 数据流的中位数
中位数是有序列表中间的数,如果列表长度是偶数,中位数则是中间两个数的平均值.
例如:
    [2, 3, 4]的中位数是3
    [2, 3]的中位数是(2 + 3) / 2 = 2.5
设计一个支持以下两种操作的数据结构:
    addNum(num: int) 从数据流中添加一个整数到数据结构
    findMedian() 返回目前所有元素的中位数

思路:
    对于一个有序列表,我们可以将其从中间分为两个部分,使得左边的数全部小于右边的数,
    当列表中的总数是奇数时,我们让左边的数多一个.
    当我们要寻找中位数时,判断当前数据结构中的数的个数,如果是偶数,那么就返回左边数
    的最后一个元素与右边数的第一个元素的和/2
    如果是奇数,那么就是左边的数的最后一个数.

    按照这样,我们可以维护一个小顶堆与一个大顶堆,小顶堆里存储的数恒大于等于大顶堆中的数.

"""
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count = 0
        # 大顶堆,存储的是中位数左边的数
        self.left_nums = []
        # 小顶堆,存储的是中位数右边的数
        self.right_nums = []

    def addNum(self, num: int) -> None:
        # 总数加1
        self.count += 1
        # 将数添加到左边的数组中,并弹出其中的最大值
        heapq.heappush(self.left_nums, -num)
        left_top = -heapq.heappop(self.left_nums)
        # 将这个最大值添加到右边数组中
        # 这样可以保证右边数组的所有值都大于等于左边数组
        heapq.heappush(self.right_nums, left_top)
        # 如果添加之后总数为奇数,那么我们需要将右边的堆顶移动到左边的堆顶.
        if self.count & 1:
            right_top = heapq.heappop(self.right_nums)
            heapq.heappush(self.left_nums, -right_top)

    def findMedian(self) -> float:
        # 说明是奇数,返回左边数组的最后一位
        if self.count & 1:
            return -self.left_nums[0]
        # 偶数则返回左边数组最大值与右边数组最小值的和/2
        else:
            return (-self.left_nums[0] + self.right_nums[0]) / 2


if __name__ == "__main__":
    test = MedianFinder()
    test.addNum(1)
    test.addNum(2)
    test.addNum(3)
    print(test.left_nums)
    print(test.right_nums)
    print(test.findMedian())
