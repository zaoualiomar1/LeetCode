class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head 
        
        while fast and fast.next : 
            fast = fast.next.next 
            slow = slow.next 
            
            if fast == slow : 
                return fast.val
        
        return False 