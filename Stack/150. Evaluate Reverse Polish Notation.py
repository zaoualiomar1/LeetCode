class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = ['+', '-','*','/']
        stack = []
        
        for token in tokens :
            if token not in operators : 
                stack.append(int(token))
            else : 
                b = int(stack.pop())
                a =int  (stack.pop())

                if token == "+" : 
                    stack.append(a + b)
                elif token == "*": 
                    stack.append(a* b)
                elif token == "-" : 
                    stack.append(a-b)
                else : 
                    result = abs(a) // abs(b)
                    if a * b < 0:
                        result = -result
                    stack.append(result)
                
        return stack[-1]
                     