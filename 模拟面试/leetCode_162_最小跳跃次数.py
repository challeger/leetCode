"""
day: 2020-09-12
url: https://leetcode-cn.com/problems/zui-xiao-tiao-yue-ci-shu/
题目名: 最小跳跃次数
为了给刷题的同学一些奖励,力扣团队引入了一个弹簧游戏机.
游戏机由 N 个特殊弹簧排成一排,编号为 0 到 N-1.初始有一个小球在编号 0 的弹簧处.
若小球在编号为 i 的弹簧处,通过按动弹簧,可以选择把小球向右弹射 jump[i] 的距离,或者向左弹射到任意左侧弹簧的位置.
也就是说,在编号为 i 弹簧处按动弹簧,小球可以弹向 0 到 i-1 中任意弹簧或者 i+jump[i] 的弹簧（若 i+jump[i]>=N,
则表示小球弹出了机器.小球位于编号 0 处的弹簧时不能再向左弹.
为了获得奖励,你需要将小球弹出机器.请求出最少需要按动多少次弹簧,可以将小球从编号 0 弹簧弹出整个机器,即向右越过编号 N-1 的弹簧.
思路:
1.bfs
    每次将下一次可以跳跃的节点加入队列中,直到某次跳跃可以到达终点.
    防止重复访问,应增加一个 visited 数组
    减少时间复杂度,每次记录上次到达的最远的位置,然后从左边开始寻找节点时,应该从该位置开始
"""
from typing import List
from collections import deque


class Solution:
    def minJump(self, jump: List[int]) -> int:
        if not jump:
            return 0
        n = len(jump)
        queue = deque()
        visited = {0}
        queue.append(0)
        count = 0
        far = 1
        while queue:
            size = len(queue)
            count += 1
            for _ in range(size):
                index = queue.popleft()
                next_node = index + jump[index]
                if next_node >= n:
                    return count
                if next_node not in visited:
                    queue.append(next_node)
                    visited.add(next_node)
                for i in range(far, index):
                    if i not in visited and (i + jump[i]) > next_node:
                        queue.append(i)
                        visited.add(i)
                far = max(far, index+1)
