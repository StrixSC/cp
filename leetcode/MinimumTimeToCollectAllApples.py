from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        seen = set()

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):
            seen.add(node)
            time = sum(dfs(n) for n in adj[node] if n not in seen) 
            if not time and not hasApple[node]:
                return 0
            else:
                return time+2
        
        return max(0, dfs(0)-2)
