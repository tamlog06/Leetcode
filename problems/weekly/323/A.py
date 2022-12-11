class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            grid[i].sort()

        ans = 0
        for j in range(n):
            max_val = 0
            for i in range(m):
                max_val = max(max_val, grid[i][j])
            ans += max_val

        return ans
