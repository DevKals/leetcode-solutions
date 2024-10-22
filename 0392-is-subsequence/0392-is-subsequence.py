class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True # !!! check edgecase of s == "" (else, line 6 fails)
        t_ptr, s_ptr = 0, 0
        while t_ptr < len(t): 
            if s[s_ptr] == t[t_ptr]: 
                s_ptr +=1
                if s_ptr == len(s): # If s_ptr reaches end of s, all chars matched
                    return True
            t_ptr += 1
        return False
        
        
        
        
        '''
        t_dict = {}
        for i, char in enumerate(t): 
            t_dict[i] = [char, 'unseen']
        for char in s: 
            key, found = 0, False
            while key < len(t): 
                if char == t_dict[key][0] and t_dict[key][1] == 'unseen': 
                    t_dict[key][1] = 'seen'
                    found = True
                    break 
                else: 
                    t_dict[key][1] = 'seen'
                    key += 1  
            if found == False: 
                return False
            else: 
                continue 
        return True
        '''

        
        