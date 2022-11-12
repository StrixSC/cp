import os
import sys

"""
Runtime: 254 ms, faster than 87.26% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 21.8 MB, less than 31.60% of Python3 online submissions for Product of Array Except Self.
"""
class Solution:
    """
    This solution had the best runtime/mem consumption
    """
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        zeroes = [i for i in range(len(nums)) if not nums[i]]

        zero_count = len(zeroes)
        res = [0 for _ in nums]

        # If we have more than 2 zeroes in the numbers list, any product will always contain a zero, thus the result will always be 0
        if zero_count > 1:
            return res 

        if zero_count == 1:
            nums[zeroes[0]] = 1

        product = nums[0]
        for num in nums[1:]:
            product *= num

        if zero_count == 1:
            res[zeroes[0]] = product
            return res

        for i, num in enumerate(nums):
            res[i] = int(product/num)

        return res
        
def rinput():
	data = input()
	return data.split(" ");

if __name__ == "__main__":
	solution = Solution()
	res = solution.productExceptSelf([1,2,3,4])
	print(res)

# input: 2,7,11,15,9