# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        
        current = self.removeNodes(head.next)
        if head.val < current.val:
            return current
        else:
            head.next = current
            return head

                
vals = [1,1,1,1,1]
head = ListNode(vals[0])
current = head
for val in vals[1:]:
    tmp = ListNode(val)
    current.next = tmp
    current = tmp

sol = Solution().removeNodes(head)
vals = []
current = sol
while current:
    vals.append(current.val)
    current = current.next

print(vals)
