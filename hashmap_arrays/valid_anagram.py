# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

class Solution(object):
    
    def isAnagram(self, s:str, t:str)-> bool :
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # if len(s)!= len(t): 
        #     return False 
        
        # for i in s : 
        #     if i not in t : 
        #         return False
        #     else: 
        #         if s.count(i) != t.count(i): 
        #             return False  
        # return True 

        if len(s) != len(t) : 
            return False 

        
        if len(s)!= len(t): 
            return False 
        countS, countT = {},{}
        for i in range(len(s)): 
            countS[s[i]] = 1+ countS.get(s[i],0)
            countT[t[i]] = 1+ countT.get(t[i],0)

        for k in countS : 
            if countS[k] != countT.get(k,0) : 
                return False 
        return True 
            
            