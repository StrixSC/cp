import os
import sys

class Solution:
    # Binary Search method (initial numbers list needs to be sorted)
    def twoSumBS(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1

        while left != right:
            val = nums[left] + nums[right]
            if val == target:
                return [left, right]
            elif val < target:
                left += 1
            elif val > target:
                right -= 1

        return []

    # Hashmap method:
    def twoSumHM(self, nums:list[int], target:int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            if (target - num) in seen:
                return [seen[target - num], i]
            seen.update({num: i})
        
        return []

def rinput():
	data = input()
	return data.split(" ");

if __name__ == "__main__":
	solution = Solution()
	res = solution.twoSumBS([3,2,4], 6)
	print(res)

# input: 2,7,11,15 9