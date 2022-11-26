import time
class Solution:

    def threeSum2(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        l, r = 0, len(nums)
        seen = dict()

        while l < r:
            left = nums[l]
            right = nums[r]
            valid = [v for v in seen.keys() if left + right + v == 0]
            if len(valid) == 0:
                left += 1
                continue
        
            for v in valid:
                if seen[v] != l and seen[v] != r:
                    if seen[v] + left + right == 0 and [seen[v], left, right] not in res:
                        res.append(seen[v], left, right)
                    
            if seen[v] + left + right > 0: 
                r += 1
            else:
                l += 1

            seen[l] = left

        return res
    
    """
    Runtime: 6559 ms, faster than 10.40% of Python3 online submissions for 3Sum. (Rather slow...)
    Memory Usage: 18.1 MB, less than 72.84% of Python3 online submissions for 3Sum.
    """
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        i, k = 0, len(nums) - 1
        nums.sort()
        while i < k: 
            j = i + 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in res:
                    res.append([nums[i], nums[j], nums[k]])
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
            k = len(nums) - 1
            i += 1 
        
        return res


# print(Solution().threeSum(nums = [-1,0,1,2,-1,-4]))
# print(Solution().threeSum(nums = [0,0,0]))
# print(Solution().threeSum(nums = [0,0,0,0]))
# print(Solution().threeSum(nums = [-2,0,1,1,2]))
print(Solution().threeSum(nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]))