from collections import defaultdict;
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adj = defaultdict(list)
        for i in range(1, len(parent)):
            adj[parent[i]].append(i)

        res = 1
        def dfs(node=0, parent=None):
            nonlocal res
            if node not in adj:
                return 1
            tmp = 1
            for child in adj[node]:
                child_ans = dfs(child, node)
                if s[child] != s[node]:
                    res = max(res, child_ans + tmp)
                    tmp = max(tmp, child_ans+1)
            return tmp
        dfs()
        return res
