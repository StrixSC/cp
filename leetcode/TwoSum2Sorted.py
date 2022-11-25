class Solution:
    """
    Runtime: 294 ms, faster than 50.76% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
    Memory Usage: 15.1 MB, less than 10.18% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
    """
    def twoSum2(self, numbers: list[int], target: int) -> list[int]:
        length = len(numbers)
        if length in [0, 1]:
            return []
            
        left = 0 
        right = len(numbers)

        while left != right:
            result = numbers[left] + numbers[right - 1]
            if result == target:
                return [left + 1, right]
            elif result < target:
                left += 1
            elif result > target:
                right -= 1
        
        return []

    """
    Runtime: 278 ms, faster than 58.50% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
    Memory Usage: 15 MB, less than 41.38% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
    """
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return [left + 1, right + 1]

print(Solution().twoSum([2,7,11,15], target=9))
print(Solution().twoSum([5, 25, 75], target=100))
print(Solution().twoSum(numbers = [2,3,4], target = 6))
print(Solution().twoSum(numbers = [-1,0], target = -1))