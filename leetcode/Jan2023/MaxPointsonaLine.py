import math
from collections import defaultdict
class Solution:
    def computeSlope(self, point1, point2):
        denom = point2[0] - point1[0]
        if denom == 0: 
            return math.inf
        return (point2[1] - point1[1])/denom

    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) < 2:
            len(points)
        mx = 0
        for i in range(len(points)):
            dic = defaultdict(int)
            for j in range(i+1, len(points)):
                slope = self.computeSlope(points[j], points[i])
                dic[slope] += 1
                mx = max(mx, dic[slope])
        
        return mx + 1
            