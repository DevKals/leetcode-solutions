class Solution:
    def countSegments(self, s: str) -> int:
        seg_ls = s.strip(" ").split(" ")
        print(seg_ls, "\n\n\n")
        count = 0
        for i in seg_ls: 
            if not i: 
                continue
            else: count +=1
        return count
    
    
        
