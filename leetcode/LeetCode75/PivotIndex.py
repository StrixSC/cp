class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        if nums[-1] == nums[0]:
            return 0
        for i in range(1, len(nums)):
            if nums[-1] - nums[i] == nums[i - 1]: return i

        return -1
Solution().pivotIndexDP(nums=[1,7,3,6,5,6])