import sys
sys.setrecursionlimit(10**6)
from collections import deque

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        self.m, self.n = len(grid), len(grid[0])

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        ans = []
        q = [[queries[i], i] for i in range(len(queries))]
        q.sort(key=lambda x: x[0])

        see = [[False] * self.n for _ in range(self.m)]
        see[0][0] = True
        que = deque([(0, 0)])
        next_que = deque([])

        ans = [0]
        for k, _ in q:
            if k <= grid[0][0]:
                ans.append(ans[-1])
                continue

            while que:
                x, y = que.popleft()
                if k > grid[x][y]:
                    ans[-1] += 1

                    for nx, ny in zip(dx, dy):
                        nx += x
                        ny += y
                        if 0 <= nx < self.m and 0 <= ny < self.n and not see[nx][ny]:
                            see[nx][ny] = True
                            que.append((nx, ny))
                else:
                    next_que.append((x, y))

            que = next_que
            next_que = deque([])
            ans.append(ans[-1])

        true_ans = [0] * len(queries)
        for i in range(len(queries)):
            true_ans[q[i][1]] = ans[i]

        return true_ans

