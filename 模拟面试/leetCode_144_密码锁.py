"""
day: 2020-09-05
url: https://leetcode-cn.com/problems/open-the-lock/
题目名: 打开转盘锁

思路:
BFS
双向BFS
"""
from typing import List


class Solution:
    # 单向BFS
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
        # 把deadends作为visited数组
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        if '0000' == target:
            return 0
        queue = deque()
        queue.append(('0000', 0))

        while queue:
            node, step = queue.popleft()
            for i in range(4):
                for add in (1, -1):
                    cur = node[:i] + str((int(node[i]) + add) % 10) + node[i+1:]
                    if cur == target:
                        return step + 1
                    if cur not in deadends:
                        queue.append((cur, step + 1))
                        deadends.add(cur)
        return -1

    def openLock_double_bfs(self, deadends: List[str], target: str) -> int:
        # 转为集合,O(1)查找
        deadends = set(deadends)
        # 特判
        if '0000' in deadends:
            return -1
        if '0000' in target:
            return 0
        # 起始节点
        left = set()
        left.add('0000')
        # 结束节点
        right = set()
        right.add(target)
        step = 0

        while left:
            next_level = set()
            # 每次都搜索节点较少的一边
            if len(left) > len(right):
                left, right = right, left
            # 普通的bfs
            for node in left:
                for i in range(4):
                    for add in (1, -1):
                        cur = node[:i] + str((int(node[i]) + add) % 10) + node[i+1:]
                        # 如果当前边的节点,在另一边的节点中了,那么说明再往下走一层,就可以连通,也就是可以解锁了.
                        if cur in right:
                            return step + 1
                        # 将节点加入下一层要加入的节点中,将deadends作为我们的visited数组..
                        if cur not in deadends:
                            next_level.add(cur)
                            deadends.add(cur)
            # 每次走到下一层,步数都要+1
            step += 1
            left = next_level
        return -1


if __name__ == "__main__":
    test = ["0201", "0101", "0102", "1212", "2002"]
    test2 = '0202'
    s = Solution()
    print(s.openLock_double_bfs(test, test2))
