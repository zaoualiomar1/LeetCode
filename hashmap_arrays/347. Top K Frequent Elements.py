class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        count = {}
        for num in nums: 
            count[num]= 1 + count.get(num, 0)
            
        sorted_count = sorted(count.items(), key = lambda x : x[1], reversed = True )
        return [num for num, freq in sorted_count[:k]]
    
    
    
        """
        count = {}
        freq = [[] for i in range(len(nums) +1)]

        for num in nums : 
            count[num] = 1+ count.get(num,0)
        for key,v in count.items(): 
            freq[v].append(key)
        
        res = []
        for i in range(len(freq)-1,0,-1): 
            for n in freq[i]:
                res.append(n)
                if len(res) == k : 
                    return res 
        
        """
        
        
        
        
        