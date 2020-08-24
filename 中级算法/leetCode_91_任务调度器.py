"""
day: 2020-08-24
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xwvaot/
题目名: 任务调度器
题目描述: 给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的A-Z字母表示的26 种不同种类的任务。
任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。
然而，两个相同种类的任务之间必须有长度为n的冷却时间，因此至少有连续n个单位时间内CPU在执行不同的任务，或者在待命状态。
你需要计算完成所有任务所需要的最短时间。
示例:
输入：tasks = ["A","A","A","B","B","B"], n = 2
输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
    在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间
    而执行一个任务只需要一个单位时间，所以中间出现了待命状态
思路:
    记录数组中出现次数最多的任务的任务数max_task_count
    那么完成这个任务的时间time是 (max_task_count-1) * (n + 1)
    我们可以用(max_task_count-1)*(n+1)-max_task_count的时间去完成
    剩余的任务,若剩余的任务中,有次数跟最大次数相同的任务,需要额外增加一个
    时间.
    当数组的长度大于time时,我们执行任务中不会出现待命状态,那么所需的时间
    就是数组的长度
"""
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import defaultdict
        length = len(tasks)
        if length <= 1:
            return length
        # 记录各任务出现的次数
        task_map = defaultdict(int)
        for task in tasks:
            task_map[task] += 1
        # 按照出现次数进行排序
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        # 第一个就是出现次数最多的任务
        max_task_count = task_sort[0][1]
        # 至少需要的最短时间, 按照间隔来算即可
        res = (max_task_count - 1) * (n + 1)
        for sort in task_sort:
            # 如果有长度和最大长度相同的任务,则要+1
            if sort[1] == max_task_count:
                res += 1
            # 否则后面的任务长度都比它小,直接退出
            else:
                break
        # 若res小于length,代表在完成次数最多的任务的空闲时间里,不足以完成剩余的任务
        # 所以答案必然就是数组中的任务数
        return max(res, length)


if __name__ == "__main__":
    test = ["A", "A", "A", "B", "B", "B"]
    test1 = 2
    s = Solution()
    print(s.leastInterval(test, test1))
