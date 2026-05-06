class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head 
        while fast and fast.next : 
            fast = fast.next.next 
            slow = slow.next 
            

        
        # Inverser la 2eme list 
        curr = slow.next 
        slow.next = None 
        prev = None 
        
        while curr : 
            tmp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = tmp 
        
        # Fusioner les deux lists 
        
        first, second = head, prev 
        while second: 
            tmp1 = first.next 
            tmp2 = second.next 
            
            first.next = second
            second.next = tmp1 
            
            first = tmp1 
            second = tmp2 
        
        
        return head 
        