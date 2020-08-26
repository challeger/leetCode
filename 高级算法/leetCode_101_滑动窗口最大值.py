"""
day: 2020-08-25
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xw4q0r/
题目名: 滑动窗口最大值
给定一个数组nums,有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧.你只可以看到
在滑动窗口内的k个数字.滑动窗口每次只向右移动一位.返回滑动窗口中的最大值
示例:
    输入: nums = [1, 3, -1, -3, 5, 3, 6, 7]
    输出: [3, 3, 5, 5, 6, 7]
思路:
    用一个双端队列来存储nums在窗口范围内的,降序排列的索引.
    每次滑动窗口,我们首先判断队首元素是否还在窗口范围内,不在
    则弹出它,然后判断队列剩余的元素中,是否比新加入窗口的元素小,
    是则将其弹出,直到没有比它小的元素,或者队列已经空了..
    这样,我们队首指向的值,就是窗口中的最大值..
"""
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if not n * k:
            return []
        if k == 1:
            return nums

        def clean_deque(i):
            # 判断队首元素是否在窗口范围内,不在则将其弹出
            if deq and deq[0] == i-k:
                deq.popleft()
            # 将所有比新加入元素小的元素弹出
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # 队列存储窗口范围内的数的索引,按他们指向的值降序排列
        deq = deque()
        output = []
        right = 0
        while right < n:
            # 判断队首元素是否在窗口范围内,不在就弹出队首元素
            # 然后对剩余的元素进行判断,若比新加入窗口的元素小
            # 那么就弹出
            clean_deque(right)
            # 将新加入窗口的元素添加到队列中
            deq.append(right)
            # 窗口右移
            right += 1
            # 在right=k,也就是窗口刚开始时再计算
            if right >= k:
                output.append(nums[deq[0]])
        return output


if __name__ == "__main__":
    test = [1, 3, -1, -3, 5, 3, 6, 7]
    test1 = 3
    s = Solution()
    print(s.maxSlidingWindow(test, test1))
