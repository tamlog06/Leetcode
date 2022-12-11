class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        ans = -1
        for i in range(len(nums)):
            tmp_len = 0
            tmp_val = nums[i]
            while d[tmp_val] > 0:
                tmp_val *= tmp_val
                tmp_len += 1

            if tmp_len >= 2:
                ans = max(ans, tmp_len)

        return ans
