from collections import defaultdict

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        counts = [0 for _ in range(n)]
        ll = defaultdict(int)
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node=0, par=None):
            prev = ll[labels[node]] # This is what was missing from my solution (taken from warrenruud)
            ll[labels[node]] += 1
            for child in adj[node]:
                if child != par: dfs(child, node)
            counts[node] = ll[labels[node]] - prev

        dfs()
        return counts    
