class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        for i, cost in enumerate(sorted(costs)):
            coins -= cost
            if coins < 0:
                return i
            elif coins == 0:
                return i + 1

print(Solution().maxIceCream(costs = [1,3,2,4,1], coins = 7))