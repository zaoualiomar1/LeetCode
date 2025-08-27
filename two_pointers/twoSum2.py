class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        i = 0 
        j = len(numbers) - 1 
        
        while i < j : 
            hulk = numbers [i] + numbers[j]
            if  hulk < target : 
                i+=1   
            elif hulk > target : 
                j-=1 
            else : 
                return [i+1, j+1]
                