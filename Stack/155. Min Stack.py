class MinStack(object):

    def __init__(self):
        self.stack = []
        self.stack_min = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        self.stack.append(val)
        if self.stack_min: 
            current_min = min(val, self.stack_min[-1])
        else : 
            current_min = val 
        self.stack_min.append(current_min)

    def pop(self):
        """
        :rtype: None
        """
        self.stack_min.pop()
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack_min[-1]