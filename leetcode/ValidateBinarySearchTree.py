import sys
import math
sys.path.append('..')
from utils.trees import TreeNode, TreeBuilder

class Solution:
    def isValidBST(self, root: TreeNode, min_val=math.inf) -> bool:
        if root is not None:
            min_val = min(min_val, root.val)
        return True

tb1 = TreeBuilder([2, 2, 2])
tb2 = TreeBuilder([5,1,4,None,None,3,6])
tb3 = TreeBuilder([5,4,6,None,None,3,7])
tb3.print_tree(root=tb3.root)
print(Solution().isValidBST(root=tb3.root))
# print(Solution().isValidBST(root=[5,1,4,None,None,3,6]))
