class Solution:
    """
    My solution, passed 248/360 test cases. This is not a good solution at all.
    """
    def trap(self, height: list[int]) -> int:
        res, l, r = 0, 0, len(height) - 1
        if not (r + 1): return 0

        while l < r:
            for i in range(l, r):
                if height[i] >= height[l]:
                    l = i
            
            for i in range (r - 1, l, -1):
                if height[i] >= height[r]:
                    r = i
                else:
                    break
                
            for i in range(l + 1, r):
                water = min(height[l], height[r]) - height[i]
                res += water if water >= 0 else 0

            if height[l] < height[r]:
                r, l = l, 0
            else:
                r -= 1

        return res

    """
    Second solution:
    Runtime: 286 ms, faster than 53.43% of Python3 online submissions for Trapping Rain Water.
    Memory Usage: 16.1 MB, less than 46.50% of Python3 online submissions for Trapping Rain Water.
    """
    def trap(self, height: list[int]) -> int:
        res, l, r, lm, rm = 0, 0, len(height) - 1, 0, 0
        if not (r + 1): return 0

        while l < r:
            lm = max(lm, height[l])
            rm = max(rm, height[r])

            if lm < rm:
                res += lm-height[l]
                l+=1
            else:
                res += rm-height[r]
                r-=1

        return res


print(Solution().trap(height =  [0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap(height = [4,2,0,3,2,5]))
print(Solution().trap(height = [1,2,0,3,1,2,1,3]))
print(Solution().trap(height = [5,4,1,2]))
print(Solution().trap(height = [4,3,3,9,3,0,9,2,8,3]))
print(Solution().trap(height = [9,6,8,8,5,6,3]))