class Solution(object):
    def longestConsecutive(self, nums:list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        # The Trick here is the check if every number have no left neighbor 
        
        longest = 0 
        numSet = set(nums)
        for n in numSet : 
            if (n-1) not in numSet :
                length = 0 
                if (n+1) in numSet : 
                    length = 0 
                    while (n+length) in numSet: 
                        length+=1 
                    longest = max(longest, length)
        return longest 
    
    
        # ---
        # Other Solution 
        s=set(nums)
        m=0
        for n in s:
            if n-1 not in s:
                l=1
                while n+1 in s:
                    n+=1
                    l+=1
                m=max(m,l)
        return m
                        
                 
        
    

solution = Solution()