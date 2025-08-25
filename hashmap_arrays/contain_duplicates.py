class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
    
        #return not ( len(nums) == len(set(nums)))
        
        hashset = set()
        for n in nums :
            if n in hashset: 
                return True
            hashset.add(n)
        
        return False
            
     
    
 