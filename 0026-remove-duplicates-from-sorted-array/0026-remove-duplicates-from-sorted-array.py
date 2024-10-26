class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # HINT 1: HANDLE EMPTY LIST CASE: 
        if not nums: return 0 
        
        # HINT: 2 ptr approach = SLOW (track uniques), FAST (runs thru list and compares adj elts)
        slow, fast = 0, 1      
        while fast < len(nums):
            # Inc slow only if unique elt found - inc fast always. 
            if nums[slow] != nums[fast]:        
                slow +=1 # accounts for one (more) unique elt found
                # "catches up" to where fast idx is currently as it may have gone up by alot 
                    # (over-writes next valid idx place with next unique elt) - "in-place" feature HERE !
                nums[slow] = nums[fast] 
            fast +=1  
        return (slow+1)
            