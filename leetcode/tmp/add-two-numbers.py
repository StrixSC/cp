class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def extract_value_from_listnode(listnode: ListNode):
            val = []
            node = listnode
            while node:
                val.append(node.val)
                node = node.next
            
            return int("".join(str(i) for i in reversed(val)))

        first_val = extract_value_from_listnode(l1)
        second_val = extract_value_from_listnode(l2)
        sum_val = first_val + second_val
        splitted = list(map(int, str(sum_val)[::-1]))
        root = ListNode(splitted[0], next=ListNode())
        for val in splitted[1:]:
            current = root.next
            while current.val is None:
                current = current.next
            current.next = ListNode(val)
            

        return root
    
    def addTwoNumbersCorrection(self, l1: ListNode, l2: ListNode):
        carry = 0
        root = current = ListNode(-1)
        while l1 or l2:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            
            if l2: 
                v2 = l2.val
                l2 = l2.next
                
            carry, result = divmod(v1+v2+carry, 10)
            
            current.next = ListNode(result)
            current = current.next
        
        if carry:
            current.next = ListNode(carry)
        
        return root.next
    
if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(2, next=ListNode(4, next=ListNode(3)))
    l2 = ListNode(5, next=ListNode(6, next=ListNode(4)))
    sol = []
    solved = solution.addTwoNumbersCorrection(l1, l2)
    node = solved
    while node:
        sol.append(node.val)
        node = node.next
    print("".join([str(i) for i in sol]))
