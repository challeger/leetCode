"""
day: 2020-09-07
url: https://leetcode-cn.com/problems/top-k-frequent-elements/
题目名: 前k个高频元素
给定一个非空的整数数组, 返回其中出现频率前 k 高的元素

思路:
记录出现次数,排序,输出.
"""
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counter = Counter(nums)
        foo = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(foo[i][0])
        return res


if __name__ == "__main__":
    test = [1, 1, 1, 2, 2, 3]
    s = Solution()
    print(s.topKFrequent(test, 2))
