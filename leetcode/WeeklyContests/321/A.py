class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return n

        l = 0
        while l < n:
            lsum = sum(range(0, l))
            rsum = sum(range(n, l, -1))
            if lsum == rsum:
                return l
            l += 1
        
        return -1

print(Solution().pivotInteger(8))
print(Solution().pivotInteger(1))
print(Solution().pivotInteger(4))