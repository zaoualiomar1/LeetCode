class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        result = 0 
        current_sum = 0 
        prefix_count = {0:1}
        for num in nums : 
            current_sum += num 
            if current_sum - k in prefix_count : 
                result += prefix_count[current_sum -k ]
            
            prefix_count[current_sum] = 1 + prefix_count.get(current_sum,0)
        return result 
