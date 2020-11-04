"""
day: 2020-11-04
url: https://leetcode-cn.com/problems/insert-interval/
题目名: 插入区间
给出一个无重叠的,按照区间起始断点排序的区间仍然有序且不重叠
(如果有必要的话,可以合并区间)

示例1:
    输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
    输出: [[1, 5], [6, 9]]

示例2:
    输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    输出: [[1,2],[3,10],[12,16]]


思路:
    遍历二维列表的每一个区间,如果当前区间的右区间,小于要插入区间的左区间;或者当前区间的左区间
    大于要插入区间的右区间,那么它们之间是没有交集的,所以就直接添加到结果中,否则要计算两个区间之间的并集.
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        left, right = newInterval
        is_inserted = False
        for l, r in intervals:
            # 当前区间的l大于要插入的区间的右边,说明在区间右侧,且没有交集
            if l > right:
                if not is_inserted:
                    res.append([left, right])
                    is_inserted = True
                res.append([l, r])
            # 当前区间的r小于要插入区间的左边,说明在区间左侧且没有交集
            elif r < left:
                res.append([l, r])
            else:
                # 计算交集
                left = min(left, l)
                right = max(right, r)

        if not is_inserted:
            res.append([left, right])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
