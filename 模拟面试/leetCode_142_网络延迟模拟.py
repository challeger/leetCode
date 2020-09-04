from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        import heapq
        from collections import defaultdict
        graph = defaultdict(list)
        # 建立一个邻接表
        for u, v, w in times:
            graph[u].append((v, w))
        # 起点位置
        pq = [(0, K)]
        # 已经求出最短路径的节点集合
        dist = {}
        while pq:
            # 将堆中的最小值弹出,意为走目前能走的最短路径
            d, node = heapq.heappop(pq)
            # 如果已经走过该节点了,就跳过本次循环
            if node in dist:
                continue
            # 否则将节点加入集合中
            dist[node] = d
            # 遍历节点的邻接节点
            for nei, d2 in graph[node]:
                # 如果邻接节点没有走过,就加入堆中,准备下次走
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))
        return max(dist.values()) if len(dist) == N else -1

    def networkDelayTime_SPFA(self, times: List[List[int]], N: int, K: int) -> int:
        from collections import deque, defaultdict
        graph = defaultdict(list)
        # 建立一个邻接表
        for u, v, w in times:
            graph[u].append((v, w))
        queue = deque()
        queue.append(K)
        dist = {i: float('inf') for i in range(1, N+1)}
        dist[K] = 0
        while queue:
            head = queue.popleft()
            for next_node in graph[head]:
                distance = dist[head] + next_node[1]
                if distance < dist[next_node[0]]:
                    dist[next_node[0]] = distance
                    queue.append(next_node[0])
        max_value = max(dist.values())
        return -1 if max_value == float('inf') else max_value


if __name__ == "__main__":
    test = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    test_1 = 4
    test_2 = 2
    s = Solution()
    print(s.networkDelayTime_SPFA(test, test_1, test_2))
