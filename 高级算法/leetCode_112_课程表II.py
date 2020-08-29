"""
day: 2020-08-29
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xd9kfc/
题目名: 课程表II
现在你总共有n门课需要选, 记为0到n-1
在选修某些课程之前需要一些先修课程,例如,想要学习课程0,你需要先完成课程1,我们用一个匹配来表示他们[0, 1]
给定课程总量以及它们的先决条件,返回你为了学完所有课程所安排的学习顺序.
可能会有多个正确的顺序,你只要返回一种就可以了.如果不可能完成所有课程,返回一个空数组.
示例:
    输入: 4, [[1,0],[2,0],[3,1],[3,2]]
    输出: [0,1,2,3] or [0,2,1,3]
思路:
1. 入度表+广度优先遍历
    入度,是指在图中,指向某节点的节点的个数
    当入度为0时,说明没有任何节点指向该节点

    在本题中, 我们的入度即表示该课程的前驱课程的数量.
    我们用一个入度表来表示所有课程对应的入度
    邻接表来表示指向该节点的节点集合

    我们首先遍历数组,生成入度表与邻接表.
    然后建立一个队列,将入度表中所有入度为0的节点加入队列中..
    每次出队,就代表我们学习了一门课程,将这门课程加入结果队列中
    然后学习了本门课程之后,那些将该课程作为前驱课程的节点的入度也-1,
    若-1之后,入度为0,表示本课程也可以学习了,那么就将其加入队列..

    若图中是有环的,那么总会有课程的入度不为0,也就是处于不能学习状态,那么最终的
    学习了的课程必定小于我们需要学习的课程数量,这是就表示无法安排课程..返回[]
    否则返回res
2. 深度优先遍历
    定义一个标志列表flags,定义三种状态:
        0: 未被DFS访问过
        1: 被当前节点启动的DFS访问过
       -1: 被其他节点启动的DFS访问过
    我们对numCourses个节点依次执行DFS,判断每个节点启动的DFS中是否存在环.存在则直接返回False.
    本次dfs无环则将节点添加到结果中..
    如果有环,那么必定会有节点无法添加到结果数组中,只需要判断结果数组的长度是否等于需要学习的课程的数量即可
    DFS:
        1. 判断flag[i] == 1 or flag[i] == -1,等于1表示有环,等于-1表示其他DFS访问过,且无环.
        2. 将当前访问的节点i标为1,表示本轮已访问过该节点
        3. 递归访问节点i的所有邻接节点j,若有环,返回false
        4. 所有邻接节点都遍历完了,没有环,则将当前的节点i标为-1,并返回true
"""
from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 广度优先
        if not numCourses:
            return []

        # 入度表
        in_deq = [0 for _ in range(numCourses)]
        # 邻接表
        adj = [set() for _ in range(numCourses)]
        for second, first in prerequisites:
            in_deq[second] += 1
            adj[first].add(second)
        queue = deque()
        for idx in range(len(in_deq)):
            if not in_deq[idx]:
                queue.append(idx)
        res = []
        while queue:
            course = queue.popleft()
            res.append(course)
            for idx in adj[course]:
                in_deq[idx] -= 1
                if not in_deq[idx]:
                    queue.append(idx)
        return res if len(res) == numCourses else []

    def findOrder_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not numCourses:
            return []
        adj = [[] for _ in range(numCourses)]
        # 标记课程是否访问过
        flags = [0 for _ in range(numCourses)]
        res = []

        # 建立邻接表
        for second, first in prerequisites:
            adj[first].append(second)

        def dfs(i):
            # -1表示在其他课程开启的dfs中已经遍历了该课程,所以可以直接跳过接下来的dfs
            if flags[i] == -1:
                return True
            # 1表示在本次dfs中,已经遍历过一次该课程,再次遇到说明出现了环,所以返回false
            elif flags[i] == 1:
                return False
            # 将当前课程标记为正在访问
            flags[i] = 1
            for course in adj[i]:
                if not dfs(course):
                    return False
            # 标记为访问完成
            flags[i] = -1
            res.append(i)
            return True

        for i in range(numCourses):
            if not flags[i]:
                dfs(i)
        return res[::-1] if len(res) == numCourses else []


if __name__ == "__main__":
    test = [[1, 0], [2, 0], [3, 1], [3, 2]]
    s = Solution()
    print(s.findOrder_dfs(4, test))
