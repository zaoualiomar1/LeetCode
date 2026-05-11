class Solution(object):
    
    def build_stack(s:str) -> str : 
        stack = []
        for char in s : 
            if char  == "#" : 
                if stack : 
                    stack.pop()
            else : 
                stack.append(char)
        
        return ''.join(stack)
    def backspaceCompare(self, s, t) -> bool :
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        return self.build_stack (s) == self.build_stack(t)
        
        

    
