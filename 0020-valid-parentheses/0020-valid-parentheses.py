class Solution:
    def isValid(self, s: str) -> bool:
        
        ''' HINT 1: USE A STACK OF CHARACTERS (created using a LIST) '''
        stack = [] # init empty stack 
        open_dict = { '(':')' , '{':'}', '[':']' }

        for char in s: 
            ''' HINT 2: When you encounter an opening bracket, push it to the top of the stack.'''
            if char in open_dict: 
                stack.append(char)
                continue # NECESARRY IF U NEED TO SKIP 'if stmt' DIRECTLY FOLLOWING AN 'IF'
            ''' HINT 3: Upon finding the first closing bracket: 
                Check "PEEK" if top of stack is the opening for it - only poss if stack not empty '''
            if not stack or char != open_dict[stack.pop()]:
                return False

        if len(stack) != 0: # 'return not stack' returns 'True' if stack empty (as desired for validity)
            return False
        
        return True      

           

