import math
import heapq

class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        score = 0
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for _ in range(k):
            score -= nums[0]
            heapq.heapreplace(nums, math.ceil(nums[0]/3))
        return score

print(Solution().maxKelements(nums = [10,10,10,10,10], k = 5))
print(Solution().maxKelements(nums = [1,10,3,3,3], k = 3))