class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if not nums: 
            return 0 
        
        slow, fast = 0, 0       
        while fast < len(nums): 
            #if nums[fast] == val: 
                # fast +=1 - causing errors here !! Not needed twice in one iter ! 
            if nums[fast] != val: 
                nums[slow] = nums[fast]
                slow += 1
            fast +=1        
        return slow
                
        