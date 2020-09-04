"""
day: 2020-09-04
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdg3xr/
题目名: 天际线问题
城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓,现在,假设您获得了城市风光图片上
显示的所有建筑物的位置和高度,请编写一个程序以输出由这些建筑物形成的天际线.

每个建筑物的几何信息用三元组[L, R, H]表示,L和R分别表示第i座建筑物左右边缘的x坐标,H是其高度.假设所有建筑物
都是在绝对平坦且高度为0的表面上的完美矩形.

请输出以[[x1, y1], [x2, y2]...]格式的关键点的列表,关键点是水平线段的左端点,任何两个相邻建筑物之间的地面也
是天际线的一部分..

    输入列表已经按左x坐标L进行升序排列
    输出列表必须按x位排列
    输出天际线中不能有连续相同高度的水平线
示例:
    输入: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ]
    输出: [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]
思路:
    我们将所有建筑的左端点与右端点添加到一个列表中,按照它们的x坐标进行排序,若
    x相等,则按照y坐标排序,在入队时,将左端点的高度取反,以此来标记左端点,也有利于
    将heapq的小顶堆转为大顶堆

    然后我们遍历该数组,第一个遇到的端点必然是左端点..
    如果我们遇到的端点是左端点,就将端点入堆..
    如果我们遇到的是右端点,那么就将堆中,所有右边界小于该右端点的 左端点出堆,对于这些端点,他们的值必然都
    已经添加到了结果中了,

    如果当前堆顶发生了变化,那么说明遇到了一个新的关键点,将其加入结果中.
"""
from typing import List
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        res = [[0, 0]]
        # 维护一个大顶堆
        heap = [[0, float('inf')]]
        points = []
        for left, right, height in buildings:
            # 用负数来标记左端点,同时将heapq中的小顶堆转为大顶堆
            points.append((left, -height, right))
            points.append((right, height, 0))
        points.sort()

        for left, height, right in points:
            # 遇到右端点,将所有右边界比该端点小的左端点移出堆
            while left >= heap[0][1]:
                heapq.heappop(heap)
            # 遇到左端点,入堆,记录当前左端点的右端点
            if height < 0:
                heapq.heappush(heap, [height, right])
            # 如果最大高度发生了变化,说明遍历到了新的关键点
            # 发生变化有两种情况,一种是有新的节点入堆,并且该节点的高度比之前的高度要高
            # 那么当前的关键点就是,(该节点的x坐标,该节点的高度)
            # 另一种情况是遍历到了当前堆最高节点的右端点,那么就将最高点弹出,若堆中还有节点
            # 那么当前的关键点就是,(右端点的x坐标,当前节点的高度)
            if res[-1][1] != -heap[0][0]:
                res.append([left, -heap[0][0]])
        return res[1:]


if __name__ == "__main__":
    test = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    s = Solution()
    print(s.getSkyline(test))
