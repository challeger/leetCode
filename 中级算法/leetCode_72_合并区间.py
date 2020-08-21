"""
day: 2020-08-21
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xv11yj/
题目名: 合并区间
题目描述: 给定一个区间的集合,请合并所有重叠的区间
示例:
    输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
    输出: [[1,6], [8,10], [15,18]]
思路:
    先将intervals按照左边的数字进行升序排列,然后线性扫描.
    每次判断res最后一个元素的右边界是否大于interval的左边界,若大于则
    将res最后一个元素的右边界取max(res[-1][1], interval[1])
    否则res.append(interval)
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            if res and res[-1][1] >= interval[0]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)
        return res


if __name__ == "__main__":
    test = [[2, 6], [1, 3], [8, 10], [15, 18]]
    s = Solution()
    print(s.merge(test))
