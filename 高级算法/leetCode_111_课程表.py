"""
day: 2020-08-28
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xd54x2/
题目名: 课程表
你这个学期必须选修numCourse门课程,记为0到numCourse-1
再选修某些课程之前需要一些先修课程,例如,想要学习课程0,你需要先完成课程1,我们用一个匹配来表示他们[0, 1]
给定课程总量以及它们的先决条件,请你判断是否可能完成所有课程的学习?
示例:
    输入: 2, [[1, 0]]
    输出: true
    输入: 2, [[1, 0], [0, 1]]
    输出: false
思路:
1. 入度表+广度优先遍历
    入度,是指在图中,指向某节点的节点的个数
    当入度为0时,说明没有任何节点指向该节点

    在本题中, 我们的入度即表示该课程的前驱课程的数量.
    我们用一个入度表来表示所有课程对应的入度
    邻接表来表示指向该节点的节点集合

    我们首先遍历数组,生成入度表与邻接表.
    然后建立一个队列,将入度表中所有入度为0的节点加入队列中..
    每次出队,就代表我们学习了一门课程,那么需要学习的课程数量-1.
    然后学习了本门课程之后,那些将该课程作为前驱课程的节点的入度也-1,
    若-1之后,入度为0,表示本课程也可以学习了,那么就将其加入队列..

    若图中是有环的,那么总会有课程的入度不为0,也就是处于不能学习状态,那么最终的
    需要学习的课程数量必定不为0,这是就表示无法安排课程..
    否则表示可以安排课程
2. 深度优先遍历
    定义一个标志列表flags,定义三种状态:
        0: 未被DFS访问过
        1: 被当前节点启动的DFS访问过
       -1: 被其他节点启动的DFS访问过
    我们对numCourses个节点依次执行DFS,判断每个节点启动的DFS中是否存在环.存在则直接返回False.
    DFS:
        1. 判断flag[i] == 1 or flag[i] == -1,等于1表示有环,等于-1表示其他DFS访问过,且无环.
        2. 将当前访问的节点i标为1,表示本轮已访问过该节点
        3. 递归访问节点i的所有邻接节点j,若有环,返回false
        4. 所有邻接节点都遍历完了,没有环,则将当前的节点i标为-1,并返回true
"""
from typing import List
from collections import deque


class Solution:
    def canFinish_bfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        # 入度表
        # 入度:指有向图中指向某点的点的个数
        # 在本题中,表示学习该课程需要的前驱课程的数量
        in_degrees = [0 for _ in range(numCourses)]
        # 邻接表,通过这个节点,可以到达的节点的集合
        # 在本题中,即表示将本门课程作为前驱课程的课程的集合
        adj = [set() for _ in range(numCourses)]
        # 遍历数组,建立入度表和邻接表
        for second, first in prerequisites:
            in_degrees[second] += 1
            adj[first].add(second)
        # 所有入度为0的节点
        queue = deque()
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
        while queue:
            # 依次弹出节点,弹出节点就相当于学习该们课程
            top = queue.popleft()
            # 要学的课程少了一门
            numCourses -= 1
            # 将这个节点指向的所有节点的入度-1
            # 表示前驱条件完成了一个
            for successor in adj[top]:
                in_degrees[successor] -= 1
                # 若-1之后入度为0,那么添加到队列中
                # 入度为0,说明此时课程的前驱条件已经都完成了
                # 那么就可以学习该课程
                if in_degrees[successor] == 0:
                    queue.append(successor)
        # 若图是有向无环图,那么所有节点必定都入队和出队过,即完成了拓扑排序
        # 否则,一定有节点的入度不为0,我们每次节点出队时,都执行numCourses -= 1
        # 若numCourses==0,说明完成了拓扑排序,也就是true
        return not numCourses

    def canFinish_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i):
            # -1表示在另外启动的dfs中,已经遍历过该节点
            # 既然已经走到了这里,说明这个节点之后是无环的,直接返回True
            if flags[i] == -1:
                return True
            # 1表示在本次dfs中,已经遍历过该节点
            # 此时重复遍历,说明有环,则返回False
            if flags[i] == 1:
                return False
            # 设置为本次dfs已经遍历过
            flags[i] = 1
            # 深度遍历
            for j in adj[i]:
                if not dfs(j):
                    return False
            # 本轮dfs结束,将该节点设置为在另外启动的dfs中遍历过
            flags[i] = -1
            return True

        # 邻接表
        adj = [[] for _ in range(numCourses)]
        flags = [0] * numCourses
        # 建立邻接表
        for second, first in prerequisites:
            adj[first].append(second)
        # 对每个节点进行dfs
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


if __name__ == "__main__":
    test1 = [[1, 0], [0, 1]]
    s = Solution()
    print(s.canFinish_dfs(2, test1))
