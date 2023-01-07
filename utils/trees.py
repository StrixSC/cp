class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeBuilder:
    def __init__(self, arr):
        self.arr = arr
        self.count = len(arr)
        self.root = self.build_tree(0)

    def build_tree(self, index):
        root = None
        if index < self.count:
            root = TreeNode(self.arr[index])
            root.left = self.build_tree(2*index+1)
            root.right = self.build_tree(2*index+2)
        return root
    
    # https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def print_tree(self, root: TreeNode, level=0):
        if root:
            self.print_tree(root.right, level+1)
            print(f"{' ' * 4 * level} -> {root.val}")
            self.print_tree(root.left, level+1)
