from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)

        for a, b, c in roads:
            graph[a][b] = c
            graph[b][a] = c

        # ans = float('inf')
        ans = 10**10

        see = [False] * (n + 1)
        from collections import deque
        q = deque()
        q.append(1)

        while q:
            node = q.popleft()
            see[node] = True
            for next_node, cost in graph[node].items():
                if not see[next_node]:
                    q.append(next_node)
                ans = min(ans, cost)

        return ans
